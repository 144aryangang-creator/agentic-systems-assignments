class StudentPerformance:
    def __init__(self, scores_list):
        # Stores the list of scores provided by the user
        self.scores = scores_list

    def score_difference(self):
        try:
            # Attempt to access the first (index 0) and last (index -1) scores
            # This will naturally trigger an IndexError if the list is empty
            first_score = self.scores[0]
            last_score = self.scores[-1]
            
            difference = last_score - first_score
            print(f"Difference (Last - First): {difference}")
            
        except IndexError:
            # Triggered if self.scores is []
            print("No scores available to calculate difference")

# --- Interactive Input Logic (No Hardcoding) ---

user_input = input("Enter student scores separated by spaces: ")

try:
    # Convert input string into a list of integers
    # .split() converts "90 80" into ["90", "80"]
    input_scores = [int(s) for s in user_input.split()]
    
    # Create the object and run the method
    performance = StudentPerformance(input_scores)
    performance.score_difference()

except ValueError:
    # Triggered if the user enters non-numeric text
    print("Invalid input: Please enter only numbers.")