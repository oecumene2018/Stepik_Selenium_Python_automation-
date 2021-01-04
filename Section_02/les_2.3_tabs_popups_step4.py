# Alerts

# Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert,
# но и нажать кнопку OK, чтобы закрыть alert. Alert является модальным окном: это означает,
# что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert.
# Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept():
#
# alert = browser.switch_to.alert
# alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
#
# alert = browser.switch_to.alert
# alert_text = alert.text
# Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением
# или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда,
# что и в случае с alert:
#
# confirm = browser.switch_to.alert
# confirm.accept()

# Для confirm-окон можно использовать следующий метод для отказа:
#
# confirm.dismiss()
# То же самое, что и при нажатии пользователем кнопки "Отмена".
#
# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
# Чтобы ввести текст, используйте метод send_keys():
#
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()


# Задание: принимаем alert
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


import math, time
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)
    value = browser.find_element_by_id("input_value").text
    result = str(math.log(abs(12*math.sin(int(value)))))
    browser.find_element_by_id("answer").send_keys(result)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

except Exception as error:
    print(f"Something went wrong.  Traceback: {error}.")
else:
    print("Test passed successfully!")

finally:
    time.sleep(7)
    browser.quit()
