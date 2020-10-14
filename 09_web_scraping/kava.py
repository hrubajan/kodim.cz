from requests_html import HTMLSession
import json

session = HTMLSession()
stranka = session.get("https://www.mall.cz/instantni-kava")
stranka.html.render(sleep=5)

final = []
final.append("název_produktu" + ',' + "cena" + ',' + "dostupnost")
insta_kavy = stranka.html.find(".lst-item")
for kava in insta_kavy:
    title = kava.find(".lst-product-item-title")[0].text
    price = kava.find(".lst-product-item-price-value")[0].text
    availability = kava.find(".lst-product-item-availability-wrapper")[0].text
    polozka = title + ',' + price + ',' + availability
    #print(polozka)
    final.append(polozka)

print(final)

import csv
with open("kodim.cz/09_web_scraping/insta_kava.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file,delimiter="\n")
    writer.writerow(final)