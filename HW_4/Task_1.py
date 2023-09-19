"""
Напишите функцию для транспонирования матрицы
"""

def transpose_matrix(matrix: list) -> list:
    len_column = len(matrix)
    len_rows = len(matrix[0])
    result = [[0] * len_column for i in range(len_rows)]
    for i in range(len_rows):
        for j in range(len_column):
            result[i][j] = matrix[j][i]
    return result

matrix = [[1,2,3],[3,4,5],[3,4,5]]
for i in matrix:
    print(i)
transposed_matrix = transpose_matrix(matrix)
print('===========')
for i in transposed_matrix:
    print(i)