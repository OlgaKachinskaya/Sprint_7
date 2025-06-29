import pytest
from data import Url, ResponseBody, DataForRegistration
import requests
import allure

class TestCreateNewCourier:

    @allure.title('Успешное создание нового курьера. ручка /api/v1/courier')
    def test_success_creation_courier(self, generate_courier_data):
        with allure.step('Выполнить регистрацию курьера'):
            registration = requests.post(f'{Url.main_url}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        with allure.step('Проверить успешное создание курьера'):
            assert registration.status_code == 201 and registration.json() == ResponseBody.courier_creation_success


    @allure.title('Невозможность создания двух одинаковых курьеров')
    def test_creation_courier_double_error(self, create_courier):
        with allure.step('Попытка создать дубликат курьера'):
            response = requests.post(f'{Url.main_url}{Url.CREATE_COURIER}', json=create_courier[0])
        with allure.step('Проверить ошибку дублирования'):
            assert response.status_code == 409 and response.json() == ResponseBody.courier_name_already_exist

    @allure.title('Создание курьера, если одного из полей нет, запрос возвращает ошибку. ручка /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_without_enoigh_field(self, data_setup):
        with allure.step('Попытка создания курьера с неполными данными'):
            response = requests.post(f'{Url.main_url}{Url.CREATE_COURIER}', data_setup)
        with allure.step('Проверить ошибку недостатка данных'):
            assert response.status_code == 400 and (response.json() == ResponseBody.courier_registration_not_enough_data)