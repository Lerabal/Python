# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint
n = int(input("Введите количество элементов массива "))
x = int(input("Введите число "))
list_1 = [randint(1, 48) for _ in range(n)]
print(list_1)
list_2=[abs(list_1[i]-x) for i in range(len(list_1))]
print(list_1[list_2.index(min(list_2))])