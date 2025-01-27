class Product:
    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Price: {self.price}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print("Product added successfully.")

    def update_product(self, product_id, name=None, category=None, quantity=None, price=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if category:
                product.category = category
            if quantity:
                product.quantity = quantity
            if price:
                product.price = price
            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products.values():
                print(product)


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            product = Product(product_id, name, category, quantity, price)
            inventory.add_product(product)
        elif choice == '2':
            product_id = input("Enter product ID to update: ")
            name = input("Enter new product name (leave blank to keep current): ")
            category = input("Enter new product category (leave blank to keep current): ")
            quantity = input("Enter new product quantity (leave blank to keep current): ")
            price = input("Enter new product price (leave blank to keep current): ")
            inventory.update_product(product_id, name or None, category or None, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == '3':
            product_id = input("Enter product ID to delete: ")
            inventory.delete_product(product_id)
        elif choice == '4':
            inventory.view_inventory()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()