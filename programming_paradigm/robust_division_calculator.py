def safe_divide(numerator, denominator):
    """
    Perform division safely, handling errors.

    Parameters:
        numerator: The numerator (can be string or numeric)
        denominator: The denominator (can be string or numeric)

    Returns:
        str: Result of division or an error message
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"

