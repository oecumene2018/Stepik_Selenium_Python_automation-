import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
result = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    target_link = browser.find_element_by_link_text(result)
    target_link.click()
    time.sleep(1)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Kyryl")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("And")
    input3 = browser.find_element_by_css_selector("input.form-control.city")
    input3.send_keys("Kyiv")
    input4 = browser.find_element_by_css_selector("input#country.form-control")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

except Exception as error:
    print(f"A problem occurred. Traceback: {error}")

finally:
    time.sleep(15)
    browser.quit()




