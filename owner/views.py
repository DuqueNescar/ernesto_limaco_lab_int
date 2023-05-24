from django.shortcuts import render

# Create your views here.
def owner_list(request):
    date_context = {
        'nombre' : 'ernesto carlos',
    }

    return  render(request,'owner/owner.list.html',date_context)