from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.akbank.com/doviz-kurlari')

with open("akbank.html", "w", encoding="utf-8") as f:
    f.write(r.text)

with open("akbank.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.title)

