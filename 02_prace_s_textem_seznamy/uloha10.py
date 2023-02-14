nazvy = [
...   'Někdo to rád horké, extended edition',
...   'Adéla ještě nevečeřela',
...   'Kulový blesk'
... ]

delky = [136, 105, 82]
trvani = [str(cas//60)+":"+str(cas%60) for cas in delky]

trvani
#['2:16', '1:45', '1:22']