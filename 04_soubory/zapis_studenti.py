studenti = ["Dan", "Petra", "Vlasta", "Jindra"]

# mode w jako write, soubor je otevreny pro zapis, pokus mode chybi, je soubor otevren pro cteni
soubor = open("kodim.cz/05_soubory/studenti.txt", mode="w", encoding="utf-8")

[soubor.write(student + "\n") for student in studenti]
soubor.close()