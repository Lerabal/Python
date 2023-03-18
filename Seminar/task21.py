# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# print(dictionary)

# for dict_i in dictionary:
#     print(dict_i)
#     for key in dict_i:
#         print(dict_i[key].strip())

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
n = set()
for dict_i in dictionary:
    # print(i)
    for key in dict_i:
    # print(i[j])
        n.add(dict_i[key])
print(n)
