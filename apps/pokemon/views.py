from django.shortcuts import render

from apps.pokemon.models import pokemon


# Create your views here.
def pokemon_list(request):

    # data_context = [
    #     {
    #         'nombre': 'Katty Paredes',
    #         'edad': 16,
    #         'pais': 'Perú',
    #     }
    # ]

    data_context = pokemon.objects.filter(tipo='fuego')

    return render(request, 'pokemon/templates/pokemon/archivopokemon.html', context={'data': data_context})
