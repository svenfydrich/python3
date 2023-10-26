from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.muenchen.de/veranstaltungen/event/heute"

driver = webdriver.Chrome()
driver.get(url)

items = driver.find_elements(By.CSS_SELECTOR, "h3.m-event-list-item__headline")

for item in items:
    print(item.text)
