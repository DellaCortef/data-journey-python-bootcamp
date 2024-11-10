# exercise 11
all_user_input = " "

while True:
    user_input = input("Please, enter a text taht I will print until you type exit: ")
    if user_input.lower() == "exit":
        print("Exiting... ")
        break
    else:
        all_user_input += user_input + " " # Concatenate input with a space for separation
        print(all_user_input)

print("Concatenated input: ", all_user_input.strip()) # Display the result after exiting

# exercise 12
invalid_numbers = []

while True:
    number_input = int(input("Please, enter a valid number between 1 to 10: "))
    if number_input < 1 or number_input > 10:
        print("Invalid number! Please, enter a valid number between 1 to 10!")
        invalid_numbers.append(number_input)
        print(invalid_numbers)
    else:
        print(f"Nice! Your valid number is {number_input} after {invalid_numbers}!")
        break

# exercise 13
actual_page = 1
total_pages = int(input("Please, enter the number of pages: "))

while actual_page < total_pages:
    print(f"Extracting data from {actual_page} of the {total_pages}!")
    actual_page += 1

print(f"All the pages from {total_pages} were extracted!")

# exercise 14
maximum_attempts = int(input("Please, enter the number of maximum attempts: "))
attempt = 1

while attempt < maximum_attempts:
    print(f"Attempt {attempt} of {maximum_attempts}!")
    # Code to try connect to server
    if True:
        print("Connection successful!")
        break
    attempt += 1
else:
    print(f"Failed to connect to server after {maximum_attempts}")

# exercise 15
itens = input("Please, enter a list of objects separated by comma: ")
itens = [1, 2, 3, "exit", 4, 5]
i = 0

while i < len(itens):
    if itens[i] == "exit":
        print(f"The {itens[i]} command was reached!")
        break
    # Code to process the item
    print(f"Processing item {itens[i]}")
    i += 1

        
