from inputdata import *
def interface():
    print("""1 - добавление персоны,
2 - поиск, 
3 - вывод на экран,
4 - импорт в файл
5 - удаление персоны
6 - изменить запись\n""")
ask = int(input())
if ask == 1:
    input_data()
elif ask == 2:
    search()
elif ask == 3:
    print_data()
elif ask == 4:
    load()
elif ask == 5:
    delete_line()
elif ask == 5:
    change_line()  