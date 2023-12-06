from ui import *
from logger import *

def copyContacts():
    user_number_contact = int(input("Введите номер контакта: "))
    copy_contact = ""
    
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        for nn, contact in enumerate(contacts_list, 1):
            if user_number_contact == nn:
                copy_contact = contact
    
    with open("copycontacts.txt", "a", encoding="utf-8") as file:
        file.write(f"{copy_contact}\n\n")
        print("\nКонтакт скопирован!\n")

def editingContacts():
    user_number_contact = int(input("Введите номер контакта: "))
    edit_contact = CreateContact()
    changeable_contact = ""

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        for nn, contact in enumerate(contacts_list, 1):
            if user_number_contact == nn:
                changeable_contact = contact
    
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        old_data = file.read()

    new_data = old_data.replace(changeable_contact, edit_contact)
    new_data = new_data.rstrip()

    with open ("phonebook.txt", 'w', encoding="utf-8") as file:
        file.write(f"{new_data}\n\n")
        print("\nКонтакт изменён!\n")

def actionsWithContacts():
    print(
        "Возможные варианты действия:\n"
        "1. Редактировать контакт.\n"
        "2. Копировать контакт.\n"
        )
    
    user_input = input("Выберите вариант: ")
    
    while user_input not in ("1", "2"):
        print("Некорректный ввод!")
        user_input = input("Введите вариант: ")

    match user_input:
        case "1":
            editingContacts()
        case "2":
            copyContacts()