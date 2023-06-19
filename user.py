class User:
    def __init__(self, firstname, surname, age, phonenumber):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.phonenumber = phonenumber
    def __str__(self):
        return f"Jméno: {self.firstname}, Příjmení: {self.surname}, Věk: {self.age}, Telefonní číslo: {self.phonenumber}"