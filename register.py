from user import *
class Users():

    def __init__(self):
        #seznam uživatelů
        self.register = []

    def add_user(self):
        #načtení vstupů
        firstname: str = input("Zadejte jméno pojištěnce:")
        surname: str = input("Zadejte příjmení pojištěnce:")
        age: int = input("Zadejte věk pojištěnce:")
        phonenumber: str = input("Zadejte telefonní číslo pojištěnce:")

        #vytvoření pojištěnce
        new_user = User(firstname, surname, age, phonenumber)
        self.register.append(new_user)
        print(f"Přidali jste nového pojištěnce {new_user}")
        #přidání do seznamu

    def show_users(self):
        print("Seznam pojištěnců:")
        for user in self.register :
            print(user)

    def search_user(self):
        # Search for the value
        searched_firstname = str(input("Zadejte vyhledávané jméno: "))   #dát mimo metodu
        searched_surname = str(input("Zadejte vyhledávané příjmení: "))    #mimo

        for user in self.register:
            if searched_firstname == user.firstname and searched_surname == user.surname:
                print("Nalezen záznam:")
                print(user)
                print()

