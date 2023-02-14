import sys

cislo1 = int(sys.argv[1])
cislo2 = int(sys.argv[2])

if cislo1 > cislo2:
  print(cislo1)
elif cislo2 > cislo1:
  print(cislo2)
else:
  print("Cisla jsou si rovna")