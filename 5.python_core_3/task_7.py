from collections import Counter

def check_uniqueness(numbers):
    # Используем Counter для подсчета количества каждого элемента
    count = Counter(numbers)
    
    # Проверяем, все ли элементы уникальны
    all_unique = all(value == 1 for value in count.values())

    if all_unique:
        print("Все числа уникальны.")
    else:
        print("Есть дублирующиеся элементы:")
        for num, freq in count.items():
            if freq > 1:
                print(f"Число {num}, количество повторений {freq}")

# Пример использования:
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
check_uniqueness(numbers)