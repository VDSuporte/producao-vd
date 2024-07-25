# usuarios/views.py

import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

@login_required
def user_list_view(request):
    users = User.objects.all()
    return render(request, 'user-list.html', {'users': users})


def generate_verification_code():
    return str(random.randint(100000, 999999))


def send_verification_email(email, code):
    subject = 'Código de Verificação'
    message = f'Seu código de verificação é: {code}'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def login_view(request):
    if request.method == "POST":
        identifier = request.POST['identifier']
        password = request.POST['password']
        # Verifique se o identifier é um email ou username
        try:
            user = User.objects.get(Q(username=identifier) | Q(email=identifier))
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            messages.success(request, 'Sucesso!!! 🚀🚀🚀')
            return redirect('menu')  # Substitua 'menu' pelo nome da sua URL para a página inicial
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if not email.endswith('@viadupla.com'):
            messages.error(request, 'O e-mail deve terminar com "@viadupla.com".')
        elif password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
        else:
            try:
                verification_code = generate_verification_code()
                send_verification_email(email, verification_code)
                request.session['verification_code'] = verification_code
                request.session['username'] = username
                request.session['password'] = password
                request.session['email'] = email
                return redirect('verify_email')
            except Exception as e:
                messages.error(request, f'Erro ao enviar e-mail: {e}')

    return render(request, 'cadastro.html')


def verify_email_view(request):
    if request.method == 'POST':
        entered_code = request.POST['verification_code']
        if entered_code == request.session.get('verification_code'):
            username = request.session.get('username')
            password = request.session.get('password')
            email = request.session.get('email')
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('usuarios')
            except:
                messages.error(request, 'Erro ao criar usuário. Tente novamente.')
        else:
            messages.error(request, 'Código de verificação incorreto.')

    return render(request, 'verify_email.html')


def request_password_reset_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            verification_code = generate_verification_code()
            send_verification_email(email, verification_code)
            request.session['reset_verification_code'] = verification_code
            request.session['reset_email'] = email
            return redirect('verify_reset_code')
        except User.DoesNotExist:
            messages.error(request, 'E-mail não encontrado.')
    return render(request, 'request_password_reset.html')


def verify_reset_code_view(request):
    if request.method == 'POST':
        entered_code = request.POST['verification_code']
        if entered_code == request.session.get('reset_verification_code'):
            return redirect('reset_password')
        else:
            messages.error(request, 'Código de verificação incorreto.')
    return render(request, 'verify_reset_code.html')


def reset_password_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password != password_confirm:
            messages.error(request, 'As senhas não coincidem.')
        else:
            email = request.session.get('reset_email')
            try:
                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Senha redefinida com sucesso!')
                return redirect('usuarios')
            except User.DoesNotExist:
                messages.error(request, 'Erro ao redefinir a senha.')
    return render(request, 'reset_password.html')

