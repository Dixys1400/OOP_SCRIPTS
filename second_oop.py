class ClothingItem:
    def __init__(self, name, size, price, category):
        self.name = name
        self.size = size
        self.price = price
        self.category = category


    def __str__(self):
        return f"{self.name} ({self.category}), size: {self.size}, price: {self.price}$"


class Boutique:
    def __init__(self, name):
        self.name = name
        self.inventory = []


    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added: {item}")

    def show_catalog(self):
        print(f"Catalog of the boutique {self.name}:")
        if not self.inventory:
            print("Not items available.")
        for item in self.inventory:
            print(f" - {item}")


    def find_by_category(self, category):
        results = [item for item in self.inventory if item.category.lower() == category.lower()]
        print(f"Items in category '{category}'")
        if results:
            for item in results:
                print(f" - {item}")
        else:
            print("No items found in this category.")



def main():
    boutique = Boutique("Fashion Loft")

    while True:
        print("\n ====== MENU ======")
        print("1. Add clothing item")
        print("2. Show catalog")
        print("3. Find by category")
        print("4. Exit")
        choice = input("Choose an option (1-4)")


        if choice == "1":
            name = input("Name: ")
            size = input("Size: ")
            price = float(input("Price: "))
            category = input("Category: ")
            item = ClothingItem(name, size, price, category)
            boutique.add_item(item)

        elif choice == "2":
            boutique.show_catalog()

        elif choice == "3":
            category = input("Enter category to search: ")
            boutique.find_by_category(category)

        elif choice == "4":
            print("👋 Exiting boutique. See you soon, bro!")
            break

        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()

