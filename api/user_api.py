import allure
import requests

import urls


class UserApi:
    @allure.step("Зарегистрировать юзера")
    def register(self, payload):
        return requests.post(urls.USER_CREATE, json=payload)

    @allure.step("Залогиниться юзером")
    def login(self, payload):
        return requests.post(urls.USER_LOGIN, json=payload)

    @allure.step("Изменить данные юзера")
    def update_user(self, token, payload):
        headers = {"Authorization": token} if token else None
        return requests.patch(urls.USER, json=payload, headers=headers)

    @allure.step("Удалить юзера")
    def delete_user(self, token):
        headers = {"Authorization": token}
        return requests.delete(urls.USER, headers=headers)
