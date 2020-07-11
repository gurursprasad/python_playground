import time

from selenium import webdriver

#pause the test for few seconds using Time class

prodlist = []
prodlist1= []
driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    prodlist.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(prodlist)
time.sleep(5)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div/button").click()
time.sleep(5)
names = driver.find_elements_by_xpath("//tr/td[2]/p")
for name in names:
    prodlist1.append(name.text)
print(prodlist1)
assert prodlist == prodlist1