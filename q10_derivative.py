from sympy import symbols, diff, exp, sin, ln

x = symbols('x')
f = 4 * exp(2*x) - sin(3*x) + 5 * x**3 - ln(2*x)

d1 = diff(f, x)
d2 = diff(f, x, 2)
d3 = diff(f, x, 3)
d4 = diff(f, x, 4)

print("First derivative of f(x):")
print(d1)

print("\nSecond derivative of f(x):")
print(d2)

print("\nThird derivative of f(x):")
print(d3)

print("\nFourth derivative of f(x):")
print(d4)
