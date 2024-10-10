def add_even_column(matrix):
    new_column = []
    
    for row in matrix:
        count_ones = row.count(1)
        new_column.append(0 if count_ones % 2 == 0 else 1)

    for i in range(len(matrix)):
        matrix[i].append(new_column[i])
    
    return matrix

matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 1],
    [1, 0, 0]
]

updated_matrix = add_even_column(matrix)

for row in updated_matrix:
    print(row)
