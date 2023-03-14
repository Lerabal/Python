# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
a = number % 10  # последняя цифра
b = number//100  # первая цифра
c = number % 100//10  # средняя цифра
print("Сумма цифр трехзначного числа = ", a + b + c)

# print(bool(''))
# print(bool(None))
# print(bool(1))
# print(bool(7))
# print()

# print(int(True))
# print(int(False))
# print()

# print(bool(12 // 6))
# print(bool(13 // 6))
# print(bool(5 // 6))
# print()
# print(bool(18 % 6))
# print(bool(19 % 6))

# if 12 // 6:
# print('больше 5')
# if 19 % 6:
# print('не кратно 6')
# if not 18 % 6:
# print('кратно 6')