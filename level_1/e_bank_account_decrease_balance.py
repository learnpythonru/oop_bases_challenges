"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
        return self.balance

    def decrease_balance(self, outcome: float):
        if self.balance - outcome < 0:
            raise ValueError("You can't receive more than you have")
        self.balance -= outcome
        return self.balance

    def info_bank_account(self):
        return f'{self.owner_full_name}, {self.balance} '


if __name__ == '__main__':
    user_acc = BankAccount('Oleg Ivanov', 1000.5)
    print(f"Баланс счета до снятия: {user_acc.balance}")
    user_acc.decrease_balance(500.5)
    print(f"Баланс счета после снятия 500: {user_acc.balance}")
    try:
        user_acc.decrease_balance(100000)
    except ValueError as e:
        print(e)
