from bs4 import BeautifulSoup
import requests
import json


def performRequest(url: str) -> str:
    response = requests.get(url)

    if (response.status_code == 200):
        return response.text
    else:
        return "Failed request"
    

url = "https://www.akbank.com/_vti_bin/AkbankServicesSecure/FrontEndServiceSecure.svc/GetCurrencyRates"
r: str = performRequest(url)

# İlk decode işlemi: dıştaki JSON string'ini decode etme
decoded_response = json.loads(r)

# GetCurrencyRatesResult anahtarındaki iç içe geçmiş JSON string'ini çıkarma
inner_json_string = decoded_response['GetCurrencyRatesResult']

# İç içe geçmiş JSON string'ini tekrar decode etme
clean_inner_json_string = inner_json_string.replace('\u000d', '').replace('\u000a', '').replace('\\', '')

# İkinci decode işlemi: temizlenmiş JSON string'ini decode etme
final_data = json.loads(clean_inner_json_string)

# Sonuçları print etme
print(final_data["date"])

for currency in final_data["cur"]:
    if (currency["KurTuru"] == "08"):
        print(f"Sembol : {currency['Title']}\tAlış : {currency['DovizAlis']}\tSatış : {currency['DovizSatis']}\tKur Türü : {currency['KurTuru']}")
