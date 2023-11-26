import decimal

"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс
       BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: decimal.Decimal) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: decimal.Decimal) -> None:
        self.balance += amount

    def decrease_balance(self, amount: decimal.Decimal) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount('Ivanov Ivan Ivanovich', decimal.Decimal('1000'))
    bank_account.increase_balance(decimal.Decimal('500'))
    bank_account.decrease_balance(decimal.Decimal('100'))
    credit_account = CreditAccount('Ivanov Ivan Ivanovich', decimal.Decimal('800'))
    credit_account.is_eligible_for_credit()
    credit_account.decrease_balance(decimal.Decimal('800'))
    credit_account.increase_balance(decimal.Decimal('1000'))

