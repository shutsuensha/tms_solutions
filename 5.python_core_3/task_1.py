def create_matrix(n):
    start = 100  
    step = 2     
    matrix = []  

    # Заполняем матрицу
    for i in range(n):
        row = []
        for j in range(n):
            row.append(start)
            start += step
        matrix.append(row)

    return matrix

n = int(input("Введите размер матрицы: "))
matrix = create_matrix(n)

# Печать матрицы
for row in matrix:
    print(row)