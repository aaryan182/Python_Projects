import random  # Import random module for selecting random questions
import json    # Import json module for working with JSON files
import time    # Import time module for tracking quiz duration

def load_questions():
    """
    Load quiz questions from a JSON file.
    
    Returns:
        list: A list of question dictionaries
    """
    with open("questions.json", "r") as f:  # Open the JSON file in read mode
        questions = json.load(f)["questions"]  # Extract the "questions" array from the JSON
    return questions  # Return the list of questions

def get_random_questions(questions, num_questions):
    """
    Select a random subset of questions.
    
    Args:
        questions (list): List of all available questions
        num_questions (int): Number of questions to select
        
    Returns:
        list: Randomly selected questions
    """
    if num_questions > len(questions):  # If requested more questions than available
        num_questions = len(questions)  # Use all available questions instead
    
    random_questions = random.sample(questions, num_questions)  # Select random questions without replacement
    return random_questions  # Return the selected questions

def ask_questions(questions):
    """
    Display a question with options and verify the user's answer.
    
    Args:
        questions (dict): A question dictionary containing the question text, options, and answer
        
    Returns:
        bool: True if the user's answer is correct, False otherwise
    """
    print(questions["question"])  # Display the question text
    for i, option in enumerate(questions["options"]):  # Loop through answer options with indices
        print(str(i+1) + ".", option)  # Display each option with a number
        
    number = int(input("select the correct number: "))  # Get user's answer as a number
    
    # Validate user input
    if number < 1 or number > len(questions["options"]):
        print("Invalid choice, defaulting to wrong answer")
        return False  # Return False for invalid inputs
    
    # Check if the selected option matches the correct answer
    correct = questions["options"][number-1] == questions["answer"]
    return correct  # Return True if correct, False if wrong

# Main program starts here
questions = load_questions()  # Load all questions from the file

# Ask user how many questions they want to answer
total_questions = int(input("enter the number of questions : "))

# Select random questions based on user input
random_questions = get_random_questions(questions, total_questions)

correct = 0  # Initialize counter for correct answers
start_time = time.time()  # Record the start time of the quiz

# Loop through each selected question
for question in random_questions:
    is_correct = ask_questions(question)  # Ask the question and check if answer is correct
    if is_correct:
        correct += 1  # Increment correct answer counter if answer was correct
    
    print("---------")  # Print separator between questions
        
completed_time = time.time() - start_time  # Calculate total quiz duration

# Display quiz summary
print("Summary")
print("Total Questions", total_questions)
print("Correct Answers ", correct)
print("Score: ", str(round((correct/total_questions)*100, 2))+ "%")  # Calculate and format percentage score
print("Time: ", round(completed_time, 2), "seconds")  # Display quiz duration in seconds