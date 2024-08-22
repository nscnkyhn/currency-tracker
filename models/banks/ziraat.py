import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driverOptions = webdriver.ChromeOptions()
#driverOptions.add_argument("--headless=new")
driver = webdriver.Chrome(options=driverOptions)
driver.get("https://www.ziraatbank.com.tr/tr/fiyatlar-ve-oranlar")
assert "Ziraat Bankası" in driver.title
dovizKurlarıButtonElement = driver.find_element(By.XPATH, "//div[@data-module='DovizKur']")
dovizKurlarıButtonElement.click()
dovizKurlarıTableElement = driver.find_element(By.ID, "result-dovizkur")
dovizKurlarıHTMLTable = dovizKurlarıTableElement.get_attribute("innerHTML")

table_data = [[cell.text for cell in row("td")] for row in BeautifulSoup(dovizKurlarıHTMLTable)("tr")]
print(table_data)

time.sleep(3)
driver.close()