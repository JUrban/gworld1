#!/usr/bin/env python3
"""Exact, bounded construction tests for weighted-orbit-proof.md.

Rational exponential tensor coordinates, NOT 1+X Magnus coordinates.
This implements the rational free basis and integral-power construction;
it is not the full finite-union commutator decision algorithm.
"""
from fractions import Fraction as Q
from math import factorial


def add(a, b, scalar=1):
    out = dict(a)
    for w, value in b.items():
        out[w] = out.get(w, 0) + scalar * value
        if not out[w]:
            del out[w]
    return out


def scale(a, scalar):
    return {w: value * scalar for w, value in a.items() if value * scalar}


def key(word):
    return len(word), word


class Basis:
    """Exact sparse elimination; each row retains original-basis coordinates."""
    def __init__(self):
        self.rows = {}
        self.originals = []

    def reduce(self, value):
        value = dict(value)
        coordinates = {}
        for pivot in sorted(self.rows, key=key):
            coefficient = value.get(pivot, 0)
            if coefficient:
                row, expression = self.rows[pivot]
                value = add(value, row, -coefficient)
                coordinates = add(coordinates, expression, coefficient)
        return value, coordinates

    def insert(self, value):
        remainder, used = self.reduce(value)
        if not remainder:
            return False
        index = len(self.originals)
        self.originals.append(value)
        pivot = min(remainder, key=key)
        coefficient = remainder[pivot]
        expression = add({index: Q(1)}, used, -1)
        self.rows[pivot] = (scale(remainder, Q(1) / coefficient),
                            scale(expression, Q(1) / coefficient))
        return True

    def coordinates(self, value):
        remainder, coordinates = self.reduce(value)
        if remainder:
            raise ValueError('Vector outside rational basis span')
        return coordinates


class Tensor:
    def __init__(self, rank, degree):
        self.rank, self.degree = rank, degree
        self.one = {(): Q(1)}
        self.letters = [{(i,): Q(1)} for i in range(rank)]
        self.hall = [dict(weight=1, pair=None, lie=x) for x in self.letters]
        for d in range(2, degree + 1):
            pending = []
            for i, a in enumerate(self.hall):
                for j, b in enumerate(self.hall[:i]):
                    if a['weight'] + b['weight'] != d:
                        continue
                    if a['pair'] is not None and a['pair'][1] > j:
                        continue
                    pending.append(dict(weight=d, pair=(i, j),
                                        lie=self.bracket(a['lie'], b['lie'])))
            self.hall.extend(pending)
        self.layers = {}
        for d in range(1, degree + 1):
            indices = [i for i, h in enumerate(self.hall) if h['weight'] == d]
            basis = Basis()
            for i in indices:
                assert basis.insert(self.hall[i]['lie'])
            self.layers[d] = indices, basis
        self._groups = {}
        self._logs = {}

    def mul(self, a, b):
        out = {}
        for u, x in a.items():
            for v, y in b.items():
                if len(u) + len(v) <= self.degree:
                    w = u + v
                    out[w] = out.get(w, 0) + x * y
        return {w: value for w, value in out.items() if value}

    def bracket(self, a, b):
        return add(self.mul(a, b), self.mul(b, a), -1)

    def layer(self, a, d):
        return {w: x for w, x in a.items() if len(w) == d}

    def exp(self, a):
        assert () not in a
        out, term = dict(self.one), dict(self.one)
        for k in range(1, self.degree + 1):
            term = self.mul(term, a)
            if not term:
                break
            out = add(out, term, Q(1, factorial(k)))
        return out

    def log(self, a):
        assert a.get(()) == 1
        b = add(a, self.one, -1)
        out, term = {}, dict(self.one)
        for k in range(1, self.degree + 1):
            term = self.mul(term, b)
            if not term:
                break
            out = add(out, term, Q((-1)**(k+1), k))
        return out

    def inv(self, a):
        return self.exp(scale(self.log(a), -1))

    def power(self, a, n):
        return self.exp(scale(self.log(a), n))

    def comm(self, a, b):
        return self.mul(self.mul(self.mul(self.inv(a), self.inv(b)), a), b)

    def group_hall(self, i):
        if i not in self._groups:
            h = self.hall[i]
            if h['pair'] is None:
                value = self.exp(h['lie'])
            else:
                a, b = h['pair']
                value = self.comm(self.group_hall(a), self.group_hall(b))
            self._groups[i] = value
        return self._groups[i]

    def log_hall(self, i):
        if i not in self._logs:
            self._logs[i] = self.log(self.group_hall(i))
        return self._logs[i]

    def from_hall(self, terms):
        value = dict(self.one)
        for i, n in terms:
            value = self.mul(value, self.exp(scale(self.log_hall(i), Q(n))))
        return value

    def collect(self, value, start=1):
        value = dict(value)
        answer = []
        for d in range(start, self.degree + 1):
            indices, basis = self.layers[d]
            coordinates = basis.coordinates(self.layer(value, d))
            for j, coefficient in sorted(coordinates.items()):
                i = indices[j]
                answer.append((i, coefficient))
                value = self.mul(self.exp(scale(self.log_hall(i), -coefficient)), value)
        assert value == self.one, ('Collection residual', value)
        return answer


