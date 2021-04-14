import time


def test_add_to_card_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_element_by_css_selector('#add_to_basket_form button[type=submit]')
    time.sleep(13)
    assert button.is_enabled() and button.is_displayed(), 'Add to card button is not displayed'
