# Generators yield values one by one instead of storing them all in ṁemory

# Generator of fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a # Yielding instead of returning (like async iterators in JS)
        a, b = b , a + b  # move to the next Fibonacci number
        
# Using the generator
for num in fibonacci(5):
    print(num)  