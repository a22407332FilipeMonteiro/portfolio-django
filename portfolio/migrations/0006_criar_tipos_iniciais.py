from django.db import migrations


def criar_tipos(apps, schema_editor):
    Tipo = apps.get_model('portfolio', 'Tipo')
    
    tipos_iniciais = [
        ('Frontend', 'Tecnologias de interface (HTML, CSS, JS, frameworks)'),
        ('Backend', 'Tecnologias de servidor (Python, Django, APIs)'),
        ('Base de Dados', 'Sistemas de armazenamento de dados (SQLite, PostgreSQL, MySQL)'),
        ('Storage', 'Armazenamento de ficheiros e media (S3, Cloudinary)'),
        ('Outros', 'Ferramentas auxiliares (Git, GitHub, Codespaces, IDEs)'),
    ]
    
    for nome, descricao in tipos_iniciais:
        Tipo.objects.get_or_create(nome=nome, defaults={'descricao': descricao})


def apagar_tipos(apps, schema_editor):
    Tipo = apps.get_model('portfolio', 'Tipo')
    Tipo.objects.filter(nome__in=[
        'Frontend', 'Backend', 'Base de Dados', 'Storage', 'Outros'
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_tipo_alter_tecnologia_tipo'),  
    ]

    operations = [
        migrations.RunPython(criar_tipos, apagar_tipos),
    ]