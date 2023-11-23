"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""
import decimal


class BankAccount:
    def __init__(self, owner_full_name: str, balance: decimal.Decimal):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: decimal.Decimal):
        self.balance += income

    def decrease_balance(self, expense: decimal.Decimal):
        if (self.balance - expense) < 0:
            raise ValueError('exceeded the limit')
        else:
            self.balance -= expense

    def __str__(self):
        return f'{self.owner_full_name}: {self.balance}'


if __name__ == '__main__':
    account = BankAccount(owner_full_name='John Smith',
                          balance=decimal.Decimal('1_000_000.00'))

    print(f'Initial limit: {account.balance}')
    account.decrease_balance(decimal.Decimal('999_999'))
    print(f'Positive limit: {account.balance}')
    account.decrease_balance(decimal.Decimal('1_000_001'))
