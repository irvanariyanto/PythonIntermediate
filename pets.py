class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "Meowww"

class Dog(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "Wooof"

def Main():

    pets = [Cat("jess",3),Dog("jack",2),Cat("fred",7), Pet("thePet", 5)]
    for pet in pets:
        print "Name:" + pet.name + ", age:" + str(pet.age) + ", says:" + pet.talk()

if __name__ == "__main__":
    Main()
