import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()
    

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_quest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# Запустите тест:
# pytest -s -v test_fixture7.py

#  Вы увидите, что запустятся два теста.  В названии каждого теста в квадратных скобках будет написан параметр,
#  с которым он был запущен. Таким образом мы можем быстро и без дублирования кода увеличить количество проверок
#  для похожих сценариев.


# admin@admins-iMac Stepik_automation % cd Section_03/tests
# admin@admins-iMac tests % pytest -s -v test_pytest_parametr.py
# ================================================================ test session starts ================================================================
# platform darwin -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /usr/local/opt/python@3.9/bin/python3.9
# cachedir: .pytest_cache
# rootdir: /Users/admin/Documents/Stepik_automation/Section_03/tests, configfile: pytest.ini
# collected 2 items
#
# test_pytest_parametr.py::test_quest_should_see_login_link[ru]
# start browser for test...
# PASSED
# quit browser...
#
# test_pytest_parametr.py::test_quest_should_see_login_link[en-gb]
# start browser for test...
# PASSED
# quit browser...
#
#
# ================================================================= 2 passed in 5.77s =================================================================
# admin@admins-iMac tests %
