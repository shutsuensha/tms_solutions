def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 12
b = 18
result = gcd(a, b)
print(f"НОД чисел {a} и {b}: {result}")