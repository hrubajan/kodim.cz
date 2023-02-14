hlasy = [ 
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]
""" 
SPATNE za a] : [ sum(kraj[0]) for kraj in hlasy]
proc to nefunguje:
    hlasy je seznam seznamu
    kraj je seznam cisel, postupne jednolive radky te tabulky hlasy
    kraj[0] je prvni cislo kazdeho radku tabulky hlasy
    sum(kraj[0]) aplikuje funkci sum na cislo, jenze funkce sum slouzi ke scitani hodnot seznamu, nedava smysl secist jedine cislo => crashne to 
"""

# DOBRE za a]:
sum ( [kraj[0] for kraj in hlasy] )
sum ( [kraj[1] for kraj in hlasy] )
sum ( [kraj[2] for kraj in hlasy] )
sum ( [kraj[3] for kraj in hlasy] )
sum ( [kraj[4] for kraj in hlasy] )

# v JEDNOM RADKU za a]
[ sum ( kraj[x] for kraj in hlasy ) for x in range(5) ]
#[1296501, 766454, 909361, 996101, 791656]

# b] => vyhral prvni kandidat (pomoci poctu hlasu nebo indexu)
kandidati_celkem = [  sum ( kraj[x] for kraj in hlasy ) for x in [0,1,2,3,4] ] 
max( kandidati_celkem)
#1296501

# nebo
kandidati_celkem.index( max(kandidati_celkem) )
#0

# c] => nejvyssi - Praha, nejnizsi - Plzensky kraj
kraj_celkem = [ sum(radek) for radek in hlasy ]
#[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]
max(kraj_celkem)
#734717
min(kraj_celkem)
#122031

# c] reseni jinak rovnou s indexem
kraj_celkem.index( max(kraj_celkem) )
#0
kraj_celkem.index( min(kraj_celkem) )
#10

# d]
kraje_celkem = [sum(radek) for radek in hlasy]
kraje_celkem
#[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]

jmena = ['igor', 'augustyn', 'vladan', 'ondrej', 'radim']

vyherni_pozice = [ radek.index(max(radek)) for radek in hlasy]
vyherni_pozice
#[4, 0, 1, 3, 1, 0, 2, 4, 0, 1, 4, 2, 2, 3]

[pozice for pozice in vyherni_pozice] 
#[4, 0, 1, 3, 1, 0, 2, 4, 0, 1, 4, 2, 2, 3]

[jmena[pozice] for pozice in vyherni_pozice] 
#['radim', 'igor', 'augustyn', 'ondrej', 'augustyn', 'igor', 'vladan','radim', 'igor', 'augustyn', 'radim', 'vladan', 'vladan', 'ondrej']

# e]
[ [round(kandidat/sum(kraj)*100,2) for kandidat in kraj] for kraj in hlasy]
"""
[[10.72, 5.88, 30.64, 19.71, 33.05], 
 [39.45, 9.73, 7.57, 23.13, 20.12], 
 [29.01, 35.05, 0.73, 25.3, 9.91], 
 [5.89, 32.74, 0.57, 39.64, 21.16], 
 [28.97, 37.13, 11.81, 5.61, 16.47], 
 [57.03, 0.93, 14.61, 12.09, 15.34], 
 [27.98, 17.79, 35.24, 17.1, 1.88], 
 [3.24, 28.28, 7.56, 28.44, 32.49], 
 [52.82, 2.36, 2.7, 29.85, 12.27], 
 [30.59, 41.9, 7.8, 18.92, 0.79], 
 [32.21, 1.23, 8.63, 24.96, 32.97], 
 [26.52, 0.37, 48.6, 4.49, 20.02], 
 [40.1, 8.26, 41.52, 5.83, 4.29], 
 [20.14, 15.7, 4.86, 53.93, 5.37]]
"""

[ [str(round(x/sum(kraj)*100,2))+"%" for x in kraj] for kraj in hlasy] 
"""
[['10.72%', '5.88%', '30.64%', '19.71%', '33.05%'], 
 ['39.45%', '9.73%', '7.57%', '23.13%', '20.12%'], 
 ['29.01%', '35.05%', '0.73%', '25.3%', '9.91%'], 
 ['5.89%', '32.74%', '0.57%', '39.64%', '21.16%'], 
 ['28.97%', '37.13%', '11.81%', '5.61%', '16.47%'], 
 ['57.03%', '0.93%', '14.61%', '12.09%', '15.34%'], 
 ['27.98%', '17.79%', '35.24%', '17.1%', '1.88%'], 
 ['3.24%', '28.28%', '7.56%', '28.44%', '32.49%'], 
 ['52.82%', '2.36%', '2.7%', '29.85%', '12.27%'], 
 ['30.59%', '41.9%', '7.8%', '18.92%', '0.79%'], 
 ['32.21%', '1.23%', '8.63%', '24.96%', '32.97%'], 
 ['26.52%', '0.37%', '48.6%', '4.49%', '20.02%'], 
 ['40.1%', '8.26%', '41.52%', '5.83%', '4.29%'], 
 ['20.14%', '15.7%', '4.86%', '53.93%', '5.37%']] 
"""

# f] volebni ucast nad 50%
kraje_celkem
#[734717, 230829, 617705, 163324, 230910, 208240, 230368, 346487, 323858, 242661, 122031, 496111, 484124, 328708]
pocet_obyvatel
#[1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]

[ kraje_celkem[x] > (pocet_obyvatel[x]*0.5) for x in range(14)]   
#[True, False, True, True, False, False, True, False, True, False, False, False, True, True]