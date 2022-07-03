import urllib, json
import requests


def main(currency):
    curr = currency['currency'] + '_in'
    url_api = "https://belarusbank.by/api/kursExchange?"
    with urllib.request.urlopen(url_api) as url:
        data = json.loads(url.read())
    return { 'sender': "Nikolay Grinkevich", 'rate': data[0][curr] }