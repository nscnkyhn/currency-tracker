import requests

url = "https://customers.garantibbva.com.tr/internet/digitalpublic/currency-convertor-public/v1/currency-convertor/currency-list-detail"

headers = {
    "Accept": "application/json",
    "Accept-Language": "en,tr;q=0.9,tr-TR;q=0.8,en-US;q=0.7",
    "Authorization": "",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "JSESSIONID=4621A1E6B3712CC50D913212B182B35D; rxVisitor=1722429054620PNATO55JTPKJLU54P06S18VN990OLBTQ; dtCookie=v_4_srv_66_sn_0C277DEDDBBC86C1527D86F4616B11A9_perc_100000_ol_0_mul_1_app-3Af257a4f77568aef4_1_app-3Ad121d29f2475c438_1; dtSa=-; dtPC=66$555817872_398h-vKUANAHQPTULTTSTFWHHUDMPVPVPKFHTE-0e0; rxvt=1724357619068|1724355802770",
    "DNT": "1",
    "Origin": "https://webforms.garantibbva.com.tr",
    "Pragma": "no-cache",
    "Referer": "https://webforms.garantibbva.com.tr/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "channel": "Internet",
    "client-id": "DslahJXaDW59ibNZppCm",
    "client-session-id": "0b13-f382-c671-476e-85f7",
    "client-type": "ArkClient",
    "dialect": "TR",
    "guid": "dd7261f750174e93b4b047eba4aea7ae",
    "ip": "127.0.0.1",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "state": "",
    "tenant-app-id": "",
    "tenant-company-id": "GAR",
    "tenant-geolocation": "TUR",
    "x-client-trace-id": "dd7261f750174e93b4b047eba4aea7ae"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
