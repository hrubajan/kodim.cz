# otevreni textoveho souboru
vstup = open("kodim.cz/05_soubory/behani.txt", encoding="utf-8")
behy = [ int(radka.strip().replace("km","").strip()) for radka in vstup]
# uzavreni souboru
vstup.close()
print(behy)

vystup = open("kodim.cz/05_soubory/behani_nove.txt", mode="w", encoding="utf-8")
[vystup.write(str(beh*1000) + " m\n") for beh in behy]
vystup.close()