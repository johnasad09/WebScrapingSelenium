# this code fetches the upcoming events and their dates from python.org and then save it to a csv file, 
# Selenium web scraping

from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

list = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

data = [item.text for item in list]
pprint(data)
events = [{"date": item.split('\n')[0], "event": item.split('\n')[1]} for item in data]
print(events)

with open("events.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["date", "event"])
    writer.writeheader()
    writer.writerows(events)

driver.quit()
