import json
import controller
db_path = 'db.json'


def change_number():
    print('Введите имя и фамилию сотрудника, чей номер нужно изменить:  ')
    name = input('Имя - ')
    surname = input('Фамилия - ')
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] and surname == data[i]['Surname']:
                data[i]['Phone number'] = input('Новый телефон: ')
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nИзменения успешно внесены.\n')
    controller.user_choice()


def change_dep():
    print('Введите имя и фамилию сотрудника, которого переводят в другой отдел:  ')
    name = input('Имя - ')
    surname = input('Фамилия - ')
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] and surname == data[i]['Surname']:
                data[i]['Department'] = input('Новый отдел: ')
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nИзменения успешно внесены.\n')
    controller.user_choice()


def change_pos():
    print('Введите имя и фамилию сотрудника, которого назначают на другую должность:  ')
    name = input('Имя - ')
    surname = input('Фамилия - ')
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] and surname == data[i]['Surname']:
                data[i]['Position'] = input('Новая должность: ')
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nИзменения успешно внесены.\n')
    controller.user_choice()


def delete_entry():
    print('Введите имя и фамилию сотрудника, которого нужно удалить из системы:  ')
    name = input('Имя - ')
    surname = input('Фамилия - ')
    with open(db_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(data.index(data[-1])+1):
            if name == data[i]['Name'] and surname == data[i]['Surname']:
                del data[i]
    with open(db_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nДанные успешно удалены.\n')
    controller.user_choice()
