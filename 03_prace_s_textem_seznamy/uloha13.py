# prikazova radka
# doplnujici / 13 / jine reseni 12 e]

"""
UVOD K ENUMERATE

seznam = ["a", "b", "c"]
seznam
['a', 'b', 'c']
[slovo for slovo in seznam]
['a', 'b', 'c']
[ [cislo_slova, slovo] for cislo_slova, slovo in enumerate(seznam)]
[[0, 'a'], [1, 'b'], [2, 'c']]
"""

[ [cislo_kraje, kraj] for cislo_kraje,kraj in enumerate(hlasy)]
# vrati:
[[0, [78774, 43179, 225111, 144799, 242854]], [1, [91062, 22451, 17475, 53391, 46450]], [2, [179186, 216499, 4493, 156305, 61222]], [3, [9619, 53476, 926, 64737, 34566]], [4, [66904, 85730, 27271, 12964, 38041]], [5, [118755, 1929, 30426, 25178, 31952]], [6, [64467, 40993, 81181, 39392, 4335]], [7, [11221, 97970, 26179, 98539, 112578]], [8, [171064, 7638, 8752, 96666, 39738]], [9, [74235, 101680, 18920, 45904, 1922]], [10, [39309, 1505, 10531, 30458, 40228]], [11, [131584, 1812, 241122, 22267, 99326]], [12, [194133, 39985, 200997, 28229, 20780]], [13, [66188, 51607, 15977, 177272, 17664]]]

[[kandidat for kandidat in kraj] for kraj in hlasy]
# vrati:
[[78774, 43179, 225111, 144799, 242854], [91062, 22451, 17475, 53391, 
46450], [179186, 216499, 4493, 156305, 61222], [9619, 53476, 926, 64737, 34566], [66904, 85730, 27271, 12964, 38041], [118755, 1929, 30426, 
25178, 31952], [64467, 40993, 81181, 39392, 4335], [11221, 97970, 26179, 98539, 112578], [171064, 7638, 8752, 96666, 39738], [74235, 101680, 18920, 45904, 1922], [39309, 1505, 10531, 30458, 40228], [131584, 1812, 241122, 22267, 99326], [194133, 39985, 200997, 28229, 20780], [66188, 51607, 15977, 177272, 17664]]

# jenom pro prvni radek:
[[ round(kandidat/sum(hlasy[0]),2) for kandidat in kraj] for kraj in hlasy]
# vrati:
[[0.11, 0.06, 0.31, 0.2, 0.33], [0.12, 0.03, 0.02, 0.07, 0.06], [0.24, 0.29, 0.01, 0.21, 0.08], [0.01, 0.07, 0.0, 0.09, 0.05], [0.09, 0.12, 0.04, 0.02, 0.05], 
[0.16, 0.0, 0.04, 0.03, 0.04], [0.09, 0.06, 0.11, 0.05, 0.01], [0.02, 0.13, 0.04, 0.13, 0.15], [0.23, 0.01, 0.01, 0.13, 0.05], [0.1, 0.14, 0.03, 0.06, 0.0], 
[0.05, 0.0, 0.01, 0.04, 0.05], [0.18, 0.0, 0.33, 0.03, 0.14], [0.26, 0.05, 0.27, 0.04, 0.03], [0.09, 0.07, 0.02, 0.24, 0.02]]

# pro vsechny radky:
[[ round(kandidat/sum(hlasy[cislo_kraje]),2) for kandidat in kraj] for cislo_kraje, kraj in enumerate(hlasy)]
# vrati:
[[0.11, 0.06, 0.31, 0.2, 0.33], [0.39, 0.1, 0.08, 0.23, 0.2], [0.29, 0.35, 0.01, 0.25, 0.1], [0.06, 0.33, 0.01, 0.4, 0.21], [0.29, 0.37, 0.12, 0.06, 0.16], 
[0.57, 0.01, 0.15, 0.12, 0.15], [0.28, 0.18, 0.35, 0.17, 0.02], [0.03, 0.28, 0.08, 0.28, 0.32], [0.53, 0.02, 0.03, 0.3, 0.12], [0.31, 0.42, 0.08, 0.19, 0.01], 
[0.32, 0.01, 0.09, 0.25, 0.33], [0.27, 0.0, 0.49, 0.04, 0.2], [0.4, 0.08, 0.42, 0.06, 0.04], [0.2, 0.16, 0.05, 0.54, 0.05]]