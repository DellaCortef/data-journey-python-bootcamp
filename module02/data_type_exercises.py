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
value9  = input("Please, enter a number: ")
value10 = input("Please, enter another number: ")
total6  = float(value9) + float(value10)
print(total6)

## 7. Create a program that calculates the average of two user-supplied floating numbers.
value11 = input("Please, enter a number: ")
value12 = input("Please, enter another number: ")
total7  = (float(value11) + float(value12)) / 2
print(total7)

## 8. Develop a program that calculates the power of a number (base and exponent provided by the user).
base     = input("Please, enter a base number: ")
exponent = input("Please, enter a exponent number: ")
total8   = float(base) ** float(exponent)
print(total8)

## 9. Write a program that converts the temperature from Celsius to Fahrenheit.
celsius    = input("Please, enter a celsius number: ")
fahrenheit = (float(celsius) * 9 / 5) + 32
print(fahrenheit)

## 10. Write a program that calculates the area of ​​a circle, taking the radius as input.
radius      = input("Please, enter a circle radius: ")
circle_area = float(radius) ** 2 * math.pi
print(f"{circle_area:.2f}")