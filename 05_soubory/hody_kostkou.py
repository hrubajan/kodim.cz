import random
import sys

pocet_hodu = int(sys.argv[1])

hod_kostkou = [random.randint(1,12) for _ in range(pocet_hodu)]
#print(hod_kostkou) 

vystup = open("kodim.cz/05_soubory/hody.txt", "w", encoding="utf-8")
vystup.write( ", ".join( [str(x) for x in hod_kostkou] ) )

vystup.close()