import json
soubor = open('priklad/absolventi.json',encoding='utf-8')

# .read() umi cely soubor nacist se vsim vsudy do jednoho velkeho retezce
text = soubor.read() 

soubor.close()

# fce .loads() tento retezec precte a pokud jsou v nem data ve formatu JSON prevede je na Py slovnik
absolventi = json.loads(text) 

print(absolventi)

# pokud se nechceme obtezovat se ctenim souboru:
"""
import json
soubor = open('kodim.cz/07_slovniky_json/absolventi.json', encoding='utf-8')
# muzeme pouzit metodu .load(), ktera umi precist JSON primo z otevreneho souboru
absolventi = json.load(soubor)
soubor.close()
print(absolventi)
"""