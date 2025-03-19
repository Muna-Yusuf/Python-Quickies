def calculator():
    """
    A simple calculator that takes two numbers and an operation 
    from the user, then performs the calculation and prints the result.
    """

    # Take user input for the first number
    num1 = float(input("Enter first number: "))

    # Take user input for the second number
    num2 = float(input("Enter second number: "))

    # Take user input for the operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the appropriate calculation based on the operation input
    if operation == '+':
        result = num1 + num2  # Addition
    elif operation == '-':
        result = num1 - num2  # Subtraction
    elif operation == '*':
        result = num1 * num2  # Multiplication
    elif operation == '/':
        # Check for division by zero to avoid errors
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operation"  # Handle invalid operations

    # Display the result
    print(f"Result: {result}")

# Run the calculator function only if the script is executed directly
if __name__ == "__main__":
    calculator()
