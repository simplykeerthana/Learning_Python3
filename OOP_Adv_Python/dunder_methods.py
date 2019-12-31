class Toy():
    def __init__(self, color, age):
        self.color = color 
        self.age = age


    def __str__(self): #you can sometimes modify dunder methods
        return f'{self.color}'

    def __len__(self):
        return 5

   # def __del__(self):
       # print('deleted!')

    def __call__(self):
        return('yess?')

action_figure = Toy('red', 0)
print(action_figure.__str__()) #dunder methods like __str__() are recognized by python

#the above dunder method can be written like 
print(str(action_figure))
print(len(action_figure))

#del action_figure
print(action_figure())


#exercise Extending Lists

class SuperList(list):
    def __len__(self):
        return 1000

super_List1 = SuperList();

print(len(super_List1))

super_List1.append(5)

print(super_List1[0])
print(issubclass(list,object))
print(super_List1)
 

