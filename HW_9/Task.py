"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

from random import choice, randint
import csv
import json


def read_csv(path: str = 'num.csv'):
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, dialect='excel', delimiter=';')
        for row in reader:
            if row:
                result.append(tuple(map(float, row)))
    return result


def write_to_json(result: dict, path: str = 'result.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def deco(func):
    num_list = read_csv()

    def wrapper():
        result = {}
        for abc in num_list:
            roots = func(abc)
            a, b, c = abc
            result[f'{a=}, {b=}, {c=}'] = roots
        return result

    return wrapper


def deco_json(func):
    def wrapper():
        roots = func()
        write_to_json(roots)
        return roots

    return wrapper


def generate_nums(count: int):
    result_nums = []
    for _ in range(count):
        result_nums.append((choice([*range(-100, 0), *range(1, 101)]), randint(-100, 100), randint(-100, 100)))
    with open('num.csv', 'w', encoding='utf-8') as file:
        csv.writer(file, dialect='excel', delimiter=';').writerows(result_nums)


@deco_json
@deco
def quadratic_equation(nums: tuple):
    a, b, c = nums
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discr == 0:
        return (round(-b / (2 * a), 2),)
    else:
        return (None,)


generate_nums(500)
print(quadratic_equation())
