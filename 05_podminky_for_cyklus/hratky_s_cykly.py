import sys

cisla = [int(x) for x in sys.argv[1:]]

for cislo in cisla:
# a) 
  print(cislo)
# b) 
  print([cislo, cislo*-1])
  print(str(cislo) + ", " + str(-(cislo)))
# c) 
for cislo in cisla:
  if cislo > 0:
    print(cislo)
# d)
for cislo in cisla:
  if cislo > 0:
    print(cislo)
  else:
    print(cislo*-1)

""" for x in cisla:
  if x % 2 == 0:
    print(x) """