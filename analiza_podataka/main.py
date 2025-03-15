from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product("Laptop", 80000, 5)
product2 = Product("Telefon", 50000, 10)
product3 = Product("Monitor", 20000, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()} RSD")
from cart import Cart

cart = Cart()
cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

print("Proizvodi u korpi:")
cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.calculate_total()} RSD")
