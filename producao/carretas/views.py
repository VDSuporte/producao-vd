from .models import Carretas

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Acessorios
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404
from .models import Carretas, Acessorios

# Create your views here.




def acessorios_carreta(request, carreta_id):
    carreta = get_object_or_404(Carretas, pk=carreta_id)
    acessorios = Acessorios.objects.filter(carreta=carreta)
    return render(request, 'acessorios.html', {'carreta': carreta, 'acessorios': acessorios})

class CarretasCreate(CreateView):
    model = Carretas
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'eixos', 'pneus',
              'suspensao', 'altura', 'pbt', 'toneladas', 'litros', 'tipo', 'tara', 'suspensor',
              'bolsa', 'mola', 'locada', 'transportadora', 'notafiscal', 'status']
    template_name = 'form-carretas.html'
    success_url = reverse_lazy('cadastrar-acessorios')


class CarretasUpdate(UpdateView):
    model = Carretas
    fields = ['frota', 'placa', 'motorista', 'renavam', 'anomod', 'cor', 'chassi', 'crlv', 'marca', 'modelo', 'eixos', 'pneus',
              'suspensao', 'altura', 'pbt', 'toneladas', 'litros', 'tipo', 'tara', 'suspensor',
              'bolsa', 'mola', 'locada', 'transportadora', 'notafiscal', 'status']
    template_name = 'form-carretas.html'
    success_url = reverse_lazy('listar-cadastros-carretas')


class CarretasDelete(DeleteView):
    model = Carretas
    template_name = 'form-carretas-excluir.html'
    success_url = reverse_lazy('listar-cadastros-carretas')


class CarretasList(ListView):
    model = Carretas
    template_name = 'lista/carretas-list.html'

class AcessoriosCreate(CreateView):
    model = Acessorios
    fields = ['placaacc', 'bottomclaro', 'bottomescuro', 'bottomtepar', 'api', 'descarga', 'dreno', 'graudbolt',
              'olhodegato', 'mangote', 'macarico']
    template_name = 'form-acessorios.html'
    success_url = reverse_lazy('listar-cadastros-carretas')

class AcessoriosUpdate(UpdateView):
    model = Acessorios
    fields = ['placaacc', 'bottomclaro', 'bottomescuro', 'bottomtepar', 'api', 'descarga', 'dreno', 'graudbolt',
              'olhodegato', 'mangote', 'macarico']
    template_name = 'form-acessorios.html'
    success_url = reverse_lazy('listar-cadastros-acessorios')

class AcessoriosDelete(DeleteView):
    model = Acessorios
    template_name = 'form-acessorios-excluir.html'
    success_url = reverse_lazy('listar-cadastros-carretas')

class AcessoriosList(ListView):
    model = Acessorios
    template_name = 'lista/acessorios-list.html'


