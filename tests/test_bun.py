import allure
import pytest
from Stellar_Burgers.bun import Bun

@allure.feature('Проверка создания булочки с разными параметрами')
class TestBun:
    @allure.title('Проверка инициализации булочки с параметрами: {name}, {price}')
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price

