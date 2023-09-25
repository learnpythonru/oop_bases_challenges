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
    def __init__(self) -> None:
        self.usernames = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> str:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        if username in self.usernames:
            self.usernames.remove(username)
            print(f"Username {username} has been deleted from the list.")
        else:
            print(f"Username {username} hasn't been found in the list.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        if self.usernames:
            self.usernames.clear()
            print("All usernames has been cleared.")
        else:
            print("The list of usernames is already empty .")


if __name__ == '__main__':
    usernames = SuperAdminManager()
    username_list = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']
    
    [usernames.add_user(x) for x in username_list]
    print(usernames.get_users())

    usernames.ban_username('Wilhelm')
    usernames.ban_username('Arsen')
    print(usernames.get_users())

    usernames.ban_all_users()
    print(usernames.get_users())
    usernames.ban_all_users()