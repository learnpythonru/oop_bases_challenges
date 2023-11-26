"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может
расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него
       юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение:
       "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы
       из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные
       методы.
"""


class UserManager:
    def __init__(self) -> None:
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> str:
        if username not in self.usernames:
            return 'Такого пользователя не существует.'
        self.usernames.remove(username)
        return 'Пользователь успешно заблокирован'


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user('qwerty1234')
    user_manager.get_users()
    admin_manager = AdminManager()
    admin_manager.add_user('qwerty1234')
    admin_manager.get_users()
    admin_manager.ban_username('qwerty1234')
    super_admin_manager = SuperAdminManager()
    super_admin_manager.add_user('qwerty1234')
    super_admin_manager.get_users()
    super_admin_manager.ban_username('qwerty')
    super_admin_manager.ban_all_users()


