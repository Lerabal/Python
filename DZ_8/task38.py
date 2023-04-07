def writing_person():
    last_name = input("Фамилия: ")
    name = input("имя: ")
    surn_name = input("Отчество: ")
    tel = input("Телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(
        f"фамилия:{last_name} имя:{name} отчество:{surn_name} телефон:{tel}\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)


def print_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def load():
    new_phonebook = input("Введите путь: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")

def delete_person(name):
    """Удаляет данные"""
    persons = data.read()
    with open("phonebook.txt", "w", encoding="utf8" ) as data:
        for person in persons:
            if name != person:
                data.write(person)

print("""1 - добавление персоны,
2 - поиск, 
3 - вывод на экран,
4 - импорт в файл
5 - удаление персоны\n""")
ask = int(input())
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    load()
elif ask == 5:
    name = input('кого удаляем?: ')
    delete_person(name)
    
# C:\Users\lera_\PYTHON\DZ_8\phonebook_1.txt

