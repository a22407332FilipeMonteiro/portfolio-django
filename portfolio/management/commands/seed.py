# portfolio/management/commands/seed.py
from django.core.management.base import BaseCommand
from datetime import date
from portfolio.models import (
    Licenciatura, Docente, UnidadeCurricular,
    Tipo, Tecnologia, Competencia, Projeto, Formacao
)


class Command(BaseCommand):
    help = 'Popula a BD com dados de teste para o portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 A semear a base de dados...')

        # ===== LICENCIATURA =====
        licenciatura, _ = Licenciatura.objects.get_or_create(
            nome='Licenciatura em Engenharia Informática',
            defaults={
                'sigla': 'LEI',
                'universidade': 'Universidade Lusófona',
                'duracao_anos': 3,
                'ects_total': 180,
                'descricao': 'Licenciatura focada em desenvolvimento de software, sistemas distribuídos e bases de dados.',
                'url_oficial': 'https://www.ulusofona.pt/licenciaturas/engenharia-informatica',
            }
        )
        self.stdout.write(f'  ✓ Licenciatura: {licenciatura.nome}')

        # ===== DOCENTES =====
        docente, _ = Docente.objects.get_or_create(
            nome='Lúcio Studer',
            defaults={
                'email': 'lucio.studer@ulusofona.pt',
                'pagina_lusofona': 'https://www.ulusofona.pt',
            }
        )
        self.stdout.write(f'  ✓ Docente: {docente.nome}')

        # ===== UNIDADES CURRICULARES =====
        uc_pw, _ = UnidadeCurricular.objects.get_or_create(
            nome='Programação Web',
            defaults={
                'ano': 2,
                'semestre': 2,
                'descricao': 'Desenvolvimento de aplicações web com Django, HTML, CSS e JavaScript.',
                'licenciatura': licenciatura,
            }
        )
        uc_pw.docentes.add(docente)
        self.stdout.write(f'  ✓ UC: {uc_pw.nome}')

        # ===== TECNOLOGIAS =====
        tipo_frontend = Tipo.objects.get(nome='Frontend')
        tipo_backend = Tipo.objects.get(nome='Backend')
        tipo_bd = Tipo.objects.get(nome='Base de Dados')
        tipo_outros = Tipo.objects.get(nome='Outros')

        tecnologias_data = [
            ('Python', tipo_backend, 'Linguagem de programação versátil e fácil de ler.', 'https://www.python.org', 5),
            ('Django', tipo_backend, 'Framework web em Python que segue o padrão MVT.', 'https://www.djangoproject.com', 4),
            ('HTML', tipo_frontend, 'Linguagem de marcação para estruturar páginas web.', 'https://developer.mozilla.org/docs/Web/HTML', 4),
            ('CSS', tipo_frontend, 'Linguagem de estilo para apresentação de páginas web.', 'https://developer.mozilla.org/docs/Web/CSS', 3),
            ('JavaScript', tipo_frontend, 'Linguagem de programação para interatividade no browser.', 'https://developer.mozilla.org/docs/Web/JavaScript', 3),
            ('SQLite', tipo_bd, 'Base de dados relacional leve, usada em desenvolvimento.', 'https://www.sqlite.org', 3),
            ('Git', tipo_outros, 'Sistema de controlo de versões distribuído.', 'https://git-scm.com', 4),
            ('GitHub', tipo_outros, 'Plataforma de hosting para repositórios Git.', 'https://github.com', 4),
            ('VS Code', tipo_outros, 'Editor de código da Microsoft, gratuito e extensível.', 'https://code.visualstudio.com', 5),
        ]

        tecnologias = {}
        for nome, tipo, descricao, website, nivel in tecnologias_data:
            tec, _ = Tecnologia.objects.get_or_create(
                nome=nome,
                defaults={
                    'tipo': tipo,
                    'descricao': descricao,
                    'website': website,
                    'nivel_interesse': nivel,
                }
            )
            tecnologias[nome] = tec
            self.stdout.write(f'  ✓ Tecnologia: {nome} ({tipo.nome})')

        # ===== COMPETÊNCIAS =====
        competencias_data = [
            ('Programação Backend', 'Técnica', 4, 'Desenvolvimento do lado do servidor.'),
            ('Programação Frontend', 'Técnica', 3, 'Desenvolvimento de interfaces de utilizador.'),
            ('Modelação de Dados', 'Técnica', 4, 'Diagramas ER e modelação de bases de dados.'),
            ('Trabalho em Equipa', 'Soft Skill', 4, 'Capacidade de colaborar em projetos.'),
            ('Resolução de Problemas', 'Soft Skill', 4, 'Análise e resolução de problemas técnicos.'),
            ('Inglês', 'Linguística', 4, 'Leitura e escrita técnica em inglês.'),
        ]

        competencias = {}
        for nome, tipo, nivel, descricao in competencias_data:
            comp, _ = Competencia.objects.get_or_create(
                nome=nome,
                defaults={
                    'tipo': tipo,
                    'nivel': nivel,
                    'descricao': descricao,
                }
            )
            competencias[nome] = comp
            self.stdout.write(f'  ✓ Competência: {nome}')

        # ===== PROJETOS =====
        projeto, _ = Projeto.objects.get_or_create(
            nome='Portfólio Pessoal',
            defaults={
                'descricao': 'Aplicação web em Django para apresentar o meu percurso académico, projetos, tecnologias e competências.',
                'data_inicio': date(2026, 2, 1),
                'github': 'https://github.com/a22407332FilipeMonteiro/portfolio-django',
                'destaque': True,
                'unidade_curricular': uc_pw,
            }
        )
        projeto.tecnologias.set([
            tecnologias['Python'], tecnologias['Django'],
            tecnologias['HTML'], tecnologias['CSS'],
            tecnologias['SQLite'], tecnologias['Git'],
            tecnologias['GitHub'],
        ])
        projeto.competencias.set([
            competencias['Programação Backend'],
            competencias['Programação Frontend'],
            competencias['Modelação de Dados'],
            competencias['Resolução de Problemas'],
        ])
        self.stdout.write(f'  ✓ Projeto: {projeto.nome}')

        # ===== FORMAÇÕES =====
        formacao, _ = Formacao.objects.get_or_create(
            nome='Licenciatura em Engenharia Informática',
            defaults={
                'instituicao': 'Universidade Lusófona',
                'data_inicio': date(2024, 9, 1),
                'data_fim': date(2027, 7, 31),
                'descricao': 'Licenciatura de 3 anos em Engenharia Informática.',
            }
        )
        formacao.tecnologias.set([tecnologias['Python'], tecnologias['Django']])
        formacao.competencias.set(list(competencias.values()))
        self.stdout.write(f'  ✓ Formação: {formacao.nome}')

        self.stdout.write(self.style.SUCCESS('\n✅ Base de dados semeada com sucesso!'))