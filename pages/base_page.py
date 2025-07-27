from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_element(self, locator, timeout=25):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def fill_field(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_and_find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_dynamic_locator(self, locator, value):
        method, locator_str = locator
        return method, locator_str.format(value)

    def is_element_visible(self, locator, timeout=25):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_with_javascript(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_visibility(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def drag_and_drop(self,bun_ingredient, constructor_zone):
        """Перетаскивает ингредиент в конструктор"""
        source = self.wait_and_find_element(bun_ingredient)
        target = self.wait_and_find_element(constructor_zone)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()


    def is_element_present(self, locator):
        try:
            element = self.wait_and_find_element(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def navigate_to_url(self, url):
        self.driver.get(url)

    def wait_for_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    def wait_for_text_change(self, locator, initial_text, timeout=30):
        self.wait_for_condition(
            lambda _: self.get_element_text(locator) != initial_text, timeout
        )
        return self.wait_and_find_element(locator)

    def get_element_attribute(self, locator, attribute_name):
        element = self.wait_and_find_element(locator)
        return element.get_attribute(attribute_name)

    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.wait_and_find_element(formatted_locator)

    def format_locator(self, locator, value):
        method, locator_str = locator
        return method, locator_str.format(value)