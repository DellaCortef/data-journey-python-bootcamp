# Importing necessary libraries
import requests
from pydantic import BaseModel

# Defining the schema for Pokémon data using Pydantic
class PokemonSchema(BaseModel):
    name: int
    type: str

    # Configuration for the Pydantic model
    class Config:
        orm_mode = True

# Defining a function to fetch Pokémon data from the PokeAPI
def catch_pokemon(id: int) -> PokemonSchema:
    # Sending a GET request to the PokeAPI to fetch Pokémon details by ID
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()

    # Debugging: Print the full data to understand its structure
    print(data)

    # Extracting the Pokémon's types from the API response
    data_types = data['types']
    types_list = []

    # Looping through the types to extract and store their names
    for type_info in data_types:
        types_list.append(type_info['type']['name'])

    # Joining the types into a single string, separated by commas
    types = ', '.join(types_list)

    # Returning a validated instance of PokemonSchema with the Pokémon's name and types
    return PokemonSchema(name=data['name'], type=types)

# Using the function to fetch data for a Pokémon with ID 24 (Arbok, for example)
pokemon = catch_pokemon(24)

# Printing the structured Pokémon data
print(pokemon)
