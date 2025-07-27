BASE_URL = "https://stellarburgers.nomoreparties.site/api"

API_ENDPOINTS = {
    "register": "/auth/register",
    "login": "/auth/login",
    "orders": "/orders",
    "user": "/auth/user"
}

EXISTING_USER = {
    "email": "test-user@example.com",
    "password": "P@ssw0rd123",
    "name": "Test User"
}

USER_MISSING_FIELDS = {
    "email": "missing-fields@test.com",
    "password": "",
    "name": ""
}

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f"
]

INVALID_INGREDIENT = "invalid_ingredient_hash"