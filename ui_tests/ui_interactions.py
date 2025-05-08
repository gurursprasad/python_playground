from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver_path = "/home/guru/Desktop/Desktop/GuruPrasad/GuruDocs/PracticePython/practice_python/ui_tests/chrome_driver/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# Alerts
alert_button = "alertbtn"
driver.find_element(By.ID, alert_button).click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()
# alert.send_keys("Test")


# Multi windows
driver.find_element(By.LINK_TEXT, "Open Window").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.close()
driver.switch_to.window(windows[0])


# Dropdown using select class
dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option2")
dropdown.select_by_value("option3")
dropdown.select_by_index(1)

