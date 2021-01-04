#
# Задание: работа с выпадающим списком
#
# Для этой задачи мы придумали еще один вариант капчи для роботов.
# Придется немного переобучить нашего робота, чтобы он справился с новым заданием.
#
# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу http ://suninjuly.github.i o /selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
#
# Когда ваш код заработает, попробуйте запустить его на странице
# http :/ /suninjuly.github.i o /selects2.html. Ваш код и для нее тоже должен пройти успешно.

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

try:
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    result = str(num1+num2)
    select = Select(browser.find_element_by_tag_name("select")).select_by_value(result)
    button = browser.find_element_by_class_name("btn.btn-default").click()

except Exception as error:
    print(f"There is an error.  Traceback: {error}.")

finally:
    time.sleep(7)
    browser.quit()