from pprint import pprint
vstup = open("04_lekce/preznamkovani.csv",encoding="utf-8")
studenti = [radek.strip() for radek in vstup]
vstup.close()
#print(f"tabulka {studenti}")

prepis = [radek.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","F") for radek in studenti[1:]]
print(prepis)


vystup = open("04_lekce/preznamkovani_nove.csv", mode="w", encoding="utf-8")
vystup.write(studenti[0] + '\n')
[vystup.write(radek + '\n') for radek in prepis]
vystup.close()



