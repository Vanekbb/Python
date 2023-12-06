from logger import *
from actions_contacts import *

def userInterface():
    with open("phonebook.txt", "a"):
        pass

    with open("copycontacts.txt", "a"):
        pass

    user_input = None
    
    while user_input != "5":
        print(
        "Возможные варианты действия:\n"
        "1. Добавить контакт.\n"
        "2. Вывод списка контактов.\n"
        "3. Поиск контакта.\n"
        "4. Действия с контактами.\n"
        "5. Выход.\n"
        )
    
        user_input = input("Введите вариант: ")

        while user_input not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод!")
            user_input = input("Введите вариант: ")

        print()

        match user_input:
            case "1":
                writeContact()
            case "2":
                printConstacts()
            case "3":
                searchConstacts()
            case "4":
                actionsWithContacts()
        print()
