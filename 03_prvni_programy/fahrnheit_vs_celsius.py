import sys
Fahrnheita = sys.argv[1]
Celsia = round(5*(int(sys.argv[1])-32)/9)

print(Fahrnheita + " stupnu Fahrnheita je " + str(Celsia) + " stupnu Celsia")