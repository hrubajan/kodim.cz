cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]

# uloha 13 a 14
# 1. maximum
maximum = sorted(cisla)[-1]
print(maximum)

# 1. maximum funkce
def highest_number(x):
    my_max = x[0]
    for item in x:
        if my_max < item:
            my_max = item
    return my_max
print(highest_number([77,48,19,17,93,90]))

# 2. maximum
druhe_max = sorted(cisla)[-2]
print(druhe_max)

"""
# aby byly 2 stejna cisla brana jako 1 hodnota
seznam = [5,5,4,3]
# seradime
seznam_set = sorted(seznam)
# udelame z toho set --> jako distinct v sql
seznam_set = list(set(seznam_set))
print(f'seznam : {seznam_set}')
print(f'2 nejvetsi max: {seznam_set[-2]}')
"""