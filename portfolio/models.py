from django.db import models


# Licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, default='')
    universidade = models.CharField(max_length=100)
    duracao_anos = models.IntegerField()
    ects_total = models.IntegerField(default=0)
    descricao = models.TextField(blank=True)
    url_oficial = models.URLField(blank=True, default='')

    class Meta:
        verbose_name = 'Licenciatura'
        verbose_name_plural = 'Licenciaturas'

    def __str__(self):
        return self.nome


# Docente
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    pagina_lusofona = models.URLField()
    foto = models.ImageField(upload_to='docentes/', null=True, blank=True)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.nome


# Unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', null=True, blank=True)

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente, blank=True)

    class Meta:
        verbose_name = 'Unidade Curricular'
        verbose_name_plural = 'Unidades Curriculares'

    def __str__(self):
        return self.nome


# Tecnologia
class Tecnologia(models.Model):
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # ex: Linguagem, Framework, Ferramenta, BD
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    website = models.URLField()
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)  # 1-5

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'

    def __str__(self):
        return self.nome


# Competencia
class Competencia(models.Model):
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # ex: Técnica, Soft Skill, Linguística
    nivel = models.IntegerField(choices=NIVEL_CHOICES, default=3)  # 1-5
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Competência'
        verbose_name_plural = 'Competências'

    def __str__(self):
        return self.nome


# Projeto
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    github = models.URLField()
    demo = models.URLField(null=True, blank=True)
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    destaque = models.BooleanField(default=False)

    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    competencias = models.ManyToManyField(Competencia, blank=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


    def __str__(self):
        return self.nome


# Formacao
class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField(blank=True)

    competencias = models.ManyToManyField(Competencia, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    class Meta:
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'


    def __str__(self):
        return self.nome


# TFC
class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField(blank=True)
    area = models.CharField(max_length=100)
    link = models.URLField()
    destaque = models.BooleanField(default=False)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    class Meta:
        verbose_name = 'TFC'
        verbose_name_plural = 'TFCs'

    def __str__(self):
        return self.titulo


# Experiencia Profissional (entidade extra obrigatória)
class ExperienciaProfissional(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)

    competencias = models.ManyToManyField(Competencia, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    class Meta:
        verbose_name = 'Experiência Profissional'
        verbose_name_plural = 'Experiências Profissionais'

    def __str__(self):
        return f"{self.cargo} @ {self.empresa}"


# Making Of
class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    imagem = models.ImageField(upload_to='makingof/', null=True, blank=True)
    tipo = models.CharField(max_length=50)  # ex: Modelação, Implementação, Erro, Decisão
    entidade_relacionada = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Making Of'
        verbose_name_plural = 'Making Of'

    def __str__(self):
        return self.titulo