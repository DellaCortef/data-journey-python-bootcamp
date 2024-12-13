class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive number.")

# Usage example
person = Person("John", 30)

# Using the getter method to access the 'name' attribute
print("Name:", person.name) # Output: Name: João

# Using the setter method to change the 'name' attribute
person.name = "Mary"
print("New name:", person.name) # Output: New name: Maria

# Using the get method