""" import sys

nazev = sys.argv[1]

if nazev[-4:] == ".csv":
  print(nazev)
else:
  print("Dany soubor neumim zpracovat")
"""

import sys

nazev = sys.argv[1]

if nazev.endswith(".csv"):
  print(nazev)
  print(nazev[:-4])
else:
  print("Dany soubor neumim zpracovat")