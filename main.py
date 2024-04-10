from pprint import pprint
from application.additional_file import corrector, corrector_2, fusion_contact, phone_number_correction

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#
# # # TODO 1: выполните пункты 1-3 ДЗ
# # # ваш код

contacts_list_1 = contacts_list[1::]
stage_1 = corrector(contacts_list)
dictionary_contacts = corrector_2(stage_1, contacts_list[0])
result = fusion_contact(dictionary_contacts, contacts_list[0])
result = phone_number_correction(result)

#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # #   # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
