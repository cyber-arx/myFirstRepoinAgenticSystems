# Function 1: Greeting
def greet_student(name):
    return f"Hello, {name}"


# Function 2: Calculate statistics
def calculate_stats(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score


# Function 3: Determine pass/fail
def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Main function
def main():
    # Take input
    name = input("Enter student name: ")
    scores_input = input("Enter scores separated by spaces: ")
    
    # Convert input string into list of integers
    scores = list(map(int, scores_input.split()))
    
    # Call functions
    greeting = greet_student(name)
    subjects, average = calculate_stats(scores)
    result = evaluate_result(average)
    
    # Print final output
    print(greeting)
    print(f"Subjects: {subjects}")
    print(f"Average Score: {average}")
    print(f"Result: {result}")


# Start program
main()
