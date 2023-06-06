from typing import Any

from django.db.models import Q
from django.shortcuts import render
from owner.forms import OwnerForm
#crear mi vista se necesita importar el modelo

from owner.models import Owner




# Create your views here.
def owner_list(request):

    data_context = [
        {
            'nombre': 'Katty Paredes',
            'edad': 16,
            'dni': 88842232,
            'pais': 'Perú',
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Miguel Valera',
            'edad': 26,
            'dni': 43452345,
            'pais': 'España',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Jesús de la Cruz',
            'edad': 30,
            'dni': 88842232,
            'pais': 'Colombia',
            'vigente': False,
            'pokemons': [
                {

                }
            ]
        },
        {
            'nombre': 'Liliana Vargas',
            'edad': 24,
            'dni': 85552232,
            'pais': 'España',
            'vigente': True,
            'pokemons': [
                {

                }
            ]
        }
    ]

    """crear un objeto en una tabla de la base de datos """
    # p = Owner(nombre = "Duque Nescar", descripcion="PruebaBD" , pais= "españa")
    # p.save()
    #
    # p.nombre = "Mother "
    # p.save()

    """filtrar datos .filter()"""
    #
    # data_context = Owner.objects.filter(nombre = 'Duque Nescar')

    # """ ACORTAR datos """
    #
    # data_context = Owner.objects.all()[5:12]

    # """ Actualizar  datos a un cierto grupo de datos o un solo registro """
    #
    # Owner.objects.filter(nombre__startswith="Margarita Tello ").update(pais="peru")

    """consulta complejas """

    query = Q(nombre__startswith="Margarita Tello ") | Q(nombre__startswith="Duque Nescar")
    data_context = Owner.objects.filter(query)



    # """ eliminando un dato  """
    #
    # data_context = Owner.objects.get(id=13)
    # data_context.delete()

    return render(request,'owner/owner_list.html',context= {'data':data_context})

def owner_search(request):

    query = request.GET.get('q', '')
    print("Query: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )

    data_context = Owner.objects.filter(results)
    #data_context = Owner.objects.filter(results).distinct()


    return render(request, 'owner/owner_serch.html',context={'data':data_context, 'query':query})

def owner_details(request):
    """ Obtener todos los elementos de una tabla de bd"""
    owners = Owner.objects.all()

    owners = Owner.objects.all()

    return render(request, 'owner/owner_details.html', context={'data': owners})

def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data ['nombre']
        descripcion = form.cleaned_data ['descripcion']
        pais =form.cleaned_data ['pais']

        form.save()

    else:
        form= OwnerForm()

    return  render(request, 'owner/owner_create.html', {'form':form})