# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

num = int(input("Введите число: "))
i = 1
factorial = 1
while i <= num:
    factorial = factorial*i
    i += 1
print(factorial)

# try:
# print('<<< Вычисление факториала - N! >>>')
# number = int(input('Введите N: '))
# if number < 0:
# print('Введено отрицательное значение')
# else:
# i = 0
# factorial = 1
# while i < number:
# i += 1
# factorial *= i
# print(f'{number}! = {factorial}')
# except:
# print('Введено не допустимое значение')
