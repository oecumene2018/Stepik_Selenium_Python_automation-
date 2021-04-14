# Задание: оформляем тесты в стиле unittest
#
# Попробуйте оформить тесты из первого модуля в стиле unittest.
#
# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание
# Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
# Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё.
# Ловить исключения не надо (во всяком случае, здесь)!
#
# Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты
# даже при наличии неожиданного исключения.
#
# Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.

import unittest
import time
from selenium import webdriver


class TestFormFill(unittest.TestCase):

    def test_formFill01(self):
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual("Congratulations! You have successfully registered!", success_text, "Congratulations page "
                                                                                             "did not load.")
        time.sleep(3)
        browser.quit()


    def test_formFill02(self):
        fields = ['First name*', 'Last name*', 'Email*']
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        for field in fields:
            input_text = browser.find_element_by_xpath(f'//label[text()="{field}"]/following-sibling::input')
            input_text.send_keys('Any text')
        time.sleep(1)
        browser.find_element_by_css_selector('button.btn').click()
        time.sleep(1)
        success_text = browser.find_element_by_tag_name('h1').text
        self.assertEqual("Congratulations! You have successfully registered!", success_text, "Congratulations page "
                                                                                             "did not load.")
        time.sleep(1)
        browser.quit()



if __name__ == "__main__":
    unittest.main()