def decimal_to_binary_recursive(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2)

number = 13
binary_representation = decimal_to_binary_recursive(number)
print(f"Двоичное представление числа {number}: {binary_representation}")