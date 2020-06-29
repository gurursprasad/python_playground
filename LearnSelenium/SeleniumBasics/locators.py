from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='name']").send_keys("GuruPrasad")
# driver.find_element_by_name("name").send_keys("Guru")
driver.find_element_by_name("email").send_keys("gurursprasad@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
assert "success" in message
# driver.close()