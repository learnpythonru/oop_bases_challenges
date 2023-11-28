"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance


class CreditAccount(BankAccount):
    def increase_balance(self, amount: float) -> float:
        self.balance += amount

    def decrease_balance(self, amount: float) -> float:
        self.balance -= amount

    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000
# class CreditAccount:
#     def __init__(self, owner_full_name: str, balance: float):
#         self.owner_full_name = owner_full_name
#         self.balance = balance

#     def increase_balance(self, amount: float):
#         self.balance += amount

#     def decrease_balance(self, amount: float):
#         self.balance -= amount

#     def is_eligible_for_credit(self):
#         return self.balance > 1000


if __name__ == '__main__':
    owner_1 = BankAccount('ALexandr Ivanov', 1500.00)
    print(owner_1.owner_full_name)
    print(owner_1.balance)
    owner_2 = CreditAccount('Oleg Olegov', 1000.00)
    print(owner_2.owner_full_name)
    print(owner_2.balance)
    owner_2.increase_balance(300.00)
    print(owner_2.balance)
    owner_2.decrease_balance(100.00)
    print(owner_2.is_eligible_for_credit())
