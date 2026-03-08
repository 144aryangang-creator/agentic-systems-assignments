try:
    # Taking inputs and converting them to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Performing operations
    print(f"Sum: {num1 + num2}")
    print(f"Division result: {num1 / num2}")

except ValueError:
    # Triggered if input() cannot be cast to an integer
    print("Invalid input")

except ZeroDivisionError:
    # Triggered if the second number is zero
    print("Cannot divide by zero")
