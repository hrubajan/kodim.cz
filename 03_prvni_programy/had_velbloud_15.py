import sys

camel = sys.argv[1]

lokace_velka_pismena = [cislo_znaku for cislo_znaku,znak in enumerate(camel) if znak.isupper()]

prelokace = [0] + lokace_velka_pismena + [len(camel)]

rozsekani = [ camel[prelokace[x]:prelokace[x+1]] for x in range(0,len(prelokace)-1) ]

had = "_".join(rozsekani).lower()

print(lokace_velka_pismena)
print(prelokace)
print(rozsekani)
print(had)


# Masterpiece of PETR KUBELKA
"""
super_velbloud = "tohleJeHad"

slovo = "vyhra" if "A".islower() else "prohra"
print(slovo)

vysledek = "".join(["_" + pismeno.lower() if pismeno.isupper() else pismeno for pismeno in super_velbloud])
print(vysledek)
"""
