# ЗАДАНИЕ: НЕЗАВИСИМОСТЬ ОТ ДАННЫХ
#
# Хорошие автотесты должны быть максимально независимы от данных. Худшее, что можно сделать в тесте
# это "захардкодить" проверки для объектов, которые существуют только на вашем конкретном инстансе.
# Почему? Потому что данные будут постоянно меняться, и при каждом таком изменении придется чинить
# автотесты. Еще это ухудшает переиспользование метода: допустим, мы хотим прогнать тест для множества
# товаров, тогда придется писать большое количество проверок: по одной для каждого товара.
# В конечном итоге, это сказывается на качестве продукта, так как такие тесты работают на узкой выборке
# страниц.
#
# Общая рекомендация: ваши тесты не должны зависеть от того, что вы не можете контролировать.
# Это может быть информация, уже хранящаяся в базе данных, или сторонние сервисы, которые использует
# ваше приложение. Вы можете проверять конкретные данные только в случае, когда используете специально
# подготовленную тестовую базу, инициируемую перед каждым запуском тестов, или добавляете нужные данные
# в базу данных напрямую или через API приложения.
#
# Попробуйте запустить автотест, который мы написали на предыдущем шаге, на странице
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.
#
# Если в предыдущем тесте после добавления товара в корзину вы проверяли в сообщении сайта
# фиксированную строку "The shellcoder's handbook", то тест упадет, так как теперь мы добавили
# другой товар. Если тест прошел, то вы молодец и можете просто вставить новый проверочный код в
# этом задании.
#
# ЧТОБЫ ТЕСТ БЫЛ НЕЗАВИСИМЫМ ОТ КОНТЕНТА:
#
# Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.
# Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
# Сделайте такой же метод для цены.
# Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.