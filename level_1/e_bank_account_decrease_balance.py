"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


from cmath import exp


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if self.balance >= 0:
            self.balance += income
        print(f'Баланс {self.owner_full_name} увеличен на {income} тугриков. Текущий баланс - {self.balance} тугриков')

    def decrease_balance(self, expense: float):
        if self.balance - expense < 0:
            raise ValueError
        self.balance -= expense 
        print(f'Баланс {self.owner_full_name} уменьшен на {expense} тугриков. Текущий баланс - {self.balance} тугриков')

if __name__ == '__main__':
    account = BankAccount('Dusky', 99.9)
    account.decrease_balance(99.9)
    print(account.balance)
    account.decrease_balance(99.9)
    print(account.balance)

