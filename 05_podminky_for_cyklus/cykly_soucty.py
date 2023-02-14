cisla = [1,2,3,4,5]

soucet = 0

for cislo in cisla:
  soucet += cislo
  # v pripade odtabulovani vrati kumulovany soucet
  print(f'Kumulovany soucet: {soucet}')
# bez tabulatoru vrati rovnou soucet vsech cisel
print(f'Soucet vsech cisel pomoci cyklu: {soucet}')
# soucet take lze pomocu sum()
print(f'Soucet vsech cisel pomoci sumy: {sum(cisla)}')