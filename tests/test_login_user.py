import allure

import data


class TestLoginUserApi:
    @allure.title("Логин существующего юзера")
    @allure.description("Зарегистрированный юзер может войти")
    def test_login_user(self, user_api, created_user):
        payload = {
            "email": created_user["email"],
            "password": created_user["password"],
        }
        response = user_api.login(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    @allure.description("Вход с неверными данными возвращает ошибку")
    def test_login_user_wrong_credentials(self, user_api):
        payload = {"email": "no_such_user@test.ru", "password": "wrong_password"}
        response = user_api.login(payload)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_INCORRECT_CREDENTIALS
