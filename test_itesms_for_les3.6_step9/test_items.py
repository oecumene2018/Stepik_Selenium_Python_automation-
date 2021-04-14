import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button, 'Basket button does not exist on the page'

