# this code writes in search box of wikipedia and then pressses ENTER button.
# Selenium WebScraping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# count = drive.find_element(By.CSS_SELECTOR, value="#articlecount a")
# locating through content text link
# count = drive.find_element(By.LINK_TEXT, value="A Peculiar Family")
# count.click()

# typing in the search bar through selenium
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)



# drive.quit()
