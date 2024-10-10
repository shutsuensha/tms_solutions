def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


number = 52
if is_prime(number):
    print(f"Число {number} является простым")
else:
    print(f"Число {number} не является простым")
