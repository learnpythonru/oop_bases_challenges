"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float) -> None:
        self.amount = amount
        if self.balance - self.amount >= self.min_balance:
            self.balance = self.balance - self.amount
        else:
            raise ValueError("You are fuckin looser. You don't have enough money. Please fund your wallet")


if __name__ == '__main__':
    bank_accaunt = BankAccount(owner='Oleg', balance=1000)
    bank_accaunt.decrease_balance(200)
    print(bank_accaunt.balance)
    bank_accaunt.decrease_balance(899)
    print(bank_accaunt.balance)
    bank_accaunt.decrease_balance(2)
    print(bank_accaunt.balance)



