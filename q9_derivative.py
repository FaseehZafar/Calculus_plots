from sympy import symbols, diff, sqrt, exp

t = symbols('t')
f = ((sqrt(t) * (3*t + t*5 - 10)) + (t3 - exp(t))) / t*2

df_dt = diff(f, t)

print("The derivative of the function f(t) is:")
print(df_dt)

