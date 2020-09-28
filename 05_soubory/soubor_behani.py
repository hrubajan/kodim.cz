# otevreni textoveho souboru
vstup = open("04_lekce/behani.txt", encoding="utf-8")
behy = [ int(radka.strip().replace("km","").strip()) for radka in vstup]
# uzavreni souboru
vstup.close()
print(behy)

vystup = open("04_lekce/behani_nove.txt", mode="w", encoding="utf-8")
[vystup.write(str(beh*1000) + " m\n") for beh in behy]
vystup.close()