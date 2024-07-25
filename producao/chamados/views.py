from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Chamados
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ChamadoForm  # Supondo que você tenha um formulário para 'Chamados'
from django.conf import settings


class ChamadosCreate(CreateView):
    model = Chamados
    fields = ['nome', 'email', 'descricao', 'departamento', 'status', 'data']  # Campo 'status' adicionado
    template_name = 'chamado.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosUpdate(UpdateView):
    model = Chamados
    fields = ['nome', 'email', 'descricao', 'departamento', 'status', 'data']
    template_name = 'chamado.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosDelete(DeleteView):
    model = Chamados
    template_name = 'chamado-excluir.html'
    success_url = reverse_lazy('listar-chamados')


class ChamadosList(ListView):
    model = Chamados
    template_name = 'lista/chamados-list.html'


def solicitar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save()

            # Enviar e-mail para o administrador
            mensagem_administrador = f"""
            Novo Chamado Solicitado

            Detalhes do chamado:
            Nome: {chamado.nome}
            Email: {chamado.email}
            Departamento: {chamado.departamento}
            Descrição: {chamado.descricao}
            Status: {chamado.status}
            Data: {chamado.data}
            """
            send_mail(
                'Novo Chamado Solicitado',
                mensagem_administrador,
                settings.EMAIL_HOST_USER,
                ['aprendiz.bi@viadupla.com'],
                fail_silently=False,
            )

            # Enviar e-mail para a pessoa que solicitou o chamado
            mensagem_usuario = f"""
            Olá {chamado.nome},

            Recebemos sua solicitação de chamado. Aqui estão os detalhes:

            Nome: {chamado.nome}
            Email: {chamado.email}
            Departamento: {chamado.departamento}
            Descrição: {chamado.descricao}
            Status: {chamado.status}
            Data: {chamado.data}

            Aguarde até receber uma resposta!

            Atenciosamente:
            Via Dupla Transportes
            """
            send_mail(
                'Confirmação de Solicitação de Chamado',
                mensagem_usuario,
                settings.EMAIL_HOST_USER,
                [chamado.email],
                fail_silently=False,
            )

            return redirect('listar-chamados')
    else:
        form = ChamadoForm()

    return render(request, 'chamado.html', {'form': form})
