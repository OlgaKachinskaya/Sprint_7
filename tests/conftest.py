import pytest
from data import Url, DataForRegistration
import generators
import requests
import allure

@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'firstName': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Url.main_url}{Url.CREATE_COURIER}', json=create_courier_body)
    login_courier = requests.post(f'{Url.main_url}{Url.courier_login}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]
    requests.delete(f'{Url.main_url}{Url.courier_delete}{login_courier.json()["id"]}')

@pytest.fixture()
def generate_courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'firstName': name}
    login_courier_body = {'login': login, 'password': password}
    yield [creation_courier_body, login_courier_body]
    login_courier = requests.post(f'{Url.main_url}{Url.courier_login}', json=login_courier_body)
    courier_id = login_courier.json().get("id", "")
    requests.delete(f'{Url.main_url}{Url.courier_delete}'.replace(":id", str(courier_id)))

@pytest.fixture
def cancel_order_after_test():
    tracks = []
    yield tracks

    with allure.step('Отмена тестовых заказов (пост-условие)'):
        for track in tracks:
            cancel_url = f"{Url.main_url}{Url.order_cancel}?track={track}"
            requests.put(cancel_url)