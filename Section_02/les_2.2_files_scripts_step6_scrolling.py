#Задание на execute_script

# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
# который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
#
# Для этой задачи вам понадобится использовать метод execute_script,
# чтобы сделать прокрутку в область видимости элементов, перекрытых футером.

# Метод execute_script
#
# Рассмотрим еще один очень полезный и мощный метод, но он требует хотя бы минимальных знаний JavaScript.
# С помощью метода execute_script можно выполнить программу, написанную на языке JavaScript,
# как часть сценария автотеста в запущенном браузере.

# Обратите внимание, что исполняемый JavaScript нужно заключать в кавычки (двойные или одинарные).
# Если внутри скрипта вам также понадобится использовать кавычки, а для выделения скрипта вы уже используете
# двойные кавычки, то в скрипте следует поставить одинарные:
#
# browser.execute_script("document.title='Script executing';")
# Такой формат записи тоже будет работать:
#
# browser.execute_script('document.title="Script executing";')
# Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой.
# Изменим сначала заголовок страницы, а затем вызовем alert:
#
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

# мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
# Делается это с помощью следующего скрипта:
#
# "return arguments[0].scrollIntoView(true);"
# Мы дополнительно передали в метод scrollIntoView аргумент true, чтобы элемент после скролла оказался
# в области видимости. Другие возможные параметры метода можно посмотреть здесь:
# https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
#
# В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
#
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# В метод execute_script мы передали текст js-скрипта и найденный элемент button,
# к которому нужно будет проскроллить страницу.
# После выполнения кода элемент button должен оказаться в верхней части страницы.
# Подробнее о методе см https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView .
#
# Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
#
# browser.execute_script("window.scrollBy(0, 100);")
# !Важно. Мы не будем в этом курсе изучать, как работает JavaScript,
# и обойдемся только приведенным выше примером скрипта с прокруткой страницы.
# Для сравнения приведем скрипт на этом языке, который делает то же, что приведенный выше пример для WebDriver:
#
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);


import math, time
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    x_val = int(browser.find_element_by_id("input_value").text)
    result = str(math.log(abs(12*math.sin(x_val))))
    input = browser.find_element_by_tag_name("input")
    input.send_keys(result)
    robot_box = browser.find_element_by_id("robotCheckbox").click()
    robot_radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_radio)
    robot_radio.click()
    button = browser.find_element_by_class_name("btn.btn-primary").click()

except Exception as error:
    print(f"There is a problem.  Traceback: {error}")

finally:
    time.sleep(7)
    browser.quit()