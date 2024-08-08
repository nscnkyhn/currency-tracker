from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

def performRequest(url: str, headers: dict = []) -> str:
    response = requests.get(url, headers=headers)

    if (response.status_code == 200):
        return response.text
    else:
        return "Failed request"
    
now = datetime.now()
date = now.strftime('%Y-%m-%d')
timestamp = now.timestamp()

url = f"https://www.isbank.com.tr/_vti_bin/DV.Isbank/PriceAndRate/PriceAndRateService.svc/GetFxRates?Lang=tr&fxRateType=IB&date={date}&time={timestamp}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

r: str = performRequest(url, headers=headers)
decoded_data = json.loads(r)

for currency in decoded_data["Data"]:
    print(f"Sembol : {currency['code']}\tAlış : {currency['fxRateBuy']}\tSatış : {currency['fxRateSell']}\tAçıklama : {currency['description']}")
