class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} eats.")

    def make_sound(self):
       print(f"{self.name} made a sound.")

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars!")

    def eat(self):
        print(f"{self.name} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")

    def eat(self):
        print(f"{self.name} eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")

    def eat(self):
        print(f"{self.name} eats bananas.")

animal1 = Lion("Tinoy")
animal2 = Elephant("Cham")
animal3 = Monkey("Yao")

zoo_animals = [animal1, animal2, animal3]

for animal in zoo_animals:
    animal.make_sound()
    animal.eat()
    print("-----")  
