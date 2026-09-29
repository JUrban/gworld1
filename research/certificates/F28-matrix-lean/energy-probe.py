import sympy as s
A,B,C,D=s.symbols('a b c d')
M=s.Matrix([[A,B],[C,D]])
Q=s.Matrix([[0,-1],[2,1]])
P=s.Matrix([[4,1],[1,2]])
E=s.expand(s.trace(P.adjugate()*M.T*P*M))
print('E =',E)
V=Q*M*Q.inv()
print('conjugate =',V)
print('invariance =',s.expand(E.xreplace(dict(zip([A,B,C,D],list(V))))-E))
variables=s.Matrix([A,B,C,D]);H=s.hessian(E,variables)/2
L,DD=H.LDLdecomposition(hermitian=False)
print('LDL',L,DD)
print('squares',L.T*variables)
