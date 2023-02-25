from django import forms
from .models import Jobs

class Jobs(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ('titulo', 'descricao','categoria','prazo_entrega', 'preco', 'referencias')