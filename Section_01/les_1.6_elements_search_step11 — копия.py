import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
fields = ['First name*', 'Last name*', 'Email*']

try:
    browser = webdriver.Chrome()
    browser.get(link)
    for field in fields:
        input = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
        input.send_keys('Any text')
    time.sleep(2)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(2)

    #  на success странице находим элемент, содержащий нужный текст
    check_success_text = browser.find_element_by_tag_name('h1')
    success_text = check_success_text.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == success_text, "Congratulations page did not load."

except Exception as error:
    print(f'there is a problem. Traceback: {error}.')

finally:
    time.sleep(10)
    browser.quit()

