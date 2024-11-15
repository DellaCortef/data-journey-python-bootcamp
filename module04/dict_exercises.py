#### Exercises 11 - Data Update
products = [
    {"id": 1, "name": "Teclado", "price": 100},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 300}
]

# Iterate through the list of products
for product in products:
    # Check if the product's ID is equal to 2
    if product["id"] == 2:
        # Update the price of the product to 90
        product["price"] = 90

# Print the updated list of products
print(products)

#### Exercise 12 - Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# # update() method
dict1.update(dict2)
print(dict1)

# unpacking operator
dict3 = {**dict1, **dict2}
print(dict3)

# merge Dictionaries using |
dict4 = dict1 | dict2
print(dict4)

# loop and keys() method
def merge_dict(d1, d2):
    for i in d2.keys():
        d1[i]=d2[i]
    return d1

dict5 = merge_dict(dict1, dict2)
print(dict5)

# dict constructor
dict6 = dict1.copy()
dict6.update(dict2)
print(dict6)

#### Exercise 13 - Data Filtering in Dictionary
stock_count = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# Use a dictionary comprehension to filter products with a stock quantity greater than 0
filtered_stock_count = {product: quantity for product, quantity in stock_count.items() if quantity > 0}

# Print the dictionary containing only products with a stock quantity greater than 0
print(filtered_stock_count)

#### Exercise 14 - Extraction of Keys and Values
dictionary = {"a": 1, "b": 2, "c": 3}

# Separating keys from dict
keys_dict = list(dictionary.keys())

# Separating values from dict
values_dict = list(dictionary.values())

print(f"Keys: {keys_dict}\nValues: {values_dict}")

#### Exercise 15 - Item Frequency Counting
def count_character_occurrences(input_string):
    # Initialize an empty dictionary
    char_count = {}
    
    # Loop through each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # Otherwise, add it to the dictionary with a count of 1
            char_count[char] = 1
            
    return char_count

input_string = input("Please, enter a setence: ")
result = count_character_occurrences(input_string)
print(f"The number of occurrences: {result}")