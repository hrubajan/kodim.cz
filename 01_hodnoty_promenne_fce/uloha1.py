hodin = 7
mzda = 450
dni = 21

mesicni_prijem = hodin*mzda*dni
print(mesicni_prijem)

pausal = 0.6
dan = 0.15

zivnostnik = mesicni_prijem - ((mesicni_prijem*(1-pausal))*dan)
print(zivnostnik)