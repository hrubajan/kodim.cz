# LEVEL 1
import sys
username = sys.argv[1]
password = sys.argv[2]
system_pwd = 'Heslo123'

if password == system_pwd:
  print('Pristup povolen')
else:
  print('Pristup odepren')

""" # LEVEL 2 user input
username = input('Username: ')
password = input('Password: ')
system_pwd = 'Heslo123'

if password == system_pwd:
  print('Pristup povolen')
else:
  print('Pristup odepren') """

""" # LEVEL 3 funkce
import sys
jmeno = sys.argv[1]
heslo = sys.argv[2]
spravne_jmeno = ['peta', 'verca']
spravne_heslo = ['python', 'sql']

def je_v_databazi(jmeno,heslo):
  for index in range(len(spravne_heslo)):
    if jmeno == spravne_jmeno[index] and heslo == spravne_heslo[index]:
      return True # nebo rovnou 'Vitej uzivateli'
  return False # a rovnou 'Spatny login' a nemusi se pokracovat nize if podminkou
odpoved = je_v_databazi(jmeno,heslo)

if odpoved == True:
  print('Vitej uzivateli')
else:
  print('Spatny login') """