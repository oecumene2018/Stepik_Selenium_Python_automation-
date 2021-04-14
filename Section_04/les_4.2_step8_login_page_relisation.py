#
# РЕАЛИЗАЦИЯ LOGINPAGE
#
# Если вы хорошо ориентируетесь в тест-дизайне, скорее всего вас немного коробит тест с переходом к логину —
# там ведь нет никаких проверок. Давайте проверим, что мы действительно перешли на страницу логина. Для этого
# нам будет нужен новый Page Object. Заодно разберемся, как между ними переключаться в ходе теста.
#
# Скачайте файл с шаблоном для LoginPage. Добавьте его в папку pages. Внутри есть заглушки для методов проверок:
#
should_be_login_url
should_be_login_form
should_be_register_form
# Реализуйте их самостоятельно:
#
# 1. В файле locators.py создайте класс LoginPageLocators
#
# 2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators
#
# 3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке.
# Напишите сначала красный тест, чтобы убедиться в понятности вывода.
#
# 4. В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера.
# Для этого используйте соответствующее свойство Webdriver.
#
# 5. Добавьте изменения в коммит с осмысленным сообщением
#
# Теперь посмотрим, как можно осуществлять переход между страницами.