from sympy import Function, symbols, init_printing, Eq, Derivative,  pprint, dsolve, exp, latex, cos
def solve_ode(eqn):
    soln = dsolve(eqn)
    init_printing()
    print("The given equation is :")
    pprint(eqn)
    print("The solution of the equation is :")
    pprint(soln)
    print(latex(eqn))
    print(latex(soln))
    with open("tex_output.tex", "w") as file:
        file.write(latex(eqn)+ "\n")
        file.write(latex(soln)+"\n")


x = symbols('x')
y = Function('y')(x)
# solve_ode(eqn=Eq(Derivative(y,x) - y**2, 2), dep = ['y'], indep = ['x'])
solve_ode(eqn=Eq(Derivative(y,x, 4) + Derivative(y,x, 3) + Derivative(y,x, 2), 5*x**2 + cos(x)))

