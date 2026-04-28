# Apontamentos



## Commit 1 — Setup app portfolio | 28/04/2026

**Commit:** `feat(portfolio): adicionar app portfolio com listagem de projetos`

**O que fiz:**
- Criei `portfolio/urls.py` com namespace próprio.
- Criei a view `lista_projetos` e adicionei a rota no `config/urls.py`.
- Criei `templates/portfolio/` com `base.html` e `lista_projetos.html`.

**Dificuldade:** Tive um erro `TemplateDoesNotExist` porque a pasta `portfolio/templates/portfolio/` ainda não existia. Resolvido criando a estrutura.

**Decisão:** Usei `app_name = 'portfolio'` para evitar conflitos com a app `escola`.



## Commit 2 — Criar Projeto | 28/04/2026

**Commit:** `feat(portfolio): adicionar formulário de criação de projetos`

**O que fiz:**
- Criei `portfolio/forms.py` com `ProjetoForm` (ModelForm).
- Adicionei a view `criar_projeto` e a rota `projetos/novo/`.
- Criei o template `form_projeto.html` (será reutilizado para editar).
- Adicionei botão "+ Novo Projeto" na listagem.

**Dificuldade:** O formulário marcava o campo `video` como obrigatório, mesmo estando definido com `blank=True` no modelo. Resolvi sobrepondo `required = False` no `__init__` do form para vários campos opcionais (vídeo, demo, imagem, descrição, etc.).

**Decisão:** Reutilizar o mesmo template `form_projeto.html` para criar e editar projetos, passando um título dinâmico via contexto.


## Commit 3 — Editar Projeto | 28/04/2026

**Commit:** `feat(portfolio): adicionar edição de projetos`

**O que fiz:**
- Adicionei a view `editar_projeto` reutilizando `ProjetoForm`.
- Adicionei a rota `projetos/<int:id>/editar/`.
- Adicionei botão "Editar" em cada cartão da listagem.

**Decisão:** Reutilizei o template `form_projeto.html` (do commit 2) para a edição, mudando apenas o título via contexto. Reduz duplicação de código.

**Aprendizagem:** O `ModelForm` com `instance=projeto` pré-preenche o formulário e atualiza o objeto certo na BD. Sem o `instance`, o `form.save()` criaria um registo novo em vez de atualizar.




