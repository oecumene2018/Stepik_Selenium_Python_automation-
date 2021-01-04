# Проверка состояния включения/выключения checkboxe/radiobutton с помощью .get_attribute()

# from selenium import webdriver
#
# link = 'http://suninjuly.github.io/math.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# people_radio = browser.find_element_by_id('peopleRule')
# people_checked = people_radio.get_attribute("checked")
# print("Value of people radio: ", people_checked)
# assert people_checked is not None, "People radiobutton is not selected by default"
#
# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# if robots_checked == None:
#     print("It's Ok, the robots radiobutton is not checked by default")
# else:
#     assert robots_checked is None, "Robots radiobutton is checked by default. It's a bug!"
#
# browser.quit()

# Value of people radio:  true
# It's Ok, the robots radiobutton is not checked by default


# Задание: поиск сокровища с помощью get_attribute
#
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex
# у картинки с изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
#
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
#

import math, time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"


def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    pic_val = browser.find_element_by_tag_name('img').get_attribute("valuex")
    result = calculate(pic_val)
    input = browser.find_element_by_id("answer").send_keys(result)
    robot_box = browser.find_element_by_id("robotCheckbox").click()
    robots_radio = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name("btn.btn-default").click()

except Exception as error:
    print(f"Error: {error}.")

finally:
    time.sleep(10)
    browser.quit()
