def sum_diagonals(matrix):
    M = len(matrix)
    N = len(matrix[0])
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(M):
        if i < N:
            main_diagonal_sum += matrix[i][i]
        if i < N:
            secondary_diagonal_sum += matrix[i][N - 1 - i]

    return main_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_sum, secondary_sum = sum_diagonals(matrix)

print(f"Сумма элементов главной диагонали: {main_sum}")
print(f"Сумма элементов побочной диагонали: {secondary_sum}")