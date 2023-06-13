from bs4 import BeautifulSoup
import requests
import json

from unidecode import unidecode


def bestSellers():
    url = "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", {"class":"box no-padding"})
    div = div.find_all("div", {"class": "product-cr"})

    results = []

    for index, item in enumerate(div, start=1):
        name = item.find("div", {"class": "name"}).find("span").text
        name = unidecode(name)
        results.append(f"{index}. {name}")
    return results

def newReleases():
    url = "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=2"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", {"class":"box no-padding"})
    div = div.find_all("div", {"class": "product-cr"})

    results = []

    for index, item in enumerate(div, start=1):
        name = item.find("div", {"class": "name"}).find("span").text
        name = unidecode(name)
        results.append(f"{index}. {name}")
    return results

def publisherOfTheWeek():
    url = "https://www.kitapyurdu.com/yayinevi/the-kitap/7446.html"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", {"class":"box no-padding"})
    div = div.find_all("div", {"class": "product-cr"})

    results = []

    for index, item in enumerate(div, start=1):
        name = item.find("div", {"class": "name"}).find("span").text
        name = unidecode(name)
        results.append(f"{index}. {name}")
    return results

print(bestSellers())