import generators
from data import Url, ResponseBody, DataForRegistration
import requests
import allure


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера. ручка /api/v1/courier/login')
    def test_successful_courier_login(self, create_courier):
        with allure.step('Авторизация курьера'):
            response = requests.post(
                f'{Url.main_url}{Url.courier_login}', json={'login': create_courier[2], 'password': create_courier[3]}
            )
        with allure.step('Проверить успешную авторизацию'):
            assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Авторизация несуществующего курьера. ручка /api/v1/courier/login')
    def test_unregistrated_courier_login(self):
        with allure.step('Сгенерировать данные несуществующего курьера'):
            login_data = {
                'login': generators.login_generator(),
                'password': generators.password_generator()
            }
        with allure.step('Попытка авторизации'):
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=login_data)
        with allure.step('Проверить ошибку авторизации'):
            assert response.status_code == 404 and response.json() == ResponseBody.courier_account_not_found

    @allure.title('Попытка входа с пустым паролем. ручка /api/v1/courier/login')
    def test_courier_login_empty_password_error(self, create_courier):
        with allure.step('Готовим данные с пустым паролем'):
            data_response = {'login': create_courier[2], 'password': ''}
        with allure.step('Отправляем запрос с пустым паролем'):
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=data_response)
        with allure.step('Проверяем ошибку недостатка данных'):
            assert response.status_code == 400 and response.json() == ResponseBody.courier_login_not_enough_data

    @allure.title('Попытка входа с пустым логином. ручка /api/v1/courier/login')
    def test_courier_login_empty_login_error(self, create_courier):
        with allure.step('Готовим данные с пустым логином'):
            data_response = {'login': '', 'password': create_courier[3]}
        with allure.step('Отправляем запрос с пустым логином'):
            response = requests.post(f'{Url.main_url}{Url.courier_login}', json=data_response)
        with allure.step('Проверяем ошибку недостатка данных'):
            assert response.status_code == 400 and response.json() == ResponseBody.courier_login_not_enough_data