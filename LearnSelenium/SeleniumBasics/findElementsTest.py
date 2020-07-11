from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(20000)
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
for city in cities:
    print(city.text)