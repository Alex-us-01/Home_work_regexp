from pprint import pprint


def create_dictionary(keys: list, contact_list: list):
    dict_1 = {}
    for number, element in enumerate(contact_list):
        dict_1[keys[number]] = element
    return dict_1


def corrector(list_for_correction :list):
    # print(list_for_correction)
    print('Вход в corrector')
    list_1 = list_for_correction[1::]

    for element in list_1:
        list_3 = []
        # print('FOR - 1')
        # print(f' FOR_1 - element - {element}')
        # print(f'Первый элемент - {len(element[0])}\n'
        #       f'Второй элемент - {len(element[1])}\n'
        #       f'Третий элемент - {len(element[2])}')
        if len(element[0]) and len(element[1]) and len(element[2]) != 0:
            print(f'Все три элемента заполнены!')

        else:
            # list_3 = []
            for i in element[0:3]:
                if len(i.split()) > 1:
                    for el_2 in i.split():
                        list_3.append(el_2)
                else:
                    if len(i.split()) == 1:
                        # print(f'ELSE - {i}')
                        list_3.append(i)
            print(list_3)
        step = 0
        for el_3 in list_3:
            # print(f'Меняю {element[step]} на {el_3}')
            element[step] = el_3
            step += 1

    # print(list_1)
    # for i in list_1:
    #     print(i)
    return list_1



def test(list_1 :list, keys: list):
    dict_1 = {}

    # print(keys[step])
    for element in list_1:
        # print(keys[step])
        print(element)
        dict_contact = {}
        key_dict = f'{element[0]} {element[1]}'
        res = key_dict in  dict_1
        if res == True:
            print('Совпадение')
            step = 0
            for el_1 in element:
                print('Вход в цикл')
                print(f'Значение_1 - {dict_1[key_dict][keys[step]]} --- Значение_2 - {el_1}')
                if dict_1[key_dict][keys[step]] == el_1:
                    print('Вход IF_1')
                    print(f'---{dict_1[key_dict][keys[step]]} - {el_1}')
                    step += 1
                elif dict_1[key_dict][keys[step]] != el_1 and dict_1[key_dict][keys[step]] == '':
                    print('Вход ELIF_1')
                    dict_1[key_dict][keys[step]] = el_1
                    print('Перезаписано')
                    step += 1

        else:
            if element[2] == '':
                dict_1[f'{element[0]} {element[1]}'] = {}
                step = 0
                for el_2 in element:
                    dict_1[f'{element[0]} {element[1]}'][keys[step]] = el_2
                    # print(el_2)
                    step += 1

            else:
                dict_1[f'{element[0]} {element[1]} {element[2]}'] = {}
                step = 0
                for el_2 in element:
                    dict_1[f'{element[0]} {element[1]} {element[2]}'][keys[step]] = el_2
                    # print(el_2)
                    step += 1


            # dict_1[f'{element[0]} {element[1]} {element[2]}'] = {}
            # step = 0
            # for el_2 in element:
            #
            #     dict_1[f'{element[0]} {element[1]} {element[2]}'][keys[step]] = el_2
            #     # print(el_2)
            #     step += 1
    pprint(dict_1)


def fusion_contact(dict_: dict, keys: list):
    result = {}
    name = []
    for key, value in dict_.items():

        # print(f' {key} - {value}')
        # print(len(key.split(' ')))
        if len(key.split(' ')) == 3:
            dict_key = key.split(' ')[0:2]
            # print(dict_key)
            k2 = f'{dict_key[0]} {dict_key[1]}'

            res = k2 in dict_
            # print(res)
            if res == True:
                # print(k2)
                name.append(k2)
                step = 0
                for i in keys:
                    # print(f'{dict_[key][i]} - {dict_[k2][i]}')
                    if dict_[key][i] == dict_[k2][i]:
                        step += 1
                    elif dict_[key][i] != dict_[k2][i] and dict_[key][i] == '':
                        dict_[key][i] = dict_[k2][i]

    # del dict_[name]




    return dict_, name





test_list = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'], ['Усольцев Олег Валентинович', '', '', 'ФНС', 'главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц', '+7 (495) 913-04-78', 'opendata@nalog.ru'], ['Мартиняхин Виталий Геннадьевич', '', '', 'ФНС', '', '+74959130037', ''], ['Наркаев', 'Вячеслав Рифхатович', '', 'ФНС', '', '8 495-913-0168', ''], ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', 'cоветник отдела Интернет проектов Управления информационных технологий', '', ''], ['Лукина Ольга', '', 'Владимировна', 'Минфин', '', '+7 (495) 983-36-99 доб. 2926', 'Olga.Lukina@minfin.ru'], ['Паньшин Алексей Владимирович', '', '', 'Минфин', '', '8(495)748-49-73', '1248@minfin.ru'], ['Лагунцов Иван Алексеевич', '', '', 'Минфин', '', '+7 (495) 913-11-11 (доб. 0792)', ''], ['Лагунцов Иван', '', '', '', '', '', 'Ivan.Laguntcov@minfin.ru'], ['Лукина', 'Оксана', 'Владимировна', 'Минфин', '', '+7 (495) 983-36-99 доб. 2929', 'OLukina@minfin.ru']]

