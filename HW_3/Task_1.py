"""
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

count_friends = int(input('Сколько друзей пошло в поход?\n'))
hike_dict = {}
items_list = []
while count_friends > 0:
    name = input('Введите имя: ')
    items = input('Что он взял с собой?\n').split(',')
    hike_dict[name] = tuple(items)
    items_list += items
    count_friends -= 1
names = []
for name in hike_dict:
    names.append(name)
common_items = set(hike_dict[names[0]])
for i in range(len(names) - 1):
    common_items = common_items & set(hike_dict[names[i+1]])
unique_items = set(hike_dict[names[0]])
for i in range(len(names)-1):
    unique_items = unique_items ^ set(hike_dict[names[i+1]])
for i in set.copy(unique_items):
    if items_list.count(i) > 1:
        unique_items.discard(i)
print('Вещи, которые взяли все друзья -', *common_items)
print('Уникальные вещи -', *unique_items)
for key in hike_dict:
    other_friends = list(set(hike_dict.keys()) - set(key))
    items = set(hike_dict[key])
    common_items = set(hike_dict[other_friends[0]])
    for i in range(len(other_friends) - 1):
        common_items = common_items & set(hike_dict[other_friends[i+1]])
    common_items_exept_one = common_items - items
    if common_items_exept_one:
        print(f'У всех, кроме {key} есть вещи', *common_items_exept_one)
