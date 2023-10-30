from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n')

def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
        return data_first, data_second  
    
def put_data():
    print('Из какого файла вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету вы хотите изменить?")
        number_journal = int(input('Введите номер записи для замены: '))
        new_input = input('Введите новую запись: ')

        with open('data_first_variant.csv', 'r+', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            for i in range(len(data_first)):
                if i + 1 != number_journal:
                    data_first_version_second.append(data_first[i])
                else:
                    data_first_version_second.append(new_input + '\n')
            file.seek(0)
            file.writelines(data_first_version_second)
        print('Запись заменена успешно!')

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        new_name = name_data()
        new_surname = surname_data()
        new_phone = phone_data()
        new_address = address_data()
        with open('data_second_variant.csv', 'r+', encoding='utf-8') as file:
            data_second = file.readlines()
            data_second_version_second = []
            for i in range(len(data_second)):
                if i + 1 != number_journal:
                    data_second_version_second.append(data_second[i])
                else:
                    data_second_version_second.append((f'{new_name};{new_surname};{new_phone};{new_address}\n'))
            file.seek(0)
            file.writelines(data_second_version_second)
        print('Запись заменена успешно!')


def delete_data():
    print('Из какого файла вы хотите удалить данные?')
    data_first = []
    data_second = []

    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()

    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()

    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какие записи по счету вы хотите удалить?")
        delete_indices = input('Введите номера записей через пробел: ').split()
        delete_indices = [int(i) for i in delete_indices]

        data_first_version_second = []
        for i in range(len(data_first)):
            if i + 1 not in delete_indices:
                data_first_version_second.append(data_first[i])

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_first_version_second)

        print('Записи удалены успешно!')

    else:
        print("Какую именно запись по счету вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        data_second_version_second = []
        for i in range(len(data_second)):
            if i + 1 != number_journal:
                data_second_version_second.append(data_second[i])

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_second_version_second)

        print('Запись удалена успешно!')