from django import forms
from .models import Padre

class PadreForm(forms.ModelForm):
    class Meta:
        model = Padre
        fields = ('nom',)