class Weighted:
    def __init__(self, tensor, x_terms, y_terms, p, q):
        self.m, self.p, self.q = tensor, p, q
        self.x = tensor.from_hall(x_terms)
        self.y = tensor.from_hall(y_terms)
        self.bx, self.by = tensor.log(self.x), tensor.log(self.y)
        self.C, self.D = tensor.layer(self.bx, p), tensor.layer(self.by, q)
        assert self.C and self.D
        assert all(len(w) >= p for w in self.bx)
        assert all(len(w) >= q for w in self.by)
        assert tensor.bracket(self.C, self.D)
        self.low = Basis()
        assert self.low.insert(self.C)
        if p == q:
            assert self.low.insert(self.D)
        self.alayers = {p: list(self.low.originals)}
        for d in range(p + 1, tensor.degree + 1):
            self.alayers[d] = list(tensor.layers[d][1].originals)

        self.generators = []
        self.nodes = []
        self.special = {}
        self.decomposable_dimensions = {}
        for d in range(p, tensor.degree + 1):
            decomposables = Basis()
            for u in range(p, d):
                for a in self.alayers.get(u, []):
                    for b in self.alayers.get(d-u, []):
                        decomposables.insert(tensor.bracket(a, b))
            self.decomposable_dimensions[d] = len(decomposables.originals)
            forced = []
            if d == p:
                forced.append(('C', self.C, self.bx))
            if d == q:
                forced.append(('D', self.D, self.by))
            fresh = []
            for label, lead, actual in forced:
                if not decomposables.insert(lead):
                    raise ValueError('Leading factor is decomposable: ' + label)
                fresh.append((label, lead, actual))
            for lead in self.alayers[d]:
                if decomposables.insert(lead):
                    fresh.append((None, lead, lead))
            for label, lead, actual in fresh:
                number = len(self.generators)
                self.generators.append(dict(weight=d, lead=lead, value=actual))
                self.nodes.append(dict(weight=d, pair=None, generator=number,
                                       lead=lead, value=actual))
                if label:
                    self.special[label] = number
            pending = []
            for i, a in enumerate(self.nodes):
                for j, b in enumerate(self.nodes[:i]):
                    if a['weight'] + b['weight'] != d:
                        continue
                    if a['pair'] is not None and a['pair'][1] > j:
                        continue
                    pending.append(dict(weight=d, pair=(i, j), generator=None,
                                        lead=tensor.bracket(a['lead'], b['lead']),
                                        value=tensor.bracket(a['value'], b['value'])))
            self.nodes.extend(pending)
            check = Basis()
            for node in self.nodes:
                if node['weight'] == d:
                    assert check.insert(node['lead']), ('Weighted Hall dependence', d)
            assert len(check.originals) == len(self.alayers[d]), ('Dimension mismatch', d)
        self.basis = Basis()
        for node in self.nodes:
            assert self.basis.insert(node['value'])
        tail = [i for i, h in enumerate(tensor.hall) if h['weight'] > p]
        self.klogs = [self.bx] + ([self.by] if p == q else [])
        self.klogs.extend(tensor.log_hall(i) for i in tail)
        self.kterms = [x_terms] + ([y_terms] if p == q else [])
        self.kterms.extend([[(i, 1)] for i in tail])

    def kcoordinates(self, logvalue):
        m = self.m
        low = self.low.coordinates(m.layer(logvalue, self.p))
        value = m.exp(logvalue)
        answer = []
        for i, b in enumerate(self.klogs[:len(self.low.originals)]):
            n = low.get(i, Q(0))
            answer.append(n)
            if n:
                value = m.mul(m.exp(scale(b, -n)), value)
        tail = dict(m.collect(value, self.p + 1))
        answer.extend(tail.get(i, Q(0)) for i, h in enumerate(m.hall)
                      if h['weight'] > self.p)
        assert len(answer) == len(self.klogs)
        return answer

    def auto(self, label, correction):
        return Auto(self, self.special[label], correction)


