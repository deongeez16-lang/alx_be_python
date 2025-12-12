from robust_division_calculator import safe_divide

print(safe_divide(10, 5))    # Should print "The result of the division is 2.0"
print(safe_divide(10, 0))    # Should print "Error: Cannot divide by zero."
print(safe_divide("ten", 5)) # Should print "Error: Please enter numeric values only."

