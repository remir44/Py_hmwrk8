import add_employee as ae
import user_interface as ui
import change as c
import view as v


def user_choice():
    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 4:
        user_choice()
    elif choice_num == 0:
        ae.create_json()
    elif choice_num == 1:
        ae.add_to_json()
    elif choice_num == 2:
        print("Какие изменения вы хотите внести?\n")
        choice_num = ui.submenu()
        if choice_num == 5:
            c.change_number()
        elif choice_num == 6:
            c.change_dep()
        elif choice_num == 7:
            c.change_pos()
        elif choice_num == 8:
            c.delete_entry()
        elif choice_num == 9:
            user_choice()
    elif choice_num == 3:
        v.view_all()
    elif choice_num == 4:
        print('\nРабота с системой завершена.')
        exit()
