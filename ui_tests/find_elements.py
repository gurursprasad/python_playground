import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

dropdown_list = ".ui-menu-item" # css
country_auto_suggest_textbox = "autosuggest" # id


driver.find_element(By.ID, country_auto_suggest_textbox).send_keys("IND")
time.sleep(2)

list_items = driver.find_elements(By.CSS_SELECTOR, dropdown_list)
for item in list_items:
    if item.text.lower() == "India".lower():
        item.click()
        break

print(driver.find_element(By.ID, country_auto_suggest_textbox).get_attribute("value"))