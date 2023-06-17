from django.forms import ModelForm

from apps.owner.models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ('nombre', 'pais','descripcion')
