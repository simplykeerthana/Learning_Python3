class Toy():
    def __init__(self, color, age):
        self.color = color 
        self.age = age


    def __str__(self): #you can sometimes modify dunder methods
        return f'{self.color}'

    def __len__(self):
        return 5

action_figure = Toy('red', 0)
print(action_figure.__str__()) #dunder methods like __str__() are recognized by python

#the above dunder method can be written like 
print(str(action_figure))
print(len(action_figure))