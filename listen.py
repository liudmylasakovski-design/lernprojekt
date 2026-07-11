status_codes = [200,301,404,500]

for code in status_codes:
    if code == 200:
        print(code, "Ok")
    elif code == 404:
        print(code, "Seite nicht gefunden")
    elif code == 500:
        print(code, "Server Fehler")
    else: 
        print(code, "weiterleitung")