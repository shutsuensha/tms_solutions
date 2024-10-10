def list_statistics(numbers):
    # Находим сумму, минимальное и максимальное значение
    total_sum = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return total_sum, minimum, maximum


numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

total_sum, minimum, maximum = list_statistics(numbers)

# Печатаем результаты
print(f"Сумма всех чисел: {total_sum}")
print(f"Минимальное число: {minimum}")
print(f"Максимальное число: {maximum}")