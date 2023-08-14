class Animal():
    def __init__(self, name, height, age, weight):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
    
    def __str__(self):
        message = "name is {} , height is {}, age is {}, weight is {}".format(self.name,self.height, self.age, self.weight)
        return(message)
    
    def eat(self):
        print("Is eating ... ")

    def sleep(self):
        print("is sleeping...")


class Bird(Animal):

    def __init__(self, name, height, age, weight, wing_length, can_fly):
        super().__init__(name, height, age, weight)
        self.wing_length = wing_length
        self.can_fly = can_fly

    def sleep(self):
        super().sleep()
        print("sleep on tree .. ")

    def eat(self):
        print("is pecking...")
    


class Mamel(Animal):
    def __init__(self,name, height, age, weight, giving_birth, breast_feeding):
        super().__init__(name, height, age, weight)
        self.giving_birth = giving_birth
        self.breast_feeding = breast_feeding

    def __str__(self):
        super().__str__()
        messege = "giving_birth {} , breast_feeding {} " .format(self.giving_birth, self.breast_feeding)
        return messege


    def sleep(self):
        super().sleep()
        print("sleep on the earth...")
    


class Reptile(Animal):
    pass

my_rep = Reptile("Snake", 150, 5, 12)
print(my_rep)
my_rep.sleep()





# my_bird = Bird("eagle", 80, 4, 30, 100, True)
# print(my_bird)

# my_bird.sleep()
# my_bird.eat()