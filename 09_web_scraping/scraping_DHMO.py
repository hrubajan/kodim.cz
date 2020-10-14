from requests_html import HTMLSession
# stahuju data live z bezici webovky
session = HTMLSession()
stranka = session.get("http://scrape.kodim.cz/dhmo/index")

# Nechť program vypíše na výstup nadpisy všech sekcí (značka h2).
nadpis_sekce = stranka.html.find("h2")
for sekce in nadpis_sekce:
  print(sekce.text)

# Nechť program vypíše na výstup cesty všech odkazů na stránce (značka a, atribut href). 
odkazy = stranka.html.find("a")
for odkaz in odkazy:
  print(odkaz.attrs["href"])

# Nechť program vypíše na výstup cesty ke všem obrázkům na stránce (značka img, atribut src).
obrazky = stranka.html.find("img")
for obrazek in obrazky:
  print(obrazek.attrs["src"])