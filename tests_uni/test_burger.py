import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns_updates_bun_reference(self, burger, sample_bun):
        burger.set_buns(sample_bun)
        assert burger.bun == sample_bun

    def test_add_ingredient_increases_list_size(self, burger, sample_ingredients):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(sample_ingredients[0])
        assert len(burger.ingredients) == initial_count + 1

    def test_remove_ingredient_decreases_list_size(self, burger, sample_ingredients):
        for ing in sample_ingredients:
            burger.add_ingredient(ing)

        initial_count = len(burger.ingredients)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == initial_count - 1

    def test_remove_nonexistent_ingredient_raises_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_changes_order(self, burger, sample_ingredients):
        for ing in sample_ingredients:
            burger.add_ingredient(ing)

        original_order = [ing.get_name for ing in burger.ingredients]
        burger.move_ingredient(0, 2)
        new_order = [ing.get_name for ing in burger.ingredients]

        assert new_order != original_order
        assert new_order == [original_order[1], original_order[2], original_order[0]]

    @pytest.mark.parametrize("bun_price, ingredients_data, expected_total", [
        (100.0, [("Cheese", 50.0), ("Bacon", 70.0)], 320.0),
        (200.0, [("Lettuce", 10.0)], 410.0),
        (150.0, [], 300.0)
    ])
    def test_calculate_total_price(self, burger, bun_price, ingredients_data, expected_total):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for name, price in ingredients_data:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == expected_total

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        lines = receipt.split('\n')

        assert f"(==== {bun.get_name()} ====)" in lines[0]
        assert f"= {ingredient.get_type().lower()} {ingredient.get_name()} =" in lines[1]
        assert f"(==== {bun.get_name()} ====)" in lines[2]
        assert f"Price: {burger.get_price()}" in lines[4]