# pets everywhere 

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 2)]

my_pets = Pets(my_cats)

my_pets.walk()