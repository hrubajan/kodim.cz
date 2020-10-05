import sys

x = int(sys.argv[1])

if x in range(1,11) or x in range(19,29):
  if x % 2 == 0:
    print(f'Cislo ({x}) je sude, cerne')
  else: 
    print(f'Cislo ({x}) je liche, cervene')
elif x in range(11,19) or x in range(29,37):
  if x % 2 == 0:
    print(f'Cislo ({x}) je sude, cervene')
  else: 
    print(f'Cislo ({x}) je liche, cerne')
elif x == 0:
  print(f'Cislo je {x}, neni sude ani liche, cerne ani cervene')
else:
  print('Cislo je mimo rozsah rulety')