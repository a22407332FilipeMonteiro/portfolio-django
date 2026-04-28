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



## Commit 4 — Apagar Projeto | 28/04/2026

**Commit:** `feat(portfolio): adicionar eliminação de projetos`

**O que fiz:**
- Adicionei a view `apagar_projeto` com confirmação.
- Adicionei a rota `projetos/<int:id>/apagar/`.
- Criei o template `apagar_projeto.html` com confirmação.
- Adicionei botão "Apagar" em cada cartão.

**Decisão:** Em vez de apagar diretamente num link (GET), usei uma página intermédia com formulário POST. Mais seguro: protege contra cliques acidentais e respeita o princípio REST de que pedidos GET não devem alterar dados.

**CRUD completo:** Com este commit, o CRUD dos Projetos fica completo (Create, Read, Update, Delete).



## Commit 5 — CRUD Tecnologias | 28/04/2026

**Commit:** `feat(portfolio): adicionar CRUD completo de Tecnologias`

**O que fiz:**
- Implementei CRUD completo de Tecnologias (criar, editar, apagar).
- Criei templates **genéricos** (`form_generico.html` e `apagar_generico.html`) reutilizáveis.
- Adicionei "Tecnologias" no menu de navegação.

**Decisão importante:** Em vez de criar templates específicos para cada classe (`form_tecnologia.html`, `apagar_tecnologia.html`, etc.), criei templates genéricos que recebem `titulo`, `objeto` e `voltar_url` por contexto. Isto vai poupar muito código nos próximos CRUDs (Competências e Formações).

**Vantagem do Django:** O facto de o `ModelForm` gerar o formulário automaticamente a partir do modelo, e os templates genéricos iterarem sobre `form.fields`, permite reutilizar 100% do código entre diferentes entidades. Só precisei de definir o form e a view — o resto é genérico.


## Commit 6 — CRUD Competências | 28/04/2026

**Commit:** `feat(portfolio): adicionar CRUD completo de Competências`

**O que fiz:**
- Implementei CRUD completo de Competências.
- Criei `lista_competencias.html` com indicador visual de nível (bolas ● / ○).
- Adicionei "Competências" no menu de navegação.

**Vantagem da reutilização:** Como já tinha os templates genéricos (`form_generico.html` e `apagar_generico.html`) do commit anterior, **só precisei criar 1 template novo** (a listagem) em vez de 3. O Django mostra aqui a sua força: com `ModelForm` + templates genéricos + views simples, replicar o CRUD para uma nova entidade leva poucos minutos.

**Dificuldade:** Inicialmente criei o `lista_competencias.html` 
diretamente em `portfolio/templates/` (sem a subpasta `portfolio/`), 
o que fazia com que o Django retornasse 404. Resolvi movendo o 
ficheiro para `portfolio/templates/portfolio/lista_competencias.html`. 

**Aprendizagem:** Em Django, o caminho passado ao `render()` deve 
corresponder à estrutura `app/templates/app/template.html` para 
evitar conflitos entre templates de apps diferentes com o mesmo nome.