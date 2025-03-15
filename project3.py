import json  # Import the json module to handle JSON file operations

def add_person():
    """
    Function to collect contact information from user input.
    Returns a dictionary containing the person's details.
    """
    name = input("name: ")  # Ask user for the contact's name
    age = input("age: ")    # Ask user for the contact's age
    email = input("email: ") # Ask user for the contact's email
    
    # Create a dictionary with the collected information
    person = {"name": name, "age": age, "email": email}
    return person  # Return the dictionary representing the person

def display_people(people):
    """
    Function to display a list of people with their details.
    Takes a list of person dictionaries as input.
    """
    for i, person in enumerate(people): # Loop through the list with index and value pairs
        # Print each person with their index number, name, age, and email
        print(i+1, "-", person["name"], "|", person["age"] , "|" , person["email"])
        
        
def delete_contact(people):
    """
    Function to delete a contact from the list.
    First displays the list, then asks for a number to identify which contact to delete.
    """
    display_people(people)  # Show the list of contacts
    
    while True:  # Loop until a valid number is entered
        number = input("Enter a number to delete: ")  # Ask for the contact number to delete
        try: 
            number = int(number)  # Try to convert input to integer
            if number <= 0 or number > len(people):  # Check if number is in valid range
                print("Invalid number, out of range")
            else: 
                break  # Exit the loop if number is valid
        except: 
            print("Invalid number")  # Error if input cannot be converted to integer
    
    people.pop(number-1)  # Remove the person at index (number-1) from the list
    print("Person deleted")  # Confirm deletion

def search(people):
    """
    Function to search for contacts by name.
    Searches case-insensitive partial matches in names.
    """
    search_name = input("Search for a name: ").lower()  # Get search term and convert to lowercase
    results = []  # Initialize empty list for search results
    
    for person in people:  # Loop through all contacts
        name = person["name"]  # Get the person's name
        if search_name in name.lower():  # Check if search term is in the name (case-insensitive)
            results.append(person)  # Add matching person to results
    
    display_people(results)  # Display the search results
    

# Main program starts here
print("Hi, welcome to the Contact Management System.")  # Welcome message
print()  # Print empty line for spacing

# Open the contacts file and load the data
with open("contacts.json", "r") as f:  # Open the file in read mode
    people = json.load(f)["contacts"]  # Load JSON data and extract the contacts list

# Main program loop
while True:  # Run until explicitly broken with 'break'
    print()  # Print empty line for spacing
    print("Contact list size:", len(people))  # Display the number of contacts
    # Ask user for command and convert to lowercase for case-insensitive matching
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()

    if command == "add":  # If user wants to add a contact
        person = add_person()  # Call function to collect person details
        people.append(person)  # Add the new person to the contacts list
        print("Person added!")  # Confirm addition (note: typo fixed from "Peron")
    elif command == "delete":  # If user wants to delete a contact
        delete_contact(people)  # Call function to handle deletion
    elif command == "search":  # If user wants to search contacts
        search(people)  # Call function to handle search
    elif command == "q":  # If user wants to quit
        break  # Exit the main loop
    else:  # If user entered an invalid command
        print("Invalid command.")  # Show error message

# Save the updated contacts list to the file
with open("contacts.json", "w") as f:  # Open file in write mode
    json.dump({"contacts": people}, f)  # Save the contacts list as JSON data