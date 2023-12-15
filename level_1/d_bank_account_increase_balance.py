"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income
        return self.balance

    def info_bank_account(self):
        return f'{self.owner_full_name}, {self.balance} '


if __name__ == '__main__':
    user_acc = BankAccount('Oleg Ivanov', 500.0)
    info = user_acc.info_bank_account()
    print(info)
    user_acc.increase_balance(1000.0)
    print(f"Баланс счета после пополнения: {user_acc.balance}")
