import sys
hodin = int(sys.argv[1]) 
minut = int(sys.argv[2])
minuty = 60*hodin + minut
print(str(hodin) + "hodin a " + str(minut) + "minut je: " + str(minuty) + "minut")
