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
    @pytest.mark.win10
    def test_guest_should_see_login_link_on_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")


# Предположим, у нас есть regression-тесты, которые нужно запускать только для определенной операционной системы,
# например, для Windows 10. Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному из тестов эту метку.
#
# pytest.ini:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10

# Чтобы запустить только regression-тесты для Windows 10, нужно использовать логическое И:
#
# pytest -s -v -m "regression and win10" test_fixture81.py
# Должен выполнится тест test_guest_should_see_basket_link_on_the_main_page.
