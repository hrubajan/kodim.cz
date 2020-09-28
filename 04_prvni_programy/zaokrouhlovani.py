# ULOHA 5
"""
# ruzne druhy zaokrouhlovani
import math
import sys
nahoru = math.ceil(float(sys.argv[1]))
dolu = math.floor(float(sys.argv[1]))
klasik = round(float(sys.argv[1]))
print(f'zaokrouhleni nahoru => {nahoru}')
print(f'zaokrouhleni dolu => {dolu}')
print(f'zaokrouhleni round => {klasik}')
"""


# ULOHA 8
""" 
# klasicke zaokrouhlovani (=> napriklad i u 4.5 ma zaokrouhlit nahoru)
import math
import sys

# cislo dane prikazovou radkou
zaokr = round( float(sys.argv[1]) + 0.05)
print(zaokr)

# cisla dane seznamem
cisla = [1.4, 2.5, 3.5, 6.4, 8.5]
zaokr = [round(x+0.05) for x in cisla]
print(zaokr) 
"""





