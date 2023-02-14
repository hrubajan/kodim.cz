cisla1 = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
cisla2 = [3, 5, 8, 9, 14, 17, 20]
cisla3 = [20, 16, 12, 9, 7, 4, 1]

# vzestupne/sestupne
if sorted(cisla1) == cisla1:
  print('Vzestupne')
elif sorted(cisla1)[::1] == cisla1:
  print('Sestupne')
else:
  print('Neserazeno')

# Petr rychle reseni jen na vzestupny seznam
print(cisla1 == sorted(cisla1))

# dalsi reseni
nejvyssi = 0
for polozka in cisla1:
  if polozka > nejvyssi:
      nejvyssi = polozka
  else:
    print('neni vzestupny')
    exit()
print('je vzestupny')

"""
# reseni for cyklem postupne
for i in range(len(cisla1)-1):
  if cisla1[i] < cisla1[i+1]:
    print(f'{cisla1[i]} {cisla1[i+1]}')
    print('True')
  else:
    print('False')
    exit()
"""

"""
# reseni funkci
def je_razen_vzestupne(seznam):
  for i in range(len(seznam)-1):
    if seznam[i] > seznam[i+1]:
      return False
    elif seznam[i] < seznam[i+1]:
      print(f"{seznam[i]} {seznam[i+1]}")
      continue
  return True
print(je_razen_vzestupne(cisla2))
"""


"""
# Petr reseni - projet cele pole pomoci for cyklu -> pokud to nesedi vratim False -> jinak musim dojet az na konec for cyklu a vratit True
def je_razen_vzestupne(seznam):
  for i in range(len(seznam)-1):
    if seznam[i] > seznam[i+1]:
      return False
  return True
print(je_razen_vzestupne(cisla1))
"""

