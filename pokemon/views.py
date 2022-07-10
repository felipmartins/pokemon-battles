from random import choices
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pokemon, PokemonTeam, CopyPokemon
from .serializers import serializa_objeto
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def random_pokemon_team_generator(request):
    pokemons = choices(Pokemon.objects.all(),k=6)
    serialized = {
        'first':serializa_objeto(pokemons[0]),
        'second':serializa_objeto(pokemons[1]),
        'third':serializa_objeto(pokemons[2]),
        'fourth':serializa_objeto(pokemons[3]),
        'fifth':serializa_objeto(pokemons[4]),
        'sixth':serializa_objeto(pokemons[5]),
    }
    return JsonResponse(serialized)


@login_required
def index(request):
    if len(PokemonTeam.objects.all().filter(pokemon_trainer=request.user.id)) > 0:

        context = {'poke_team': PokemonTeam.objects.all().filter(pokemon_trainer=request.user.id)[0] }

        return render(request, 'index_has_team.html', context)
    else:

        context = {'user': get_object_or_404(User, id=request.user.id)}

        return render(request, 'index_has_not_team.html', context)

def generate_pokemon_team(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    choices_pokemons = choices(Pokemon.objects.all(),k=6)
    pokemons = []

    for each_pokemon in choices_pokemons:
        pokemon = CopyPokemon(name=each_pokemon.name,
                           type_1=each_pokemon.type_1,
                           type_2=each_pokemon.type_2,
                           total=each_pokemon.total,
                           hp=each_pokemon.hp,
                           atk=each_pokemon.atk,
                           defense=each_pokemon.defense,
                           sp_atk=each_pokemon.sp_atk,
                           sp_def=each_pokemon.sp_def,
                           speed=each_pokemon.speed)
        pokemon.save()
        pokemons.append(pokemon)
        

    poke_team = PokemonTeam(pokemon_trainer=user,
                        pokemon_1=pokemons[0],
                        pokemon_2=pokemons[1],
                        pokemon_3=pokemons[2],
                        pokemon_4=pokemons[3],
                        pokemon_5=pokemons[4],
                        pokemon_6=pokemons[5],
    )

    poke_team.save()

    return redirect('home')


def delete_pokemon_team(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    poke_team = get_object_or_404( PokemonTeam, pokemon_trainer=user)
    poke_team.pokemon_1.delete()
    poke_team.pokemon_2.delete()
    poke_team.pokemon_3.delete()
    poke_team.pokemon_4.delete()
    poke_team.pokemon_5.delete()
    poke_team.pokemon_6.delete()
    poke_team.delete()

    return redirect('home')

def new_user(request):

    form = UserForm(request.POST)
    if form.is_valid():
        new_user = User.objects.create_user(request.POST['username'], 
                                            request.POST['email'],
                                            request.POST['password'],
                                            first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'])
        new_user.save()
        return redirect("home")