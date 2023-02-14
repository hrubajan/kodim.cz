soubor = open("kodim.cz/06_podminky_for_cyklus/banka.txt","r",encoding="utf-8")
data = [float(x.strip()) for x in soubor]
soubor.close()

""" urok = 1.025
poradi = 0
# hodnot je 10 z toho 3 jsou zaporne
for x in data:
  poradi += 1
  if x > 0:
    zustatky = round(x*urok,2)
    print(f'{poradi}. zustatek na sporicim ucte navyseny o urok: {zustatky} Kc') """

# enumerate, prida poradove cislo podle puvodniho seznamu i se zapornymi hodnotami
urok = 1.025
for poradove_cislo, cislo in enumerate(data):
  if cislo > 0:
    zustatky = round(cislo*urok,2)
    print(f'{poradove_cislo+1}. zustatek na sporicim ucte navyseny o urok: {zustatky} Kc')