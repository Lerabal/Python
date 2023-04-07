from data_create import *


def input_data():
    lastname = last_name()
    firstname = first_name()
    phonenum = phone()

    with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "a", encoding="utf-8") as file:
        file.write(f"\n {lastname}\t{firstname}\t{phonenum}")


def print_data():
    with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "r", encoding="utf-8") as data:
        data_new = data.read()
        print(data_new)


def search():
    lookfor = input("кого ищем? ")
    bool_1 = False
    with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                bool_1 = True
        if bool_1 == False:
            print("Такой записи нет ")


def load():
    new_phonebook = input("Введите путь: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "a+", encoding="utf-8") as data_1:
            data_1.write("\n")
            for line in data:
                if line not in data_1:
                    data_1.write(line)


def delete_line():
    line_str = input("Кого удалить?  ")
    with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()
        for line in lines:
            if line_str not in line:
                data.write(line)
            else:
                print(line)
                ask = input("Удалить строку(y,n)? ")
                while ask not in ("y", "n"):
                    print("Ввод некорректный")
                    ask = input("Удалить строку(y,n)? ")
                if ask == "n":
                    data.write(line)


def change_line():
    line_str = input("Что изменить?  ")
    with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("C:\Users\lera_\PYTHON\DZ8\phonebook.txt", "w", encoding="utf-8") as data1:
            for line in lines:
                if line_str not in line:
                    data1.write(line)
                else:
                    lastname = input("Введите новые данные(Фамилия): ")
                    name = input("Введите новые данные(Имя): ")
                    phone = input("Введите новые данные(Телефон): ")
                    data1.write(f"\n {lastname}\t{name}\t{phone}")


print_data()