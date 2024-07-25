from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Justificativa
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import JustificativaForm

class JustificativaCreate(CreateView):
    model = Justificativa
    fields = ['nome', 'email', 'descricao', 'titulo', 'status', 'data']
    template_name = 'justificativa.html'
    success_url = reverse_lazy('justificativa-lista')

class JustificativaUpdate(UpdateView):
    model = Justificativa
    fields = ['nome', 'email', 'descricao', 'titulo', 'status', 'data']
    template_name = 'justificativa.html'
    success_url = reverse_lazy('justificativa-lista')

class JustificativaDelete(DeleteView):
    model = Justificativa
    template_name = 'justificativa-excluir.html'
    success_url = reverse_lazy('justificativa-lista')

class JustificativaList(ListView):
    model = Justificativa
    template_name = 'lista/justificativa-listas.html'  # Template diferente para a listagem


def solicitar_justificativa(request):
    if request.method == 'POST':
        form = JustificativaForm(request.POST)
        if form.is_valid():
            justificativa = form.save()
            try:
                # Enviar e-mail para o administrador
                send_mail(
                    'Nova Justificativa Solicitada',
                    f'Detalhes da justificativa:\n\nNome: {justificativa.nome}\nEmail: {justificativa.email}\nTítulo: {justificativa.titulo}\nDescrição: {justificativa.descricao}\nStatus: {justificativa.status}',
                    settings.EMAIL_HOST_USER,
                    ['aprendiz.bi@viadupla.com'],  # Substitua pelo e-mail do administrador
                    fail_silently=False,
                )

                # Enviar e-mail para a pessoa que solicitou a justificativa
                send_mail(
                    'Confirmação de Solicitação de Justificativa',
                    f'Olá {justificativa.nome},\n\nRecebemos sua solicitação de justificativa. Aqui estão os detalhes:\n\nEmail: {justificativa.email}\nNome: {justificativa.nome}\nTítulo: {justificativa.titulo}\nDescrição: {justificativa.descricao}\nStatus: {justificativa.status}\n\nAtenciosamente,\nSua Empresa',
                    settings.EMAIL_HOST_USER,
                    [justificativa.email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f'Erro ao enviar e-mail: {e}')

            return redirect('justificativa-abertura')
    else:
        form = JustificativaForm()
    return render(request, 'justificativa/solicitar-justificativa.html', {'form': form})