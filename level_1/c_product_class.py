"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: int):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def info_about_product(self):
        return f'Data about product: {self.name}, {self.description}, {self.price}, {self.weight}'


if __name__ == '__main__':
    phone = Product('IPhone', '15 Pro', 1100, 195)
    info = phone.info_about_product()
    print(info)
    