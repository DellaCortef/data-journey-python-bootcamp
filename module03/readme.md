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