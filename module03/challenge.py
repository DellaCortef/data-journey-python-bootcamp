#0. Using Loop conditions to do the challenge

#1. Ask the user to enter their name

#2. Ask the user to provide their salary. Convert to float

#3. Ask the user to inform the amount of the bonus received in percentage. Convert to float

#4. Calculate the value of the final bonus

#5. Print the KPI value to the end user

###-----------------------------------------------------------------------###

# Declaring vals
valid_user_name   = False
valid_user_salary = False
valid_user_bonus  = False

# Prompts the user to enter their name
while valid_user_name is not True:
    try:
        user_name = input("Please, enter your name: ")

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
        user_salary = float(input("Please, enter your salary: "))

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
        user_bonus = float(input("Please, enter your bonus: "))

        # Check if the bonus is negative
        if user_bonus < 0:
            raise ValueError("There is no negative Bonus! Please, enter a valida bonus: ")
        else:
            valid_user_bonus = True
            print(f"Valid bonus is {user_bonus}!")
    except ValueError as e:
        print(e)

# Assuming a calculation logic for the final bonus and KPI
final_bonus = user_salary * (1 + user_bonus)
kpi = (user_salary + final_bonus) / 1000

# Print information for the user
print(f"Your KPI is: {kpi:.2f}")
print(f"{user_name}, your salary is R${user_salary:.2f} and your final bonus is R${final_bonus:.2f}.")