import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
driver.find_element(By.ID, "openwindow").click()
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
# time.sleep(20)

# Checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(3)

# Alerts
name = "Guru"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()
