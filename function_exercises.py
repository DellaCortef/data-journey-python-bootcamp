# #### Exercise 16 - Sum of list of numbers
# def sum_of_numbers_in_list(numbers):
#     """
#     Returns the sum of all numbers in a list.

#     :param numbers: List of numbers (int or float)
#     :return: Sum of all numbers in the list
#     """
#     return sum(numbers)

# try:
#     # Request input and parse it into a list
#     user_input = input("Please, enter a list of numbers (separated by spaces): ")
#     if not user_input.strip():
#         raise ValueError("The input list is empty.")

#     # Filter valid numbers from the input
#     list_number = []
#     for num in user_input.split():
#         try:
#             list_number.append(float(num))
#         except ValueError:
#             print(f"Skipping invalid input: {num}")

#     if not list_number:
#         raise ValueError("No valid numbers were entered.")

#     # Call the function and print the result
#     result = sum_of_numbers_in_list(list_number)
#     print(f"The result of the sum of the list is {result}!")

# except ValueError as e:
#     print(f"Invalid input: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

#### Exercise 17 - Prime numbers


#### Exercise 18 - Reversed string


#### Exercise 19 - Pair combination


#### Exercise20 - Sorted dict
