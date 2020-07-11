import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

searchItems = []
driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//nav[@id='primaryNav']/div[2]/button")).click().perform()
time.sleep(5)
wait = WebDriverWait(driver,5)
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Genealogies")))
items = driver.find_elements_by_xpath("//nav[@id='primaryNav']/div[2]/ul/li")
for item in items:
    searchItems.append(item.text)
    if item.text == "Genealogies":
        item.click()
print(searchItems)