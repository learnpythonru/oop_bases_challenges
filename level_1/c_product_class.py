"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""

class Product:
    
    def __init__(self, name: str, description: str, price: float, weight:float):
        self.name = name
        self.desciption = description
        self.price = price
        self.weight = weight
        
    


if __name__ == '__main__':
    product1 = Product('Sofa', 'Not new but comfartable', 125.7, 65.9)
    print(f'Информация о продукте: {product1.name}, {product1.desciption}, ${product1.price}, {product1.weight}kg')

