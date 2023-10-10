import random


class Triangle:
    def __init__(self, first_side, second_side, third_side):
        self.a = first_side
        self.b = second_side
        self.c = third_side

    def check_is_triangle(self):
        if self.a < self.b + self.c and self.b < self.c + self.a and self.c < self.a + self.b:
            length_type = 'Треугольник разносторонний'
            if self.a == self.b == self.c:
                length_type = 'Треугольник равносторонний'
            elif self.a == self.b or self.b == self.c or self.c == self.a:
                length_type = 'Треугольник равнобедренный'
            return f'Треугольник с такими сторонами существует. {length_type}'
        else:
            return 'Треугольник с такими сторонами не существует'


class Matrix:
    def __init__(self, count_rows: int, count_columns: int):
        self.rows = count_rows
        self.columns = count_columns
        self.matrix = [[random.randint(1, 100) for i in range(self.rows)] for j in range(self.columns)]

    def print_matrix(self):
        return self.matrix

    def trans_matrix_zip(self):
        return list(zip(*self.matrix))


matrix1 = Matrix(5, 5)
print(matrix1.print_matrix())
print(matrix1.trans_matrix_zip())

triangle1 = Triangle(10, 10, 8)
triangle2 = Triangle(10, 10, 10)
triangle3 = Triangle(10, 9, 8)
triangle4 = Triangle(10, 10, -8)
print(triangle1.check_is_triangle())
print(triangle2.check_is_triangle())
print(triangle3.check_is_triangle())
print(triangle4.check_is_triangle())
