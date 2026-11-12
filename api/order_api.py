import allure
import requests

import urls


class OrderApi:
    @allure.step("Создать заказ")
    def create_order(self, payload, token=None):
        headers = {"Authorization": token} if token else None
        return requests.post(urls.ORDERS, json=payload, headers=headers)

    @allure.step("Получить заказы юзера")
    def get_orders(self, token=None):
        headers = {"Authorization": token} if token else None
        return requests.get(urls.ORDERS, headers=headers)

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return requests.get(urls.INGREDIENTS)
