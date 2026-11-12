import allure

import data


class TestCreateOrderApi:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.description("Авторизованный юзер может создать заказ с ингредиентами")
    def test_create_order_with_auth(self, order_api, created_user, ingredient_hash):
        payload = {"ingredients": [ingredient_hash]}
        response = order_api.create_order(payload, token=created_user["access_token"])

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации")
    @allure.description("Заказ можно создать без авторизации")
    def test_create_order_without_auth(self, order_api, ingredient_hash):
        payload = {"ingredients": [ingredient_hash]}
        response = order_api.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Создание заказа без ингредиентов возвращает ошибку")
    def test_create_order_without_ingredients(self, order_api):
        response = order_api.create_order({"ingredients": []})

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_INGREDIENTS_REQUIRED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Создание заказа с неверным хешем возвращает ошибку")
    def test_create_order_with_invalid_hash(self, order_api):
        payload = {"ingredients": ["invalid_ingredient_hash"]}
        response = order_api.create_order(payload)

        assert response.status_code == 500
