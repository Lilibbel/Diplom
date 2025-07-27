import random
import string

def generate_random_user():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    return {
        "email": f"{username}@test.com",
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "name": username.capitalize()
    }