# list_1 = corrector(test_list)
# print(list_1)


list_test_2 = [['Усольцев', 'Олег', 'Валентинович', 'ФНС', 'главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц', '+7 (495) 913-04-78', 'opendata@nalog.ru'], ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', '', '+74959130037', ''], ['Наркаев', 'Вячеслав', 'Рифхатович', 'ФНС', '', '8 495-913-0168', ''], ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', 'cоветник отдела Интернет проектов Управления информационных технологий', '', ''], ['Лукина', 'Ольга', 'Владимировна', 'Минфин', '', '+7 (495) 983-36-99 доб. 2926', 'Olga.Lukina@minfin.ru'], ['Паньшин', 'Алексей', 'Владимирович', 'Минфин', '', '8(495)748-49-73', '1248@minfin.ru'], ['Лагунцов', 'Иван', 'Алексеевич', 'Минфин', '', '+7 (495) 913-11-11 (доб. 0792)', ''], ['Лагунцов', 'Иван', '', '', '', '', 'Ivan.Laguntcov@minfin.ru'], ['Лукина', 'Оксана', 'Владимировна', 'Минфин', '', '+7 (495) 983-36-99 доб. 2929', 'OLukina@minfin.ru']]

# test(list_test_2, test_list[0])

t = {'email': '',
                                 'firstname': '',
                                 'lastname': 'Наркаев',
                                 'organization': 'ФНС',
                                 'phone': '8 495-913-0168',
                                 'position': '',
                                 'surname': 'Рифхатович'}

# print('email' in t)
#     # print(True)
# if t['firstname'] == '':
#     print(True)

# t['firstname'] = 'A'
# print(t)
# t['firstname'] = 'B'
# print(t)



dict_test = {'Лагунцов Иван': {'email': 'Ivan.Laguntcov@minfin.ru',
                   'firstname': 'Иван',
                   'lastname': 'Лагунцов',
                   'organization': '',
                   'phone': '',
                   'position': '',
                   'surname': ''},
 'Лагунцов Иван Алексеевич': {'email': '',
                              'firstname': 'Иван',
                              'lastname': 'Лагунцов',
                              'organization': 'Минфин',
                              'phone': '+7 (495) 913-11-11 (доб. 0792)',
                              'position': '',
                              'surname': 'Алексеевич'},
 'Лукина Оксана Владимировна': {'email': 'OLukina@minfin.ru',
                                'firstname': 'Оксана',
                                'lastname': 'Лукина',
                                'organization': 'Минфин',
                                'phone': '+7 (495) 983-36-99 доб. 2929',
                                'position': '',
                                'surname': 'Владимировна'},
 'Лукина Ольга Владимировна': {'email': 'Olga.Lukina@minfin.ru',
                               'firstname': 'Ольга',
                               'lastname': 'Лукина',
                               'organization': 'Минфин',
                               'phone': '+7 (495) 983-36-99 доб. 2926',
                               'position': '',
                               'surname': 'Владимировна'},
 'Мартиняхин Виталий Геннадьевич': {'email': '',
                                    'firstname': 'Виталий',
                                    'lastname': 'Мартиняхин',
                                    'organization': 'ФНС',
                                    'phone': '',
                                    'position': 'cоветник отдела Интернет '
                                                'проектов Управления '
                                                'информационных технологий',
                                    'surname': 'Геннадьевич'},
 'Наркаев Вячеслав Рифхатович': {'email': '',
                                 'firstname': 'Вячеслав',
                                 'lastname': 'Наркаев',
                                 'organization': 'ФНС',
                                 'phone': '8 495-913-0168',
                                 'position': '',
                                 'surname': 'Рифхатович'},
 'Паньшин Алексей Владимирович': {'email': '1248@minfin.ru',
                                  'firstname': 'Алексей',
                                  'lastname': 'Паньшин',
                                  'organization': 'Минфин',
                                  'phone': '8(495)748-49-73',
                                  'position': '',
                                  'surname': 'Владимирович'},
 'Усольцев Олег Валентинович': {'email': 'opendata@nalog.ru',
                                'firstname': 'Олег',
                                'lastname': 'Усольцев',
                                'organization': 'ФНС',
                                'phone': '+7 (495) 913-04-78',
                                'position': 'главный специалист – эксперт '
                                            'отдела взаимодействия с '
                                            'федеральными органами власти '
                                            'Управления налогообложения '
                                            'имущества и доходов физических '
                                            'лиц',
                                'surname': 'Валентинович'}}

# print(dict_test)
a = fusion_contact(dict_test, test_list[0])

print(a[1])
del dict_test[a[1][0]]
# a_2 = dict_test.pop(a[1])
# res = a in dict_test
# print(res)
# dict_test.pop
#
pprint(dict_test)