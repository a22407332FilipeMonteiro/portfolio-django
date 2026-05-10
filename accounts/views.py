# accounts/views.py
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.utils.encoding import force_str
from django.urls import reverse
from .forms import RegistoForm, MagicLinkForm
from .models import MagicLink


class _Email7bit(EmailMessage):
    """EmailMessage que força Content-Transfer-Encoding: 7bit para não partir URLs com quoted-printable."""
    def _add_bodies(self, msg):
        if self.body or not self.attachments:
            encoding = self.encoding or settings.DEFAULT_CHARSET
            body = force_str(self.body or '', encoding=encoding, errors='surrogateescape')
            msg.set_content(body, subtype=self.content_subtype, charset=encoding, cte='7bit')


def login_view(request):
    # Se já está autenticado, redireciona para a home
    if request.user.is_authenticated:
        return redirect('portfolio:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('portfolio:home')
        else:
            return render(request, 'accounts/login.html', {
                'mensagem': 'Credenciais inválidas. Tenta novamente.',
            })
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:home')


def registo_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio:home')

    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo_autores, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = RegistoForm()
    
    return render(request, 'accounts/registo.html', {'form': form})


# ============ MAGIC LINK ============

def magic_link_pedir(request):
    """Página onde o utilizador pede um magic link por email."""
    if request.method == 'POST':
        form = MagicLinkForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Verifica se o utilizador existe com este email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, 'accounts/magic_link.html', {
                    'form': form,
                    'mensagem': 'Não existe conta com esse email.',
                    'erro': True,
                })
            
            # Gera o token
            magic_link = MagicLink.gerar_token(email)

            # Detecta se está no Codespaces e constrói o link correto
            codespace_name = os.environ.get('CODESPACE_NAME')
            port_domain = os.environ.get('GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN', 'app.github.dev')

            if codespace_name:
                host = f"{codespace_name}-8000.{port_domain}"
                scheme = 'https'
            else:
                host = request.get_host()
                scheme = 'https' if request.is_secure() else 'http'

            link = f"{scheme}://{host}{reverse('accounts:magic_login', args=[magic_link.token])}"

            print(f"\n{'='*70}\nMAGIC LINK:\n{link}\n{'='*70}\n")

            corpo = (
                f'Ola {user.username}!\n\n'
                f'Clica neste link para entrares automaticamente no Portfolio:\n\n'
                f'{link}\n\n'
                f'Este link e valido durante 15 minutos e so pode ser usado uma vez.\n\n'
                f'Se nao pediste este link, ignora este email.'
            )
            mensagem = _Email7bit(
                subject='O teu link magico - Portfolio Filipe',
                body=corpo,
                to=[email],
            )
            mensagem.encoding = 'us-ascii'
            mensagem.send()
            
            return render(request, 'accounts/magic_link.html', {
                'form': MagicLinkForm(),
                'mensagem': f'Enviámos um link para {email}. Verifica a tua caixa de entrada (em desenvolvimento, vê o terminal).',
                'erro': False,
            })
    else:
        form = MagicLinkForm()
    
    return render(request, 'accounts/magic_link.html', {'form': form})


def magic_login(request, token):
    """Endpoint que valida o token e faz login automaticamente."""
    magic_link = get_object_or_404(MagicLink, token=token)
    
    if not magic_link.is_valido():
        return render(request, 'accounts/magic_link_erro.html', {
            'mensagem': 'Este link já expirou ou foi usado. Pede um novo.',
        })
    
    # Encontra o utilizador
    try:
        user = User.objects.get(email=magic_link.email)
    except User.DoesNotExist:
        return render(request, 'accounts/magic_link_erro.html', {
            'mensagem': 'Utilizador não encontrado.',
        })
    
    # Marca o link como usado
    magic_link.usado = True
    magic_link.save()
    
    # Faz login com backend explícito (forma oficial)
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    
    return redirect('portfolio:home')