import allure

import data


class TestGetUserOrdersApi:
    @allure.title("Получение заказов авторизованного юзера")
    @allure.description("Авторизованный юзер получает список своих заказов")
    def test_get_user_orders_with_auth(self, order_api, created_user):
        response = order_api.get_orders(token=created_user["access_token"])

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()
        assert "total" in response.json()
        assert "totalToday" in response.json()

    @allure.title("Получение заказов без авторизации")
    @allure.description("Неавторизованный запрос возвращает ошибку")
    def test_get_user_orders_without_auth(self, order_api):
        response = order_api.get_orders()

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == data.MESSAGE_NOT_AUTHORISED
