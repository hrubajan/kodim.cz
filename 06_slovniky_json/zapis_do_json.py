import json

# ze souboru knihovna
kniha = {
  'ID':123456,
  'nazev':'Ucime se Python',
  'autor': [
    {
      'jmeno':'Martin',
      'prijmeni':'Podloucky'
    }
  ],
  'zanr': [
    'technika',
    'naucna literatura'
  ],
  'vydani': [
    {
      'rok':2019,
      'pocet-stran':895,
      'isbn':'987-3-16-148410-0'
    }
  ],
  'nakladatelstvi':'CPRESS',
  'pocet-kusu':5
}

soubor = open('kodim.cz/07_slovniky_json/zapis_kniha.json',"w",encoding='utf-8')

# vem data z 'kniha' uloz je jako JSON a vloz je do 'soubor', odsad o 4
json.dump(kniha, soubor, indent=4)
soubor.close()

# zapis z kodim.cz
"""
import json
hodiny = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
soubor = open('hodiny.json', 'w', encoding='utf-8')
json.dump(hodiny, soubor)
soubor.close()
"""