import re


def create_dictionary(keys: list, contact_list: list):
    dict_1 = {}
    for number, element in enumerate(contact_list):
        dict_1[keys[number]] = element
    return dict_1


def corrector(list_for_correction: list):
    list_1 = list_for_correction[1::]

    for element in list_1:
        list_3 = []
        if len(element[0]) and len(element[1]) and len(element[2]) != 0:
            pass
        else:
            for i in element[0:3]:
                if len(i.split()) > 1:
                    for el_2 in i.split():
                        list_3.append(el_2)
                else:
                    if len(i.split()) == 1:
                        list_3.append(i)
        step = 0
        for el_3 in list_3:
            element[step] = el_3
            step += 1

    return list_1


def test(list_1: list, keys: list):
    dict_1 = {}
    for element in list_1:
        key_dict = f'{element[0]} {element[1]}'
        res = key_dict in dict_1
        if res == True:
            step = 0
            for el_1 in element:
                if dict_1[key_dict][keys[step]] == el_1:
                    step += 1
                elif dict_1[key_dict][keys[step]] != el_1 and dict_1[key_dict][keys[step]] == '':
                    dict_1[key_dict][keys[step]] = el_1
                    step += 1

        else:
            if element[2] == '':
                dict_1[f'{element[0]} {element[1]}'] = {}
                step = 0
                for el_2 in element:
                    dict_1[f'{element[0]} {element[1]}'][keys[step]] = el_2
                    step += 1

            else:
                dict_1[f'{element[0]} {element[1]}'] = {}
                step = 0
                for el_2 in element:
                    dict_1[f'{element[0]} {element[1]}'][keys[step]] = el_2
                    step += 1

    return dict_1


def fusion_contact(dict_: dict, keys: list):
    result = {}
    for key, value in dict_.items():

        if len(key.split(' ')) == 3:
            dict_key = key.split(' ')[0:2]
            k2 = f'{dict_key[0]} {dict_key[1]}'

            res = k2 in dict_
            if res == True:
                step = 0
                for i in keys:
                    if dict_[key][i] == dict_[k2][i]:
                        step += 1
                    elif dict_[key][i] != dict_[k2][i] and dict_[key][i] == '':
                        dict_[key][i] = dict_[k2][i]

    list_result = []

    for key, value in dict_.items():

        step = 0
        list_contact_ = []
        for element in keys:
            list_contact_.append(value[element])
        list_result.append(list_contact_)
        step += 1
    return list_result


def search_contact(list_contact: list, name: list):
    for i in list_contact:
        name_1 = ' '.join(name)
        name_2 = ' '.join(i[:3])
        if name_1 in name_2:
            return True
        else:
            return False


def phone_number_correction(list_contacts: list):
    pattern = r"(\+7|8)[\s(]*(\d{3})[)\s-]*(\d{3})[-]?(\d{2})[-]?(\d{2})[\s(]*(доб.)*[\s]?(\d{4})*[)]*"
    substitution = r"+7(\2)\3-\4-\5 \6\7"
    for element in list_contacts:
        result = re.sub(pattern, substitution, element[5])
        element[5] = result
    return list_contacts


def corrector_2(list_1: list, keys: list):
    dict_1 = {}

    for element in list_1:
        if element[0] and element[2] and element[2] != '':
            key_dict = f'{element[0]} {element[1]} {element[2]}'
            result = key_dict in dict_1
            if result == True:
                step = 0
                for el_1 in element:
                    if dict_1[key_dict][keys[step]] == el_1:
                        step += 1
                    elif dict_1[key_dict][keys[step]] != el_1 and dict_1[key_dict][keys[step]] == '':
                        dict_1[key_dict][keys[step]] = el_1
                        step += 1
            else:
                if element[2] == '':
                    dict_1[f'{element[0]} {element[1]}'] = {}
                    step = 0
                    for el_2 in element:
                        dict_1[f'{element[0]} {element[1]}'][keys[step]] = el_2
                        step += 1

                else:
                    dict_1[f'{element[0]} {element[1]} {element[2]}'] = {}
                    step = 0
                    for el_2 in element:
                        dict_1[f'{element[0]} {element[1]} {element[2]}'][keys[step]] = el_2
                        step += 1


        else:
            name_contact = ' '.join(element[:2])
            for key, value in dict_1.items():
                if name_contact in str(key):
                    step = 2
                    for i in element[2::]:
                        if dict_1[key][keys[step]] == i:
                            pass

                        elif dict_1[key][keys[step]] != i and i != '':
                            dict_1[key][keys[step]] = i
                        step += 1

    return dict_1
