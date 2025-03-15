# MRO = Method Resolution Order which is called first in multiple inheritance

class A:
    def show(self):
        return "A"
    
class B: 
    def show(self):
        return "B"
    
class C: 
    def show(self):
        return "C"

class D(B, C): # Multiple inheritance
    pass

d = D()

print(d.show())  # B ( follows C3 linearization : D -> B -> C -> A)
print(D.mro())   # shows method resolution ( class D -> class B -> class C -> class object)