# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# from random import randint

# lo, hi = 3, 8
# data = [randint(1, 10) for _ in range(20)]
# print("Массив:", data, sep='\n')
# indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
# print("Ин:", indexes, sep='\n')
# result = []
# i = len(indexes)
# while i :
#     i -= 1
#     result.append(data.pop(indexes[i]))
# print("Остальные элементы:", data, sep='\n')
# print("Обязательные элементы:", result, sep='\n')

from random import randint


def FillArray(arraySize):
    return [randint(-8, 15) for i in range(arraySize)]


len_array1 = int(input("Введите количество элементов  массива "))
array1 = FillArray(len_array1)
print(array1)
min_1 = int(input("Введите диапазон от (min) "))
max_1 = int(input("Введите диапазон до (max) "))
indexes = [i for i, v in enumerate(array1) if min_1 <= v <= max_1]
print (f"Индексы чисел лежащих в диапазоне от {min_1} до {max_1} = {indexes}")

