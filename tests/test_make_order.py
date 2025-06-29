import allure
import pytest
import requests
from data import Url, Flags
from data import DataForOrder


class TestCreationOrder:
    @allure.title('Успешный тест на создание заказа . ручка /api/v1/orders ')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_diff_colour(self, scooter_color):
        order_data = DataForOrder.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.main_url}{Url.create_order}', json=order_data)
        assert order.status_code == 201 and Flags.successful_order_creation in order.json()
        requests.put(f"{Url.main_url}{Url.order_cancel}?track={order.json()['track']}")