# Handles order-related operations

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = "Pending"

    def process_order(self):
        """Process the order if stock is available"""
        if self.quantity <= self.product.stock:
            self.product.update_stock(self.quantity)
            self.status = "Completed"
            print(f"Order {self.order_id} has been completed.")
        else:
            self.status = "Failed"
            print(f"Order {self.order_id} failed: Insufficient stock.")

    def get_status(self):
        """Return order status"""
        return f"Order[{self.order_id}] - Status: {self.status}"
