# Importing the requests library to make HTTP requests
import requests

# Sending a GET request to the PokeAPI to fetch details of the Pokémon with ID 15
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/15")

# Parsing the JSON response into a Python dictionary
data = response.json()

# Extracting the types of the Pokémon from the data
data_types = data['types']  # 'types' is a key in the API response
types_list = []  # Initializing an empty list to hold the Pokémon types

# Looping through the types and appending the type names to the list
for type_info in data_types:
    types_list.append(type_info['type']['name'])

# Joining the types into a single string, separated by commas
types = ', '.join(types_list)

# Printing the Pokémon's name and its types
print(data['name'], types)

# Example of joining a list of strings into a single string
example_list = ["luciano", "fabio", "bruno"]
unique_list = ', '.join(example_list)  # Joining list elements with commas

# Printing the joined string (corrected variable name)
print(unique_list)