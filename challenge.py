##1. Ask the user to enter their name
user_name = input("Please, enter your name: ")

##2. Ask the user to provide their salary. Convert to float
user_salary = input("Please, enter your currently salary: ")
user_salary = float(user_salary)

##3. Ask the user to inform the amount of the bonus received in percentage. Convert to float
user_bonus = input("Please, enter ypur currently percentage bonus: ")
user_bonus = float(user_bonus)

##4. Calculate the value of the final bonus
total_amount = user_salary * (1 + user_bonus)

##5. Print the KPI value to the end user
print(total_amount)

##6. Print a personalized message with the end user's name, salary and bonus
print(f"Dear {user_name}, your total amount is {total_amount}!")