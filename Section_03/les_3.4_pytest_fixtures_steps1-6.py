# ФИКСТУРЫ


# https://medium.com/@dmrlx/введение-в-pytest-cc6175c7d0dc
# Фикстурами в PyTest'е называют функции, которые выполняются с различным scope-ом
# и возвращают какое-то значение либо выполняют какие-то действия.
#
# Пример:
#
# import time
# import pytest
#
# @pytest.fixture(scope='class', autouse=True)
# def suite_data():
#     print("\n> Suite setup")
#     yield
#     print("> Suite teardown")
#
# В данном примере “@pytest.fixture” — декоратор, указывающий, что функция ниже является фикстурой,
# “scope=’…’” указывает на “очерёдность” выполнения, а “autouse=True” говорит о том,
# что фикстура будет применена для каждого сьюта в тестовом фреймворке
#
# Очерёдность выполнения - их четыре: “session”, “module”, “class” и “function”.
# Выполняются они в такой же последовательности.
#
# Из фикстуры можно передать значение в сьют с помощью оператора yield. При этом после yield можно добавить ещё код,
# который будет выполнен после кейса. Таким образом можно сказать, что всё, что идёт до оператора yield является
# “setup”, а всё, что после — “teardown” (yield, к слову, может ничего и не возвращать, а просто будет разделителем,
# отделяющим сетап от тирдауна).


# https://habr.com/ru/post/448786/ :
# в pytest и в этой книге test fixtures относятся к механизму, который обеспечивает pytest,
# чтобы отделить код “подготовка к (getting ready for)” и “очистка после (cleaning up after)” от ваших тестовых функций.
#
# pytest fixtures — одна из уникальных фишек, которые поднимают pytest над другими тестовыми средами,
# и являются причиной того, почему многие уважаемые люди переключаются на… и остаются с pytest.

# https://habr.com/ru/post/448786/

# Обмен Fixtures через conftest.py
#
# Можно поместить фикстуры в отдельные тестовые файлы, но для совместного использования фикстур в нескольких тестовых
# файлах лучше использовать файл conftest.py где-то в общем месте, централизованно для всех тестов.
# Для проекта задач все фикстуры будут находиться в tasks_proj/tests/conftest.py.
#
# Оттуда, fixtures могут быть разделены любым тестом. Вы можете поместить fixtures в отдельные тестовые файлы,
# если вы хотите, чтобы fixture использовался только в тестах этого файле. Аналогично, вы можете иметь другие
# файлы conftest.py в подкаталогах каталога top tests. Если вы это сделаете, fixtures, определенные
# в этих низкоуровневых файлах conftest.py, будут доступны для тестов в этом каталоге и подкаталогах.
# Однако до сих пор fixtures в проекте «Задачи» были предназначены для любого теста.
# Поэтому использование всех наших инструментов в файле conftest.py в корне тестирования, tasks_proj/tests,
# имеет наибольший смысл.
#
# Хотя conftest.py является модулем Python, он не должен импортироваться тестовыми файлами.
# Не импортируйте conftest ни когда! Файл conftest.py считывается pytest и считается локальным плагином,
# что станет понятно, когда мы начнем говорить о плагинах в главе 5 «Плагины» на стр. 95.
# Пока что считайте tests/conftest.py как место где мы можем поместить fixtures, для использования всеми тестами
# в каталоге тестов. Затем давайте переработаем некоторые наши тесты для task_proj,
# чтобы правильно использовать фикстуры.



# ИСПОЛЬЗОВАНИЕ FIXTURES ДЛЯ SETUP И TEARDOWN

