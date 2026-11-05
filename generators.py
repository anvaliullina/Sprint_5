import random
import string
import uuid


def generate_email():
    unique_id = uuid.uuid4().hex[:8]
    numbers = random.randint(100, 999)
    return f"test{unique_id}_student_52_{numbers}@yandex.ru"


def generate_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=10))
