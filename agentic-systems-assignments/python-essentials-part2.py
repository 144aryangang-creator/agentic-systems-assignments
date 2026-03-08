def user_info():
    # Input for names
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Input for age
    age_input = input("Enter your age: ")

    try:
        # Convert to integer
        age = int(age_input)

        # Check for negative age
        if age < 0:
            print("Age cannot be negative")
        else:
            # Full Name using concatenation (+)
            full_name = first_name + " " + last_name
            print("Full Name: " + full_name)

            # Age next year
            print(f"You will be {age + 1} next year")

    except ValueError:
        # Triggered if age_input is not numeric
        print("Invalid age input")

# Run the function
user_info()
