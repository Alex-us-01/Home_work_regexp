from pprint import pprint
from application.additional_file import create_dictionary, corrector

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
print(contacts_list)
# list_keys = contacts_list[0]
#
# # # TODO 1: выполните пункты 1-3 ДЗ
# # # ваш код
# print(contacts_list[0])
contacts_list_1 = contacts_list[1::]
dict_2 = {}
for element in contacts_list_1:
    # print(element)
    a = corrector(element)
    contacts_list_1[element]
    # print(a)





    # print(element)#
    # if len(element[0]) and len(element[1]) and len(element[2]) != 0:
    #     # print(element)
    #     dict_1 = create_dictionary(list_keys, element)
    #     dict_2[f'{element[0]} {element[1]} {element[2]}'] = dict_1
    # else:
    #   pass


#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
