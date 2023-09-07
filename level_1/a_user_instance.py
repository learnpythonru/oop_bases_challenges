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
    ivan = User(name='Иван', username='Ванька разбойник', age=30, phone='+89035555555')
    print(f'Информация о пользователе: имя - {ivan.name}, юзернейм - {ivan.username}, возраст - {ivan.age}, телефон - {ivan.phone}.')

