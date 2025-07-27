from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from tests_ui.data import FEED_URL

class OrderFeedPage(BasePage):
    def select_recent_order(self):
        self.click_element(OrderFeedPageLocators.RECENT_ORDER_ITEM)

    def get_order_details_text(self):
        return self.get_element_text(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    def get_total_orders_count(self):
        return int(self.get_element_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))

    def get_today_orders_count(self):
        element = self.wait_and_find_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT)
        return int(element.text.strip())

    def open_order_feed_page(self):
        self.navigate_to_url(FEED_URL)
        self.wait_for_visibility(OrderFeedPageLocators.FEED_PAGE_HEADER)

    def navigate_to_constructor(self):
        self.click_element(OrderFeedPageLocators.CONSTRUCTOR_TAB)

    def navigate_to_feed(self):
        self.wait_for_visibility(OrderFeedPageLocators.BURGER_MENU_TITLE)
        self.click_element(OrderFeedPageLocators.ORDER_FEED_TAB)

    def click_place_order_button(self):
        self.click_element(OrderFeedPageLocators.PLACE_ORDER_BUTTON)

    def navigate_to_profile(self):
        self.click_element(OrderFeedPageLocators.PROFILE_BUTTON)

    def navigate_to_order_history(self):
        self.click_element(OrderFeedPageLocators.ORDER_HISTORY_LINK)

    def close_order_details(self):
        self.click_element(OrderFeedPageLocators.ORDER_DETAILS_CLOSE_BUTTON)

    def get_order_number_from_details(self):
        self.wait_for_text_change(OrderFeedPageLocators.ORDER_NUMBER, "9999")
        return self.get_element_text(OrderFeedPageLocators.ORDER_NUMBER)

    def is_order_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        order_locator = OrderFeedPageLocators.ORDER_ID_IN_LIST
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.wait_and_find_element(order_locator)

    def is_order_in_progress_section(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.find_and_format_locator(OrderFeedPageLocators.ORDER_IN_PROGRESS_SECTION, formatted_id)
        return True