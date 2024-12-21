# Importing necessary libraries
import json
import requests
from pydantic import BaseModel

# Defining the schema for Pokémon data using Pydantic
class PokemonSchema(BaseModel):
    name: int
    type: str

    # Configuration for the Pydantic model
    class Config:
        orm_mode = True

# Function to fetch Pokémon data from the PokeAPI and save it to a JSON file
def pega_pokemon(id: int) -> PokemonSchema:
    # Sending a GET request to the PokeAPI to fetch Pokémon details by ID
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()

    # Saving the entire Pokémon data to a local JSON file named after the Pokémon
    with open(f"{data['name']}.json", 'w') as f:
        json.dump(data, f)

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
pokemon = pega_pokemon(24)

# Printing the structured Pokémon data
print(pokemon)
