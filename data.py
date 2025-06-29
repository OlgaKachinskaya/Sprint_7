import generators

class Url:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = '/api/v1/courier'
    courier_login = '/api/v1/courier/login'
    courier_delete = '/api/v1/courier/:id'
    create_order = '/api/v1/orders'
    get_order_list = '/api/v1/orders'
    order_cancel = '/api/v1/orders/cancel'
    track_order = '/v1/orders/track?t='

class DataForOrder:
    order_data = {
        "firstName": "Ольга",
        "lastName": "Качинская",
        "address": "Шелковичная",
        "metroStation": "Комсомольская",
        "telephone": "+79165432331"
    }

    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(), 'password': generators.password_generator(), 'firstName': generators.name_generator()}
    ]

class ResponseBody:
    courier_creation_success = {'ok': True}
    courier_name_already_exist = {'code':  409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    courier_registration_not_enough_data = {'code': 400, 'message': 'Недостаточно данных для входа'}
    courier_account_not_found = {'code': 404, 'message': 'Учетная запись не найдена'}
    courier_login_not_enough_data = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    successful_order_creation = 'track'
    successful_get_order_last = 'orders'

class DataForRegistration:
    reg_data = [{'password': generators.password_generator(), 'first_name': generators.name_generator()},
                {'login': generators.login_generator(), 'first_name': generators.name_generator()}
    ]