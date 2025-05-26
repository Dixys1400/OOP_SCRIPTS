


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:2}$"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)
        print(f"Added: {item}")

    def total(self):
        return sum(item.price for item in self.items)

    def print_receipt(self):
        print("\n Ticket:")
        for item in self.items:
            print(f" - {item}")
        print(f"💰 Total: ${self.total():.2}$\n")



class Cafe:
    def __init__(self):
        self.menu = [
            MenuItem("Cappuccino", 3.5),
            MenuItem("Americano", 2.5),
            MenuItem("croissant", 2),
            MenuItem("Sandwich", 3)
        ]

    def show_menu(self):
        print("📋 Меню:")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item}")

    def take_order(self):
        order = Order()
        while True:
            self.show_menu()
            choice = input("Select a dish number (or 'q' to complete):")
            if choice.lower() == 'q':
                break
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.menu):
                    order.add_item(self.menu[idx])
                else:
                    print("❌ Invalid number.")
            except ValueError:
                print("Enter number.")
        order.print_receipt()

cafe = Cafe()
cafe.take_order()
