# Задание: поиск элемента по XPath
#
# На этот раз воспользуемся возможностью искать элементы по XPath.
#
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации,
# как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки.
# Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.
#
# Ваши шаги:
# В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
# XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# Запустите ваш код.
# Если вы подобрали правильный селектор и все прошло хорошо,
# то вы получите код, который нужно отправить в качестве ответа на это задание.

import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Kir")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("And")
    input3 = browser.find_element_by_css_selector("input.form-control.city")
    input3.send_keys("Kyiv")
    input4 = browser.find_element_by_css_selector("input#country.form-control")
    input4.send_keys("Ukraine")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


except Exception as error:
    print(f"Some problem occurred.  Traceback: {error}.")

finally:
    time.sleep(15)
    browser.quit()
