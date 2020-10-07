import json
from pprint import pprint

# nejdriv probehla instalace v konzoli: pip python requests
# pak import funkce:
import requests

# requests.get mi stahne data z webove stranky a ulozi do promenne response:
response = requests.get("http://api.kodim.cz/python-data/people")

# vytisknu si response, pokud 200 tak je vse v poradku ( <Response [200]> )
#print(response)

# vsechna data ulozena v .text chci nacist jako json soubor a ulozit do promenne seznam 
seznam = json.loads(response.text)
#pprint(seznam)

# a) Zjistěte kolik lidí celkem seznam obsahuje
print(f'Seznam obsahuje {len(seznam)} lidi')

# b) Zjistěte jaké všechny informace máme o jednotlivých osobách
print('O osobach vime:', [info for info in seznam[0]])

# c) Zjistěte, kolik je v souboru mužů a žen
gender = [gender['gender'] for gender in seznam]
male = gender.count('Male')
female = gender.count('Female')
print(f'V souboru je {male} muzu a {female} zen')