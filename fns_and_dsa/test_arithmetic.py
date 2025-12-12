from arithmetic_operations import perform_operation

print("Add:", perform_operation(5, 6, "add"))
print("Subtract:", perform_operation(10, 3, "subtract"))
print("Multiply:", perform_operation(4, 7, "multiply"))
print("Divide:", perform_operation(20, 4, "divide"))
print("Divide by zero:", perform_operation(5, 0, "divide"))
print("Invalid operation:", perform_operation(5, 5, "mod"))

