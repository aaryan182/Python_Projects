# Python has @classmethod and @staticmethod which behave differently

class MyClass: 
    class_variable = "Shared value"
    
    @classmethod
    def class_method(cls):
        return f"Class method called accessing: {cls.class_variable}"
    
    @staticmethod
    def static_method():
        return "Static method called. No access to class variables"
    
# Calling methods
print(MyClass.class_method()) # can access class_variable
print(MyClass.static_method()) # cannot access class_variable