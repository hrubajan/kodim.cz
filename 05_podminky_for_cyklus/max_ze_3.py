import sys

cislo1 = int(sys.argv[1])
cislo2 = int(sys.argv[2])
cislo3 = int(sys.argv[3])

if cislo1 > cislo2 and cislo1 > cislo3:
  print(cislo1)
elif cislo2 > cislo3:
  print(cislo2)
else:
  print(cislo3)

""" import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if x > y:
  if x > z:
    print(x)
  else:
    print(z)
elif y > z:
  print(y)
else: 
  print(z) """