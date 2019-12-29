#object oriented programming in python


#everythinig in Python is an object

print("all the data types in Python")
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

#objects have methods and attributes 
# you create your own objects using the class keyword. 

 #  more and more technology requires thousands of lines. so you need classes

 #for example Amazon Delivery Drones can be broken down into different functionality and each can be its own classes

 #OOP is a paradigm is a way to think about our code and structure the code.

 #previous programming languages 
 
 #assembly language - really close to machine language
 # procedural code - C Programming Language

# class name should start with a Capital Letter
 
class Big_Object:
     pass

obj = Big_Object() # instantiating the object, creating a new object

print(type(Big_Object))
print("the type of class Big_Object is " + str(type(obj)))

#creating our own objects
#self must be always included as a paramenter for a fucntion in a class

class Player_Characters:
    #like a constructor
    membership = True #class objects 
    def __init__(self,name, age):
        if(Player_Characters.membership):
            self.name = name #attribute
            self.age = age #atttributes

    def run(self):
      print("run")
      return 'done'
#class method
    @classmethod
    def adding_things(cls, num1, num2): #cls is short for class
         return cls('teddy', num1 + num2)

    def shout(self):
        print(f'My name is {self.name}')

 
#static methods does not have a cls 

player1 = Player_Characters('Johnny', 45)

print(player1.name  + " " +  str(player1.age))

player2 = Player_Characters('Tommy', 33)

print(player2.name + " " +  str(player2.age))

 #self is like this in Java 

print(player1.run()) 

#print(player1.adding_things(4,5))

player3 = Player_Characters.adding_things(2,3)

print(player3.age) # its a methods on the class  

print(player3.name)
#attributes and methods - to add functionlaity of to the program


#help(player1)

print(player1.membership)
print(player2.membership)

# exercise cats everywhere

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    




cat1 = Cat("Peanut", 5)
cat2 = Cat("Anthony", 3)
cat3 = Cat("Mary", 2)



def get_oldest_cat(*args):
    return max(args)


print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")


#review

#claassical OOP is of classes class, class object attributes, methods, class methods and static methods. 


#the four pillars of OOP : encapsulation, abstraction

# encapsulation, hidind attributes, methods in the class
# abstraction: only have or know what is necessary. everything else is hidden, abstraction can be overridden if there is no data type restrictions. so use public and private




# _name is a private variable, but there is no gurantee of private and non-changeable



