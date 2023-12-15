"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> bool:
        if username in self.usernames:
            self.usernames.remove(username)
            return True
        else:
            print(f"Такого пользователя не существует.")
            return False


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:    # функция не работает.
        self.usernames = []


if __name__ == '__main__':
    user_manager = UserManager()

    # Добавляем пользователей
    user_manager.add_user("Ivan")
    user_manager.add_user("Aleksey")
    user_manager.add_user("Oleg")

    # Выводим список пользователей
    print("Список пользователей (UserManager):", user_manager.get_users())

    # Создаем экземпляр класса AdminManager
    admin_manager = AdminManager()

    # Наследуем список пользователей от UserManager
    admin_manager.usernames = user_manager.usernames    # Механизм наследования!!!

    # Забанить пользователя
    admin_manager.ban_username("Aleksey")

    # Выводим обновленный список пользователей
    print("Список пользователей (AdminManager):", admin_manager.get_users())

    # Создаем экземпляр класса SuperAdminManager
    super_admin_manager = SuperAdminManager()

    # Наследуем список пользователей от AdminManager
    super_admin_manager.usernames = admin_manager.usernames     # Механизм наследования!!!

    # Забанить всех пользователей
    super_admin_manager.ban_all_users()

    # Выводим обновленный список пользователей
    print("Список пользователей (SuperAdminManager):", super_admin_manager.get_users())