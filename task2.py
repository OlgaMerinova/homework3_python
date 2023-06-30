# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict_friends_atribute = {"Олег": ("палатка", "рюкзак", "панама", "спальный мешок", "очки"), \
                        "Василий": ("спальный мешок", "рюкзак", "матрас","кошелек", "спрей от комаров"), \
                        "Иван": ("рюкзак", "очки", "маска для сна", "компас", "сапоги")}


all_items_set = list(dict_friends_atribute.values())
must_have_item = set(all_items_set[0])

for items in all_items_set:
    must_have_item = must_have_item.intersection(set(items))

print(f'Вещи, которые есть у всех друзей: {must_have_item}')
print()

for key, value in dict_friends_atribute.items():
    result = set(value)
    for key_tmp, value_tmp in dict_friends_atribute.items():
        if key != key_tmp:
            result -= set(value_tmp)
    print(f'Вещи, которые есть только у {key}: {result}')
print()

for key, value in dict_friends_atribute.items():
    result1 = set()
    count = 1
    for key_tmp, value_tmp in dict_friends_atribute.items():
        if key != key_tmp:
            if count == 1:
                result = set(value_tmp)
            else:
                result &= set(value_tmp)
            count += 1
    for element in result:
        if element not in value:
            print(f'У друга {key} нет вещи {element}, а у остальных есть')





