def math_operations(a, b):
    """
    This function takes two numbers as input and returns their sum and product using lambda functions.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    tuple: A tuple containing the sum and the product of the two numbers.
    """
    sum_numbers = (lambda x, y: x + y)(a, b)
    product_numbers = (lambda x, y: x * y)(a, b)
    return sum_numbers, product_numbers

def main():
    # Get user input for the numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Call the math_operations function with the provided numbers
    sum_result, product_result = math_operations(a, b)

    # Print the results
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

# call the main function
main()
