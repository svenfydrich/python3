from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# hier wird dir URL zum Scrapen eingegeben
url = "https://www.muenchen.de/veranstaltungen/event/heute"
driver = webdriver.Chrome()
driver.get(url)

# hier werden die zu scrapende CSS-Tags eingegeben
events = driver.find_elements(By.CSS_SELECTOR, "h3.m-event-list-item__headline") #das sind hier die namen der veranstaltungen
dates_and_times = driver.find_elements(By.CSS_SELECTOR, "p time")
locations = driver.find_elements(By.CSS_SELECTOR, '[itemprop="location"]')

concert_data = {
    "Name der Veranstaltung": [],
    "Datum und Uhrzeit": [],
    "Ort": []
}

for concert, date_and_time, location in zip(events, dates_and_times, locations):
    concert_name = concert.text
    date_and_time_text = date_and_time.text
    location_text = location.text
    concert_data["Name der Veranstaltung"].append(concert_name)
    concert_data["Datum und Uhrzeit"].append(date_and_time_text)
    concert_data["Ort"].append(location_text)

# schließt den web-driver
driver.quit()

# Create a DataFrame
df = pd.DataFrame(concert_data)

# exportiert den pandas dataframe zu einer excel-tabelle
excel_file = "events_table.xlsx"
df.to_excel(excel_file, index=False)

#exportiert den pandas dataframe zu einer csv-datei
df.to_csv("events_table.csv", index=False, sep='\t')
