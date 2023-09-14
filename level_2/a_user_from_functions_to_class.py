""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""

class User:
    def __init__(self, user_id: int, username: str, name: str):
        self.user_id = user_id
        self.username = username
        self.name = name

    def make_username_capitalized(self):
        return self.username.capitalize()

    def __str__(self):
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'
    
if __name__ == '__main__':
    person = User(1, 'billiejinn', 'pavel')
    print(person.make_username_capitalized())
    print(person)
    