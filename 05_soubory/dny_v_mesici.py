
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
mesice = ["jan", "feb", "mar","apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

vystup = open("kodim.cz/05_soubory/kalendar.txt",mode="w", encoding="utf-8")
vystup.write("Mesic\tPocet dni\n")

[vystup.write(mesice[i] + "\t" + str(pocty_dni[i]) + "\n") for i in range(12)]

vystup.close()

# jiny mozny postup
""" 
pocty_dni = [
  [31, "leden"],
  [28, "unor"],
  [31, "brezen"],
  [30, "duben"],
  [31, "kveten"],
  [30, "cerven"],
  [31, "cervenec"],
  [31, "srpen"],
  [30, "zari"],
  [31, "rijen"],
  [30, "listopad"],
  [31, "prosinec"]
]

vystup = open("04_lekce/kalendar.txt",mode="w", encoding="utf-8")
vystup.write("Mesic\tPocet dni\n")

[vystup.write(mesic[1] + "\t" + str(mesic[0]) + "\n") for mesic in pocty_dni]

vystup.close()
"""