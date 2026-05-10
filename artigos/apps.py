from django.apps import AppConfig


class ArtigosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artigos'
    verbose_name = 'Artigos'

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(_criar_grupo_autores, sender=self)


def _criar_grupo_autores(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    try:
        from artigos.models import Artigo
        group, _ = Group.objects.get_or_create(name='autores')
        ct = ContentType.objects.get_for_model(Artigo)
        perms = Permission.objects.filter(
            content_type=ct,
            codename__in=['add_artigo', 'change_artigo', 'view_artigo', 'delete_artigo'],
        )
        group.permissions.set(perms)
    except Exception:
        pass
