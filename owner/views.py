from django.shortcuts import render

# Create your views here.
def owner_list(request):
    date_context = [{

        'nombre' : 'ernesto ',
        'apellido': 'limaco',
        'edad':17,
        'dni': 1111111,
        'pais': 'perusalen',
    }]

    return  render(request,'owner/owner_list.html',context= {'data':date_context})