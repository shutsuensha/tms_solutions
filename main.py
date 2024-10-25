def calculate_column_percentages(matrix):
    total_sum = sum(sum(row) for row in matrix)
    
    M = len(matrix)
    N = len(matrix[0])
    
    column_sums = [0] * N
    
    for i in range(M):
        for j in range(N):
            column_sums[j] += matrix[i][j]
    
    column_percentages = [(column_sum / total_sum) * 100 for column_sum in column_sums]
    
    return total_sum, column_sums, column_percentages


matrix = [
    [12, 34, 56],
    [90, 23, 45],
    [89, 10, 11]
]

total_sum, column_sums, column_percentages = calculate_column_percentages(matrix)

print(f"Общая сумма элементов матрицы: {total_sum}")
print(f"Суммы элементов по столбцам: {column_sums}")
print(f"Процентные доли по столбцам: {column_percentages}")