def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Элемент найден на позиции: {result}")
else:
    print("Элемент не найден")