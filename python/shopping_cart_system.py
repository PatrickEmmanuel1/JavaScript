from abc import ABC, abstractmethod

# Product class to manage individual product details
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock  # Encapsulated attribute

    # Public method to access private stock attribute
    def check_stock(self):
        return self.__stock

    # Update stock after purchase
    def reduce_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        return False

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Available: {self.__stock} items"
# Abstract base class for cart operations
class CartOperations(ABC):
    @abstractmethod
    def add_to_cart(self, product, quantity):
        pass

    @abstractmethod
    def remove_from_cart(self, product_id):
        pass
class ShoppingCart(CartOperations):
    def __init__(self):
        self.items = {}  # Dictionary to store products and quantities

    def add_to_cart(self, product, quantity):
        if product.check_stock() < quantity:
            print(f"Not enough stock for {product.name}. Available: {product.check_stock()}")
            return
        product.reduce_stock(quantity)
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"{quantity} of {product.name} added to cart.")

    def remove_from_cart(self, product_id):
        if product_id in self.items:
            product = self.items[product_id]['product']
            quantity = self.items[product_id]['quantity']
            product.reduce_stock(-quantity)  # Return stock back
            del self.items[product_id]
            print(f"Removed {product.name} from cart.")
        else:
            print("Item not in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Items in cart:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name}: {quantity} @ ${product.price} each")

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        print(f"Total Amount: ${total}")
        return total
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def view_products(self, products):
        print(f"\nAvailable Products for {self.name}:")
        for product in products:
            print(product)

    def checkout(self):
        print(f"{self.name} is checking out.")
        total = self.cart.calculate_total()
        print(f"Order placed successfully! Total: ${total}\n")

# Main function to demonstrate the shopping cart system
def main():
    # Sample products
    products = [
        Product(1, "Laptop", 1200, 5),
        Product(2, "Smartphone", 800, 10),
        Product(3, "Headphones", 150, 15)
    ]

    # Customer
    customer = Customer("Alice")

    # Display available products
    customer.view_products(products)

    # Shopping actions
    customer.cart.add_to_cart(products[0], 1)  # Adding 1 Laptop to cart
    customer.cart.add_to_cart(products[1], 2)  # Adding 2 Smartphones to cart
    customer.cart.view_cart()
    
    # Removing item from cart
    customer.cart.remove_from_cart(1)  # Remove Laptop
    customer.cart.view_cart()

    # Final checkout
    customer.checkout()

# Run the system
main()