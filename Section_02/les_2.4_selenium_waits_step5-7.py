# Selenium Waits (Implicit Waits) Ожидания

# Используются, когда применяется java_script или возможны сбои в загрузке данных с сервера
# и элементы появляются не сразу или постепення или со спецэффектами.

# В таких ситуациях решение с time.sleep() не годится: оно не масштабируемое и трудно поддерживаемое.
#
# Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов из-за
# асинхронной работы скриптов или задержек от сервера, поэтому мы будем ждать появление элемента на странице
# в течение заданного количества времени (например, 5 секунд).
# Проверять наличие элемента будем каждые 500 мс. Как только элемент будет найден,
# мы сразу перейдем к следующему шагу в тесте.
# Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.
#
# В Selenium WebDriver есть специальный способ организации такого ожидания,
# который позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам.
# Ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз,
# когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.
#
# Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep()
# и добавить одну строчку с методом implicitly wait:

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# Теперь мы можем быть уверены, что при небольших задержках в работе сайта наши тесты продолжат работать стабильно.
# На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде,
# чем выбросить исключение NoSuchElementException.

# Задание: Про Exceptions
#
# Теперь мы знаем, как настроить ожидание поиска элемента. Во время поиска WebDriver каждые 0.5 секунды проверяет,
# появился ли нужный элемент в DOM-модели браузера (Document Object Model — «объектная модель документа»,
# интерфейс для доступа к HTML-содержимому сайта). Если произойдет ошибка, то WebDriver выбросит одно из следующих
# исключений (exceptions):
#
# Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
# Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
# то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время
# решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом,
# то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
# Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.
# Знание причин появления исключений помогает отлаживать тесты и понимать, где находится баг в случае его возникновения.

# Задание:

# Какую ошибку вы увидите в консоли, если попытаетесь выполнить
# команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?

# Ответ: NoSuchElementException

# Explicit Waits (WebDriverWait и expected_conditions)
#
# В предыдущем шаге мы решили проблему с ожиданием элементов на странице.
# Однако методы find_element проверяют только то, что элемент появился на странице.
# В то же время элемент может иметь дополнительные свойства, которые могут быть важны для наших тестов.
# Рассмотрим пример с кнопкой, которая отправляет данные:
#
# Кнопка может быть неактивной, то есть её нельзя кликнуть;
# Кнопка может содержать текст, который меняется в зависимости от действий пользователя.
# Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
# Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.
# Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна, то WebDriver все равно
# проэмулирует действие нажатия на кнопку, но данные не будут отправлены.
#
# Давайте попробуем запустить следующий тест:
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
# Мы видим, что WebDriver смог найти кнопку с id="verify" и кликнуть по ней, но тест упал
# на поиске элемента "verify_message" с итоговым сообщением:
#
# no such element: Unable to locate element: {"method":"id","selector":"verify_message"}
# Это произошло из-за того, что WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной.
# На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки,
# но неактивная кнопка в момент загрузки — обычное дело для реального сайта.
#
# Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться,
# когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных
# ожиданий (Explicit Waits), которые позволяют задать СПЕЦИАЛЬНОЕ_ОЖИДАНИЕ_ДЛЯ_КОНКРЕТНОГО_ЭЛЕМЕНТА.
# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions. Улучшим наш тест:
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# ЧТО ПРОИСХОДИТ:
# Обратите внимание, что в объекте WebDriverWait используется функция UNTIL, в которую передается правило ожидания,
# элемент, а также значение, по которому мы будем искать элемент.
# Как вы видите, в этом случае нужно использовать поиск элементов с помощью класса By, который мы рассмотрели ранее
# (https://stepik.org/lesson/138920/step/2?unit=196194).
# ELEMENT_TO_BE_CLICKABLE вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
#

# В модуле EXPECTED_CONDITIONS есть много других правил, которые позволяют реализовать необходимые ожидания:
#
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

# Описание каждого правила можно найти на сайте
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
#
# Если мы захотим проверять, что кнопка становится неактивной после отправки данных,
# то можно задать негативное правило с помощью метода until_not:
#
# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

# Задание: ждем нужный текст на странице
#
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100,
# используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
#
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

# Вот правильный синтаксис для text_to_be_present_in_element
# .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    book_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element_by_id("book").click()
    submit_button = browser.find_element_by_id("solve")

# Скролим страницу вниз, чтобы показалось новое поле для ввода и кнопка Submit:
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    input_value = math.log(abs(12*math.sin(int(browser.find_element_by_id("input_value").text))))
    browser.find_element_by_id("answer").send_keys(str(input_value))
    submit_button.click()

except Exception as error:
    print(f"There is a problem.  Traceback: {error}")
else:
    print(browser.switch_to.alert.text)
#     Congrats, you've passed the task! Copy this code as the answer to Stepik quiz: 28.98581837897664

finally:
    time.sleep(7)
    browser.quit()





