# PAGE OBJECT ДЛЯ ГЛАВНОЙ СТРАНИЦЫ САЙТА
#
# Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина.
#
# 1. Откройте файл main_page.py
#
# 2. В нем нужно сделать импорт базового класса BasePage:
#
# from .base_page import BasePage
# 3. В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage.
# Класс-предок в Python указывается в скобках:
#
# class MainPage(BasePage):
# таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка.
#
# 4. Перенесите метод из предыдущего урока в класс MainPage:
#
# def go_to_login_page(browser):
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()

# Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера,
# мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self ,
# чтобы иметь доступ к атрибутам и методам класса:
#
# def go_to_login_page(self):
#
# Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом
# с помощью self:
#
# self.browser.find_element_by_css_selector("#login_link")
# Заодно заменим find на более универсальный:
#
# self.browser.find_element(By.CSS_SELECTOR, "#login_link")
# Итого, файл main_page.py:
#
# from .base_page import BasePage
# from selenium.webdriver.common.by import By
#
# class MainPage(BasePage):
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#         login_link.click()
