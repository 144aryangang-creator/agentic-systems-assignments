class StudentMarks:
    def __init__(self, marks_list):
        self.marks = marks_list

    def last_three_avg(self):
        try:
            # Check if the list has fewer than 3 elements
            if len(self.marks) < 3:
                # Raising a LookupError to signify we can't find the needed indices
                raise LookupError
            
            # Negative indexing to slice the last three elements
            last_three = self.marks[-3:]
            avg = sum(last_three) / 3
            print(f"Average of the last three marks: {avg:.2f}")
            
        except LookupError:
            print("Not enough marks to calculate average")

# --- Interactive Logic (No Hardcoded Data) ---

def run_student_app():
    user_string = input("Enter all student marks separated by spaces: ")
    
    try:
        # Convert the input string into a list of integers dynamically
        # .split() handles any number of spaces between entries
        marks = [int(m) for m in user_string.split()]
        
        # Create object with the dynamic list
        student_obj = StudentMarks(marks)
        
        # Call the method
        student_obj.last_three_avg()
        
    except ValueError:
        # This catches if the user types something like "85 90 A+"
        print("Invalid input: Please enter only numeric values.")

if __name__ == "__main__":
    run_student_app()