# Задание: запуск автотестов для разных языков интерфейса
#
# Мы хотим, чтобы разрабатываемый нами интернет-магазин работал одинаково хорошо для пользователей из любой страны.
# Чтобы убедиться в работоспособности решения с поддержкой разных языков, мы планируем запускать набор автотестов
# для каждого языка. Вам как разработчику автотестов нужно реализовать решение, которое позволит запускать автотесты
# для разных языков пользователей, передавая нужный язык в командной строке.
#
# Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
# Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться
# в фикстуре browser и передаваться в тест как параметр.
# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления
# в корзину. Например, можно проверять товар, доступный по
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
# Тест должен запускаться с параметром language следующей командой:

# pytest --language=es test_items.py

# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
# Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
# Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно
# отправить только один раз.
# Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.
# Это задание с peer-review, поэтому кроме формальных критериев другие учащиеся могут проверять
# корректность написания вашего кода.

# Важно! Если при рецензировании чужого решения вы получаете ошибку вроде:
#
# raise ValueError("option names %s already added" % conflict)
# ValueError: option names {'--language'} already added

# Перепроверьте, что у вас нет своего conftest.py в директории выше, смотри шаг 4:
# https://stepik.org/lesson/237240/step/4?unit=209628

# Ваше решение будет проверяться по следующим критериям:
#
# 1) Тест в репозитории можно запустить командой pytest --language=es, тест успешно проходит.
# 2) Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду time.sleep(30)
# сразу после открытия ссылки. Запустите тест с параметром --language=fr и визуально проверьте,
# что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
# 3) Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
# 4) В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным
# для проверяемой страницы. Есть assert.
# Название тестового метода внутри файла test_items.py соответствует задаче.
# 5) Название test_something не удовлетворяет требованиям.


# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose language version: ru, en-gb, es, fr (etc.)")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    version_lang = request.config.getoption('language')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs',
                                        {'intl.accept_languages': version_lang})
        print(f"\nStarting browser for testing {version_lang} version...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', version_lang)
        print(f"\nStarting browser for testing {version_lang} version...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser {version_lang} still is not implemented")
    yield browser
    print("\nQuitting browser...")
    browser.quit()

# test_items.py

import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_on_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button, 'Basket button does not exist on the page'

