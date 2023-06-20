from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.owner.forms import OwnerForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

#crear mi vista se necesita importar el modelo

from apps.owner.models import Owner
from django.core import serializers as ssr

from apps.owner.serializers import OwnerSerializer


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

    return render(request, 'owner/templates/owner/owner_list.html', context= {'data':data_context})

def owner_search(request):

    query = request.GET.get('q', '')
    print("Query: {}".format(query))

    results = (
        Q(nombre__icontains=query)
    )

    data_context = Owner.objects.filter(results)
    #data_context = Owner.objects.filter(results).distinct()


    return render(request, 'owner/owner_serch.html', context={'data':data_context, 'query':query})

def owner_details(request):
    """ Obtener todos los elementos de una tabla de bd"""
    owners = Owner.objects.all()

    return render(request, 'owner/owner_details.html', context={'data': owners})

def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data ['nombre']
        descripcion = form.cleaned_data ['descripcion']
        pais =form.cleaned_data ['pais']

        form.save()
        return redirect('owner_details')


    else:
        form= OwnerForm()

    return  render(request, 'owner/owner_create.html', {'form':form})

def owner_delete(request,id_owner):

    print("ID Owner_ {}".format(id_owner))

    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return  redirect('owner_details')

def owner_edit(request,id_owner):
    #print("ID Owner a editar  {}".format(id_owner))
    owner =Owner.objects.get(id=id_owner)
    print("Datos del owner a editor: {}".format(owner))
    form =OwnerForm(initial={'nombre':owner.nombre,'descripcion':owner.descripcion,'pais':owner.pais})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_details')

    return render(request, 'owner/owner_update.html', context={'form':form})


class OwnerList(ListView):
    model = Owner
    template_name = 'owner/owner_list_vc.html'

class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_create.html'
    success_url = reverse_lazy('owner_list_vc')

class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')

class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = 'owner/owner_confirm_delete.html'


""" Seria Lazer """

def ListOwnerSerializer(request):
    lista_owner = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'descripcion'])


    return HttpResponse(lista_owner, content_type="application/json")


@api_view(['GET', 'POST'])

def owner_api_view(request):

    if request.method == 'GET':
        print("Ingresar a GET")
        queryset= Owner.objects.all()
        serializers_class = OwnerSerializer(queryset,many=True)

        return Response(serializers_class.data,status=status.HTTP_200_OK)
        """seimorta status"""

    elif request.method =='POST':
        print("Data owner {}".format(request.data))
        serializers_class = OwnerSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def owner_details_view(request, pk):
    owner = Owner.objects.filter(id=pk).first()


    if owner:
        if request.method == 'GET':
            serializers_class = OwnerSerializer(owner)
            return Response(serializers_class.data)


        elif request.method == 'PUT':
            serializers_class = OwnerSerializer(owner, data=request.data)

            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            owner.delete()
            return Response('Owner ha sido eliminado correctamente de la BD', status=status.HTTP_200_OK)
