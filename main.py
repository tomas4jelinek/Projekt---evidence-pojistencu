from register import Users

usersregister = Users()

while True:

    print("Vítejte v evidenci pojištěných.\n")
    print("Vyberte akci: \n 1 - Přidat nového pojištěnce \n 2 - Zobrazit všechny pojištěnce \n 3 - Vyhledat pojištěnce \n Pro ukončení aplikace stiskněte Enter\n")

    action = input("Zadejte vaší akci:")

    if (action =="1"):
        usersregister.add_user()

    elif(action =="2"):
        usersregister.show_users()

    elif(action =="3"):
        usersregister.search_user()

#dokumentace + screenshoty na github