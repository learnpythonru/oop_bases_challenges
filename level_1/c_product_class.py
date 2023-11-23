"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""
import decimal


class Product:
    def __init__(self, name: str, description: str, price: decimal.Decimal, weight: float):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def get_product_info(self):
        return f"Product info: {self.name}, {self.description}, {self.price}, {self.weight}"


if __name__ == '__main__':
    product = Product(
        name='Watermelon',
        description='Watermelon is a sweet fruit usually consumed in summer',
        price=decimal.Decimal('23.56'),
        weight=5.56
    )

    about = product.get_product_info()
    print(about)
