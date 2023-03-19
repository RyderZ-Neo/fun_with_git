class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print("i am an animal")
class Dog(Animal):
    def speak(self):
        print("i am a dog named", self.name)
        print("i am "+ str(self.age)+ "years old." )
'''animal = Animal(name='fluu',age= 5)
animal.speak()'''

dog1 = Dog(name='william',age=7)
dog1.speak()