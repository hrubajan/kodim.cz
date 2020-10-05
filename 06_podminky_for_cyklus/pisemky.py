znamky = [2,3,1,2,4,3,2,1,2,5,4,1,2,3,1,5,4,1,2,3,1,4,2,1,3,2,1,2,1,4,5]

vyborne = 0
chvalitebne = 0
dobre = 0
dostatecne = 0
nedostatecne = 0

for znamka in znamky:
  if znamka == 1:
    vyborne += 1
  elif znamka == 2:
    chvalitebne += 1
  elif znamka == 3:
    dobre += 1
  elif znamka == 4:
    dostatecne += 1
  else:
    nedostatecne += 1

print(f'Dohromady z {len(znamky)} znamek bylo {vyborne} znamek za 1, {chvalitebne} znamek za 2, {dobre} znamek za 3, {dostatecne} znamek za 4 a {nedostatecne} znamek za 5.')
