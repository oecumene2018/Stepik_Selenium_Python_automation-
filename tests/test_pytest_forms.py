import pytest
import time
from selenium import webdriver


def test_form_fill01():
    try:
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/registration1.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        assert "Congratulations! You have successfully registered!" == success_text, "Congratulations page did not load."

    finally:
        time.sleep(1)
        browser.quit()


def test_form_fill02():
    try:
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()

        browser.get("http://suninjuly.github.io/registration2.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        assert "Congratulations! You have successfully registered!" == success_text, "Congratulations page did not load."

    finally:
        time.sleep(1)
        browser.quit()

