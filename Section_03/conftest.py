#!/usr/bin/env python
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser == 'chrome':
        print("\n start chrome for test")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()





