# Importing necessary libs and modules
import requests
from database import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema

# Create all database tables defined in the ORM models if they don't already exist
Base.metadata.create_all(bind=engine)

# Function to fetch Pokémon data from the external API
def fetch_pokemon_data(pokemon_id: int):
    """
    Fetches Pokémon data from the PokeAPI for a given Pokémon ID.

    Parameters:
    pokemon_id (int): The ID of the Pokémon to fetch.

    Returns:
    PokemonSchema: A schema object containing the Pokémon's name and types, or None if not found.
    """
    # Send a GET request to the PokeAPI with the given Pokémon ID
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    print(response)

    # Check if the response was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Extract Pokémon types and format them as a comma-separated string
        types = ', '.join(type['type']['name'] for type in data['types'])
        # Return the Pokémon data wrapped in a Pydantic schema
        return PokemonSchema(name=data['name'], type=types)
    else:
        # Return None if the Pokémon data couldn't be fetched (e.g., invalid ID or API error)
        return None

# Function to add a Pokémon to the database
def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    """
    Adds a Pokémon to the database using the provided schema.

    Parameters:
    pokemon_schema (PokemonSchema): A schema object containing the Pokémon's name and types.

    Returns:
    Pokemon: The newly added Pokémon record from the database.
    """
    # Use a database session to interact with the database
    with SessionLocal() as db:
        # Create a new Pokémon object from the schema
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    # Return the added Pokémon object
    return db_pokemon