class Auto:
    def __init__(self, weighted, generator, correction):
        self.a, self.m = weighted, weighted.m
        self.generator, self.correction = generator, correction
        weight = weighted.generators[generator]['weight']
        assert correction and min(map(len, correction)) > weight
        # Membership in the rational Lie algebra is mandatory.
        weighted.basis.coordinates(correction)
        self.images = []
        for node in weighted.nodes:
            if node['pair'] is None:
                value = node['value']
                if node['generator'] == generator:
                    value = add(value, correction)
            else:
                i, j = node['pair']
                value = self.m.bracket(self.images[i], self.images[j])
            self.images.append(value)
        self._chains = {}

    def apply(self, value):
        coordinates = self.a.basis.coordinates(value)
        out = {}
        for i, coefficient in coordinates.items():
            out = add(out, self.images[i], coefficient)
        return out

    def chain(self, value):
        cachekey = tuple(sorted(value.items()))
        if cachekey not in self._chains:
            sequence, current = [value], value
            for _ in range(self.m.degree + 1):
                current = add(self.apply(current), current, -1)
                if not current:
                    break
                sequence.append(current)
            else:
                raise AssertionError('Map is not unipotent')
            self._chains[cachekey] = sequence
        return self._chains[cachekey]

    def power_on(self, value, n):
        out, coefficient = {}, Q(1)
        for k, term in enumerate(self.chain(value)):
            if k:
                coefficient *= Q(n-k+1, k)
            out = add(out, term, coefficient)
        return out

    def integral_power(self, maximum_factorial=12):
        """Bounded test wrapper; exceeding bound is inconclusive, never no."""
        failures = []
        power = 1
        for k in range(1, maximum_factorial + 1):
            power *= k
            bad = None
            for sign in (1, -1):
                for i, value in enumerate(self.a.klogs):
                    coordinates = self.a.kcoordinates(self.power_on(value, sign*power))
                    nonintegral = [(j, str(x)) for j, x in enumerate(coordinates)
                                   if x.denominator != 1]
                    if nonintegral:
                        bad = dict(power=power, sign=sign, generator=i,
                                   nonintegral=nonintegral)
                        break
                if bad:
                    break
            if bad is None:
                return power, failures
            failures.append(bad)
        raise RuntimeError('Bounded power search inconclusive; increase bound', failures)

    def check_lie(self):
        checks = 0
        for i, a in enumerate(self.a.nodes):
            for j, b in enumerate(self.a.nodes[:i]):
                if a['weight'] + b['weight'] > self.m.degree:
                    continue
                assert self.apply(self.m.bracket(a['value'], b['value'])) == \
                    self.m.bracket(self.images[i], self.images[j])
                checks += 1
        return checks


def integral_terms(m, logvalue):
    terms = m.collect(m.exp(logvalue))
    assert all(x.denominator == 1 for _, x in terms)
    return [[i, int(x)] for i, x in terms]
