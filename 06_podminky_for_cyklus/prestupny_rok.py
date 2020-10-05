import sys

rok = int(sys.argv[1])

if rok % 100 == 0 and rok % 400 == 0:
  print(f'{rok} je prestupny')
elif rok % 4 == 0 and rok % 100 != 0:
  print(f'{rok} je prestupny')
else:
  print(f'{rok} neni prestupny')

"""
# pomoci funkce a user input
def is_leap(year):
    if year % 100 == 0 and year % 400 == 0:
      return True  
    elif year % 4 == 0 and year % 100 != 0:
      return True 
    else: 
      return False 

year = int(input("Napis rok 2"))
vysledek = is_leap(year)

if vysledek == True:
  print('Je prestupny')
else:
  print('Neni prestupny')
"""