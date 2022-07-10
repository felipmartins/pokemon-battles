from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, blank=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    atk = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name

class CopyPokemon(models.Model):
    name = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, blank=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    atk = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()

    def __str__(self):
        return self.name

class PokemonTeam(models.Model):
    pokemon_trainer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    pokemon_1 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='first')
    pokemon_2 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='second')
    pokemon_3 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='third')
    pokemon_4 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='fourth')
    pokemon_5 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='fifth')
    pokemon_6 = models.ForeignKey(CopyPokemon, on_delete=models.SET_NULL, null=True, blank=True, related_name='sixth')

    def __str__(self):
        return str(self.pokemon_trainer) + ' - ' + self.pokemon_1.name + ' - ' + self.pokemon_2.name + ' - ' + self.pokemon_3.name + ' - ' + self.pokemon_4.name + ' - ' + self.pokemon_5.name + ' - ' + self.pokemon_6.name