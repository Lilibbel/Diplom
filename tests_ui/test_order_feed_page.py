import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from tests_ui.data import EMAIL, PASSWORD

@allure.feature('Лента заказов')
@allure.story('Тесты функционала ленты заказов')
class TestOrderFeedPage:

    @allure.title('Проверка открытия модального окна с деталями заказа')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_order_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открытие страницы ленты заказов'):
            order_feed_page.open_order_feed_page()

        with allure.step('Выбор последнего заказа в ленте'):
            order_feed_page.select_recent_order()

        with allure.step('Проверка отображения деталей заказа'):
            order_details = order_feed_page.get_order_details_text()
            assert order_details != "", "Модальное окно с деталями заказа не содержит информации"

    @allure.title('Проверка отображения заказа пользователя в ленте')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_order_appears_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация пользователя'):
            account_page.perform_login(EMAIL, PASSWORD)

        with allure.step('Создание нового заказа'):
            main_page.drag_ingredient_to_constructor()
            order_feed_page.click_place_order_button()

        with allure.step('Получение номера созданного заказа'):
            order_number = order_feed_page.get_order_number_from_details()

        with allure.step('Закрытие модального окна и переход в ленту заказов'):
            order_feed_page.close_order_details()
            order_feed_page.open_order_feed_page()

        with allure.step('Проверка наличия заказа в ленте'):
            assert order_feed_page.is_order_in_feed(order_number), \
                f"Заказ {order_number} не отображается в ленте заказов"

    @allure.title('Проверка увеличения общего счетчика заказов после создания нового заказа')
    @allure.severity(allure.severity_level.NORMAL)
    def test_total_orders_counter_increment(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация пользователя'):
            account_page.perform_login(EMAIL, PASSWORD)

        with allure.step('Открытие ленты заказов'):
            order_feed_page.navigate_to_feed()

        with allure.step('Запись начального значения счетчика'):
            initial_counter = order_feed_page.get_total_orders_count()

        with allure.step('Создание нового заказа'):
            order_feed_page.navigate_to_constructor()
            main_page.drag_ingredient_to_constructor()
            order_feed_page.click_place_order_button()
            order_feed_page.get_order_number_from_details()
            order_feed_page.close_order_details()

        with allure.step('Проверка изменения счетчика'):
            updated_counter = order_feed_page.get_total_orders_count()
            assert updated_counter > initial_counter, \
                f"Общий счетчик заказов не увеличился. Было: {initial_counter}, стало: {updated_counter}"

    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    @allure.severity(allure.severity_level.NORMAL)
    def test_today_orders_counter_increment(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация пользователя'):
            account_page.perform_login(EMAIL, PASSWORD)

        with allure.step('Открытие ленты заказов'):
            order_feed_page.navigate_to_feed()

        with allure.step('Запись начального значения счетчика'):
            initial_today_orders = order_feed_page.get_today_orders_count()
            order_feed_page.navigate_to_constructor()

        with allure.step('Создание нового заказа'):
            order_feed_page.navigate_to_constructor()
            main_page.drag_ingredient_to_constructor()
            order_feed_page.click_place_order_button()
            order_feed_page.get_order_number_from_details()

        with allure.step('Проверка изменения счетчика'):
            order_feed_page.close_order_details()
            order_feed_page.navigate_to_feed()
            updated_today_orders = order_feed_page.get_today_orders_count()
            assert updated_today_orders > initial_today_orders, \
                f"Счетчик заказов за сегодня не увеличился. Было: {initial_today_orders}, стало: {updated_today_orders}"

    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_appears_in_progress_section(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация пользователя'):
            account_page.perform_login(EMAIL, PASSWORD)

        with allure.step('Создание нового заказа'):
            order_feed_page.navigate_to_constructor()
            main_page.drag_ingredient_to_constructor()
            order_feed_page.click_place_order_button()

        with allure.step('Получение номера заказа'):
            order_number = order_feed_page.get_order_number_from_details()

        with allure.step('Проверка раздела "В работе"'):
            order_feed_page.close_order_details()
            order_feed_page.navigate_to_feed()
            assert order_feed_page.is_order_in_progress_section(order_number), \
                f"Заказ {order_number} не отображается в разделе 'В работе'"