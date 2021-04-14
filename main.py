from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 130);")
button.click()
assert True


words = "Happy New Year!"
assert "New" in words

assert abs(-21354) == -21354
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError

assert 35 in [1, 45, 81, 64], "No value in the given list."
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError: No value in the given list.
