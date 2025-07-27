from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from tests_ui.data import LOGIN_URL

class AccountPage(BasePage):
    def click_profile_button(self):
        self.wait_for_visibility(AccountPageLocators.BURGER_MENU_TITLE)
        self.click_element(AccountPageLocators.PROFILE_BUTTON)

    def navigate_to_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)

    def click_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    def is_order_completed(self):
        return self.get_element_text(AccountPageLocators.COMPLETED_ORDER_STATUS) == "Выполнен"

    def is_login_form_displayed(self):
        return self.get_element_text(AccountPageLocators.LOGIN_FORM_TITLE) == "Вход"

    def open_login_page(self):
        self.navigate_to_url(LOGIN_URL)

    def perform_login(self, email, password):
        self.open_login_page()
        self.fill_field(AccountPageLocators.EMAIL_FIELD, email)
        self.fill_field(AccountPageLocators.PASSWORD_FIELD, password)
        self.click_with_javascript(AccountPageLocators.LOGIN_SUBMIT_BUTTON)