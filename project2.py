# This section demonstrates a simpler calculator without error handling
# Prompt user to input a mathematical expression
expression = input("Type an expression: ")

# This line is commented out because it would cause a runtime error
# result = 3 / 0 # one will get error that ZeroDivisionError: division by zero

# Get first number from user
operand = input("Number 1: ")  # Prompts user to enter the first number
operand2 = input("Number 2: ")  # Prompts user to enter the second number
sign = input("Sign : ")  # Prompts user to enter the operation sign (+, -, *, /)

try: 
    operand = float(operand)    # Try to convert first input to a floating-point number
    operand2 = float(operand2)  # Try to convert second input to a floating-point number
except: 
    print("Invalid operand")    # If conversion fails, print error message

# Display the expression to be calculated
print(operand , sign , operand2)

# Initialize result variable to 0
result = 0

# Perform calculation based on the operation sign
if sign == "+":
    result = int(operand) + int(operand2)  # Addition operation
elif sign == "-":
    result = int(operand) - int(operand2)  # Subtraction operation
elif sign == "*":
    result = int(operand) * int(operand2)  # Multiplication operation
elif sign == "/":
    if float(operand2) != 0:  # Check if divisor is not zero
        result = int(operand) / int(operand2)  # Division operation
    else: 
        print("Division by zero Error")  # Handle division by zero error

# Display the result of the calculation
print(result)


# This section demonstrates an improved calculator with better error handling

# Define a function to get valid numeric input from user
def get_number(number):
    while True:  # Create an infinite loop
        operand = input("Number " + str(number) + ": ")  # Prompt user for input
        try:
            return float(operand)  # Try to convert to float and return if successful
        except:
            print("Invalid number, try again")  # If conversion fails, show error and loop again

# Get first number using the function
operand = get_number(1)  # Get first number with validation
operand2 = get_number(2)  # Get second number with validation
sign = input("sign : ")   # Get operation sign

# Initialize result variable
result = 0

# Perform calculation based on operation sign
if sign == "+":
    result = operand + operand2  # Addition with float values (no type conversion needed)
elif sign == "-":
    result = int(operand) - int(operand2)  # Subtraction with integer conversion
elif sign == "*":
    result = int(operand) * int(operand2)  # Multiplication with integer conversion
elif sign == "/":
    if float(operand2) != 0:  # Check for division by zero
        result = int(operand) / int(operand2)  # Division with integer conversion
    else: 
        print("Division by zero Error")  # Handle division by zero
        
# Display the final result
print(result)