# Base class
class Vechile:
    def __init__(self, brand):
        self.brand = brand # Encapsulation ( private attribute)
    
    def move(self):
        return "Moving ..."
    

# Derived Class (Inheritance)
class Car(Vechile):
    def move(self): # Polymorphism( overriding move method)
        return "Driving a car"
    
# Using the classes 
car = Car("Bajaj")
print(car.move())  