from selenium import webdriver
from selenium.webdriver.common.by import By
#importiert selenium, eine Library um CSS-tags zu scrapen

url = "https://www.muenchen.de/veranstaltungen/event/heute" #hier URL der Website zum scrapen eingeben

driver = webdriver.Chrome() #öffnet die URL in Google Chrome
driver.get(url)

#items = driver.find_elements(By.CSS_SELECTOR, "h3.m-event-list-item__headline") #Der String selektiert die CSS-tags. Hier: Titel des Events
items = driver.find_elements(By.CSS_SELECTOR, "p.m-event-list-item__detail") # Ort, Datum und Uhrzeit
for item in items:
    print(item.text)
