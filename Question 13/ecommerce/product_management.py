# Handles product-related operations

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """Update stock after purchase"""
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Stock updated: {self.stock} items remaining.")
        else:
            print("Not enough stock available.")

    def get_info(self):
        """Return product details"""
        return f"Product[{self.product_id}]: {self.name}, Price: ${self.price}, Stock: {self.stock}"
