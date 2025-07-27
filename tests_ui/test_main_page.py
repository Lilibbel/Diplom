import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from tests_ui.data import EMAIL, PASSWORD

@allure.feature('Основной функционал')
@allure.story('Тесты главной страницы')
class TestMainPage:

    @allure.title('Проверка перехода в раздел конструктора')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigate_to_constructor_section(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы авторизации'):
            account_page.open_login_page()

        with allure.step('Клик по вкладке "Конструктор"'):
            main_page.navigate_to_constructor()

        with allure.step('Проверка видимости раздела конструктора'):
            assert main_page.is_constructor_section_visible(), \
                "Раздел конструктора не отображается!"

    @allure.title('Проверка перехода в ленту заказов')
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы авторизации'):
            account_page.open_login_page()

        with allure.step('Клик по вкладке "Лента заказов"'):
            main_page.navigate_to_order_feed()

        with allure.step('Проверка отображения счетчика заказов'):
            assert main_page.is_order_counter_visible(), \
                "Счетчик выполненных заказов не отображается!"

    @allure.title('Проверка отображения деталей ингредиента')
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_ingredient_details(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы авторизации'):
            account_page.open_login_page()

        with allure.step('Переход в раздел конструктора'):
            main_page.navigate_to_constructor()

        with allure.step('Выбор ингредиента "Флюоресцентная булка R2-D3"'):
            main_page.select_ingredient()

        with allure.step('Проверка отображения модального окна с деталями'):
            assert main_page.is_ingredient_details_displayed(), \
                "Детали ингредиента не отображаются!"

    @allure.title('Проверка закрытия окна деталей ингредиента')
    @allure.severity(allure.severity_level.NORMAL)
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы авторизации'):
            account_page.open_login_page()

        with allure.step('Переход в раздел конструктора'):
            main_page.navigate_to_constructor()

        with allure.step('Открытие деталей ингредиента'):
            main_page.select_ingredient()

        with allure.step('Закрытие модального окна'):
            main_page.close_ingredient_details()

        with allure.step('Проверка закрытия модального окна'):
            assert not main_page.is_ingredient_details_displayed(), \
                "Модальное окно с деталями не закрылось!"

    @allure.title('Проверка увеличения счетчика ингредиентов')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increment(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы авторизации'):
            account_page.open_login_page()

        with allure.step('Переход в раздел конструктора'):
            main_page.navigate_to_constructor()

        with allure.step('Получение начального значения счетчика'):
            initial_count = main_page.get_ingredient_counter_value()

        with allure.step('Добавление ингредиента в конструктор'):
            main_page.drag_ingredient_to_constructor()

        with allure.step('Проверка увеличения счетчика'):
            updated_count = main_page.get_ingredient_counter_value()
            assert updated_count == initial_count + 2, \
                f"Счетчик не изменился корректно! Ожидалось: {initial_count + 2}, фактически: {updated_count}"