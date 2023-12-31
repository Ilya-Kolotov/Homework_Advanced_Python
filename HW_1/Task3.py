"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
while True:
    num = int(input('Введите число: '))
    if 0 < num < 100_000:
        if num == 1:
            print(f'Число {num} не является простым или составным')
        else:
            count = 0
            while count == 0:
                for i in range(2, num):
                    if num % i == 0:
                        count += 1
                count += 1
            if count > 1:
                print(f'Число {num} является составным')
            else:
                print(f'Число {num} является простым')
        break
