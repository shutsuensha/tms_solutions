import random

def create_random_matrix(M, N, min_value=0, max_value=100):
    matrix = []
    for _ in range(M):
        row = [random.randint(min_value, max_value) for _ in range(N)]
        matrix.append(row)
    return matrix

M = 3  
N = 4 
matrix = create_random_matrix(M, N)

# Выводим матрицу
for row in matrix:
    print(row)