def find_min_max(matrix):
    min_value = float('inf')
    max_value = float('-inf')
    min_index = (-1, -1)
    max_index = (-1, -1)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)
    
    return min_value, min_index, max_value, max_index

matrix = [
    [12, 34, 56, 78],
    [90, 23, 45, 67],
    [89, 10, 11, 13]
]

min_value, min_index, max_value, max_index = find_min_max(matrix)

print(f"Минимальный элемент: {min_value}, Индексы: {min_index}")
print(f"Максимальный элемент: {max_value}, Индексы: {max_index}")