kurz = {
  'nazev': 'Úvod do programování',
  'lektor': 'Martin Podloucký',
  'konani': [
    {
      'misto': 'T-Mobile', 
      'koucove': [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Martina Nemčoková'
      ], 
      'ucastnic': 30
    },
    {
      'misto': 'MSD IT', 
      'koucove': [
        'Dan Vrátil', 
        'Zuzana Tučková', 
        'Martina Nemčoková'
      ], 
      'ucastnic': 25
    },
    {
      'misto': 'Škoda DigiLab', 
      'koucove': [
        'Dan Vrátil', 
        'Filip Kopecký', 
        'Kateřina Kalášková'
      ], 
      'ucastnic': 41
    }
  ]
}
# a. Vypište na výstup počet účastnic na posledním konání kurzu.
print(kurz['konani'][-1]['ucastnic'])
# b. Vypište na výstup jméno posledního kouče na prvním konání kurzu.
print(kurz['konani'][0]['koucove'][2])
# c. Vypište na výstup celkový počet konání kurzu.
print(len(kurz['konani']))
# d. Vypište na výstup všechna místa, na kterých se kurz konal. Použijte chroustání seznamů.
print([misto['misSto'] for misto in kurz['konani']])