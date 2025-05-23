


class SuperCar:
    def __init__(self, brand, model, hp):
        self.brand = brand
        self.model = model
        self.hp = hp



    def show_off(self):
        print(f"{self.brand} {self.model} рычит с {self.hp} л.с!!")


    def compare_horsepower(self, other):
        if self.hp > other.hp:
            print(f"{self.model} мощнее чем {other.model} на {self.hp - other.hp} л.с!")
        elif self.hp < other.hp:
            print(f"{other.model} мощнее чем {self.model} на {other.hp - self.hp} л.с!")
        else:
            print(f"{self.model} и {other.model} имеют одинаковую мощность")







corvette = SuperCar("Corvette", "Z06 3LZ Performance Targa", 660)
lambo = SuperCar("Lamborghini", "Huracan STO", 631)
McLaren = SuperCar("McLaren", "765LT", 752)

corvette.show_off()
lambo.show_off()
McLaren.show_off()


lambo.compare_horsepower(McLaren)

