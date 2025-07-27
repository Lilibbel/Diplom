from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def navigate_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    def click_place_order_button(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_constructor_section_visible(self):
        return self.wait_and_find_element(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    def navigate_to_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_TAB)

    def is_order_counter_visible(self):
        return self.wait_and_find_element(MainPageLocators.COMPLETED_ORDERS_SECTION).is_displayed()

    def select_ingredient(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    def is_ingredient_details_displayed(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def close_ingredient_details(self):
        self.click_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def add_ingredient_to_constructor(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    def get_ingredient_counter_value(self):
        return int(self.get_element_text(MainPageLocators.INGREDIENT_COUNTER))


    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_TARGET_ZONE)

    def get_order_success_message(self):
        return self.get_element_text(MainPageLocators.ORDER_SUCCESS_NOTIFICATION)