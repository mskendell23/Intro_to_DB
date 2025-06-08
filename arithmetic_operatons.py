def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the provided numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform ("add", "subtract", "multiply", "divide").

    Returns:
        float: The result of the operation.
        str: An error message for division  by zero or invalid operation.
    """
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation specified"
