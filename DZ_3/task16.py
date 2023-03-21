# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

from random import randint
n = int(input("Введите количество элементов массива "))
x = int(input("Введите число "))
list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
count = 0
for i in range(n):
    if list_1[i] == x:
        count += 1
print(count)

# n=int(input("ВВедите число элементов массива = "))
# x=int(input("ВВедите число X = "))
# #list=[int(input(f"Введите {i} элемент массива ")) for i in range(n)]
# #print(list)
# list=[]
# counter=0
# for i in range(n):
# list.append(int(input(f"Введите {i} элемент массива ")))
# if x ==list[i]:
# counter+=1
# print(list)
# print(f"Число {x} встречается в массиве {counter} раз/а")
# list2=list.copy()
# counter2=0
# x_str = str(x)
# for num in list2:
# num_str = str(num)
# if x_str in num_str:
# # print(number)
# for elem in num_str:
# if x_str == elem:
# counter2+=1
# print(f"Цифра {x} встречается в массиве {counter2} раз/а")