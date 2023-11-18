"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде:
    Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str) -> None:
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone

    def __str__(self) -> str:
        return f'Информация о пользователе: {self.name}, {self.username}, {self.age}, {self.phone}'


if __name__ == '__main__':
    user = User('Ivan', 'ivan111', 30, '88005553535')
    print(user)
