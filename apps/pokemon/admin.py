from django.contrib import admin
from apps.pokemon.models import pokemon


# Register your models here.
@admin.register(pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ('nombre', 'tipo', 'numero',)
    list_display = ('nombre', 'generacion', 'tipo')
    search_fields = ('nombre',)

