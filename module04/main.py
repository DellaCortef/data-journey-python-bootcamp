# Refactoring the challenge by typing variables (**Type Hint**)

###-----------------------------------------------------------------------###

# Declaring vals
valid_user_name: bool   = False
valid_user_salary: bool = False
valid_user_bonus: bool  = False

# Prompts the user to enter their name
while valid_user_name is not True:
    try:
        user_name: str = input("Please, enter your name: ")

        # Check if there are numbers in the name
        if user_name.isdigit():
            raise ValueError("You type a number! Please, enter a valid name!")
        # Check if the name is empty
        elif len(user_name) == 0:
            raise ValueError("You did not type anything!")
        # Check if there only spaces in the name
        elif user_name.isspace():
            raise ValueError("You did type only spaces in your name!")
        else:
            valid_user_name = True
            print(f"Valid name is {user_name}!")
    except ValueError as e:
        print(e)

# Asks the user to enter their salary amount and converts it to float
while not valid_user_salary:
    try:
        user_salary: float = float(input("Please, enter your salary: "))

        # Check if the salary is negative
        if user_salary < 0:
            raise ValueError("There is no negative salary!")
        else:
            valid_user_salary = True
            print(f"Valid salary is {user_salary}!")
    except ValueError as e:
        print(e)

# Asks the user to enter the bonus amount received and converts it to float
while not valid_user_bonus:
    try: 
        user_bonus: float = float(input("Please, enter your bonus: "))

        # Check if the bonus is negative
        if user_bonus < 0:
            raise ValueError("There is no negative Bonus! Please, enter a valida bonus: ")
        else:
            valid_user_bonus = True
            print(f"Valid bonus is {user_bonus}!")
    except ValueError as e:
        print(e)

# Assuming a calculation logic for the final bonus and KPI
final_bonus: float = user_salary * (1 + user_bonus)
kpi: float = (user_salary + final_bonus) / 1000

# Print information for the user
print(f"Your KPI is: {kpi:.2f}")
print(f"{user_name}, your salary is R${user_salary:.2f} and your final bonus is R${final_bonus:.2f}.")

###-----------------------------------------------------------------------###

# 1. Create a list of numbers 1 to 10 and use a loop to print each number squared.

# 2. Given the list `["Python", "Java", "C++", "JavaScript"]`, remove the item "C++" and add "Ruby".


# 3. Create a dictionary to store information about a book, including title, author, and year of publication. Print each information.
## importing libs
from typing import Dict, Any

## creating our dict
book1_dict: Dict[str, Any] = {
    "Title": "The originals",
    "Autor": "Adam Grant",
    "Year": 2016
}

## creating our dict
book2_dict: Dict[str, Any] = {
    "Title": "Infinity game",
    "Autor": "Simon Sinek",
    "Year": 2023
}

## creating a list to add our dicts
books_list: list = []

## appending our dicts
books_list.append(book1_dict)
books_list.append(book2_dict)

## iterating our list
for i in books_list:
    ## print the dict information
    print(i)


# 4. Write a program that counts the number of occurrences of each character in a string using a dictionary.


# 5. Given the list `["apple", "banana", "cherry"]` and the dictionary `{"apple": 0.45, "banana": 0.30, "cherry": 0.65}`, calculate the total price of shopping list.