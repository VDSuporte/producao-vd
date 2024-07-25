from django import forms
from .models import Chamados

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamados
        fields = ['email', 'nome', 'departamento', 'descricao', 'status', 'data']
