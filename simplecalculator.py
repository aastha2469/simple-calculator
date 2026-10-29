# Simple Calculator: addition, subtraction, multiplication, and division

try:
    # Get the first number, operation, and second number from the user
    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: "))

    # Calculate the result based on the chosen operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operation. Choose +, -, *, or /.")

    # Display the answer
    print(f"Result: {result}")

except ValueError as error:
    print(f"Invalid input: {error}")
except ZeroDivisionError as error:
    print(f"Error: {error}")