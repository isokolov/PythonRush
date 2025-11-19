# Авторизация

# Напишите программу имитации логина пользователей.
# Программа должна содержать функцию login(email, password) и register(email, password).
# При регистрации пользователя нужно вызвать функцию register и добавить пользователя в список пользователей.
# Вместо пароля нужно хранить его hash.
# При логине пользователя нужно вызвать функцию login где проверить, что hash пароля совпадает с одним из сохраненных хешей.

import hashlib

users = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    # Напишите тут ваш код


def register(email, password):
    # Напишите тут ваш код
    global users
    users[email] = hash_password(password)


def login(email, password):
    # Напишите тут ваш код
    global users
    if email in users:
        store_pass = users[email]
        our_pass = hash_password(password)
        if store_pass == our_pass:
            return True
    else:
        return False


# Example usage
register("user@example.com", "securepassword123")
login("user@example.com", "securepassword123")
login("user@example.com", "wrongpassword")
