# Мы уже упоминали, что метод find_element_by возвращает только первый из всех элементов,
# которые подходят под условия поиска. Иногда возникает ситуация,
# когда у нас есть несколько одинаковых по сути объектов на странице,
# например, иконки товаров в корзине интернет-магазина.
# В тесте нам нужно проверить, что отображаются все выбранные для покупки товары.
# Для этого существуют методы find_elements_by,
# которые в отличие от find_element_by вернут список всех найденных элементов по заданному условию.
# Проверив длину списка, мы можем удостовериться, что в корзине отобразилось правильное количество товаров.
# Пример кода (код приведен только для примера, сайта fake-shop.com скорее всего не существует):

# Набор стратегий здесь такой же, как и в случае с find_element_by:
#
# find_elements_by_css_selector;
# find_elements_by_xpath;
# find_elements_by_name;
# find_elements_by_tag_name;
# find_elements_by_class_name;
# find_elements_by_link_text;
# find_elements_by_partial_link_text.
# Также для поиска нескольких элементов мы можем использовать универсальный метод
# find_elements вместе с атрибутами класса By:
#
# from selenium.webdriver.common.by import By
#
#
# driver.find_elements(By.CSS_SELECTOR, "button.submit")
# !Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements.
# Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException,
# которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат:
# если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.

# Задание: использование метода find_elements_by
#
# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали,
# добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
# Теперь эта задача под силу только роботам ﻿🤖﻿.
#
# Используйте WebDriver и подходящий метод find_elements_by. Введите полученный код в качестве ответа к этой задаче.

import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Info")
    time.sleep(2)

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

except Exception as error:
    print(f"Something went wrong. Traceback: {error}.")

finally:
    time.sleep(20)
    browser.quit()
