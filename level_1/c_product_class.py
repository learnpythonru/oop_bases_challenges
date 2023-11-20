from decimal import Decimal


"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде:
    Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: Decimal, weight: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self) -> str:
        return f'Информация о продукте: {self.name}, {self.description}, {self.price}, {self.weight}' # noqa


if __name__ == '__main__':
    product = Product("milk", "milk from Danone's farm", Decimal('69.99'), 930)
    print(product)
