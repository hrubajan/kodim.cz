# a]

soubor = open("kodim.cz/05_soubory/auta.txt", encoding="utf-8")

kilometry = [radek.strip().replace(",",".") for radek in soubor]
#print(kilometry)

rozsek = [radek.split(" ") for radek in kilometry]
print(rozsek)

najete_km = [float(radek[-1]) for radek in rozsek]
print(najete_km)

celkem_km = sum(najete_km)
print("Soucet najetych km: " + str(celkem_km))


# b]
"""
import sys
soubor = open(sys.argv[1], encoding="utf-8")

kilometry = [radek.strip().replace(",",".") for radek in soubor]
#print(kilometry)

rozsek = [radek.split(" ") for radek in kilometry]
print(rozsek)

najete_km = [float(radek[-1]) for radek in rozsek]
print(najete_km)

celkem_km = sum(najete_km)
print("Soucet najetych km: " + str(celkem_km))
"""