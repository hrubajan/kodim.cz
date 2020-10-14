from requests_html import HTML

stranka = open("kodim.cz/09_web_scraping/uvod.html", encoding='utf-8')
obsah = stranka.read()
# vemu obsah z uvod.html a poslu ho do velkeho HTML (importovaneho z modulu), ktera si obsah precte opravdu jako html kod a ulozim do promenne html
html = HTML(html=obsah)

# hledam jen nazvy tagu bez zobacku
# pomoci find najdu vsechny vyskyty a pomoci for cyklu si je vypisu
odstavce = html.find("p") # <p> odstavec 
for odstavec in odstavce:
  print(odstavec.text)

# tecka v zavorce u find se nepise pokud hledam vsechny vyskyty (skupiny), tecka mi rika, ze se to vybira podle tridy (class)
nadpisy = html.find(".nadpis") # class="nadpis", ( tridu jsem pripsala rucne k h2)
for nadpis in nadpisy:
  print(nadpis.text)
# hledam prvek, ktery je uvnitr jineho prvku
prvky = html.find("div p") # vsechny <p> uvnitr <div>
for prvek in prvky:
  print(prvek.text)

prvky = html.find(".sekce1 p") # vsechny prvky <p> uvnitr prvku s class="sekce1"
for prvek in prvky:
  print(prvek.text)

odkazy = html.find("a") # vsechny prvky <a> 
for odkaz in odkazy:
  print(odkaz.attrs["href"]) # vypise hodnotu atributu href

""" from requests_html import HTML
soubor = open('sample.html', encoding="utf-8")
obsah = soubor.read()
soubor.close()
html = HTML(html=obsah) """