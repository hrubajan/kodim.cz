# Načtěte data ze souboru do vašeho programu jako tabulku v podobě seznamu seznamů. Každý vnořený seznam bude představovat jeden řádek tabulky.
from pprint import pprint
vstup = open("kodim_opak_studenti.txt","r",encoding="utf-8")
data = [x.strip().split('\t') for x in vstup]
#pprint(data)
vstup.close()

# 0. radek spatny format
tab = [x.replace('  ',' ').split(' ') for x in data[0]]
sloupec = '_'.join(tab[0][-2:])
del tab[0][2:4]
tab[0].append(sloupec)
data[0] = tab[0]
#print(data[0])


# Přidejte do tabulky sloupec, který bude udávat věk studenta. Věk studenta zjistíte podle roku narození, což jsou první dvě cifry rodného čísla. 
data[0].append('věk')

from datetime import datetime
rok_nyni = int(datetime.now().year)

rodne_cisla = [ x[-1] for x in data[1:] ]
# pprint(rodne_cisla)
vek = [ rok_nyni - (1900+int(rodne_cislo[:2])) for rodne_cislo in rodne_cisla ]
# print(vek)
for i in range(1,len(data)):
  data[i].append(vek[i-1])
# pprint(data)

# Přidejte do tabulky sloupec, který bude udávat zda je student muž či žena. Pohlaví poznáte podle měsíce narození (druhé dvě cifry rodného čísla). Pokud je člověk ženského pohlaví, přičítá se k první cifře měsíce narození číslo 5.
data[0].append('pohlaví')
mesice = [ int(rodne_cislo[2:4]) for rodne_cislo in rodne_cisla ]
# print(mesice)
pohlavi = []
for mesic in mesice:
  if mesic in range(1,13):
    pohlavi.append('muž')
  elif mesic in range(51,63):
    pohlavi.append('žena')
  else: print('error')
#print(pohlavi)
for i in range(1,len(data)):
  data[i].append(pohlavi[i-1])
#pprint(data)

# Přidejte do tabulky sloupec, který bude udávat univerzitní email studenta. Univerzitní mail vznikne tak, že se vezme prvních pět písmenek příjmení a první tři písmenka křestního jména. Za takto vzniklý řetězec se připojí doména @hybrid.edu.
from unidecode import unidecode
data[0].append('email')
emaily = [ unidecode(x[1].lower())[:5] + unidecode(x[0].lower())[:3] + '@hybrid.edu' for x in data[1:] ]
#print(emaily)
for i in range(1,len(data)):
  data[i].append(emaily[i-1])
#pprint(data)

# Uložte výslednou tabulku ve formátu JSON do souboru s názvem studenti.json. K tomu bude potřeba seznam seznamů převést na seznam slovníků. Každý řádek tabulky tedy bude reprezentován slovníkem, kde klíče jsou názvy sloupečků.
prvni_radek = data[0]
#print(prvni_radek)
jmeno = prvni_radek[0]
prijmeni = prvni_radek[1]
rodne_cislo = prvni_radek[2]
vek = prvni_radek[3]
pohlavi = prvni_radek[4]
email = prvni_radek[5]

list_of_dictionaries = []

for row in data[1:]:
  dictionary = {jmeno:row[0], prijmeni:row[1], rodne_cislo:row[2], vek:row[3], pohlavi:row[4], email:row[5]}
  list_of_dictionaries.append(dictionary)

# pprint(list_of_dictionaries)

import json
vystup = open('kodim_opak_studenti.json',"w",encoding='utf-8')
#vystup.write(json.dump(list_of_dictionaries, indent=4,ensure_ascii=False))
json.dump(list_of_dictionaries, vystup, indent=4, ensure_ascii=False)
vystup.close()