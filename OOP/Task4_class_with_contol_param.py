class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, name, value):
        if name == 'price':
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError("Цена должна быть положительным числом")
        elif name == 'quantity':
            if not (isinstance(value, int) and value >= 0):
                raise ValueError("Количество должно быть неотрицательным целым числом")
        super().__setattr__(name, value)

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity = {self.quantity})"
# Пример использования
try:
    prod = Product("Laptop", 1000, 10)
    prod.price = 1200
    prod.quantity = 5
    print(prod)
except ValueError as e:
    print(e)