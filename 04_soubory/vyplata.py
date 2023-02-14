# ULOHA 1
import sys
import statistics

soubor = open("kodim.cz/05_soubory/vykaz_vyplata.txt", encoding="utf-8")
vykaz = [int(radka.strip()) for radka in soubor]
#print(vykaz)

sazba = int(sys.argv[1])

vyplata_rok = sum(vykaz) * sazba
print("Za rok si vydelal: " + "{:,}".format(vyplata_rok).replace(","," ") + " Kc")

vyplata_mesic = [mesic * sazba for mesic in vykaz]
prumer_mesic = round(statistics.mean(vyplata_mesic), 2)
print("Prumerna mesicni vyplata je: " + "{:,}".format(prumer_mesic).replace(","," ") + " Kc")

# ULOHA 5
"""
import sys
vstup = open("kodim.cz/05_soubory/vykaz_vyplata.txt", encoding="utf-8")
vykaz = [int(radka.strip()) for radka in vstup]
sazba = int(sys.argv[1])

vyplata_mesic = [ "{:,} Kc".format(mesic * sazba).replace(","," ") for mesic in vykaz]
print(vyplata_mesic)
vstup.close()

vystup = open("kodim.cz/05_soubory/vykaz_vyplata_nove.txt", "w", encoding="utf-8")
[vystup.write(castka + "\n") for castka in vyplata_mesic]
vystup.close()
"""
