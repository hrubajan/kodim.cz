# random.shuffle --> zamicha seznam, uz nemusim resit duplikaty (u random.choice bych resit musela, postup reseni nize)

# Petr hezke reseni
import random
from pprint import pprint

soubor = open("kodim.cz/05_soubory/karty3.txt", "r", encoding="utf-8")

deck = [card for card in soubor]
#print("zaprasene {}".format(deck))
#print(f"zaprasene: {deck}")

deck_strip = [card.strip() for card in deck]
#pprint(f"odprasene: {deck_strip}")

random.shuffle(deck_strip)
#pprint(f"zamichano: {deck_strip}")

vybrane_karty = deck_strip[:4]
#pprint(f"vybrane karty: {vybrane_karty}")

rozdeleni = [karta.split() for karta in vybrane_karty]
pprint(f"karty: {rozdeleni}")

nahrazeni = [int( card[0].replace("kluk","10").replace("dáma","10").replace("král","10").replace("eso","1")) for card in rozdeleni]
pprint(f"nahrazeni: {nahrazeni}")

soucet = sum(nahrazeni)
pprint(f"soucet: {soucet}")
 
""" # vybirani 4 karet postupne pomoci choice a pak tu vybranou kartu pomoci delete smazat ze seznamu
import random

x = ["kral", "eso", "dama"]
prvek1 = random.choice(x)
print(prvek1)

index_prvek1 = x.index(prvek1)
del x[index_prvek1]

print(x) """