# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint
list_1 = [randint(1, 10) for _ in range(
    int(input("Введите количество элементов первого множества ")))]
list_2 = [randint(1, 10) for _ in range(
    int(input("Введите количество элементов второго множества ")))]
print(list_1)
print(list_2)

my_list = list()

for i in list_1:
    if i in my_list:
        continue
    for j in list_2:
        if i == j:
            my_list.append(i)
            newList = sorted(my_list)
            break

print(*newList)
