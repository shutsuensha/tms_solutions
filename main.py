def create_matrix(n):
    start = 100 
    step = 2    
    matrix = []  

    for i in range(n):
        row = []
        for j in range(n):
            row.append(start)
            start += step
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("  ".join(map(str, row)))


n = int(input("Введите размер матрицы: "))
matrix = create_matrix(n)
print_matrix(matrix)