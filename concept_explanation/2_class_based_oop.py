# Python follows class based OOP like js ES6 classes

class Animal: 
    def __init__(self, name): # Constructor method
        self.name = name #instance variable
        
    def speak(self): #instance method
        return f"{self.name} makes a sound"
    
# creating an object
dog = Animal("Dog")
print(dog.speak()) # Dog makes a sound
        