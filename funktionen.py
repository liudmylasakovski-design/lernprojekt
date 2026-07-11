def teste_login(benutzername, passwort):
    erlaubtes_passwort = "test123"

    if passwort == erlaubtes_passwort:
        print(benutzername, "->Login erfolgreich")
    else:
        print(benutzername, "-> Login fehlgeschlagen")

teste_login("Liudmyla", "test123")
teste_login("Liudmyla", "falsches_passwort")
teste_login("Admin", "test1223")