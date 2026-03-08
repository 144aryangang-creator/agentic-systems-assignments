class StudentScores:
    def __init__(self, scores_list):
        # The list is passed dynamically during object creation
        self.scores = scores_list

    def highest_last_two(self):
        try:
            # Check if the list has fewer than 2 scores
            if len(self.scores) < 2:
                # Manually raise an IndexError to trigger the exception handler
                raise IndexError
            
            # Use negative indexing to get the last two scores
            # scores[-1] is the last, scores[-2] is the second to last
            last_two = [self.scores[-1], self.scores[-2]]
            
            highest = max(last_two)
            print(f"Highest of the last two scores: {highest}")
            
        except IndexError:
            print("Not enough scores to find highest value")

# --- Getting User Input (No Hardcoding) ---

user_input = input("Enter student scores separated by spaces: ")

try:
    # Convert input string into a list of integers
    input_scores = [int(s) for s in user_input.split()]
    
    # Create the object and call the method
    student = StudentScores(input_scores)
    student.highest_last_two()

except ValueError:
    print("Invalid input: Please enter only numbers.")