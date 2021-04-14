words = "Happy New Year!"
assert "New" in words

assert abs(-21354) == -21354
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError

assert 35 in [1, 45, 81, 64], "No value in the given list."
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError: No value in the given list.

# Составные сообщения об ошибках
#
# Хорошо написанный текст помогает быстро локализовать найденный баг и разобраться в том,
# что произошло и из-за чего тест упал. Хороший assert сэкономит вам часы вашей работы, особенно когда
# количество тестов переходит за сотню.
#
# В целом, тут как с любым фидбеком: важно давать его точно и актуально.
# Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице:
#
# assert self.is_element_present('create_class_button', timeout=30), "No create class button"
# Примечание: Функция is_element_present() вспомогательная. Как её реализовать и использовать, мы разберемся чуть позжe.
#
# Если элемент встречается на нескольких страницах приложения, не лишним будет указать, где именно произошла ошибка:
#
# assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"
# Если вы работаете с каким-то текстом (например, проверяете информационное сообщение,
# текущий url, ссылку, placeholder в input-элементе или любой другой текст), в сообщении об ошибке всегда лучше
# выводить оба значения: то, которое ожидалось, и то, которое получили по факту. Всё как в хорошем багрепорте:
# ожидаемый и фактический результат.


# Еще один важный момент: когда вы работаете с текстом элементов на странице или любым другим контентом,
# который может измениться, всегда записывайте его в отдельную переменную для сравнения.
#
# неправильно:
#
# assert self.catalog_link.text  == "Каталог", \
#     f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"
# Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст
# на странице может измениться, и вы получите неактуальный текст об ошибке.
# Результат выполнения такого теста сложно анализировать:
#
# "Wrong language, got 'Каталог' instead of 'Каталог'"
# правильно:
#
# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"



# Задание: составные сообщения об ошибках
#
# Для закрепления материала реализуйте проверку самостоятельно.
#
# Вам дана функция test_input_text,  которая принимает два значения:
# expected_result — ожидаемый результат, и actual_result — фактический результат.
# Обратите внимание, input использовать не нужно!
#
# Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения,
# предоставить исчерпывающее сообщение об ошибке.
#
# Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!
#
# Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте ваш код на разных
# введенных значениях, проверьте вывод вашей функции на разных парах.
# Обрабатывать ситуацию с пустым или невалидным вводом не нужно.
#
# Sample Input 1:
# 8 11
# Sample Output 1:
# expected 8, got 11
# Sample Input 2:
# 11 11
# Sample Output 2:
# Sample Input 3:
# 11 15
# Sample Output 3:
# expected 11, got 15


def test_input_text(expected_result, actual_result):
    x = expected_result
    y = actual_result
    assert x == y, f"expected {x}, got {y}"

test_input_text(8,11)
test_input_text(11,11)
test_input_text(11,15)


# Задание: составные сообщения об ошибках и поиск подстроки
#
# Иногда при работе с текстами не нужны жёсткие проверки на полное совпадение, и требуется проверить,
# что некий текст является подстрокой другого текста. Это можно сделать либо с помощью ключевого слова in,
# либо с помощью функции find:
#
# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')
# Попробуйте запустить этот код в интерпретаторе, чтобы понять разницу в подходах.
#
# Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого вхождения
# подстроки в строку и -1, если подстрока не найдена. Обычно в автотестах достаточно использовать in,
# потому что это более читабельный вариант.
#
# Например, для проверки того, что в текущем url содержится строка login:
#
# assert "login" in browser.current_url, # сообщение об ошибке
# Реализуйте подобную проверку самостоятельно.
#
# Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.
#
# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и,
# в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
#
# Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!
#
# Маленький совет: попробуйте воспользоваться кнопкой "Запустить код" и протестируйте
# ваш код на разных введенных значениях, проверьте вывод вашей функции на разных парах.
# Обрабатывать ситуацию с пустым или невалидным вводом не нужно.
#
# Sample Input 1:
# fulltext some_value
# Sample Output 1:
# expected 'some_value' to be substring of 'fulltext'
# Sample Input 2:
# 1 1
# Sample Output 2:
# Sample Input 3:
# some_text some
# Sample Output 3:


def test_substring(full_string, substring):
    text = full_string
    words = substring
    assert words in text, f"expected '{words}' to be substring of '{text}'."

test_substring('fulltext', 'some_value')
# Traceback (most recent call last):
#   File "<input>", line 6, in <module>
#   File "<input>", line 4, in test_substring
# AssertionError: expected some_value to be substring of fulltext.
test_substring("1", "1")
test_substring('some_text', 'some')

