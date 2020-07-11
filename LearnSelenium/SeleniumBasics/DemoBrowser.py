from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.back()
driver.refresh()
driver.close()