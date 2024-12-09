#### Exercise 16 - Sum of list of numbers
def sum_of_numbers_in_list(numbers):
    """
    Returns the sum of all numbers in a list.

    :param numbers: List of numbers (int or float)
    :return: Sum of all numbers in the list
    """
    return sum(numbers)

try:
    # Request input and parse it into a list
    user_input = input("Please, enter a list of numbers (separated by spaces): ")
    if not user_input.strip():
        raise ValueError("The input list is empty.")

    # Filter valid numbers from the input
    list_number = []
    for num in user_input.split():
        try:
            list_number.append(float(num))
        except ValueError:
            print(f"Skipping invalid input: {num}")

    if not list_number:
        raise ValueError("No valid numbers were entered.")

    # Call the function and print the result
    result = sum_of_numbers_in_list(list_number)
    print(f"The result of the sum of the list is {result}!")

except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#### Exercise 17 - Prime numbers
def is_prime(number):
    """
    Determines if a given number is prime.

    :param number: Integer to check for primality
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to sqrt(number)
        if number % i == 0:
            return False  # Not a prime number if divisible
    return True  # Prime if no divisors are found

try:
    def main():
        """
        Main function to handle user input and check if the number is prime.
        """
        # Request user input
        user_input = input("Please, enter a number: ")
        if not user_input.strip():  # Check for empty input
            raise ValueError("The input is empty. Please provide a valid number.")
        
        # Convert input to integer
        num = int(user_input)
        
        # Check if the number is prime
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

except ValueError as e:
    print(f"Invalid input: {e}")

# Run the program
if __name__ == "__main__":
    main() 

#### Exercise 18 - Reversed string
def reverse_sentence(sentence):
    """
    Reverses the order of words in a sentence.

    :param sentence: Input sentence (string)
    :return: Reversed sentence (string)
    """
    
    # Check if the input is not a string
    if not isinstance(sentence, str):  
        return "Error: Input is not a string."
    
    # Check if the input is a numeric string
    if sentence.strip().isdigit():  
        return "Error: Input is a number, not a sentence."

    # Split the sentence into words
    words = sentence.split()  

    # Reverse the list of words
    reversed_words = words[::-1]  

    # Join the reversed words into a sentence
    return " ".join(reversed_words)  

try:
    def main():
        """
        Main function to handle user input and reverse the order of words.
        """
        # Request user input
        user_input = input("Please, enter a sentence: ")
        
        # Reverse the sentence
        reversed_sentence = reverse_sentence(user_input)

        # Print the result
        print(f"The reversed sentence is: {reversed_sentence}!")

except ValueError as e:
    print(f"Invalid input: {e}")

# Run the program
if __name__ == "__main__":
    main() 

#### Exercise 19 - Pair combination
def pair_combination(numbers_list, target_sum):
    """
    Finds all pairs of numbers in the list that add up to the target sum.

    :param numbers: List of integers
    :param target_sum: Target sum (integer)
    :return: List of tuples containing pairs of numbers
    """
    pairs = []
    # To track numbers we've already seen
    seen = set()
    
    # Debugging
    print(f"Input list: {numbers}")
    # Debugging
    print(f"Target sum: {target_sum}")

    for number in numbers:
        # Calculate the required complement
        complement = target_sum - number
        # Debugging
        print(f"Checking number: {number}, Complement needed: {complement}")
        
        # Check if the complement exists in the seen set
        if complement in seen:
            # Add the pair
            pairs.append((complement, number))
            # Debugging
            print(f"Pair found: ({complement}, {number})")
        
        # Add the current number to the seen set
        seen.add(number)
    
    # Debugging
    print(f"Seen set: {seen}")
    return pairs

# Example usage
if __name__ == "__main__":
    # Replace with your actual input
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_sum = int(input("Enter the target sum: "))
    pairs = pair_combination(numbers, target_sum)
    if pairs:
        print(f"Pairs that sum to {target_sum}: {pairs}")
    else:
        print(f"No pairs found that sum to {target_sum}.")

#### Exercise20 - Sorted dict
def get_ordered_keys(input_dict):
    """
    Returns an ordered list of keys from the input dictionary.

    :param input_dict: Dictionary to extract and order keys
    :return: List of ordered keys
    """
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary.")
    
    return sorted(input_dict.keys())  # Sort the keys in ascending order

# Example dictionary
example_dict_1 = {"banana": 3, "apple": 5, "cherry": 2}
example_dict_2 = {3: "banana", 5: "apple", 2: "cherry"}

# Get ordered keys
ordered_keys = get_ordered_keys(example_dict_2)
print(ordered_keys)  # Output: ['apple', 'banana', 'cherry']
