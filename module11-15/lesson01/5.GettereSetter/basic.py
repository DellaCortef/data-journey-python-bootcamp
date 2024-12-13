class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for attribute 'name'
    def get_name(self):
        return self._name

    # Setter for the 'name' attribute
    def set_name(self, new_name):
        self._name = new_name

    # Getter for attribute 'age'
    def get_age(self):
        return self._age

    # Setter for the 'age' attribute
    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive number.")

# Usage example
person = Person("John", 30)

# Using the getter method to access the 'name' attribute
print("Name:", person.get_name()) # Output: Name: João

# Using the setter method to change the 'name' attribute
person.set_name("Mary")
print("New name:", person.get_name()) # Output: New name: Maria

# Using the getter method to access the 'age' attribute
print("Age:", person.get_age()) # Output: Age: 30

# Using the setter method to change the 'age' attribute
person.set_age(25)
print("New age:", person.get_age()) # Output: New age: 25

# Trying to set a negative age
person.set_age(-5) # Output: Age must be a positive number.