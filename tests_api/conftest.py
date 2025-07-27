import pytest
from tests_api.utils import generate_random_user
from tests_api.api_client import ApiClient
from tests_api.data import BASE_URL


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(BASE_URL)


@pytest.fixture
def random_user():
    return generate_random_user()


@pytest.fixture
def registered_user(api_client, random_user):
    # Регистрация
    response = api_client.register(random_user)
    assert response.status_code == 200, "Ошибка регистрации тестового пользователя"

    # Авторизация
    login_data = {
        "email": random_user["email"],
        "password": random_user["password"]
    }
    login_response = api_client.login(login_data)
    assert login_response.status_code == 200, "Ошибка авторизации тестового пользователя"

    # Получение токена
    token = login_response.json()["accessToken"].split()[-1]

    yield {
        **random_user,
        "token": token
    }