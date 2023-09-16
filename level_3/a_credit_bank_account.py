"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

# код писать тут
class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def __init__(self, owner_full_name: str, balance: float) -> None:
        super().__init__(owner_full_name, balance)

    def is_eligible_for_credit(self) -> float:
        return self.balance > 1000


if __name__ == '__main__':
    arseny_porter_bank_account = BankAccount(owner_full_name='Arseny Porter', balance=1000.5)
    print(f"Bank account: {arseny_porter_bank_account.owner_full_name}")
    print(arseny_porter_bank_account.balance)

    arseny_porter_bank_account.increase_balance(10.0)
    arseny_porter_bank_account.decrease_balance(5.99)

    print(arseny_porter_bank_account.balance)
    
    arseny_porter_credit_account = CreditAccount(owner_full_name='Arseny Porter', balance=1000.5)
    print(f"Credit account: {arseny_porter_credit_account.owner_full_name}")

    print(arseny_porter_credit_account.balance)

    arseny_porter_credit_account.decrease_balance(.6)

    print(
        (f"Is {arseny_porter_credit_account.owner_full_name} with "
        f"{arseny_porter_credit_account.balance} balance eligible for the the credit: "
        f"{arseny_porter_credit_account.is_eligible_for_credit()}"))
