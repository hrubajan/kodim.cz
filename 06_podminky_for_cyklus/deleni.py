import sys

cislo1 = int(sys.argv[1])
cislo2 = int(sys.argv[2])
if cislo2 == 0:
  print("Nulou delit nelze!")
  exit()
else:
  print(round(cislo1/cislo2,3))


