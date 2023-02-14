import sys

unix1 = (sys.argv[1]).replace("\\","/")
print(unix1)

unix2 = "/".join( (sys.argv[1]).split("\\") )
print(unix2)