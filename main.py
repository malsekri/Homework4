def QuadraticFormula1(a,b,c):
    y = ((-b+(b**2-4*a*c)**0.5)/2*a)
    return y
print(QuadraticFormula1(1,2,-3))

def QuadraticFormula2(a,b,c):
    y = ((-b-(b**2-4*a*c)**0.5)/2*a)
    return y
print(QuadraticFormula2(1,2,-3))