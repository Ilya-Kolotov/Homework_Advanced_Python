"""
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""
import math


def is_simple_number(num: int):
    if num == 2:
        return True
    elif not num % 2:
        return  False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        else:
            return True

def gen_simple_number():
    num = 2
    while True:
        if is_simple_number(num):
            yield num
        num += 1

# print(is_simple_number(17))
simple_number = gen_simple_number()
for _ in range(15):
    print(next(simple_number))

