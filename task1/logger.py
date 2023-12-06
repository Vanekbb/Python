from date_create import *

def CreateContact():
    '''Add an entry'''
    surname = surnameInput()
    name = nameInput()
    patronymic = patronymicInput()
    phone = phoneInput()
    address = addressInput()

    return f"{surname} {name} {patronymic} {phone}\n{address}\n\n"

def writeContact():
    contact = CreateContact()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(contact)
        print("\nКонтакт записан.")

def printConstacts():
    '''List all entries'''
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        for nn, contact in enumerate(contacts_list, 1):
            print(f"{nn}. {contact}\n")

def searchConstacts(field=""):
    '''Search any entries'''
    print(
        "Возможные варианты поиска:\n"
        "1. По фамилии.\n"
        "2. По имени.\n"
        "3. По отчеству.\n"
        "4. По номеру.\n"
        "5. По городу."
        )
    
    index_var = int(input("Введите вариант поиска: ")) - 1

    search = input("Введите данные поиска: ")
    
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    
    contacts_list = contacts_str.rstrip().split("\n\n")

    for contact_str in contacts_list:
        contact_list = contact_str.replace("\n", " ").split(" ")
        if search in contact_list[index_var]:
            print(f"\n{contact_str}\n")