# Большинство тестов в проекте Tasks предполагают, что база данных Tasks уже настроена, запущена и готова.
# И мы должны убрать какие то записи в конце, если есть какая-то необходимость в очистке.
# И возможно понадобится также отключиться от базы данных.
# К счастью, большая часть этого позаботилась в коде задач с tasks.start_tasks_db(<directory to store db\>,
# 'tiny' or 'mongo') и tasks.stop_tasks_db(); нам просто требуется вызвать их в нужный момент,
# и ещё нам понадобится временный каталог.
#
# К счастью, pytest включает в себя отличную фикстуру под названием tmpdir.
# Мы можем использовать её для тестирования и не должны беспокоиться о очистке.
# Это не магия, просто хорошая практика кодирования от самых пытливых людей.
# (Не переживайте; мы разберем tmpdir и более подробно распишем его с помощью tmpdir_factory
# в разделе «Использование tmpdir и tmpdir_factory» на стр. 71.)


#
# ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ
#
# Фикстуры могут возвращать значение, которое затем можно использовать в тестах.
# Давайте перепишем наш предыдущий пример с использованием PyTest фикстур.
# Мы создадим фикстуру browser, которая будет создавать объект WebDriver.
# Этот объект мы сможем использовать в тестах для взаимодействия с браузером.
# Для этого мы напишем метод browser и укажем, что он является фикстурой с помощью декоратора @pytest.fixture.
# После этого мы можем вызывать фикстуру в тестах, передав ее как параметр.
# По умолчанию фикстура будет создаваться для каждого тестового метода,
# то есть для каждого теста запустится свой экземпляр браузера.
#
# pytest -s -v test_fixture2.py
# test_fixture2.py:
#
# import pytest
# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     return browser
#
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# Финализаторы — закрываем браузер
#
# Вероятно, вы заметили, что мы не использовали в этом примере команду browser.quit().
# Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов,
# а закрылись только после завершения всех тестов. Закрытие браузеров произошло благодаря встроенной фикстуре —
# сборщику мусора. Но если бы количество тестов насчитывало больше нескольких десятков,
# то открытые окна браузеров могли привести к тому, что оперативная память закончилась бы очень быстро.
# Поэтому надо явно закрывать браузеры после каждого теста. Для этого мы можем воспользоваться финализаторами.
# Один из вариантов финализатора — использование ключевого слова Python: yield.
# После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки,
# следующей за строкой со словом yield:
#
# test_fixture3.py
#
# import pytest
# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     # этот код выполнится после завершения теста
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#
# Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer.
# Можете изучить его сами по документации PyTest.
#
# Рекомендуем также выносить очистку данных и памяти в фикстуру, вместо того чтобы писать это в шагах теста:
# финализатор выполнится даже в ситуации, когда тест упал с ошибкой.




#  ОБЛАСТЬ ВИДИМОСТИ SCOPE
#
# Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”.
# Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии.
#
# Запустим все наши тесты из класса TestMainPage1 в одном браузере для экономии времени, задав scope="class" в фикстуре browser:
#
# test_fixture5.py
#
# import pytest
# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         print("finish test1")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#         print("finish test2")
# Мы видим, что в данном примере браузер открылся один раз и тесты последовательно выполнились в этом браузере.
# Здесь мы проделали это в качестве примера, но мы крайне рекомендуем всё же запускать отдельный экземпляр браузера
# для каждого теста, чтобы повысить стабильность тестов.
# Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных),
# можно вызывать и один раз за сессию запуска тестов.



# Автоиспользование фикстур
#
# При описании фикстуры можно указать дополнительный параметр autouse=True,
# который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:
#
# test_fixture_autouse.py

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Попробуйте запустить этот код и увидите, что для каждого теста фикстура подготовки данных выполнилась
# без явного вызова. Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов.
# Без явной необходимости автоиспользованием фикстур лучше не пользоваться.
#
# Итог
#
# Вспомогательные функции — это очень мощная штука, которая решает много проблем при работе с автотестами.
# Основной плюс в том, что их удобно использовать в любых тестах без дублирования лишнего кода.
#
# Дополнительные материалы про фикстуры, которые мы настоятельно советуем почитать, приведены ниже:
#
# https://habr.com/ru/company/yandex/blog/242795/
#
# https://docs.pytest.org/en/latest/fixture.html

