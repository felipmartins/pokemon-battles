def serializa_objeto(pokemon):
    return {'name': pokemon.name,
            'type_1': pokemon.type_1,
            'type_2': pokemon.type_2,
            'hp': pokemon.hp,
            'atk': pokemon.atk,
            'defense': pokemon.defense,
            'sp_atk': pokemon.sp_atk,
            'sp_def': pokemon.sp_def,
            'speed': pokemon.speed
    }