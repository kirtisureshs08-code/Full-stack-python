class Product:
    
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category

    def display_product(self):
        print("ID:", self.product_id)
        print("Name:", self.product_name)
        print("Price:", self.price)
        print("Category:", self.category)


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_item_total(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product, quantity):
        for item in self.cart:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.cart.append(CartItem(product, quantity))

    def remove_product(self, product_id):
        for item in self.cart:
            if item.product.product_id == product_id:
                self.cart.remove(item)
                print("Product Removed Successfully")
                return
        print("Product Not Found")

    def update_quantity(self, product_id, quantity):
        for item in self.cart:
            if item.product.product_id == product_id:
                item.quantity = quantity
                print("Quantity Updated")
                return
        print("Product Not Found")

    def view_cart(self):
        print("\n----- Shopping Cart -----")
        for item in self.cart:
            print(item.product.product_name,
                  "Price:", item.product.price,
                  "Qty:", item.quantity,
                  "Total:", item.calculate_item_total())

    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item.calculate_item_total()
        return total

    def apply_discount(self, total):
        if total > 10000:
            discount = total * 0.15
        elif total > 5000:
            discount = total * 0.10
        else:
            discount = 0
        return discount

    def generate_invoice(self):
        print("\n========== INVOICE ==========")
        self.view_cart()
        subtotal = self.calculate_total()
        discount = self.apply_discount(subtotal)
        final = subtotal - discount

        print("----------------------------")
        print("Subtotal =", subtotal)
        print("Discount =", discount)
        print("Final Amount =", final)
        print("============================")


# ---------------- Main Program ----------------

p1 = Product(101, "Laptop", 50000, "Electronics")
p2 = Product(102, "Mouse", 500, "Electronics")
p3 = Product(103, "Keyboard", 1500, "Electronics")

cart = ShoppingCart()

cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.add_product(p3, 1)

cart.generate_invoice()