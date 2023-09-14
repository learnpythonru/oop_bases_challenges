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
    def __init__(self, owner_full_name: str, balance: str) -> None:
        self.owner_full_name = owner_full_name
        self.balance = decimal.Decimal(balance).quantize(decimal.Decimal('1.00'))

    def increase_balance(self, income: str) -> None:
        self.balance += decimal.Decimal(income).quantize(decimal.Decimal('1.00'))
    
    def decrese_balance(self, expense: str) -> None:
        self.balance -= decimal.Decimal(expense).quantize(decimal.Decimal('1.00'))
        if self.balance < 0:
            self.balance += decimal.Decimal(expense).quantize(decimal.Decimal('1.00'))
            raise ValueError(f'operation cancelled due to insufficient account balance {self.balance}')



if __name__ == '__main__':
    account = BankAccount(owner_full_name='Petr Petrovich Petrov', balance=100.01)
    account.decrese_balance(100)
    print(f'current balance {account.balance}')
    account.decrese_balance(1)
