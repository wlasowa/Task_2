import allure

import data
import helpers


class TestChangeUserDataApi:
    @allure.title("Изменение имени юзера с авторизацией")
    @allure.description("Авторизованный юзер может изменить имя")
    def test_change_user_name_with_auth(self, user_api, created_user):
        new_name = helpers.generate_random_string(10)

        response = user_api.update_user(
            created_user["access_token"], {"name": new_name}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение email юзера с авторизацией")
    @allure.description("Авторизованный юзер может изменить email")
    def test_change_user_email_with_auth(self, user_api, created_user):
        new_email = f"{helpers.generate_random_string(10)}@test.ru"

        response = user_api.update_user(
            created_user["access_token"], {"email": new_email}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == new_email

    @allure.title("Изменение пароля юзера с авторизацией")
    @allure.description("Авторизованный юзер может изменить пароль")
    def test_change_user_password_with_auth(self, user_api, created_user):
        new_password = helpers.generate_random_string(10)

        response = user_api.update_user(
            created_user["access_token"], {"password": new_password}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Изменение данных юзера без авторизации")
    @allure.description("Неавторизованный запрос возвращает ошибку")
    def test_change_user_data_without_auth(self, user_api):
        response = user_api.update_user(None, {"name": "New Name"})

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_NOT_AUTHORISED
