import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_guest_should_can_add_to_backet(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(10)
    assert len(button.text) > 0