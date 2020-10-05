import sys

mena = sys.argv[1]
castka = int(sys.argv[2])

if mena == 'czk':
  usd = round(castka/25.0352,2)
  print(f'{castka} CZK je rovno {usd} USD')
elif mena == 'eur':
  usd = round(castka/0.9211,2)
  print(f'{castka} EUR je rovno {usd} USD')
elif mena == 'cny':
  usd = round(castka/7.0663,2)
  print(f'{castka} CNY je rovno {usd} USD')
else:
  print('Tuto menu neznam')

