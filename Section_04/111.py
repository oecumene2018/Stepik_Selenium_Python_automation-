import time
import math
from mimesis import Person
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/basket/"
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#"http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #

browser = webdriver.Chrome()
browser.get(link)
assert browser.find_element(By.XPATH, "//div[@id='content_inner']/p"), "Basket is not empty"
print("Ok")

# alert = browser.switch_to.alert
# x = alert.text.split(" ")[2]
# answer = str(math.log(abs(12 * math.sin(float(x)))))
# alert.send_keys(answer)
# alert.accept()
# browser.implicitly_wait(2)
# try:
#     alert = browser.switch_to.alert
#     alert_text = alert.text
#     print(f"Your code: {alert_text}")
#     alert.accept()
# except NoAlertPresentException:
#     print("No second alert presented")
# browser.implicitly_wait(5)

# product_name = browser.find_element(By.XPATH, "//*[@class='col-sm-6 product_main']/h1").text
# assert product_name == browser.find_element(By.XPATH, "//*[@id='messages']/div[1]/div/strong").text, \
#     "The product has not been added"
# price = browser.find_element(By.CLASS_NAME, "price_color").text
# assert price in browser.find_element(By.XPATH, "//div[@id='messages']//strong").text, "Wrong price in basket "
# if browser.find_element(By.CLASS_NAME, "alert-success"):
#     print("OK")

from mimesis import Generic

generic = Generic('en')

test_email = generic.person.email()
test_password = generic.person.password(10)
print(test_email, "\n", test_password)

# cloherty1955@gmail.com
# S#xQg@Q{&8




