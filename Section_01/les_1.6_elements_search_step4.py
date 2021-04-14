import time
from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Kyryl")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Andr")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Kyiv")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    print(f"An error occurred, traceback: {error}")

finally:
    time.sleep(30)
    browser.quit()





