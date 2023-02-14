# HINT u textaku si zkontrolovat prazdne radky na konci, dela to neplechu 

# a]
soubor = open("kodim.cz/05_soubory/slohovka.txt", encoding="utf-8")

# b] => nejdriv ocistit strip (mezery pred a za) pak split (rozdelit podle mezer mezi slovami)
seznam_slov = [slovo.strip().split(" ") for slovo in soubor]

# c]
pocet_slov_radek = [len(radek) for radek in seznam_slov]
# d]
pocet_slov_celkem = sum(pocet_slov_radek)

print(seznam_slov)
print(pocet_slov_radek)
print(pocet_slov_celkem)