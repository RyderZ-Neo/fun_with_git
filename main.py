
from an import Animal #an is filename that has the "Animal" class defined
class Dog(Animal): #Inheritance Also called Sub-Classes
    # (Have all capabilities of parents + extended abilities)
    #self.age = 10
    '''def speak(self):
        print("i am a dog named", self.name)
        print("i am "+ str(self.age)+ "years old." )'''
animal = Animal(name='fluu')
animal.speak()

dog1 = Dog(name='william')
dog1.speak()