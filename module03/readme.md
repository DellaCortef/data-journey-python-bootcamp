# debug, if, for, while, lists and dictionaries in Python
We will explore control flow structures such as if, for, and while.
We use Flow Control framework to make decisions!


## Flow Control Structures
We'll explore how to use if to make decisions based on conditions, for to iterate over sequences of data, and while to execute blocks of code while a condition is true.


### Flow Control Structures - if
if is a fundamental conditional structure in Python that evaluates whether a condition is True and, if so, executes a block of code. If the initial condition is not true, you can use elif (else if) to check additional conditions, and else to execute a block of code when none of the previous conditions are true.

Probably the best known flow control command is if. For example:
```python
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```


### Flow Control Structures - FOR

The `for` loop is used to iterate over items in any sequence, such as lists, strings, or dictionary objects, and execute a block of code for each item. It is especially useful when you need to perform an operation for each element in a collection.

The for command in Python is a little different from what it usually is in C or Pascal. Instead of always iterating over an arithmetic progression of numbers (like Pascal), or allowing the user to define the iteration step and stopping condition (like C), Python's for command iterates over the items in any sequence (whether a list or a string), in the order they appear in the sequence. For example:

```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

```python
# Measure some strings:
name = ['Luciano']
for letter in name:
    print(letter)
```

If you need to iterate over numerical sequences, the built-in `range()` function is the answer. It generates arithmetic progressions:


```python
for i in range(5):
    print(i)
```

The given waypoint is never included in the list; range(10) generates a list with 10 values, exactly the valid indices for a sequence of length 10. It is possible to start the range with another number, or change the progression ratio (including with a negative step):


```python
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

To iterate over the indices of a sequence, combine range() and len() as follows:

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```


### Flow Control Structures - WHILE

The while loop is a fundamental flow control structure in Python, allowing you to execute a block of code repeatedly while a specified condition evaluates to True. In data engineering, the use of while can be extremely useful for several tasks, such as continuous monitoring of data sources, executing ETL (Extract, Transform, Load) processes until there is no more data to process, or even implementing automatic reconnection attempts to services or databases when the first attempt fails.

#### Example of Using while in Data Engineering
A common scenario in data engineering is the need to perform a task on a periodic basis, such as checking a directory for new data, polling an API for new responses, or monitoring changes to a database. In these cases, a while loop can be used to keep the script running continuously or until a specific condition is met (for example, a shutdown signal or an error condition).

#### Practical Example: while True with Pause

A direct example of using while True in Python is to create an infinite loop that performs an action at every defined interval, such as printing a message every 10 seconds. This can be useful for monitoring processes or data in real time with a periodic check.

```python
import time

whileTrue:
    print("Checking new data...")
    # Here you can add code to check new data,
    # for example, checking the existence of new files in a directory,
    # make a query to a database or API, etc.
    
    time.sleep(10) # Pause the loop for 10 seconds
```
In this example, while True creates an infinite loop, which is a powerful way to keep a script running continuously. The print simulates the action of checking for new data, and the time.sleep(10) pauses the loop execution for 10 seconds before the next iteration. This approach is simple but effective for many monitoring and polling scenarios in data engineering, allowing the script to perform a check or task on a periodic basis.

However, it is important to use infinite loops with caution to avoid creating conditions where the script may consume unnecessary resources or become difficult to terminate in a controlled manner. In production environments, other approaches such as job scheduling (for example, using cron jobs on Unix systems) or the use of message queuing systems and database triggers may be better suited for some of these tasks.

---

#### if exercises
##### Exercise 1: Data Quality Check

You are analyzing a set of sales data and need to ensure that all records have positive values ​​for quantity and price. Write a program that checks these fields and prints "Valid data" if both are positive or "Invalid data" otherwise.

##### Exercise 2: Sensor Data Classification

Imagine you are working with data from IoT sensors. Data includes temperature ratio. You need to classify each reading as 'Low', 'Normal' or 'High'. Considering that:

Temperature < 18°C ​​is 'Low'
Temperature >= 18°C ​​and <= 26°C is 'Normal'
Temperature > 26°C is 'High'

##### Exercise 3: Filtering Logs by Severity

You are analyzing application logs and need to filter messages with severity 'ERROR'. Given a log record in dictionary format like log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'}, write a program that prints the message if the severity is 'ERROR'.

##### Exercise 4: Input Data Validation

Before processing user data in a recommendation system, you need to ensure that each user is between the ages of 18 and 65 and has provided a valid email address. Write a program that validates these conditions and prints "Valid User Data" or the specific error encountered.

##### Exercise 5: Anomaly Detection in Transaction Data

You are working on a fraud detection system and need to identify suspicious transactions. A transaction is considered suspicious if the value exceeds R$10,000 or if it occurs outside business hours (before 9am or after 6pm). Given a transaction like transaction = {'value': 12000, 'time': 20}, check if it is suspicious.


#### for exercises
##### Exercise 6: Word Count in Texts

Objective: Given a text, count how many times each single word appears in it.

##### Exercise 7: Data Normalization

Objective: Normalize a list of numbers so that they are on a scale of 0 to 1.

##### Exercise 8: Missing Data Filtering

Objective: Given a list of dictionaries representing user data, filter out those that have a specific field missing.

##### Exercise 9: Extracting Subsets of Data

Objective: Given a list of numbers, extract only those that are even.

##### Exercise 10: Data Aggregation by Category

Objective: Given a set of sales records, calculate total sales by category.


#### while exercises
##### Exercise 11: Data Reading until Flag

Purpose: Read input data until a specific keyword ("exit") is provided.

##### Exercise 12: Input Validation

Purpose: Prompt the user for a number within a specific range until the input is valid.

##### Exercise 13: Simulated API Consumption

Objective: Simulate the consumption of a paged API, where each "page" of data is processed in a loop until there are no more pages.

##### Exercise 14: Connection Attempts

Objective: Simulate reconnection attempts to a service with a maximum attempt limit.

##### Exercise 15: Data Processing with Stop Condition

Objective: Process items in a list until finding a specific value that indicates the stop.