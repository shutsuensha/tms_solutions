def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Возвращаем индекс, если нашли элемент
        elif arr[mid] < target:
            left = mid + 1  # Продолжаем поиск в правой половине
        else:
            right = mid - 1  # Продолжаем поиск в левой половине

    return -1  # Если элемент не найден

numbers = list(map(int, input("Введите отсортированный список чисел через пробел: ").split()))
target = int(input("Введите искомое число: "))

position = binary_search(numbers, target)

if position != -1:
    print(f"Элемент найден на позиции: {position}")
else:
    print("Элемент не найден в списке.")