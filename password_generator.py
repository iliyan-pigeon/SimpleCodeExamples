import random


def password_generator():
    password = ""

    for i in range(15):
        password += str(chr(random.randint(21, 126)))

    return password
