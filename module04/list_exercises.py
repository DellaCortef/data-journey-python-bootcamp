#### Exercise 06 - Elimination of Duplicates
email_list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

# Convert the list into a set to remove duplicates
# Sets automatically ensure that all elements are unique
email_list_unique = set(email_list)

# Print the unique email addresses
print(email_list_unique)

#### Exercise 07 - Data Filtering
age_list = [22, 15, 30, 17, 18]

# Use a list comprehension to filter ages from the age_list that are 18 or older
major_age = [age for age in age_list if age >= 18]

# Print the list of ages that are 18 or older
print(major_age)

#### Exercise 08 - Custom Sorting
people_dict = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 20}
]

# Sorting the keys of a Dict
people_dict.sort(key=lambda person: person["name"])

# Print the sorted Dict
print(people_dict)

#### Exercise 09 - Data Aggregation
number_list = [10, 20, 30, 40, 50]

# Adding the numbers in the list and dividing by the total number
number_list_mean = sum(number_list) / len(number_list)

# Print the number list mean
print(number_list_mean)

#### Exercise 10 - Division of Data into Groups
val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separating even numbers
even_list = [even for even in val_list if even % 2 == 0]
print(even_list)

# Separating odd numbers
odd_list = [odd for odd in val_list if odd % 2 != 0]
print(odd_list)