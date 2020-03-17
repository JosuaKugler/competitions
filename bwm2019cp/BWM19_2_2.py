from sympy import *
a, b, c = symbols('a b c')
expression = a*b/c+b*c/a+a*c/b
newexpression = expression.subs(c, sqrt(1-a**2-b**2))
diffa = diff(newexpression, a)
diffb = diff(newexpression, b)

asolutions = solve(diffa, a)
solutions = []
for solution in asolutions:
    temp = diffb.subs(a, solution)
    bsolutions = solve(temp,b)
    for possibility in bsolutions:
        if possibility > 0:
            avalue = solution.subs(b, possibility)
            if avalue > 0:
                solutions.append((avalue, possibility))       

minima = []
diffaa = diff(diffa, a)
diffba = diff(diffb, a)
diffbb = diff(diffb, b)
for solution in solutions:
    valueaa = diffaa.subs(a, solution[0])
    valueaa = valueaa.subs(b, solution[1])
    valueba = diffba.subs(a, solution[0])
    valueba = valueba.subs(b, solution[1])
    valuebb = diffbb.subs(a, solution[0])
    valuebb = valuebb.subs(b, solution[1])
    discriminant = valueaa*valuebb-valueba**2
    if discriminant > 0:
        if valueaa > 0:
            minima.append(solution)

print(minima)