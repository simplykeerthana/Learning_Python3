
from selenium import webdriver

# each web browser have diifferent drives
# the driver allows selenium to open up the respective browser and manipulate it

#create an instance of the browser

chrome_browser = webdriver.Chrome('./chromedriver')

print(chrome_browser) #this open chrome browser automatically

chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo' in chrome_browser.title)

button = chrome_browser.find_element_by_class_name('btn-default')

print(button)

chrome_browser.quit()


#you can use selenium to control webpages, create a bot to like pages