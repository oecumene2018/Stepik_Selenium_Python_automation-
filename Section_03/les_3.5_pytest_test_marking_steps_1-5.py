# МАРКИРОВКА ТЕСТОВ ЧАСТЬ 1
#
# Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям,
# но также по каким-нибудь заданным нами категориям. Например, мы можем выбрать небольшое количество
# критичных тестов (smoke), которые нужно запускать на каждый коммит разработчиков,
# а остальные тесты обозначить как регрессионные (regression) и запускать их только перед релизом.
# Или у нас могут быть тесты, специфичные для конкретного браузера (internet explorer 11),
# и мы хотим запускать эти тесты только под данный браузер.
# Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
# Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.
#
# Давайте разделим тесты в одном из предыдущих примеров на smoke и regression.
#
# test_fixture8.py:

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
#
# pytest -s -v -m smoke test_fixture8.py
# Если всё сделано правильно, то должен запуститься только тест с маркировкой smoke.
#
# При этом вы увидите warning, то есть предупреждение:
# PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?
# You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
#     PytestUnknownMarkWarning,

# Это предупреждение появилось потому, что в последних версиях PyTest настоятельно рекомендуется регистрировать
# метки явно перед использованием. Это, например, позволяет избегать опечаток, когда вы можете ошибочно пометить
# ваш тест несуществующей меткой, и он будет пропускаться при прогоне тестов.

# Как же регистрировать метки?
#
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
# Текст после знака ":" является поясняющим — его можно не писать.
#
# Снова запустите тесты:
#
# pytest -s -v -m smoke test_fixture8.py
# Теперь предупреждений быть не должно.
#
#
# Так же можно маркировать целый тестовый класс.
# В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.





# МАРКИРОВКА ТЕСТОВ ЧАСТЬ 2
#
# Инверсия
#
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию.
# Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
#
# pytest -s -v -m "not smoke" test_fixture8.py
# Объединение тестов с разными маркировками
#
# Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:
#
# pytest -s -v -m "smoke or regression" test_fixture8.py
# Выбор тестов, имеющих несколько маркировок
#
# Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной
# операционной системы, например, для Windows 10.
# Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному
# из тестов эту метку.
#
# pytest.ini:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10

# test_fixture81.py:

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
#
# pytest -s -v -m "smoke and win10" test_fixture81.py
# Должен выполнится тест test_guest_should_see_basket_link_on_the_main_page.
