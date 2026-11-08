import pytest

import helpers
from api.order_api import OrderApi
from api.user_api import UserApi


@pytest.fixture
def user_api():
    return UserApi()


@pytest.fixture
def order_api():
    return OrderApi()


@pytest.fixture
def created_user(user_api):
    user_data = helpers.generate_user_data()
    response = user_api.register(user_data)
    user_data["access_token"] = response.json()["accessToken"]
    yield user_data
    user_api.delete_user(user_data["access_token"])


@pytest.fixture
def register_response(user_api):
    user_data = helpers.generate_user_data()
    response = user_api.register(user_data)
    yield response
    user_api.delete_user(response.json()["accessToken"])


@pytest.fixture
def ingredient_hash(order_api):
    response = order_api.get_ingredients()
    return response.json()["data"][0]["_id"]
