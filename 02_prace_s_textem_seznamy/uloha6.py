jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

[len(jmeno) for jmeno in jmena]
#[5, 3, 8, 4, 7]

[jmeno.upper() for jmeno in jmena]
#['ROMAN', 'JAN', 'MIROSLAV', 'PETR', 'GABRIEL']

[jmeno+"a" for jmeno in jmena]
#['Romana', 'Jana', 'Miroslava', 'Petra', 'Gabriela']

[jmeno.lower() +"@email.cz" for jmeno in jmena]
#['roman@email.cz', 'jan@email.cz', 'miroslav@email.cz', 'petr@email.cz', 'gabriel@email.cz']