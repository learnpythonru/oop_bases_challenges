"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PrintLoggerMixin:
    def log(self, message: str) -> None:
        print(message)


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        self.price *= 1.2
        self.log(f'Increased price for PremiumProduct: {self.price}')

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'Getting info for PremiumProduct: {base_info}')
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self) -> None:
        self.price /= 1.2
        self.log(f'Decrease price for DiscountedProduct: {self.price}')

    def get_info(self) -> str:
        base_info = super().get_info()
        self.log(f'Getting info for DiscountedProduct: {base_info}')
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    premium_product = PremiumProduct(title='Whiskey', price=5000.0)
    premium_product.increase_price()
    premium_product.get_info()

    discount_product = DiscountedProduct(title='Vodka', price=450.0)
    discount_product.decrease_price()
    discount_product.get_info()
