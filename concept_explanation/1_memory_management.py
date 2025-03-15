# Python uses reference counting and garbage collection to manage memory

import sys
import gc

# Reference counting example
a = [ 1, 2, 3] # List object created in memory
b = a # another reference to the same list (not a copy)
print(sys.getrefcount(b)) # reference count decreased

del a # removes one reference
print(sys.getrefcount(b)) # Reference count decreased


#Garbage collection example ( Handles circular references )
class Node:
    def __init__(self):
        self.ref = self # creates a circular reference
        
n = Node()
del n # Object is not freed due to circular reference

gc.collect() # forces garbage collection to clean up circular references

