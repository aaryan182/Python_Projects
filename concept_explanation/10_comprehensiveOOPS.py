# Classes & Objects
#  Encapsulation (Getters/Setters, Private & Protected attributes)
#  Inheritance (Single, Multiple, Multilevel)
#  Polymorphism (Method Overriding, Method Overloading)
#  Abstraction (Using ABC module)
#  Class & Static Methods
#  Special/Magic Methods (__init__, __str__, __repr__, __new__)
#  Method Resolution Order (MRO)
#  Duck Typing


from abc import ABC, abstractmethod

# Class and Objects
class Animal: 
    """Base class for all animals"""
    
    kingdom = "Animalia"  # Class variable

    def __init__(self, name, species):
        """Constructor to initialize object attributes"""
        self.name = name  # Instance variable
        self.species = species
    
    def sound(self):
        return "Some generic animal sound"
    
    @classmethod
    def get_kingdom(cls):
        return cls.kingdom
    
    @staticmethod
    def is_alive():
        return True

# Inheritance (Single Level)
class Dog(Animal):
    """Dog class inheriting from Animal"""

    def __init__(self, name , breed):
        super().__init__(name, species="Dog")  
        self.breed = breed  
    
    def sound(self):
        return "Bark Bark"

# Multilevel Inheritance
class Puppy(Dog):
    def sound(self):
        return "Yip Yip"  

# Multiple Inheritance
class Swimmer:
    def swim(self):
        return "I can swim"

class Amphibian(Animal, Swimmer):
    """An amphibian inherits from Animal and Swimmer"""

# Abstraction
class Bird(ABC):
    """Abstract class for birds"""
    
    @abstractmethod
    def fly(self):
        pass  

class Sparrow(Bird):
    def fly(self):
        return "I can fly high"

# Encapsulation (Private & Protected Variables)
class BankAccount:
    def __init__(self, balance):
        self._protected_balance = balance  # Protected variable (_)
        self.__private_balance = balance  # Private variable (__)
    
    def get_balance(self):
        return self.__private_balance  

# Operator Overloading (Polymorphism)
class Vector: 
    """Vector class to demonstrate operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Duck Typing
class Car:
    def move(self):
        return "Car is moving"
    
class Boat:
    def move(self):
        return "Boat is sailing"

def travel(vehicle):
    return vehicle.move()  

# Method Resolution Order (MRO)
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):  # Resolves via MRO
    pass

# Special Methods (__init__, __repr__, __new__)
class Singleton:
    _instance = None
    
    def __new__(cls):
        """Ensures only one instance of class exists (Singleton Pattern)"""
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __repr__(self):
        return "Singleton instance"

# Running All Examples
dog = Dog("Buddy", "Golden Retriever")
print(dog.name, dog.breed, dog.sound())  

print(Animal.get_kingdom())  
print(Animal.is_alive())  

amphibian = Amphibian("Frog", "Amphibian")
print(amphibian.swim())  

sparrow = Sparrow()
print(sparrow.fly())  

account = BankAccount(1000)
print(account.get_balance())  #  Corrected way
# print(account.__private_balance)  #  Accessing private variable (not recommended)

vec1 = Vector(1,2)
vec2 = Vector(3,4)
print(vec1 + vec2)  #  Operator overloading working

car = Car()
boat = Boat()
print(travel(car))  # Duck Typing
print(travel(boat))  #  Duck Typing

print(D().show())  #  Resolves via MRO
print(D.mro())  #  See method resolution order

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  #  Ensures only one instance
