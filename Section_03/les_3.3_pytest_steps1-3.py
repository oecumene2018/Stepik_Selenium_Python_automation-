# PyTest — преимущества и недостатки

#Рассмотрим преимущества использования PyTest:

# 1) PyTest полностью обратно совместим с фреймворками unittest и nosetest.
# Это означает, что если изначально вы писали тесты, используя unittest, то перейти на PyTest можно буквально
# в ту же минуту. Для этого в вашем виртуальном окружении должен быть установлен пакет PyTest.
# Не забудьте активировать ваше виртуальное окружение и установите PyTest.
#
# Для Windows:
#
# > selenium_env\Scripts\activate.bat
# (selenium_env) С:\Users\user\environments>  pip install pytest==5.1.1
# Для Linux и macOS:
#
$ source selenium_env/bin/activate
#
# (selenium_env) $ pip install pytest==5.1.1
# Теперь мы можем запустить тесты в нашем файле test_abs_project.py с помощью PyTest, не изменяя сам файл. PyTest сам найдёт тесты в папке, в которой вы их запускаете, и выполнит их:
#
# pytest test_abs_project.py

# Минусы PyTest:
#
# 1) PyTest требуется устанавливать дополнительно, так как он не входит в стандартный пакет библиотек Python,
# в отличие от unittest. Нужно не забывать об этом, когда вы будете настраивать автоматический запуск тестов
# с помощью CI-сервера.
#
#
# 2) Использование PyTest требует более глубокого понимания языка Python, чтобы разобраться, как применять фикстуры,
# параметризацию и другие возможности PyTest.