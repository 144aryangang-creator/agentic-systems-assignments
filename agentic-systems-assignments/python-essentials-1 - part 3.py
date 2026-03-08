name = input ("Enter your full name : ")
age_input = input ("Enter your Age : ")


     # Convert age to integer
age = int(age_input)

        # Check for negative age first
if age < 0:
            print("Age cannot be negative")
        

        # Print greeting
print(f"Hello {name}")

        # Determine Age Category using if-elif-else
if age < 13:
            print("You are a Child")
elif 13 <= age <= 17:
            print("You are a Teenager")
elif 18 <= age <= 59:
            print("You are an Adult")
else:
            print("You are a Senior Citizen")

        # Determine Voting Eligibility
if age >= 18:
            print("You are eligible to vote")
else:
            print("You are not eligible to vote")


# Run the function
age_checker()
        
