import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Small Bun"
    bun_mock.get_price.return_value = 100.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = "Cheese"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 50.0
    return ingredient_mock

@pytest.fixture
def sample_bun():
    bun = Mock()
    bun.get_name.return_value = "Sesame Bun"
    bun.get_price.return_value = 150.0
    return bun

@pytest.fixture
def sample_ingredients():
    ingredients = []
    ingredients.append(Mock(get_name="Tomato", get_type="FILLING", get_price=30.0))
    ingredients.append(Mock(get_name="Mayo", get_type="SAUCE", get_price=20.0))
    ingredients.append(Mock(get_name="Onion", get_type="FILLING", get_price=15.0))
    return ingredients