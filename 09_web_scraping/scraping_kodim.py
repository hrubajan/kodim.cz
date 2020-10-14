from requests_html import HTMLSession
session = HTMLSession()
stranka = session.get("http://kodim.cz/kurzy/python-data/prvni-programy/")


cviceni = stranka.html.find(".exercise")
for c in cviceni:
    nadpis = c.find("h3")[0].text
    text = c.find(".exercise-body")[0].text

    print("Nadpis: " + nadpis)
    print(text)
    print()

