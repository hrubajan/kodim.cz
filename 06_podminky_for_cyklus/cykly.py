soubor = open("04_lekce/vykaz_vyplata.txt", "r", encoding="utf-8")

celkem_radku = 0 
celkem_hodin = 0
for radek in soubor:
  print("Data: " + radek.strip())
  celkem_radku += 1
  celkem_hodin = int(radek)

soubor.close()
print("Prumerna pracovni doba za mesic: " + str(round(celkem_hodin/celkem_radku,2)))