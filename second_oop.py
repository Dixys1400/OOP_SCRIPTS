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
        for item in self.inventory:
            print(f" - {item}")

    def find_by_category(self, category):
        results = [item for item in self.inventory if item.category.lower() == category.lower()]
        print(f"Category clothes of '{category}'")
        for item in results:
            print(f" - {item}")





boutique = Boutique("Fashion Loft")

boutique.add_item(ClothingItem("Jorts", "XL", 40, "Shorts"))
boutique.add_item(ClothingItem("Shirt", "L", 39.99, "Shirts"))
boutique.add_item(ClothingItem("Shoes Private", "45", 120, "Shoes"))


boutique.show_catalog()
boutique.find_by_category("Shorts")