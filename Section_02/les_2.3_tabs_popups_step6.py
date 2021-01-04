# Переход на новую вкладку браузера
#
# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера.
# WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать
# со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:
#
# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
#
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
#
# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.


# Задание: переход на новую вкладку
#
# В этом задании после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


import time, math
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)
    browser.find_element_by_css_selector('[type="submit"]').click()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    time.sleep(1)
    value = browser.find_element_by_id("input_value").text
    result = str(math.log(abs(12*math.sin(int(value)))))
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_class_name("btn.btn-primary").click()

except Exception as error:
    print(f"Something is wrong. Traceback: {error}.")
else:
    print("Test is successful!")

finally:
    time.sleep(7)
    browser.quit()




