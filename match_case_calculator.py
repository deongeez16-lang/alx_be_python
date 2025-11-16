# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Ask the user which operation to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using if/elif (Python 3.8 does not support match-case)
if operation == "+":
    result = num1 + num2
    print("The result is", result)
elif operation == "-":
    result = num1 - num2
    print("The result is", result)
elif operation == "*":
    result = num1 * num2
    print("The result is", result)
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("The result is", result)
else:
    print("Invalid operation.")

