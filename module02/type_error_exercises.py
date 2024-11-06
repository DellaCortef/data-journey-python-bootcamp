# TypeError
## When we talk about TryExcept and if, we are talking about process flow or 
## user input. We call it integration testing.

# try-except and if exercises

## 21: Temperature Converter
# try:
#     celsius = float(input("Please, enter Celsius Temperature: "))
#     fahrenheit = (float(celsius) * 9 / 5) + 32
#     print(f"{celsius}°C is equal to {fahrenheit}°F.")
# except:
#     print("Inputed data is not a number. Please, enter a valid number!")

## 22: Palindrome Checker
inputed_data = input("Please enter a word so we can test whether it's a palindrome: ")
if isinstance(inputed_data, str):
    print(f"The inputed data {inputed_data} is a word. Let's check!")
    # Convert the word to lowercase to ensure case insensitivity
    formated_data = inputed_data.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    if formated_data == formated_data[::-1]:
        print(f"The word {inputed_data} is a palindrome!")
    else:
        print(f"The word {inputed_data} is not a palindrome! Try again!")
else:
    print(f"The inputed data {inputed_data} is not a word. Try again!")


## 23: Simple Calculator


## 24: Number Sorter


## 25: Type Conversion with Validation