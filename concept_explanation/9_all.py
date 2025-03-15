# Python is interpreted , dynmaically typed , object oriented , memory managed ( garbage collection handles unused objects)



# Python 2 : print "Hello" ( No parantheses)          
#            5/2 = 2 ( Integer division)
#            ASCII default
#            range() return list


# Python 3 : print("Hello")(Function)
#            5/2 = 2.5 (Floating point)
#            Unicode default
#            range() return generator



# Python's Data Types
# Python has primitive and collection types
# Primitive: int, float , bool , str, complex
# Collections : list, tuple , set , dict



# Mutable vs Immutable Data Types
# Mutable(can change): list , dict , set
# Immutable(cannot change): int , float , str, tuple

# Mutable (lists can be modified)
lst = [1, 2, 3]
lst[0] = 100  # Allowed

# Immutable (tuples cannot be modified)
tpl = (1, 2, 3)
# tpl[0] = 100  # Error



# Difference between is and == 
# is checks the memory location and == checks value
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  #  True (values are same)
print(a is b)  #  False (different memory locations)


# Python memory management 
# uses Reference Counting and Garbage collection
import sys
x = [1, 2, 3]
print(sys.getrefcount(x))  # Shows reference count



# List vs Tuple
# List : Mutable , slower
# Tuple : Immutable , faster

lst = [1, 2, 3]  # Mutable
tpl = (1, 2, 3)  # Immutable


# swap two variables Without Temp
a, b = 5, 10
a, b = b, a  # Swaps values
print(a, b)  # Output: 10, 5


# Python's Built in Data Structures
# List : [1,2,3]
# Tuple : (1,2,3)
# Set : {1, 2,3}
# Dictionary: { "a": 1, "b": 2}



# Remove duplicates form List

lst = [1, 2, 3, 4, 4, 5]
lst = list(set(lst)) # removes duplicates
print(lst)


# List Comprehension
lst = [x**2 for x in range(5)]
print(lst)


# copy() vs deepcopy()
import copy

lst1 = [[1,2], [3,4]]
lst2 = copy.deepcopy(lst1)  # copies nested lists properly


# *args vs ** kwargs

def func(*args, **kwargs):
    print(args)  # tuple of values
    print(kwargs) # Dictionary of key value pairs
    
func(1,2 ,3 , name="Aaryan", age=22)



# Exceptional Handling
try: 
    x = 1/0
except ZeroDivisionError as e:
    print("Error:",e)


# with statement
# Automatically closes files after reading/writing

with open("file.txt", "r") as file:
    data = file.read() # file auto closes after block ends


# @staticmethod vs @classmethod

class MyClass1:
    @staticmethod
    def static_method():
        return "No access to class"
    
    @classmethod
    def class_method(cls):
        return f"Accessing class: {cls}"

print(MyClass1.static_method())
print(MyClass1.class_method())



# Generators vs Iterators
# Generators saves memory

def my_generator():
    yield 1
    yield 2
    
gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2


# Global Interpretor Lock ( GIL )
# Prevents multiple threads from executing python code at the same time
# Use multiprocessing instead

from multiprocessing import Process

def f():
    print("running in a separate process")
    
p = Process(target=f)
p.start()



from functools import reduce

nums = [1,2,3,4]
print(list(map(lambda x: x*2, nums))) # Doubles each number
print(list(filter(lambda x: x%2 == 0, nums))) # Keeps evens
print(reduce(lambda x, y: x+ y, nums)) # sums list


# Merging Dictionaries 
dict1 = {"a":1}
dict2 = {"b": 2}
merged = dict1 | dict2 
print(merged)


# Metaclasses 
# used to control class creation 

class Meta(type):
    def __new__(cls, name , bases , dct):
        print("Creating classes", name)
        return super().__new__(cls, name, bases , dct)

class MyClass(metaclass = Meta):
    pass # Triggers metaclass
