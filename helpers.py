import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_user_data(length=10):
    return {
        "email": f"{generate_random_string(length)}@test.ru",
        "password": generate_random_string(length),
        "name": generate_random_string(length),
    }
