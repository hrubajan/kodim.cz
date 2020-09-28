hodnoty = '12.1 1.68 7.45 -11.51'
list = hodnoty.split(" ")
list[-1] = str( float(list[-1])+0.25 ) 
print(list)

hodnoty = " ".join(list)
print(hodnoty)
