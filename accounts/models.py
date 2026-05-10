# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import secrets


class MagicLink(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=64, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f"Magic link para {self.email}"

    @classmethod
    def gerar_token(cls, email):
        """Cria um novo magic link com token seguro."""
        token = secrets.token_urlsafe(32)
        return cls.objects.create(email=email, token=token)

    def is_valido(self):
        """Verifica se o token ainda é válido (15 minutos e não usado)."""
        if self.usado:
            return False
        validade = self.criado_em + timedelta(minutes=15)
        return timezone.now() <= validade