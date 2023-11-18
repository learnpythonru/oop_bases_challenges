"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте
    результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        self.balance += income

    def reduce_balance(self, income: float) -> None | ValueError:
        self.balance -= income
        if self.balance < 0:
            raise ValueError
        else:
            return None


if __name__ == '__main__':
    account = BankAccount('Ivanov Ivan Ivanovich', 77500.23)
    account.reduce_balance(1000.00)
    print(account.balance)
    account.reduce_balance(80000.00)
