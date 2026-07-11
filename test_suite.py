def prüfe_status(code):
    if code == 200:
        return "BESTANDEN ✓"
    else:
        return "FEHLGESCHLAGEN ✗"

# Mehrere Testergebnisse prüfen
ergebnisse = [200, 200, 404, 200, 500]

for code in ergebnisse:
    resultat = prüfe_status(code)
    print("Status", code, "→", resultat)