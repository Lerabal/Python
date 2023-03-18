# Задача №17. Общее обсуждение
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# from random import randint
# list_1 = []
# n= int(input("Введите количество элементов"))
# for i in range(n):
#     list_1.append(randint(1,10)) 
# print(list_1)
# print(len(set(list_1)))

from random import randint
list_1=[randint(1,10) for _ in range(int(input("Введите количество элементов")))]
print(list_1)
print(len(set(list_1))) 