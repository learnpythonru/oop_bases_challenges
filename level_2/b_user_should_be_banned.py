"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

from a_user_from_functions_to_class import User


SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class CheckUser(User):
    def __init__(self, username: str, user_id: int, name: str, surname: str, age: int) -> None:
        super().__init__(username, user_id, name)
        self.surname = surname
        self.age = age

    def should_be_banned(self) -> bool:
        return self.surname in SURNAMES_TO_BAN
