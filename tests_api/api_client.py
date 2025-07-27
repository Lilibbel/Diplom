import requests
import allure
from tests_api.data import API_ENDPOINTS

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Регистрация пользователя")
    def register(self, user_data):
        return requests.post(
            f"{self.base_url}{API_ENDPOINTS['register']}",
            json=user_data
        )

    @allure.step("Авторизация пользователя")
    def login(self, credentials):
        return requests.post(
            f"{self.base_url}{API_ENDPOINTS['login']}",
            json=credentials
        )

    @allure.step("Создание заказа")
    def create_order(self, ingredients, token=None):
        headers = {}
        if token:
            headers = {"Authorization": f"Bearer {token}"}
        return requests.post(
            f"{self.base_url}{API_ENDPOINTS['orders']}",
            json={"ingredients": ingredients},
            headers=headers
        )

    @allure.step("Получение информации о пользователе")
    def get_user_info(self, token):
        return requests.get(
            f"{self.base_url}{API_ENDPOINTS['user']}",
            headers={"Authorization": f"Bearer {token}"}
        )