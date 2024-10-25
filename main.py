def find_columns_with_value(matrix, H):
    M = len(matrix)
    N = len(matrix[0])

    columns_with_H = []
    columns_without_H = []


    for j in range(N):
        has_H = False
        for i in range(M):
            if matrix[i][j] == H:
                has_H = True
                break
        if has_H:
            columns_with_H.append(j)
        else:
            columns_without_H.append(j)
    
    return columns_with_H, columns_without_H

matrix = [
    [12, 34, 56],
    [90, 23, 45],
    [89, 10, 11],
    [34, 23, 56]
]

H = 34
columns_with_H, columns_without_H = find_columns_with_value(matrix, H)

print(f"Столбцы, содержащие число {H}: {columns_with_H}")
print(f"Столбцы, не содержащие число {H}: {columns_without_H}")