#!/usr/bin/env python3
"""N5 class-two coordinate-input algorithm, including arbitrary finite torsion.

quotient_orders and center_orders use 0 for infinite order, followed by
finite orders >=2. beta[i][j] is [x_i,x_j] in the full center; powers[i]
is x_i^quotient_orders[i] for a finite quotient coordinate, and zero for
an infinite one. This is not an arbitrary finite-presentation interface.
"""
from itertools import product
from sympy import Matrix, Rational, eye, zeros
from sympy.matrices.normalforms import hermite_normal_form
from n8_class3 import smith
from n5_class2_torsionfree import integral_image
from n5_rational_lie_decomposition import decompose
from n5_central_constraints import (finite_idempotents, split,
    relation_constraints, lifting_corrections, satisfies)


def integer_kernel(a):
    if not a.cols:
        return zeros(0, 0)
    if not a.rows:
        return eye(a.cols)
    d, _, v = smith(a)
    rank = sum(d[i, i] != 0 for i in range(min(d.shape)))
    return v[:, rank:]


def relation_lattice(generators, orders):
    n, k = len(orders), len(generators)
    if not k:
        return zeros(0, 0)
    finite = [i for i, d in enumerate(orders) if d]
    a = Matrix.hstack(*(Matrix(v) for v in generators))
    extra = zeros(n, len(finite))
    for j, i in enumerate(finite):
        extra[i, j] = -orders[i]
    projected = integer_kernel(a.row_join(extra))[:k, :]
    return hermite_normal_form(projected)


class ClassTwo:
    def __init__(self, quotient_orders, center_orders, beta, powers):
        self.qo, self.zo = list(quotient_orders), list(center_orders)
        self.r, self.s = len(self.qo), len(self.zo)
        self.rf, self.sf = self.qo.count(0), self.zo.count(0)
        for orders in (self.qo, self.zo):
            free = orders.count(0)
            if any(d != 0 for d in orders[:free]) or any(d < 2 or int(d) != d for d in orders[free:]):
                raise ValueError('orders must be free-first, then finite >=2')
        if len(beta) != self.r or any(len(row) != self.r or any(len(v) != self.s for v in row) for row in beta):
            raise ValueError('invalid beta dimensions')
        if len(powers) != self.r or any(len(v) != self.s for v in powers):
            raise ValueError('invalid power dimensions')
        for v in [v for row in beta for v in row]+list(powers):
            if any(Rational(x).q != 1 for x in v):
                raise ValueError('nonintegral coordinate')
        self.beta = [[self.central(v) for v in row] for row in beta]
        self.powers = [self.central(v) for v in powers]
        for i in range(self.r):
            if any(self.beta[i][i]):
                raise ValueError('nonalternating beta')
            if not self.qo[i] and any(self.powers[i]):
                raise ValueError('infinite quotient coordinate has a power relation')
            for j in range(self.r):
                if any(self.central([a+b for a, b in zip(self.beta[i][j], self.beta[j][i])])):
                    raise ValueError('nonalternating beta')
                if self.qo[i] and any(self.central([self.qo[i]*x for x in self.beta[i][j]])):
                    raise ValueError('power-commutator inconsistency')
        # Exact integer kernel of all commutator equations/congruences.
        rows, moduli = [], []
        for j in range(self.r):
            for k in range(self.s):
                rows.append([self.beta[i][j][k] for i in range(self.r)])
                moduli.append(self.zo[k])
        finite = [i for i, m in enumerate(moduli) if m]
        a = Matrix(len(rows), self.r, sum(rows, []))
        extra = zeros(len(rows), len(finite))
        for col, row in enumerate(finite):
            extra[row, col] = -moduli[row]
        kernel = integer_kernel(a.row_join(extra))[:self.r, :]
        for j in range(kernel.cols):
            if any((kernel[i,j] != 0 if not d else kernel[i,j] % d != 0)
                   for i,d in enumerate(self.qo)):
                raise ValueError('specified center is not full')

    def central(self, vector):
        return [int(x) % d if d else int(x) for x, d in zip(vector, self.zo)]

    def normalize(self, u, z):
        u, z = list(map(int,u)), list(map(int,z))
        for i, d in enumerate(self.qo):
            if d:
                carry, u[i] = divmod(u[i], d)
                z = [a+carry*b for a,b in zip(z,self.powers[i])]
        return u+self.central(z)

    def identity(self):
        return [0]*(self.r+self.s)

    def lift(self, u):
        return self.normalize(u, [0]*self.s)

    def multiply(self, a, b):
        u, v = a[:self.r], b[:self.r]
        z = [a[self.r+k]+b[self.r+k]+sum(u[i]*v[j]*self.beta[i][j][k]
             for i in range(self.r) for j in range(i)) for k in range(self.s)]
        return self.normalize([x+y for x,y in zip(u,v)], z)

    def inverse(self, a):
        u = a[:self.r]
        z = [-a[self.r+k]+sum(u[i]*u[j]*self.beta[i][j][k]
             for i in range(self.r) for j in range(i)) for k in range(self.s)]
        return self.normalize([-x for x in u], z)

    def power(self, a, exponent):
        exponent = int(exponent)
        if exponent < 0:
            a, exponent = self.inverse(a), -exponent
        out = self.identity()
        while exponent:
            if exponent & 1:
                out = self.multiply(out, a)
            a = self.multiply(a, a)
            exponent //= 2
        return out

    def commutator(self, u, v):
        return self.central([sum(u[i]*v[j]*self.beta[i][j][k]
                            for i in range(self.r) for j in range(self.r)) for k in range(self.s)])

    def presentation(self, quotient_generators):
        k = len(quotient_generators)
        lifts = [self.lift(v) for v in quotient_generators]
        rels = relation_lattice(quotient_generators, self.qo)
        exponents, defects = [], []
        for col in range(rels.cols):
            row = list(rels[:, col])
            value = self.identity()
            for a, power in zip(lifts, row):
                value = self.multiply(value, self.power(a, power))
            assert not any(value[:self.r])
            exponents.append(row)
            defects.append(value[self.r:])
        for i in range(k):
            for j in range(i+1, k):
                exponents.append([0]*k)
                defects.append(self.commutator(quotient_generators[i], quotient_generators[j]))
        return dict(generators=quotient_generators, lifts=lifts,
                    relation_basis=rels, exponents=exponents, defects=defects)


