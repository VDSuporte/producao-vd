from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cavalos
from django.urls import reverse_lazy
from django import forms


# Create your views here.


class CavalosCreate(CreateView):
    model = Cavalos
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'suspensao', 'tracao',
              'altura', 'capdiesel', 'pbt', 'tara', 'locado', 'macaricoele', 'bombadeasfalto', 'bombahidraulica', 'esperatforca',
              'placasolar', 'status', 'bloqueador', 'transportadora', 'notafiscal', 'velocidade', 'fimdegarantia',
              'dataentregatecnica']
    template_name = 'form-cavalos.html'
    success_url = reverse_lazy('listar-cadastros-cavalos')


class CavalosUpdate(UpdateView):
    model = Cavalos
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'suspensao', 'tracao',
              'altura', 'capdiesel', 'pbt', 'tara', 'locado', 'macaricoele', 'bombadeasfalto', 'bombahidraulica', 'esperatforca',
              'placasolar', 'status', 'bloqueador', 'transportadora', 'notafiscal', 'velocidade', 'fimdegarantia',
              'dataentregatecnica']
    template_name = 'form-cavalos.html'
    success_url = reverse_lazy('listar-cadastros-cavalos')


class CavalosDelete(DeleteView):
    model = Cavalos
    template_name = 'form-cavalos-excluir.html'
    success_url = reverse_lazy('listar-cadastros-cavalos')


class CavalosList(ListView):
    model = Cavalos
    template_name = 'lista/cavalos-listas.html'