"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user = User('Alexandr', 'Beloded', 35, '8927111111')
    print (f"Информация о пользователе: имя: {user.name}, юзернэйм: {user.username}, возраст: {user.age}, телефон: {user.phone}")