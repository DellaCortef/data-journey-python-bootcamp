# importing libs
import math

# Integers (`int`)

# ## 1. Write a program that adds two integers entered by the user.
# value1 = input("Please, enter a integer number: ")
# value2 = input("Please, enter another integer number: ")
# total1 = int(value1) + int(value2)
# print(total1)

# ## 2. Create a program that receives a number from the user and calculates the remainder of dividing that number by 5.
# value3 = input("Please, enter a integer number: ")
# total2 = int(value3) % 5
# print(total2)

# ## 3. Develop a program that multiplies two numbers provided by the user and displays the result.
# value4 = input("Please, enter a integer number: ")
# value5 = input("Please, enter another integer number: ")
# total3 = int(value4) * int(value5)
# print(total3)

# ## 4. Write a program that asks for two integers and prints the integer division of the first by the second.
# value6 = input("Please, enter a integer number: ")
# value7 = input("Please, enter aanother integer number: ")
# total4 = int(value6) / int(value7)
# print(total4)

# ## 5. Write a program that calculates the square of a user-supplied number.
# value8 = input("Please, enter a integer number: ")
# total5 = int(value8) ** 2
# print(total5)

# Floating Point Numbers (`float`)

## 6. Write a program that receives two floating numbers and adds them.
# value9  = input("Please, enter a number: ")
# value10 = input("Please, enter another number: ")
# total6  = float(value9) + float(value10)
# print(total6)

# ## 7. Create a program that calculates the average of two user-supplied floating numbers.
# value11 = input("Please, enter a number: ")
# value12 = input("Please, enter another number: ")
# total7  = (float(value11) + float(value12)) / 2
# print(total7)

# ## 8. Develop a program that calculates the power of a number (base and exponent provided by the user).
# base     = input("Please, enter a base number: ")
# exponent = input("Please, enter a exponent number: ")
# total8   = float(base) ** float(exponent)
# print(total8)

# ## 9. Write a program that converts the temperature from Celsius to Fahrenheit.
# celsius    = input("Please, enter a celsius number: ")
# fahrenheit = (float(celsius) * 9 / 5) + 32
# print(fahrenheit)

# ## 10. Write a program that calculates the area of ​​a circle, taking the radius as input.
# radius      = input("Please, enter a circle radius: ")
# circle_area = float(radius) ** 2 * math.pi
# print(f"{circle_area:.2f}")


# Strings (`str`)

## 11. Write a program that takes a string from the user and converts it to uppercase.
# user_string      = input("Please, enter a string: ")
# uppercase_string = user_string.upper()
# print(uppercase_string) 


## 12. Create a program that takes the user's full name and prints the name in all lowercase letters.
# user_name      = input("Please, enter your full name: ")
# lowercase_name = user_name.lower()
# print(lowercase_name)

## 13. Develop a program that asks the user to enter a sentence and then prints this sentence without blanks at the beginning and end.
# user_sentence           = input("Please, enter a sentende: ")
# sentence_without_blanks = user_sentence.strip()
# print(sentence_without_blanks)

## 14. Make a program that asks the user to enter a date in the format "dd/mm/yyyy" and then prints the day, month and year separately.
# user_date        = input("Please, enter a date in the format dd/mm/yyyy: ")
# user_date_list   = user_date.split("/") # split the string into a list
# user_date_day    = user_date_list[0]
# user_date_month  = user_date_list[1]
# user_date_year   = user_date_list[2]
# print(f"Day:   {user_date_day} \nMonth: {user_date_month} \nYear:  {user_date_year}")

## 15. Write a program that concatenates two user-supplied strings.
# string1             = input("Please, enter a string: ")
# string2             = input("Please, enter another string: ")
# string_concatenated = string1 + string2
# print(string_concatenated)


# Booleans (`bool`)

## 16. Write a program that evaluates two Boolean expressions entered by the user and returns the result of the AND operation between them.
# boolean1               = input("Please, enter bool value: ")
# boolean2               = input("Please, enter bool value: ")
# boolean_and_comparison = bool(boolean1) and bool(boolean2)
# print(boolean_and_comparison)

## 17. Create a program that receives two Boolean values ​​from the user and returns the result of the OR operation.
# boolean1              = input("Please, enter bool value: ")
# boolean2              = input("Please, enter bool value: ")
# boolean_or_comparison = bool(boolean1) and bool(boolean2)
# print(boolean_or_comparison)

## 18. Develop a program that asks the user to enter a Boolean value and then inverts that value.
# boolean = True
# boolean = False
# boolean_inverted = not boolean
# print(boolean_inverted)

## 19. Make a program that compares whether two user-supplied numbers are equal.


## 20. Write a program that checks whether two user-supplied numbers are different.


# try-except and if

## 21: Temperature Converter


## 22: Palindrome Checker


## 23: Simple Calculator


## 24: Number Sorter


## 25: Type Conversion with Validation