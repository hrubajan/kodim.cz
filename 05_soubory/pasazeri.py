# reseni Petr

vstup = open("04_lekce/pasazeri.txt", encoding="utf-8")
# odstraneni mezer
dny = [radek.strip().split(" ") for radek in vstup]
vstup.close()
#print(dny)

# nejdriv hodnoty rozdelit podle carky a vzit cestu tam[0] nebo zpet[1], pak z hodnoty udelat integer a secist za jeden den a pak secist za cely tyden
tam = sum([ sum([int(hodnota.split(",")[0]) for hodnota in den]) for den in dny])
print("Smerem tam jelo {} pasazeru".format(tam) )

zpet = sum([ sum([int(hodnota.split(",")[1]) for hodnota in den]) for den in dny])
print("Smerem zpet jelo {} pasazeru".format(zpet) )

# moje delsi reseni
"""
vstup = open("04_lekce/pasazeri.txt", encoding="utf-8")
dny = [radek.strip().split(" ") for radek in vstup]
vstup.close()
#print(dny)

cesty = [ [cesta.split(",") for cesta in den] for den in dny]
#print(cesty)

cesty_int = [ [ [int(x) for x in cesta] for cesta in cesty[y]] for y in range(len(cesty)) ]
#print(cesty_int)

tam = sum( [ sum( [x[0] for x in cesty_int[y] ] ) for y in range(5)] )
print("Smerem tam jelo {} pasazeru".format(tam) )
zpet = sum( [ sum( [x[1] for x in cesty_int[y] ] ) for y in range(5)] )
print("Smerem zpet jelo {} pasazeru".format(zpet) )
"""