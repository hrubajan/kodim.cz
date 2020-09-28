import random

barvy = ["krize","srdce","piky","kary"]
hodnoty = ["2","3","4","5","6","7","8","9","10","kluk","dama","kral","eso"]

karta = random.choice(hodnoty) + " " + random.choice(barvy)

print("Karta: " + karta)

nahodne_cislo1 = random.randint(0,len(barvy)-1)
nahodne_cislo2 = random.randint(0,len(hodnoty)-1)

print("Karta: " + hodnoty[nahodne_cislo2] + " " + barvy[nahodne_cislo1])