# exercise 01
sales_quantity = float(input("Please, enter a number os sales quantity: "))
sales_price    = float(input("Please, enter a number os sales price: "))

# checking the values
if sales_price > 0 and sales_quantity > 0:
    print("Awesome! Both are positives!")
elif sales_quantity < 0 and sales_price > 0:
    print("Not bad! You need to improve your sales quantity!")
elif sales_quantity > 0 and sales_price < 0:
    print("Not bad! You need to improve your sales price!")
else:
    print("Not good! Both are negatives!")

# exercise 02
temperature = float(input("Please, enter the current temperature: "))

# checking the temperature range
if temperature < 18:
    print("Current temperature is low!")
elif temperature >= 18 and temperature <= 26:
    print("Nice! The temperature is normal!")
else:
    print("Wow! The temperature is too high!")

# exercise 03
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# Checking the severity of the error
if log["level"] == "ERROR":
    print(log['message'])

# exercise 04
user_age   = int(input("Please, enter your age: "))
user_email =     input("Please, enter your email: ")

# Checking the age and email conditions
if 18 <= user_age <= 65 and "@hotmail.com" in user_email:
    print("Good! Both conditions were met!")
elif 18 <= user_age <= 65 and "@gmail.com" in user_email:
    print("Good! Both conditions were met!")
elif 18 <= user_age <= 65 and "@outlook.com" in user_email:
    print("Good! Both conditions were met!")
elif 18 <= user_age <= 65 and "@hotmail.com" not in user_email:
    print("Not bad! Your email were not met the conditions!")
elif 18 <= user_age <= 65 and "@gmail.com" not in user_email:
    print("Not bad! Your email were not met the conditions!")
elif 18 <= user_age <= 65 and "@outlook.com" not in user_email:
    print("Not bad! Your email were not met the conditions!")
elif user_age < 18 or user_age > 65 and "@hotmail.com" in user_email:
    print("Not bad! Your age were not met the conditions!")
elif user_age < 18 or user_age > 65 and "@gmail.com" in user_email:
    print("Not bad! Your age were not met the conditions!")
elif user_age < 18 or user_age > 65 and "@outlook.com" in user_email:
    print("Not bad! Your age were not met the conditions!")

# exercise 05
money_transaction = {'value': 12000, 'time': 20}

# Checking if there is fraud
if money_transaction['value'] > 10000 or (money_transaction['time'] < 9 or money_transaction['time'] > 18):
    print("Sorry, but this transaction seems to be a fraud!")
else:
    print("Transaction approved!")