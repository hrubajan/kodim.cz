import statistics
import sys
prumer = statistics.mean([int(cislo) for cislo in sys.argv[1:]])
median = statistics.median([int(cislo) for cislo in sys.argv[1:]])
print("Průměr: " + str(prumer))
print("Medián: " + str(median))