def start():
    greetings = 'Добро пожаловать в систему компании N!'
    print(f'{greetings}')


def menu():
    print('\nВведите цифру из пунктов меню: \n')
    new_book = '0. Начать с нуля/сбросить предыдущие записи'
    new_entry = '1. Добавить сотрудника'
    change_entry = '2. Внести изменения в запись'
    view_all = '3. Показать все записи'
    exit_book = '4. Выход'
    print(f'{new_book}\n{new_entry}\n{change_entry}\n{view_all}\n{exit_book}')
    return digit_check()


def submenu():
    change_number = '5. Изменить номер сотрудника'
    change_dep = '6. Изменить отдел сотрудника'
    change_pos = '7. Изменить должность сотрудника'
    delete_entry = '8. Удалить запись'
    go_back = '9. Вернуться в главное меню'
    print(f'{change_number}\n{change_dep}\n{change_pos}\n{delete_entry}\n{go_back}')
    return digit_check()


def digit_check():
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()
