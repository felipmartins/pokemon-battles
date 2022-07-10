from csv import DictReader
from pokemon.models import Pokemon


def get_pokemons(path):
    with open(path) as file:
        pokemon_list =  list(DictReader(file, delimiter=';'))
    return pokemon_list

def populate():
    pokemon_list = get_pokemons('Pokemon.csv')
    for each_pokemon in pokemon_list:
        pokemon = Pokemon(name=each_pokemon['Name'],
                           type_1=each_pokemon['Type 1'],
                           type_2=each_pokemon['Type 2'],
                           total=each_pokemon['Total'],
                           hp=each_pokemon['HP'],
                           atk=each_pokemon['Attack'],
                           defense=each_pokemon['Defense'],
                           sp_atk=each_pokemon['Sp. Def'],
                           sp_def=each_pokemon['Sp. Atk'],
                           speed=each_pokemon['Speed'] )
        pokemon.save()
    return f'Banco populado com {len(pokemon_list)} pokemons'

populate()