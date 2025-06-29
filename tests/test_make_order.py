import allure
import pytest
import requests
from data import Url, Flags, DataForOrder


class TestCreationOrder:
    @allure.title('Успешный тест на создание заказа с разными цветами самоката. ручка /api/v1/orders ')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_diff_colour(self, scooter_color, cancel_order_after_test):
        DataForOrder.order_data['color'] = scooter_color
        with allure.step('Создание заказа с цветом {scooter_color}'):
            response = requests.post(
                f'{Url.main_url}{Url.create_order}',
                json=DataForOrder.order_data
            )
        with allure.step('Проверка успешного создания заказа'):
            assert response.status_code == 201 and Flags.successful_order_creation in response.json()
        cancel_order_after_test.append(response.json()['track'])