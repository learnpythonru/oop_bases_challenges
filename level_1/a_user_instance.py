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

    def __str__(self):
        return ', '.join([self.name, self.username, str(self.age), self.phone])


if __name__ == '__main__':
    user = User(
        name='John',
        username='John23',
        age=23,
        phone='88005553535'

    )

    print(user)
