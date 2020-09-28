s = [2,4.7,6,8.4,4,3,1,2,7,4,3,0,9,5,3,0.5]
print(len(s))

# vrátit číslo nacházející se přesně uprostřed v zadaném seznamu s, u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu

print(s[len(s) // 2 + len(s) % 2 - 1])

s = [2,4.7,6,8.4,4,3,1,2,7,4,3,0,9,5,3,0.5]
serazeno = sorted(s)
print(serazeno)

index = len(serazeno) // 2 

print("Pocet znaku je:",len(s))

if len(s) % 2 == 0:
  print("Median je ", (serazeno[index]+serazeno[index-1])/2)
else:
  print("Median je ", serazeno[index])