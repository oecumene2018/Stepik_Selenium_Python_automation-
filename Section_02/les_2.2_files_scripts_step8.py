#Задание: загрузка файла

# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.


# Загрузка файлов
#
# Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys.
# Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.
#
# Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — os.
# В этом случае ваш код не будет зависеть от операционной системы, которую вы используете.
# Добавление файла будет работать и на Windows, и на Linux, и даже на MaсOS.
#
# Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт,
# который вы запускаете:
#
# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
# Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__))
# и print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу.
# Подробнее о методах модуля os можете почитать самостоятельно
# в документации: https://docs.python.org/3/library/os.path.html.
# Обратите внимание, что это будет работать только при запуске кода из файла, в интерпретаторе не сработает.
#
# Если совсем непонятно что происходит, пример:
#
# Допустим, мы написали код скрипта и сохранили код в lesson2_step7.py в свой локальной папке D:\stepik_homework.
# Активируем виртуальное окружение и запускаем его python lesson2_step7.py.
# В таком случае конструкция os.path.abspath(os.path.dirname(__file__)) вернет нам путь до директории файла с кодом,
# то есть D:\stepik_homework. В эту же папку кладем файл, который хотим прикрепить, то есть file.txt.
# Тогда, после выполнения команды:
#
# file_path = os.path.join(current_dir, 'file.txt')
#
# В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
# Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt перенесем в другую папку,
# или на компьютер с другой ОС, то такой код без правок заработает и там.

import os, time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
fields = ["firstname", "lastname", "email"]

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    for field in fields:
        browser.find_element_by_name(field).send_keys(field)
    input_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test.txt")
    time.sleep(1)
    input_file.send_keys(file_path)
    browser.find_element_by_class_name("btn.btn-primary").click()

except Exception as error:
    print(f"Some error occured. Traceback: {error}.")

finally:
    time.sleep(7)
    browser.quit()

