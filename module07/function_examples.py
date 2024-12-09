# Functions examples
def sum_two_numbers(max_attempts: int = 3) -> float:
    """
    Function to sum two numbers entered by the user with comprehensive validation.
    
    Parameters:
        max_attempts (int): The maximum number of attempts to provide valid inputs.
    
    Returns:
        float: The sum of two valid numbers.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            # Prompt for the first number
            value_1_input = input("Please, enter the first valid number: ").strip()
            if not value_1_input:
                raise ValueError("Input cannot be empty.")
            value_1 = float(value_1_input)
            
            # Prompt for the second number
            value_2_input = input("Please, enter the second valid number: ").strip()
            if not value_2_input:
                raise ValueError("Input cannot be empty.")
            value_2 = float(value_2_input)
            
            # Calculate the sum
            sum_result = value_1 + value_2
            
            # Return the result
            print(f"The sum of {value_1} and {value_2} is: {sum_result}")
            return sum_result
        except ValueError as e:
            print(f"Attempt {attempt}/{max_attempts}: Invalid input. {e}")
        
    # If the user fails after max_attempts
    raise RuntimeError("Maximum attempts reached. Please try again later.")

# Example usage
try:
    result = sum_two_numbers()
    print(f"Final Result: {result}")
except RuntimeError as e:
    print(e)


# Functions examples
def multiply_two_numbers(max_attempts: int = 3) -> float:
    """
    Function to multiply two numbers entered by the user with comprehensive validation.
    
    Parameters:
        max_attempts (int): The maximum number of attempts to provide valid inputs.
    
    Returns:
        float: The multiply of two valid numbers.
    """
    for attempt in range(1, max_attempts + 1):
        try:
            # Prompt for the first number
            value_1_input = input("Please, enter the first valid number: ").strip()
            if not value_1_input:
                raise ValueError("Input cannot be empty.")
            value_1 = float(value_1_input)
            
            # Prompt for the second number
            value_2_input = input("Please, enter the second valid number: ").strip()
            if not value_2_input:
                raise ValueError("Input cannot be empty.")
            value_2 = float(value_2_input)
            
            # Calculate the sum
            sum_result = value_1 * value_2
            
            # Return the result
            print(f"The sum of {value_1} and {value_2} is: {sum_result}")
            return sum_result
        except ValueError as e:
            print(f"Attempt {attempt}/{max_attempts}: Invalid input. {e}")
        
    # If the user fails after max_attempts
    raise RuntimeError("Maximum attempts reached. Please try again later.")

# Example usage
try:
    result = sum_two_numbers()
    print(f"Final Result: {result}")
except RuntimeError as e:
    print(e)
