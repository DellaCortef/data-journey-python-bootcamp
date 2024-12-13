## In Python, method overloading is not directly supported like in some other programming languages, 
## but you can simulate overloading using default parameters or variable arguments.


class Calculator:
    def sum(self, *args):
        total = 0
        for num in args:
            total += num
        return total

# Usage example
calculator = Calculator()
print(calculator.sum(1, 2)) # Output: 3
print(calculator.sum(1, 2, 3, 4)) # Output: 10
print(calculator.sum(5, 10, 15)) # Output: 30