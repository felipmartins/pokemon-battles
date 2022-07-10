from django.contrib import admin
from .models import Pokemon, PokemonTeam, CopyPokemon

admin.site.register(Pokemon)
admin.site.register(CopyPokemon)
admin.site.register(PokemonTeam)