from requests_html import HTMLSession
import json

session = HTMLSession()
stranka = session.get("https://react-shopping-cart-67954.firebaseapp.com/")
stranka.html.render(sleep=5)

seznam = []

tricka = stranka.html.find(".shelf-item")
for tricko in tricka:
    title = tricko.find(".shelf-item__title")[0].text
    price = tricko.find(".shelf-item__price .val")[0].text
    slovnik = {
      "id" : tricko.attrs["data-sku"],
      "title" : title,
      "price" : price
    }
    seznam.append(slovnik)
    #print(title + " - " + price)

soubor = open("kodim.cz/09_web_scraping/tricka.json", "w", encoding="utf-8")
json.dump(seznam, soubor, indent=4)
soubor.close()