# Simple Calculator in Python

# Function to perform the chosen operation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

# Main program
print("Welcome to the Simple Calculator!")

# Input the first number
num1 = float(input("Enter the first number: "))

# Input the second number
num2 = float(input("Enter the second number: "))

# Input the operation
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

# Perform the calculation
result = calculate(num1, num2, operation)

# Display the result
print(f"The result of {operation}ing {num1} and {num2} is: {result}")
