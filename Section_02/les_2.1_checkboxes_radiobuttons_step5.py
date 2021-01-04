#
# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
#
# Продолжим использовать силу роботов 🤖 для решения повседневных задач.
# На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера,
# но сложным для человека.
#
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.
# Для этой задачи вам понадобится использовать атрибут .text для найденного элемента.
# Обратите внимание, что скобки здесь не нужны:
#
# x_element = browser.find_element_by_*(selector)
# x = x_element.text
# y = calc(x)
# Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
# Например, text для данного элемента <div class="message">У вас новое сообщение.</div> вернёт строку:
# "У вас новое сообщение".
#
# Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле.
# Не забудьте добавить этот код в начало вашего скрипта:
#
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже.


import math, time
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    x_element = browser.find_element_by_id('input_value')
    result = calc(x_element.text)
    input = browser.find_element_by_id('answer')
    input.send_keys(result)
    checkBox = browser.find_element_by_id('robotCheckbox')
    checkBox.click()
    radioButton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radioButton.click()
    button = browser.find_element_by_css_selector('[type="Submit"]')
    button.click()

except Exception as error:
    print(f'There is a problem.  Traceback: {error}')

finally:
    time.sleep(8)
    browser.quit()





