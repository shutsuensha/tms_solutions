import math

a = 2
b = 4
y = a**2 / 3 + (a**2 + 4) / b + ((a**2 + 4) ** 0.5) / 4 + ((a**2 + 4)**3)**0.5 / 4
print(f"{y=}")


x = 2
y = (math.cos(x**2)**2 + math.sin(2*x - 1)**2) ** (1/3)
print(f"{y=}")

y = math.cos(x) + math.sin(x)
print(f"{y=}")

y = 5*x + 3*x**2*(1 + math.sin(x)**2)**0.5
print(f"{y=}")