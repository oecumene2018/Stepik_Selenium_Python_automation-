
import math
import time
import pytest
from selenium import webdriver


# @pytest.fixture(scope="function")
# def browser():
#     print("open browser to start test...")
#     browser = webdriver.Chrome()
#     yield browser
#     print("quitting browser...")
#     browser.quit()


links_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize("link", links_list)
def test_check_page(browser, link):
    browser.get(link)
    browser.implicitly_wait(15)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    feedback = browser.find_element_by_class_name("smart-hints__hint").text
    assert feedback == "Correct!", f"Expected feedback == Correct!, instead got '{feedback}'."


# =================================== FAILURES ===================================
# ___________ test_check_page[https://stepik.org/lesson/236898/step/1] ___________
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="1735fb80d7f7d47cf0e6c6b55db4adc3")>
# link = 'https://stepik.org/lesson/236898/step/1'
#
#     @pytest.mark.parametrize("link", links_list)
#     def test_check_page(browser, link):
#         browser.get(link)
#         browser.implicitly_wait(15)
#         answer = str(math.log(int(time.time())))
#         browser.find_element_by_tag_name("textarea").send_keys(answer)
#         button = browser.find_element_by_class_name("submit-submission")
#         button.click()
#         feedback = browser.find_element_by_class_name("smart-hints__hint").text
# >       assert feedback == "Correct!", f"Expected feedback == Correct!, instead got '{feedback}'."
# E       AssertionError: Expected feedback == Correct!, instead got 'The owls '.
# E       assert 'The owls ' == 'Correct!'
#
# test_pytest_param_task.py:40: AssertionError
# ___________ test_check_page[https://stepik.org/lesson/236899/step/1] ___________
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="4785e36f7d1aa436acedf01e2a293108")>
# link = 'https://stepik.org/lesson/236899/step/1'
#
#     @pytest.mark.parametrize("link", links_list)
#     def test_check_page(browser, link):
#         browser.get(link)
#         browser.implicitly_wait(15)
#         answer = str(math.log(int(time.time())))
#         browser.find_element_by_tag_name("textarea").send_keys(answer)
#         button = browser.find_element_by_class_name("submit-submission")
#         button.click()
#         feedback = browser.find_element_by_class_name("smart-hints__hint").text
# >       assert feedback == "Correct!", f"Expected feedback == Correct!, instead got '{feedback}'."
# E       AssertionError: Expected feedback == Correct!, instead got 'are not '.
# E       assert 'are not ' == 'Correct!'
#
# test_pytest_param_task.py:40: AssertionError
# ___________ test_check_page[https://stepik.org/lesson/236905/step/1] ___________
#
# browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="d008cca9327c2b0f077d93766d64601d")>
# link = 'https://stepik.org/lesson/236905/step/1'
#
#     @pytest.mark.parametrize("link", links_list)
#     def test_check_page(browser, link):
#         browser.get(link)
#         browser.implicitly_wait(15)
#         answer = str(math.log(int(time.time())))
#         browser.find_element_by_tag_name("textarea").send_keys(answer)
#         button = browser.find_element_by_class_name("submit-submission")
#         button.click()
#         feedback = browser.find_element_by_class_name("smart-hints__hint").text
# >       assert feedback == "Correct!", f"Expected feedback == Correct!, instead got '{feedback}'."
# E       AssertionError: Expected feedback == Correct!, instead got 'what they seem! OvO'.
# E       assert 'what they seem! OvO' == 'Correct!'
#
# test_pytest_param_task.py:40: AssertionError
# =========================== short test summary info ============================
# FAILED test_pytest_param_task.py::test_check_page[https://stepik.org/lesson/236898/step/1]
# FAILED test_pytest_param_task.py::test_check_page[https://stepik.org/lesson/236899/step/1]
# FAILED test_pytest_param_task.py::test_check_page[https://stepik.org/lesson/236905/step/1]
# ========================= 3 failed, 5 passed in 38.20s =========================
#
# Process finished with exit code 1