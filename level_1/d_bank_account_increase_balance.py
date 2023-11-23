"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""
import decimal


class BankAccount:
    def __init__(self, owner_full_name: str, balance: decimal.Decimal):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: decimal.Decimal):
        self.balance += income

    def __str__(self):
        return f'{self.owner_full_name}: {self.balance}'


if __name__ == '__main__':
    account = BankAccount(
        owner_full_name='John Smith',
        balance=decimal.Decimal('1_000_000')
    )

    print(account)
    account.increase_balance(decimal.Decimal('100.01'))
    print(account)
