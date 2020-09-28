hodnoty = ['12', '1', '7', '-11']
int(hodnoty[2])+4

promena1 = hodnoty[2]
promena2 = int(promena1)+4
hodnoty[2] = str(promena2)
print(hodnoty)

# uloha 4 doplnujici, zapis do 1 radku

hodnoty = ['12', '1', '7', '-11']
hodnoty[2] = str(int(hodnoty[2])+4) 
print(hodnoty)
