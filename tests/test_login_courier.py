import generators
from data import Url, ResponseBody, DataForRegistration
import requests
import allure

class TestLoginCourier:
    @allure.title('Успешная авторизация курьера. ручка /api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        with allure.step('Авторизация курьера и проверка ответа'):
            response = requests.post(
                f'{Url.main_url}{Url.courier_login}',
                json={'login': create_courier[2], 'password': create_courier[3]}
            )
            assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Авторизация несуществующего курьера. ручка /api/v1/courier/login')
    def test_unregistrated_courier_login(self):
        with allure.step('Попытка авторизации'):
            login_data = {
                'login': generators.login_generator(),
                'password': generators.password_generator()
            }
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=login_data)
            assert response.status_code == 404 and response.json() == ResponseBody.courier_account_not_found

    @allure.title('Попытка входа с пустым паролем. ручка /api/v1/courier/login')
    def test_courier_login_empty_password_error(self, create_courier):
        with allure.step('Отправка запроса с пустым паролем'):
            data_response = {'login': create_courier[2], 'password': ''}
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=data_response)
            assert response.status_code == 400 and response.json() == ResponseBody.courier_login_not_enough_data

    @allure.title('Попытка входа с пустым логином. ручка /api/v1/courier/login')
    def test_courier_login_empty_login_error(self, create_courier):
        with allure.step('Отправка запроса с пустым логином'):
            data_response = {'login': '', 'password': create_courier[3]}
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=data_response)
            assert response.status_code == 400 and response.json() == ResponseBody.courier_login_not_enough_data
