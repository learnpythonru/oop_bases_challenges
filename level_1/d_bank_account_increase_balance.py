from decimal import Decimal


"""
У нас есть класс банковского аккаунта со свойсвами: полное имя владельца и баланс, но не релизован
метод, который увеливает баланс.

Задания:
    1. Допишите логику в метод increase_balance,
    который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова
    распечтайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: Decimal) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: Decimal) -> None:
        self.balance += income


if __name__ == '__main__':
    account = BankAccount('Ivanov Ivan Ivanovich', Decimal('77500.23'))
    print(account.balance)
    account.increase_balance(Decimal('500.00'))
    print(account.balance)
