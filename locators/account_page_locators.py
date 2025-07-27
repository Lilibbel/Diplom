from selenium.webdriver.common.by import By

class AccountPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    COMPLETED_ORDER_STATUS = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small mb-7']")
    LOGIN_FORM_TITLE = (By.XPATH, "//h2[contains(text(),'Вход')]")
    BURGER_MENU_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")