# inheritance

#all the users must be signed in , so we use inheritance

class User:
    def __init__(self, email):
        self.email = email
    def sign_in(seld):
      print('Logged In')

class Wizard(User): #users, we have to pass the parent class user to inherit sign in method
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name 
        self.power = power
    
   # def attack(self):
    #     print(f"attacking with arrows: arrows left- {self.num_arrows}")

class Archer(User): #users 
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('ran really fast')

    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")

class HybridBorg(Wizard, Archer): #multiple inheritance
    def __init__(self, name, power, arrows):

        Archer.__init__(self, name, arrows)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows()

  
wizard1 = Wizard('Peter', 50, "wizard@gmail.com")
#archer1 = Archer('Mary', 100, "mary@gmail.com")

wizard1.attack()
#archer1.attack()

#print(wizard1.sign_in())  

#you abstract the User class because both the archer and wizard share these code

#to check if something is an instance of the class you would use isinstance function

#object introspection is the ability to determine the type of the object durign run time 
 #dir() gives all the methods or attributes that a instance of a class have

wizard2 = Wizard('happy', 60, "happy@gmail.com ")

print(isinstance(wizard2, Wizard)) #return true of false, in this case it is true
#print(dir(wizard2))


# the bases class of all objects is Object
print(isinstance(wizard2, object)) # you still get true

 #polymorphism, allows us to have many forms, it gives us the ability to redefine methods in many forms
 # 
def player_attack(char):
     char.attack() # the object you pass into it calls different attack methodss

player_attack(wizard1)
#player_attack(archer1)



#for char in [wizard1, archer1]:
 #   char.attack()


print(wizard2.email)

#multiple inheritance
