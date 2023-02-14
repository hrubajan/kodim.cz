# moje reseni pres vybirani hodnoty ze stringu
import random

barvy = ["krize","srdce","piky","kary"]
hodnoty = [2,3,4,5,6,7,8,9,10,"kluk","dama","kral","eso"]

karty = [ (str(random.choice(hodnoty)) + " " + random.choice(barvy)) for _ in range(4)]
print(karty)

hodnoty_upraveno = [x.replace("kluk","10").replace("dama","10").replace("kral","10").replace("eso","1") for x in karty]
#print(hodnoty_upraveno)

karty_upraveno = [karta.split(" ") for karta in hodnoty_upraveno]
#print(karty_upraveno)

cisla = sum( [int(x[0]) for x in karty_upraveno ] )
print("Soucet hodnot vylosovanych karet je: {}".format(cisla))

# Petrovo reseni pres 2prvkovy seznam
""" import random
barvy = ["krize","srdce","piky","kary"]
hodnoty = ["2","3","4","5","6","7","8","9","10","kluk","dama","kral","eso"]

karty = [ [random.choice(barvy), random.choice(hodnoty)] for _ in range(4)]
print(karty)

hodnoty = [ card[1] for card in karty]
#print(hodnoty)

nahrazeni_pismenek = [int( cislo_karty.replace("kluk","10").replace("dama","10").replace("kral","10").replace("eso","1")) for cislo_karty in hodnoty]
#print(nahrazeni_pismenek)

soucet = sum(nahrazeni_pismenek)
print(soucet) """