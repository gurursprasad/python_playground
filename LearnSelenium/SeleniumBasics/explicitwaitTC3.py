import time

from selenium import webdriver

cart = []
driver = webdriver.Chrome(executable_path="E:\\Projects\\Browser Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(4)
driver.find_element_by_xpath("//form[@class='search-form']/button").click()
cartbuttons = driver.find_elements_by_xpath("//div[@class='products']/div/div/button")
for cartbutton in cartbuttons:
    cartbutton.click()
time.sleep(4)
driver.find_element_by_css_selector("img[alt='Cart']").click()
itemsincart = driver.find_elements_by_xpath("//div[@class='cart-preview active']/div/div/ul/li/div[@class='product-total']/p[@class='amount']")
sum1=0
for itemincart in itemsincart:
    sum1=sum1+int(itemincart.text)
    cart.append(itemincart.text)
print(cart)
print(sum1)
driver.find_element_by_xpath("//div[@class='cart-preview active']/div/button").click()
time.sleep(4)
tablecart = []
tabledatas = driver.find_elements_by_xpath("//div[@class='products']/table/tr/td[5]/p")
sum2=0
for tabledata in tabledatas:
    sum2=sum2+int(tabledata.text)
    tablecart.append(tabledata.text)
print(tablecart)
print(sum2)
assert sum1 == sum2