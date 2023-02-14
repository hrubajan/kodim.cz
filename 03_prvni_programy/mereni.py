mereni = [
  ['po', 17.3],
  ['út', 16.8],
  ['st', 15.1],
  ['čt', 13.2],
  ['pá', 14.0],
  ['so', 13.9],
  ['ne', 15.8]
]
teploty = [radek[1] for radek in mereni]
prumer = sum(teploty) / len(teploty)

rozdily = [(t-prumer) for t in teploty]
teplota_nejbliz_prumeru = rozdily.index(min(rozdily))

dny = [radek[0] for radek in mereni]

print( "Den s teplotou nejblíž průměru je: " + dny[rozdily.index(min(rozdily))] )