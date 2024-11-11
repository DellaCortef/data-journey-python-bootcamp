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