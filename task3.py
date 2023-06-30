# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

def double_list(array: list[int]) -> list[int]:
    res = set()
    for item in array:
        counter = array.count(item)
        if counter > 1:
            res.add(item)
    return list(res)

print(double_list([2, 2, 3, 3, 4, 'g', 'g', 100]))