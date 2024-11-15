# Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções
We will learn Type Hint, Lists and Dictionaries and Functions. These elements are essential for data manipulation, helping to organize, interpret and efficiently analyze information.


## Type Hint
Using Type Hint helps make code more readable and safe by specifying the type of data expected by functions and variables. In data engineering, this is especially useful for ensuring that data manipulation and analysis functions receive data in the correct format, reducing run-time errors.

To demonstrate how to use Type Hints with primitive types in Python, we will create four variables representing the most common types: int for integers, float for floating point numbers, str for strings and bool for Boolean values. Type Hints are used to indicate the type of a variable at the time of its declaration, improving code readability and facilitating error detection.

No Type Hint
```python
age = 30
height = 1.75
name = "Alice"
is_student = True
```

With Type Hint
```python
age: int = 30
height: float = 1.75
name: str = "Alice"
student: bool = True
```

Using Type Hint helps make code more readable and safe by specifying the type of data expected by functions and variables. In data engineering, this is especially useful for ensuring that data manipulation and analysis functions receive data in the correct format, reducing run-time errors.

In Python, function typing is facilitated by the use of "Type Hints", a feature introduced in Python 3.5 through PEP 484. Type Hints allow developers to specify the expected data types for a function's parameters. function and the type of data that the function should return. Although these type hints are not strictly enforced at runtime, they are extremely useful for static code analysis tools, improving code readability and helping with early error detection.


### Weak Typing vs. Strong Typing

* **Strong Typing**: In strongly typed languages, once a variable is assigned a type, it cannot automatically be treated as another type without an explicit conversion. Python is an example of a strongly typed language. This means that operations that mix incompatible types (such as adding a number to a string) will result in an error.
    
* **Weak Typing**: Weakly typed languages ​​allow greater flexibility in operations between different types, making implicit type conversions. JavaScript is a classic example, where you can add numbers to strings without errors, resulting in a text concatenation.
    
### Static vs. Static Typing Dynamics

* **Static Typing**: Statically typed languages, such as Java and C++, require that the type of each variable be declared explicitly at compile time. This helps detect type errors before the program runs, increasing type safety and potentially improving performance.
    
* **Dynamic Typing**: Python is an example of a dynamically typed language, where types are inferred at run time and do not need to be declared explicitly. This offers flexibility and speed in development, but can increase the risk of type errors that will only be detected at run time.


## 2. Lists and Dictionaries - Data structures

### Importance in Data Engineering

Lists and dictionaries are versatile data structures that allow you to efficiently store and manipulate collections of data. In data engineering, these structures are fundamental for organizing data collected from different sources, facilitating operations such as filtering, searching, aggregation and data transformation.


### Lists and Dictionaries Exercises

1. Create a list of numbers 1 to 10 and use a loop to print each number squared.
2. Given the list `["Python", "Java", "C++", "JavaScript"]`, remove the item "C++" and add "Ruby".
3. Create a dictionary to store information about a book, including title, author, and year of publication. Print each information.
4. Write a program that counts the number of occurrences of each character in a string using a dictionary.
5. Given the list `["apple", "banana", "cherry"]` and the dictionary `{"apple": 0.45, "banana": 0.30, "cherry": 0.65}`, calculate the total price of shopping list.


### List Exercises

#### Exercise 01 - List of squared numbers

#### Exercise 02 - Modify language list

#### Exercise 03 - Information from a book

#### Exercise 04 - Count occurrences of characters

#### Exercise 05 - Total price of the shopping list

#### Exercise 06 - Elimination of Duplicates
Objective: Given a list of emails, remove all duplicates.

#### Exercise 07 - Data Filtering
Objective: Given a list of ages, filter only those that are greater than or equal to 18.

#### Exercise 08 - Custom Sorting
Objective: Given a list of dictionaries representing people, order them by name.

#### Exercise 09 - Data Aggregation
Objective: Given a set of numbers, calculate the average.

#### Exercise 10 - Division of Data into Groups
Objective: Given a list of values, divide it into two lists: one for even values ​​and one for odd values.


### Dictionary Exercises

#### Exercises 11 - Data Update
Objective: Given a list of dictionaries representing products, update the price of a specific product.

#### Exercise 12 - Merging Dictionaries
Objective: Given two dictionaries, merge them into a single dictionary.

#### Exercise 13 - Data Filtering in Dictionary
Objective: Given a dictionary of product stock, filter those with quantity greater than 0.

#### Exercise 14 - Extraction of Keys and Values
Objective: Given a dictionary, create separate lists for its keys and values.

#### Exercise 15 - Item Frequency Counting
Objective: Given a string, count the frequency of each character using a dictionary.


## 3.Reading files

To read a CSV file in Python using the native module, you can use the combination of the with open... command to open the file and the .reader() method of the csv module to read the file line by line. Using with ensures that the file will be closed correctly after reading it, even if errors occur during the process. Below is a basic example of how to perform this operation:

