import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1, 350) # Generates a random ID between 1 and 350
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f"Adding {pokemon_schema.name} to database.")
            add_pokemon_to_db(pokemon_schema)
        else:
            print(f"Unable to get data for Pokémon with ID {pokemon_id}.")
        time.sleep(10)

if __name__ == "__main__":
    main()