def decide(quotient_orders, center_orders, beta, powers):
    g = ClassTwo(quotient_orders, center_orders, beta, powers)
    r, s, nf, nz = g.r, g.s, g.rf, g.sf
    n = nf+nz
    lie = [[[0]*n for _ in range(n)] for _ in range(n)]
    for i in range(nf):
        for j in range(nf):
            lie[i][j][nf:] = g.beta[i][j][:nz]
    rational = decompose(lie)
    torsion_orders = g.qo[nf:]
    nt = len(torsion_orders)
    elements = list(product(*(range(d) for d in torsion_orders)))
    rational_seen, quotient_seen = set(), set()
    branches, quotient_obstructions = [], []
    witness = None
    for mask in product((0,1), repeat=len(rational['projections'])):
        p = sum((take*p for take,p in zip(mask,rational['projections'])),zeros(n))
        q = p[:nf,:nf]
        if tuple(q) in rational_seen:
            continue
        rational_seen.add(tuple(q))
        a, b = integral_image(q), integral_image(eye(nf)-q)
        index = abs(int(a.row_join(b).det()))
        if index != 1:
            quotient_obstructions.append(dict(projection=q,bases=[a,b],index=index))
            continue
        assert all(Rational(x).q == 1 for x in q)
        for pt in finite_idempotents(torsion_orders):
            for values in product(elements,repeat=nf):
                shear = Matrix.hstack(*(Matrix(v) for v in values)) if nt and nf else zeros(nt,nf)
                pk = Matrix.vstack(Matrix.hstack(q,zeros(nf,nt)),
                    Matrix.hstack(shear*q-pt*shear,pt))
                key = tuple(int(pk[i,j]) if i<nf else int(pk[i,j])%torsion_orders[i-nf]
                            for i in range(r) for j in range(r))
                if key in quotient_seen:
                    continue
                quotient_seen.add(key)
                assert satisfies(pk,nf,torsion_orders,[])
                sides = []
                for free, finite in ((a,pt),(b,eye(nt)-pt)):
                    generators = [list(free[:,j])+list(shear*free[:,j]) for j in range(free.cols)]
                    generators += [[0]*nf+list(finite[:,j]) for j in range(nt)]
                    generators = [[int(x) if i<nf else int(x)%torsion_orders[i-nf]
                                  for i,x in enumerate(v)] for v in generators]
                    generators = list(dict.fromkeys(tuple(v) for v in generators if any(v)))
                    sides.append([list(v) for v in generators])
                branch = dict(projection=pk, quotient_generators=sides)
                branches.append(branch)
                cross = next(((i,j,g.commutator(u,v)) for i,u in enumerate(sides[0])
                              for j,v in enumerate(sides[1]) if any(g.commutator(u,v))),None)
                if cross is not None:
                    branch.update(outcome='cross_commutator_obstruction',cross_witness=cross)
                    continue
                presentations = [g.presentation(side) for side in sides]
                constraints = []
                for side,pr in enumerate(presentations,1):
                    constraints += relation_constraints(pr['exponents'],pr['defects'],nz,g.zo[nz:],side)
                central = split(nz,g.zo[nz:],constraints,tuple(not side for side in sides))
                branch.update(presentations=presentations,constraints=constraints)
                if central is None:
                    branch['outcome'] = 'central_lifting_obstruction'
                    continue
                factors, changes = [], []
                for side,pr in enumerate(presentations,1):
                    corrections = lifting_corrections(pr['exponents'],pr['defects'],len(pr['lifts']),nz,g.zo[nz:],side,central)
                    changes.append(corrections)
                    factor = [g.normalize(v[:r],[x+y for x,y in zip(v[r:],corr)]) for v,corr in zip(pr['lifts'],corrections)]
                    zproj = central if side==1 else eye(s)-central
                    factor += [[0]*r+g.central(zproj[:,j]) for j in range(s)]
                    factor = list(dict.fromkeys(tuple(v) for v in factor if any(v)))
                    factors.append([list(v) for v in factor])
                branch.update(outcome='decomposition',central_projection=central,
                              corrections=changes,factor_generators=factors)
                witness = len(branches)-1
                break
            if witness is not None:break
        if witness is not None:break
    return dict(quotient_orders=g.qo,center_orders=g.zo,beta=g.beta,powers=g.powers,
                lie_structure_constants=lie,rational=rational,
                answer=witness is not None,witness_branch=witness,
                rational_quotient_obstructions=quotient_obstructions,branches=branches)
