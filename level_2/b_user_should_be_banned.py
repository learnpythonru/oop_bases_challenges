"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
    
    def should_be_banned(self):
        return self.surname in SURNAMES_TO_BAN
    
    def __str__(self):
        return f'User(name={self.name}, surname={self.surname}, age={self.age})'

if __name__ == '__main__':
    person_blacklist = User('Adolf', 'Vaughn', 30)
    person_whitelist = User('Pavel', 'Mager', 24)
    print(person_blacklist.should_be_banned())
    print(person_whitelist.should_be_banned())