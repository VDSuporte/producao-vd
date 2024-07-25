from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class ListagemView(TemplateView):
    template_name = "listagens.html"
    success_url = reverse_lazy('listagens')