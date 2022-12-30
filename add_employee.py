import json
import controller


def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_choice()


def add_to_json():
    name = input("Введите имя: ")
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    department = input('Введите отдел: ')
    position = input('Введите должность: ')
    json_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Department": department,
        "Position": position
    }
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    controller.user_choice()
