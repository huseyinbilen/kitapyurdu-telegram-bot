from bs4 import BeautifulSoup
import requests
import json


def mostSeller():
    url = "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", {"class":"box no-padding"})
    div = div.find_all("div", {"class": "product-cr"})

    for i in div:
        name = i.find("div", {"class": "name"}).find("span").text
        print(name)

mostSeller()