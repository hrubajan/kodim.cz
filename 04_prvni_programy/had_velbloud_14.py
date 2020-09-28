import sys
#had_hodi_velblouda

velbloud1 = sys.argv[1].split("_")

# title nebo capitalize vrati velke pismeno u kazdeho noveho slova
# velbloud2 = [x.title() for x in velbloud1[1:]]

velbloud2 = [velbloud1[0]] + [x[0].upper() + x[1:] for x in velbloud1[1:]]

velbloud = "".join(velbloud2)

#print(velbloud1)
#print(velbloud2)
print(velbloud)