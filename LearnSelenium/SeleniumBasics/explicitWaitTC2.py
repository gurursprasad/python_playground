from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
wait = WebDriverWait(driver,8)
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
driver.find_element_by_xpath("//button[@class='search-button']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='search-button']")))
cartbuttons = driver.find_elements_by_xpath("//div[@class='product']/div/button")
for button in cartbuttons:
    button.click()
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div/button").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='totAmt']")))
totalamt = driver.find_element_by_xpath("//span[@class='totAmt']").text
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoinfo")))
discamt = driver.find_element_by_xpath("//span[@class='discountAmt']").text
assert float(discamt) < int(totalamt)
