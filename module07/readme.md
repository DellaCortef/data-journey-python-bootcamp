# Class 07: Python Functions and Data Structures - Part 1

Functions in Python are one of the fundamental structures of the language, allowing code reuse, organization and modularity of programs. This guide covers everything from motivation to the practical application of functions, including keywords, names, and how to use them effectively.

## Content

### Motivation

The main motivation for using functions in Python is **code reuse**. Functions allow you to write a block of code once and execute it multiple times, possibly with different arguments, to produce different results. This helps make the code more **readable**, **modular**, and **easy to debug**.

### Defining Functions

To create a function in Python, you use the keyword `def`, followed by a function name, parentheses `()` containing zero or more "parameters", and a colon `:`. The indented block of code that follows is the body of the function.

```python
def my_function():
    return "Hello, World!"
```

### Function Names

Function names follow the same rules as variable names in Python: they can contain letters, numbers (not as the first character) and underscores (`_`), but not spaces or special characters. Function names must be descriptive and, by convention, use `snake_case`.

### Parameters and Arguments

* **Parameters** are the variables listed in parentheses in the function definition. They are like placeholders for the data that the function will process.
    
* **Arguments** are the actual values ​​passed to the function when it is called.
    

```python
def sum(a, b):
    return a + b
```

### Important keywords

* `def` starts defining a function.
* `return` is used to return a value from the function. If omitted, the function returns `None` by default.
* `pass` can be used as a placeholder for an empty function, meaning "nothing".

### Calling Functions

To call a function, use the function name followed by parentheses containing the required arguments.

```python
result = sum(5, 3)
print(result) # Output: 8
```

### Default Values ​​and Named Arguments

Functions can have parameters with default values, allowing them to be called with fewer arguments.

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
```

You can also call functions with named arguments for clarity.

```python
greet(message="Welcome", name="John")
```

## Exercises

Let's review functions by adding type hints and Pydantic

1. **Calculate Average Values ​​in a List**

```python
from typing import List

def calculate_media(values: List[float]) -> float:
    return sum(values) / len(values)
```

2. **Filter Data Above a Threshold**

```python
def filter_above_(values: List[float], limit: float) -> List[float]:
    result = []
    for value in values:
        if value > limit:
            result.append(value)
    return results
```

3. **Count Unique Values ​​in a List**

```python
def count_unique_values(list: List[int]) -> int:
    return len(set(list))
```

4. **Convert Celsius to Fahrenheit in a List**

```python
def celsius_para_fahrenheit(temperatures_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperatures_celsius]
```

5. **Calculate Standard Deviation from a List**

```python
def calculate_standard_deviation(values: List[float]) -> float:
    average = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5
```

6. **Find Missing Values ​​in a Sequence**

```python
def find_missing_values(sequence: List[int]) -> List[int]:
    complete = set(range(min(sequence), max(sequence) + 1))
    return list(complete - set(sequence))
```

## Challenge

Challenge: Product Sales Analysis
Objective: Given a CSV file containing product sales data, the challenge is to read the data, process it into a dictionary for analysis, and finally calculate and report total sales by product category.

**Flow**:

```mermaid
TD graph;
    A[Home] --> B{Read CSV};
    B --> C[Process Data];
    C --> D[Calculate Sales];
    D --> E[Display Results];
    E --> F[End];
```

**Tasks**:

1. Read the CSV file and load the data.
2. Process the data into a dictionary, where the key is the category, and the value is a list of dictionaries, each containing product information (`Product`, `Quantity`, `Sale`).
3. Calculate total sales (`Quantity` * `Sale`) by category.

### Functions

1. **Read CSV**:
    
    * Function: `ler_csv`
    * Input: CSV file name
    * Output: List of dictionaries with read data

2. **Process Data**:
    
    * Function: `process_data`
    * Input: List of dictionaries
    * Output: Dictionary processed as described
    
3. **Calculate Sales by Category**:
    
    * Function: `calculate_sales_category`
    * Input: Processed dictionary
    * Output: Dictionary with total sales by category