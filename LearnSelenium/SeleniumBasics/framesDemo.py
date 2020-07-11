from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Python\\Selenium Drivers\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#iframe, frameset, frame
driver.switch_to.frame("mce_0_ifr") #frame id or name or index value
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I'm able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)