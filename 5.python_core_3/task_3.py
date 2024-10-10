def transpose_matrix(matrix):
    
    transposed = [list(row) for row in zip(*matrix)]
    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print(row)