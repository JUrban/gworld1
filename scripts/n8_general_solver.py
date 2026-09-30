#!/usr/bin/env python3
"""Complete integral recursion of the N8 candidate, on exact Magnus inputs.

There is no search cutoff in the mathematical procedure. External timeout or
resource failure is an incomplete run, never a negative answer. Completeness
uses the written general proof's structural kernel and separation lemmas.
"""
from copy import copy
from functools import reduce
from itertools import product
from math import gcd
from fractions import Fraction as Q
import sympy as S

from n8_class3 import ONE, smith
from n8_central import add, bracket
from n8_component_linear import affine_solution
from n8_penultimate import lie_tensor
from n8_projective_leading_pairs import leading_pairs
from n8_weighted_automorphisms import Basis
from n8_exact_universal_periods import Group, exact_period
from parametric_integer_linear import T, integer_solve, integer_roots, encode_poly


class GeneralSolver:
    def __init__(self, m, target, emit=None):
        self.m, self.target = m, target
        self.events = []
        self.emit = emit
        self.branch = None

    def record(self, event, **data):
        row = dict(event=event, branch=self.branch, **data)
        self.events.append(row)
        if self.emit:
            self.emit(row)

    def prefix(self, pair):
        return [self.coordinates(g, 1, self.m.degree) for g in pair]

    def view(self, end):
        m = copy(self.m)
        m.degree = end
        return m

    def truncate(self, g, end):
        return {w: x for w, x in g.items() if len(w) <= end}

    def axes(self, start, stop=None):
        if stop is None:
            stop = start
        return [(side, self.p+offset if side == 0 else self.q+offset, j)
                for offset in range(start, stop+1) for side in (0, 1)
                for j in range(len(self.m.bydegree[[self.p, self.q][side]+offset]))]

    def correct(self, pair, axes, vector, end=None):
        m = self.m if end is None else self.view(end)
        answer = [self.truncate(g, m.degree) for g in pair]
        for (side, weight, j), value in zip(axes, vector):
            assert S.sympify(value).is_Integer
            if value:
                answer[side] = m.mul(answer[side], m.power(self.m.bydegree[weight][j]['value'], int(value)))
        return answer

    def coordinates(self, g, start, end):
        m = self.view(end)
        residual = self.truncate(g, end)
        assert all(not w or len(w) >= start for w in residual)
        out = []
        for weight in range(start, end+1):
            row = m.coordinates(m.layer(residual, weight), weight)
            out += row
            residual = m.mul(m.inv(m.lift(row, weight)), residual)
        assert residual == ONE
        return out

    def commutator(self, pair, end):
        m = self.view(end)
        return m.comm(*(self.truncate(g, end) for g in pair))

    def error(self, pair, start, end):
        m = self.view(end)
        value = m.mul(m.inv(self.commutator(pair, end)), self.truncate(self.target, end))
        return self.coordinates(value, start, end)

    def affine_block(self, pair, start, stop):
        assert stop < 2*start
        end = self.d+stop
        m = self.view(end)
        axes = self.axes(start, stop)
        base = self.commutator(pair, end)
        inverse = m.inv(base)
        rhs = self.error(pair, self.d+start, end)
        columns = []
        for j in range(len(axes)):
            unit = [int(i == j) for i in range(len(axes))]
            value = self.commutator(self.correct(pair, axes, unit, end), end)
            columns.append(self.coordinates(m.mul(inverse, value), self.d+start, end))
        A = S.Matrix(len(rhs), len(axes), lambda i, j: columns[j][i])
        # Additional joint evaluation checks signed simultaneous increments.
        v = [(-1)**j*(j%3+1) for j in range(len(axes))]
        value = self.commutator(self.correct(pair, axes, v, end), end)
        actual = self.coordinates(m.mul(inverse, value), self.d+start, end)
        assert actual == list(A*S.Matrix(len(v), 1, v))
        return axes, A, S.Matrix(len(rhs), 1, rhs), integer_solve(A, S.Matrix(len(rhs), 1, rhs))

    def homogeneous(self, offset):
        axes = self.axes(offset)
        polys = []
        for side, weight, j in axes:
            e = self.m.layer(self.m.bydegree[weight][j]['value'], weight)
            polys.append(bracket(self.m, e, self.D) if side == 0 else bracket(self.m, self.C, e))
        columns = [self.m.coordinates(v, self.d+offset) for v in polys]
        dim = len(self.m.bydegree[self.d+offset])
        return axes, S.Matrix(dim, len(axes), lambda i, j: columns[j][i])

    def period(self, offset, vector):
        axes, _ = self.homogeneous(offset)
        if self.p < self.q and offset == self.q-self.p:
            direction = list(self.dc)+[0]*len(self.m.bydegree[self.q+offset])
            solution = affine_solution([list(map(int, vector))], direction)
            assert solution is not None and not solution[1] and solution[0][0]
            power = abs(solution[0][0])
            return dict(offset=offset, power=power, method='exact-Nielsen', direction=direction)
        if self.universal is None:
            w = Group(self.p, self.q, self.m.degree)
            values = [self.C, self.D]
            for h in w.hall[2:]:
                i, j = h['pair']
                values.append(bracket(self.m, values[i], values[j]))
            bases = {}
            for weight, (indices, _) in w.layers.items():
                b = Basis()
                for i in indices:
                    assert b.insert(values[i])
                bases[weight] = b
            self.universal = w, bases, w.darboux()
        w, bases, expansion = self.universal
        ambient = [{}, {}]
        for (side, weight, j), value in zip(axes, vector):
            ambient[side] = add(ambient[side], self.m.layer(self.m.bydegree[weight][j]['value'], weight), value)
        direction = []
        for side, weight in enumerate((self.p+offset, self.q+offset)):
            coefficients = bases[weight].coordinates(ambient[side])
            value = {}
            for j, x in coefficients.items():
                value = add(value, w.hall[w.layers[weight][0][j]]['lie'], Q(x))
            direction.append(value)
        result = exact_period(w, direction, offset, expansion)
        result.update(weights=[self.p, self.q], class_bound=self.m.degree,
            hall=[[h['weight'], list(h['pair']) if h['pair'] is not None else []] for h in w.hall])
        return result

    def recurse(self, pair, offset):
        if offset > self.n:
            assert self.m.comm(*pair) == self.target
            return pair
        if 2*offset > self.n:
            axes, A, rhs, solution = self.affine_block(pair, offset, self.n)
            self.record('linear-tail', offset=offset, columns=A.tolist(), rhs=list(rhs),
                        solution=None if solution is None else list(solution[0]),
                        axes=axes, prefix_coordinates=self.prefix(pair), weights=[self.p,self.q])
            if solution is None:
                return None
            answer = self.correct(pair, axes, solution[0])
            assert self.m.comm(*answer) == self.target
            return answer
        axes, A = self.homogeneous(offset)
        rhs = S.Matrix(self.error(pair, self.d+offset, self.d+offset))
        solution = integer_solve(A, rhs)
        if solution is None:
            self.record('linear-obstruction', offset=offset, columns=A.tolist(), rhs=list(rhs),
                        axes=axes, prefix_coordinates=self.prefix(pair), weights=[self.p,self.q])
            return None
        point, kernel = solution
        if not kernel.cols:
            self.record('unique-layer', offset=offset, point=list(point))
            return self.recurse(self.correct(pair, axes, point), offset+1)
        if offset >= self.q-self.p:
            periods = [self.period(offset, kernel[:, j]) for j in range(kernel.cols)]
            self.record('period-layer', offset=offset, point=list(point), kernel=kernel.tolist(), periods=periods)
            for residue in product(*(range(row['power']) for row in periods)):
                vector = point+kernel*S.Matrix(list(residue))
                self.record('period-residue', offset=offset, residue=list(residue))
                answer = self.recurse(self.correct(pair, axes, vector), offset+1)
                if answer is not None:
                    return answer
            return None
        assert kernel.cols == 1, 'Written pre-Nielsen kernel bound failed'
        block_axes, B, beta, block = self.affine_block(pair, offset, 2*offset-1)
        self.record('exception-block', offset=offset, axes=block_axes, columns=B.tolist(), rhs=list(beta),
                    point=None if block is None else list(block[0]),
                    kernel=None if block is None else block[1].tolist(),
                    prefix_coordinates=self.prefix(pair), weights=[self.p,self.q])
        if block is None:
            return None
        point, directions = block
        first = len(axes)
        row = []
        for j in range(directions.cols):
            coefficient = integer_solve(kernel, directions[:first, j])
            assert coefficient is not None and not coefficient[1].cols
            row.append(coefficient[0][0])
        if not any(row):
            self.record('fixed-exception', offset=offset, point=list(point[:first, 0]))
            return self.recurse(self.correct(pair, axes, point[:first, 0]), offset+1)
        D, U, V = smith(S.Matrix([row]))
        adapted = directions*V
        assert not any(adapted[:first, 1:]) and any(adapted[:first, 0])
        end = self.d+2*offset

        def value(vector):
            return S.Matrix(self.error(self.correct(pair, block_axes, vector, end), end, end))

        q0 = value(point)
        rplus, rminus = value(point+adapted[:, 0]), value(point-adapted[:, 0])
        q1, q2 = (rplus-rminus)/2, (rplus+rminus)/2-q0
        assert value(point+2*adapted[:, 0]) == q0+2*q1+4*q2
        _, correction = self.homogeneous(2*offset)
        columns = correction.row_join(S.Matrix.hstack(*(value(point+adapted[:, j])-q0
                   for j in range(1, adapted.cols))) if adapted.cols > 1 else S.zeros(correction.rows, 0))
        functional = next((v for v in columns.T.nullspace() if (v.T*q2)[0] != 0), None)
        assert functional is not None, 'Written full-block separation failed'
        polynomial = (functional.T*(q0+T*q1+T*T*q2))[0]
        roots = integer_roots(polynomial)
        self.record('quadratic-exception', offset=offset, adapted_kernel=adapted.tolist(),
                    parameter_step=int((S.Matrix([row])*V)[0]), functional=list(functional),
                    coefficients=[list(q0), list(q1), list(q2)], annihilated_columns=columns.tolist(),
                    polynomial=encode_poly(polynomial), integer_roots=roots)
        for root in roots:
            prefix = (point+root*adapted[:, 0])[:first, 0]
            answer = self.recurse(self.correct(pair, axes, prefix), offset+1)
            if answer is not None:
                return answer
        return None

    def solve(self):
        if self.target == ONE:
            self.record('identity-target')
            return [dict(ONE), dict(ONE)]
        self.d = min(len(w) for w in self.target if w)
        if self.d == 1:
            self.record('abelianization-obstruction')
            return None
        self.n = self.m.degree-self.d
        leading = self.m.layer(self.target, self.d)
        branch = 0
        for p in range(1, self.d//2+1):
            q = self.d-p
            pairs, trace = leading_pairs(self.m, leading, p, q)
            self.record('complete-leading-list', weights=[p, q], pairs=pairs, trace=trace)
            for cc, dd in pairs:
                self.branch = branch
                branch += 1
                self.p, self.q, self.dc = p, q, dd
                self.C, self.D = lie_tensor(self.m, cc, p), lie_tensor(self.m, dd, q)
                self.universal = None
                pair = self.m.lift(cc, p), self.m.lift(dd, q)
                answer = self.recurse(pair, 1)
                if answer is not None:
                    assert self.m.comm(*answer) == self.target
                    self.record('positive-commutator')
                    return answer
        self.record('all-leading-branches-rejected', count=branch)
        return None
