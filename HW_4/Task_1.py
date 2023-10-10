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


def trans_matrix_zip(matrix: list):
    return list(zip(*matrix))

matrix = [[99, 72, 11, 93], [24, 36, 33, 60], [97, 81, 91, 39], [97, 43, 75, 85], [29, 56, 33, 68]]
for i in matrix:
    print(i)
transposed_matrix = transpose_matrix(matrix)
print('===========')
for i in transposed_matrix:
    print(i)
transposed_matrix = trans_matrix_zip(matrix)
print('===========')
for i in transposed_matrix:
    print(i)