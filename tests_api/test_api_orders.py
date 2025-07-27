import allure
import pytest
from tests_api.data import VALID_INGREDIENTS, INVALID_INGREDIENT

@allure.feature("API заказов")
class TestOrders:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_auth(self, api_client, registered_user):
        response = api_client.create_order(
            ingredients=VALID_INGREDIENTS[:2],
            token=registered_user["token"]
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_no_auth(self, api_client):
        response = api_client.create_order(ingredients=VALID_INGREDIENTS[:2])
        assert response.status_code == 200

    @allure.title("Создание заказа с невалидными ингредиентами")
    def test_create_order_invalid_ingredients(self, api_client):
        response = api_client.create_order(ingredients=[INVALID_INGREDIENT])
        assert response.status_code == 500

    @allure.title("Создание пустого заказа")
    def test_create_empty_order(self, api_client):
        response = api_client.create_order(ingredients=[])
        assert response.status_code == 400
        assert "must be provided" in response.json()["message"]