class Animal:
    def __init__(self,name): # Constructor [Must have at least these to initialize an object of this class]
        self.name = name        # Attributes
        self.age = 2
    def speak(self):        # Method
        print("i am an animal")
        print("my name is : ",self.name)