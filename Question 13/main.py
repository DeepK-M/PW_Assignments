from ecommerce import Product, Order

# Create product
p1 = Product(101, "Laptop", 75000, 5)
print(p1.get_info())

# Create order
order1 = Order(5001, p1, 2)
order1.process_order()
print(order1.get_status())

# Another order
order2 = Order(5002, p1, 4)
order2.process_order()
print(order2.get_status())


#output:
# Product[101]: Laptop, Price: $75000, Stock: 5
# Stock updated: 3 items remaining.
# Order 5001 has been completed.
# Order[5001] - Status: Completed
# Order 5002 failed: Insufficient stock.
# Order[5002] - Status: Failed