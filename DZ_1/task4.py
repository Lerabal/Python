# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

num = int(input("Введите количество журавликов: "))
if  num % 2 == 0 and num % 3 == 0:
    kate = int((num/3)*2)
    petr = int((kate/2)/2)
    sergei = int(petr)
    print(petr, kate, sergei)
else:
    print("Введите количество журавликов кратное 6!")

