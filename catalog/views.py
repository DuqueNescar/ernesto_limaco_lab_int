from django.shortcuts import render






# Create your views here.
def catalog_list(request):

    data_context =[{
            'nombre': 'Ernesto Limaco',
            'edad': 15,
            'pais': 'Francia',
        },
        {
            'nombre': 'DuqueNescar',
            'edad': 85,
            'pais': 'Peru',
        },
        {
            'nombre': 'Limaco',
            'edad': 45,
            'pais': 'Peru',
        },
    ]

    #data_context = catalog.objects.filter(nombre='Duque Nescar')

    return render(request, 'catalog/archivocatalog.html', context={'data': data_context})