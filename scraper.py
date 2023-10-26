from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#Hier URL zum Scrapen eingeben
url = "https://www.muenchen.de/veranstaltungen/event/heute"
driver = webdriver.Chrome()
driver.get(url)

#Hier CSS-Tags zum scrapen eingeben
concerts = driver.find_elements(By.CSS_SELECTOR, "h3.m-event-list-item__headline")
dates_and_times = driver.find_elements(By.CSS_SELECTOR, "p time")
locations = driver.find_elements(By.CSS_SELECTOR, '[itemprop="location"]')


concert_data = {}

for concert, date_and_time, location in zip(concerts, dates_and_times, locations):
    concert_name = concert.text
    date_and_time_text = date_and_time.text
    location_text = location.text
    concert_data[concert_name] = date_and_time_text , location_text
#Konzert-Daten zum Terminal printen
for concert_name, date_and_time_text in concert_data.items():
    print("Veranstaltung:", concert_name)
    print("Datum und Uhrzeit:", date_and_time_text)
    print("Location:", location_text)
    print()

#Schließt 
driver.quit()