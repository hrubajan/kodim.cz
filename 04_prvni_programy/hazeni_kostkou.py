import random
import sys

kolikastenna = int(sys.argv[1])
pocet_hodu = int(sys.argv[2])

hod_kostkou = [random.randint(1,kolikastenna) for _ in range(pocet_hodu)]

print(hod_kostkou) 
