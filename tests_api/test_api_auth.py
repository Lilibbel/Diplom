import allure
import pytest
from tests_api.data import EXISTING_USER, USER_MISSING_FIELDS

@allure.feature("API авторизации")
class TestAuth:
    @allure.title("Регистрация нового пользователя")
    def test_register_new_user(self, api_client, random_user):
        response = api_client.register(random_user)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Регистрация существующего пользователя")
    def test_register_existing_user(self, api_client):
        response = api_client.register(EXISTING_USER)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Регистрация с отсутствующими полями")
    def test_register_missing_fields(self, api_client):
        response = api_client.register(USER_MISSING_FIELDS)
        assert response.status_code == 403
        assert "required fields" in response.json()["message"]

    @allure.title("Успешный вход в систему")
    def test_login_success(self, api_client, registered_user):
        response = api_client.login({
            "email": registered_user["email"],
            "password": registered_user["password"]
        })
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Вход с неверными данными")
    def test_login_failure(self, api_client):
        response = api_client.login({
            "email": "invalid@test.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        assert "incorrect" in response.json()["message"]