```python
import csv

# Path to CSV file
file_path = 'example.csv'

# Initialize an empty list to store the data
data = []

# Use the `with` context manager to open the file
with open(file_path, mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    reader_csv = csv.DictReader(file)
    
    # Iterate over the lines of the CSV file
    for line in reader_csv:
        # Add each row (a dictionary) to the data list
        data.append(line)

# Display data read from CSV file
for record in data:
    print(record)
```

## 4. Functions

### Importance in Data Engineering

Functions allow you to modularize and reuse code, essential for processing and analyzing large sets of data. In data engineering, functions are used to encapsulate data transformation, cleaning, aggregation, and analysis logic, making code more organized and maintaining code quality.

Functions in programming are powerful abstractions that allow you to encapsulate blocks of code to perform specific tasks. They serve not only to organize code and make it more readable, but also to abstract complexities, allowing programmers to think about problems at a higher level. A well-designed function can be viewed as a "mini-program" within a larger program, with its own logic and input and output data.

A classic example of this abstraction is the ordering of a list. Let's first develop a simple function in Python that sorts a list using the selection sort algorithm, a simple but effective method for small and medium-sized lists. We will then show how this task can be accomplished more directly using Python's built-in `sort()` method, which is an abstraction provided by the language to accomplish the same task.

### Custom Sort Function

```python
# Implementation of the selection sort algorithm
list = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

# Ordering the list
print("Ordered list with custom function:", list)
```

### Using the Built-in `sort()` Method

Python provides a powerful abstraction through the `sort()` method, which can sort lists in-place efficiently and with a simple syntax.

```python
# Example list
example_list = [64, 34, 25, 12, 22, 11, 90]

# Sorting the list with sort()
example_list.sort()

print("Ordered list with built-in method:", example_list)
```

The comparison between the custom sort function and the `sort()` method perfectly illustrates how abstractions in programming, such as built-in functions and methods, can significantly simplify software development. While manually implementing a sorting algorithm is a great way to understand computing principles and algorithms, in practice, using abstractions provided by the language can save time and prevent errors by allowing developers to focus on the business logic and aspects high level of its programs.

#### Example: Data Transformation with Functions

Suppose we need to clean and transform usernames in a dataset. A dedicated function can be implemented for this task.

```python
def normalize_name(name: str) -> str:
    return name.strip().lower()

names = ["Alice", "BOB", "Carlos"]
normalized_names = [normalize_name(name) for name in names]
print(normalized_names)
```

Each of these themes plays a crucial role in data engineering, enabling efficient data manipulation, ensuring code quality, and facilitating complex data analysis. These examples illustrate how lists, dictionaries, type hints, and functions can be applied to solve common problems encountered in this field.

### Function Exercises

#### Exercise 16 - 
Write a function that takes a list of numbers and returns the sum of all the numbers.

#### Exercise 17 - 
Create a function that takes a number as an argument and returns `True` if the number is prime and `False` otherwise.

#### Exercise 18 - 
Develop a function that takes a string as an argument and returns this reversed string.

#### Exercise 19 - 
Implement a function that takes two arguments: a list of numbers and a number. The function must return all combinations of pairs in the list that add up to the given number.

#### Exercise20 - 
Write a function that takes a dictionary and returns a list of sorted keys

The function naming pattern in Python follows conventions that are widely accepted by the Python community, as recommended in PEP 8, the style guide for Python coding. Adopting these standards not only improves code readability, but also makes it easier for other developers to understand and maintain, including those new to the project.

### Function Name Patterns

* **Clear and Descriptive Names**: The name of a function must be descriptive enough to indicate its purpose or what it does. For example, `calcular_area_circulo` is more descriptive than simply `area`.
    
* **Lowercase Letters with Underlines**: Functions in Python should be named using lowercase letters, with words separated by underscores to improve readability. This style is sometimes referred to as snake_case. For example, `carr_dados_usuario` is a good example.
    
* **Avoid Generic Names**: Names like `process`, `execute`, or `do_something` are too generic and do not provide enough information about what the function does. Choose names that offer an adequate level of detail.

* **Avoid Obscure Abbreviations**: Although abbreviations can shorten a function name, they can make the code less accessible to other developers. For example, `calc_media_notas` is preferable to `cmn`.
    
* **Prefixes with Verb**: Functions often perform actions, so it is useful to start the function name with a verb that describes that action, such as `get_`, `calculate_`, `process_`, `validate_` or ` clean_`.

In Python, function typing is facilitated by the use of "Type Hints", a feature introduced in Python 3.5 through PEP 484. Type Hints allow developers to specify the expected data types for a function's parameters. function and the type of data that the function should return. Although these type hints are not strictly enforced at runtime, they are extremely useful for static code analysis tools, improving code readability and helping with early error detection.

### Parameter Typing

You can specify the type of each parameter when defining a function. This clearly indicates the type of argument the function expects.

```python
def greeting(name: str, age: int) -> str:
    return f"Hello, {name}, you are {age} years old."
```

### Parameters with Default Values

Python allows you to define default values ​​for parameters, which means that the function can be called without providing all arguments, as long as the omitted ones have a defined default value. Typing works the same way, with the type being specified before the equals sign.

```python
def greeting(name: str, age: int = 30) -> str:
    return f"Hello, {name}, you are {age} years old."
```