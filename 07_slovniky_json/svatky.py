# a) Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
"""
import requests
import json
response = requests.get("http://svatky.adresa.info/json")
#print(response)

soubor = json.loads(response.text)
jmeno = soubor[0]['name']
print(f"Dnes ma svatek {jmeno}.")
"""

# Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek 
# b) user input
"""
import requests
import json
datein = input('Zadej datum ve formatu DDMM: ')
response = requests.get(f"http://svatky.adresa.info/json?date={datein}")
#print(response)
file = json.loads(response.text)
nameout = file[0]['name']
print(f"{datein[0:2]}/{datein[2:]} ma svatek {nameout}.")
"""

# b) SYS
""" 
import requests
import json
import sys
datein = sys.argv[1]
response = requests.get(f"http://svatky.adresa.info/json?date={datein}")
#print(response)
file = json.loads(response.text)

nameout = file[0]['name']

print(f"{datein[0:2]}/{datein[2:]} ma svatek {nameout}.")
"""

# muj tuning -> jmeno nebo den
"""
import requests
import json

name_or_day = input('Hledas svatek podle data(D) nebo jmena(J)? Odpovez D/J ')

if name_or_day == 'D':
  datein = input('Zadej datum ve formatu DDMM: ')
  response = requests.get("http://svatky.adresa.info/json?date="+ str(datein))
  #print(response)
  file = json.loads(response.text)
  nameout = file[0]['name']
  print(f"{datein[0:2]}/{datein[2:]} ma svatek {nameout}.")
elif name_or_day == 'J':
  namein = input('Zadej jmeno: ')
  response = requests.get("http://svatky.adresa.info/json?name="+ namein)
  #print(response)
  file = json.loads(response.text)
  dateout = file[0]['date']
  print(f"{namein} ma svatek {dateout[0:2]}/{dateout[2:]}.")
else:
  print('Spatna odpoved')
"""