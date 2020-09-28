kraje = [
...   ['Hlavní město Praha', '1 280 508'],
...   ['Jihočeský kraj', '638 782'],      
...   ['Jihomoravský kraj', '1 178 812'], 
...   ['Karlovarský kraj', '296 749'],
...   ['Kraj Vysočina', '508 952'],   
...   ['Královéhradecký kraj', '550 804'],  
...   ['Liberecký kraj', '440 636'],        
...   ['Moravskoslezský kraj', '1 209 879'],
...   ['Olomoucký kraj', '633 925'], 
...   ['Pardubický kraj', '517 087'],
...   ['Plzeňský kraj', '578 629'],  
...   ['Středočeský kraj', '1 338 982'],
...   ['Ústecký kraj', '821 377'],      
...   ['Zlínský kraj', '583 698']       
... ]
# a] 
[kraj[0] for kraj in kraje]
#['Hlavní město Praha', 'Jihočeský kraj', 'Jihomoravský kraj', 'Karlovarský kraj', 'Kraj Vysočina', 'Královéhradecký kraj', 'Liberecký kraj', 'Moravskoslezský kraj', 'Olomoucký kraj', 'Pardubický kraj', 'Plzeňský kraj', 'Středočeský kraj', 'Ústecký kraj', 'Zlínský kraj']

# b] 
pocet_obyvatel = [ int(kraj[1].replace(" ","")) for kraj in kraje]
pocet_obyvatel
#[1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]

# c]
pocet_obyvatel = [ int(kraj[1].replace(" ","")) for kraj in kraje]
pocet_obyvatel
#[1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]

nazev_kraje = [kraj[0] for kraj in kraje] 
nazev_kraje
#['Hlavní město Praha', 'Jihočeský kraj', 'Jihomoravský kraj', 'Karlovarský kraj', 'Kraj Vysočina', 'Královéhradecký kraj', 'Liberecký kraj', 'Moravskoslezský kraj', 'Olomoucký kraj', 'Pardubický kraj', 'Plzeňský kraj', 'Středočeský kraj', 'Ústecký kraj', 'Zlínský kraj']

kraje_jinak = [nazev_kraje,pocet_obyvatel]  
kraje_jinak
#[['Hlavní město Praha', 'Jihočeský kraj', 'Jihomoravský kraj', 'Karlovarský kraj', 'Kraj Vysočina', 'Královéhradecký kraj', 'Liberecký kraj', 'Moravskoslezský kraj', 'Olomoucký kraj', 'Pardubický kraj', 'Plzeňský kraj', 'Středočeský kraj', 'Ústecký kraj', 'Zlínský kraj'], [1280508, 638782, 1178812, 296749, 508952, 550804, 440636, 1209879, 633925, 517087, 578629, 1338982, 821377, 583698]]