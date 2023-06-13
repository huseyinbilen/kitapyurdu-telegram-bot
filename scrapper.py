from bs4 import BeautifulSoup
import requests
import json


def bestSellers():
    url = "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"

    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    div = soup.find("div", {"class":"box no-padding"})
    div = div.find_all("div", {"class": "product-cr"})

    results = []

    for index, item in enumerate(div, start=1):
        name = item.find("div", {"class": "name"}).find("span").text
        results.append(f"{index}. {name}")
        # print(f"{index}. {name}")
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
        results.append(f"{index}. {name}")
        # print(f"{index}. {name}")
    return results

results = newReleases()
print(results)