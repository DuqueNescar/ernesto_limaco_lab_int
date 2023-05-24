from django.contrib import admin
from owner.models import Owner
# Register your models here.
#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'pais')
    list_filter = ('nombre',)
    search_fields = ('nombre','pais',)
    fields = ('nombre',)