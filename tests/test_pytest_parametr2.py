import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()
    

languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский", marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]

@pytest.mark.parametrize('code, lang', languages)
def test_quest_should_see_login_link(browser, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("The language checked %s" % lang)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# Запустите тест:
# pytest -s -v test_fixture7.py

# admin@admins-iMac Stepik_automation % cd Section_03/tests
# admin@admins-iMac tests % pytest -s -v test_pytest_parametr2.py
# ================================================================ test session starts ================================================================
# platform darwin -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /usr/local/opt/python@3.9/bin/python3.9
# cachedir: .pytest_cache
# rootdir: /Users/admin/Documents/Stepik_automation/Section_03/tests, configfile: pytest.ini
# collected 4 items
#
# test_pytest_parametr2.py::test_quest_should_see_login_link[ru-\u0440\u0443\u0441\u0441\u043a\u0438\u0439]
# start browser for test...
# The language checked русский
# PASSED
# quit browser...
#
# test_pytest_parametr2.py::test_quest_should_see_login_link[de-\u043d\u0435\u043c\u0435\u0446\u043a\u0438\u0439]
# start browser for test...
# The language checked немецкий
# PASSED
# quit browser...
#
# test_pytest_parametr2.py::test_quest_should_see_login_link[ua-\u0443\u043a\u0440\u0430\u0438\u043d\u0441\u043a\u0438\u0439]
# start browser for test...
# The language checked украинский
# XPASS (no ua ...)
# quit browser...
#
# test_pytest_parametr2.py::test_quest_should_see_login_link[en-gb-\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439]
# start browser for test...
# The language checked английский
# PASSED
# quit browser...
#
#
# =========================================================== 3 passed, 1 xpassed in 10.61s ===========================================================
# admin@admins-iMac tests %
