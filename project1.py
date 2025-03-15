name = input("Hey type your name ?") # Ask the user to type their name in console
print(name) # Output the name to console, similar to console.log in JavaScript

print("hello", "world")  # Using comma between strings automatically adds a space when printing
print("aaryan") # Each print statement automatically starts on a new line

# Comments about data types in Python:
# string is in quotation marks (can use single or double quotes)
# int, float(decimal place) are numeric types
# boolean true/false (in Python they're True/False with capital first letter)

# Note on variable naming conventions:
# variable names can be uppercase or lowercase but cannot start with special characters except underscore or numbers
# variable names cannot start with a number, but can contain numbers

print("kya haal hai " + name + " bhai") # String concatenation using + operator

should_we_play = input("Do you want to play? ").lower() # Get user input and convert to lowercase

play = should_we_play == "yes" # Boolean variable that is True if user typed "yes"
print(play) # Print the boolean result

# Commented out code example:
# if play : 
#     print("We are gonna play")

# Conditional statements with if, elif, else:
if should_we_play == "yes":
    print("we play") # This runs if user enters exactly "yes"
elif should_we_play == "YES": 
    print("we may play") # This would never run because of the .lower() call earlier
else: 
    print("no play") # This runs for any input other than "yes"
    
# Comment about logical operators:
# and or not operators - used for combining conditions