import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nStarting browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuitting browser...")
    browser.quit()


class TestMainPage1:

    # Маркируем тест как smoke
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    # Маркируем тест как regression
    @pytest.mark.regression
    def test_guest_should_see_login_link_on_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")


# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке
# параметр -m и нужную метку:
#
# pytest -s -v -m smoke test_fixture8.py
# Если всё сделано правильно, то должен запуститься только тест с маркировкой smoke.
# При этом вы увидите warning, то есть предупреждение:
#
# PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid
# this warning - for details, see https://docs.pytest.org/en/latest/mark.html
#     PytestUnknownMarkWarning,
# Это предупреждение появилось потому, что в последних версиях PyTest настоятельно рекомендуется регистрировать
# метки явно перед использованием. Это, например, позволяет избегать опечаток, когда вы можете ошибочно пометить
# ваш тест несуществующей меткой, и он будет пропускаться при прогоне тестов.

# Метки регистрируются путем создания файла pytest.ini в корневой директории вашего тестового проекта
# и добавьте в файл следующие строки:
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
