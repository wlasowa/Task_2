import allure
import pytest

import data
import helpers


class TestCreateUserApi:
    @allure.title("Создание уникального юзера")
    @allure.description("Уникальный юзер создается, возвращаются токены")
    def test_create_user(self, user_api):
        user_data = helpers.generate_user_data()
        response = user_api.register(user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        user_api.delete_user(response.json()["accessToken"])

    @allure.title("Создание уже зарегистрированного юзера")
    @allure.description("Повторная регистрация с теми же данными возвращает ошибку")
    def test_create_user_already_registered(self, user_api, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"],
            "name": created_user["name"],
        }
        response = user_api.register(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_USER_ALREADY_EXISTS

    @allure.title("Создание юзера без обязательного поля: {param_id}")
    @allure.description("Создание без email, пароля или имени возвращает ошибку")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param({"password": "pass123", "name": "Name"}, id="no_email"),
            pytest.param({"email": "some@test.ru", "name": "Name"}, id="no_password"),
            pytest.param(
                {"email": "some@test.ru", "password": "pass123"}, id="no_name"
            ),
        ],
    )
    def test_create_user_without_required_field(self, user_api, payload):
        response = user_api.register(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_REQUIRED_FIELDS
