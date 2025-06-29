import requests
import  allure
from data import Url, Flags

class TestOrdersList:
    @allure.title('Получение списка заказов. ручка /api/v1/orders')
    def test_successful_get_order_list(self):
        with allure.step('Отправить запрос и проверить ответ'):
            response = requests.get(f'{Url.main_url}{Url.get_order_list}')
            assert response.status_code == 200 and Flags.successful_get_order_last in response.text