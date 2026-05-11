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


## Commit 7 — CRUD Formações | 28/04/2026

**Commit:** `feat(portfolio): adicionar CRUD completo de Formações`

**O que fiz:**
- Implementei CRUD completo de Formações.
- Criei `lista_formacoes.html` com layout em "timeline" (lista vertical).
- Adicionei "Formações" no menu de navegação.

**Marco:** Com este commit, a **secção 2.2 da Ficha 8 fica completa**: as 4 entidades pedidas (Projetos, Tecnologias, Competências, Formações) têm CRUD funcional via formulários.





## Commit 8 — Setup Markdownify | 28/04/2026

**Commit:** `feat(portfolio): integrar django-markdownify para making-off`

**O que fiz:**
- Instalei o pacote `django-markdownify` e configurei em `settings.py`.
- Criei a página de listagem de Making-Of com o filtro `markdownify` aplicado.
- Adicionei link "Making-Of" no menu.

**Por que usar Markdownify:** Permite escrever apontamentos do making-off em markdown (mais rápido e legível que HTML) e renderizá-los automaticamente em HTML formatado. Os utilizadores veem texto bonito sem ter que escrever HTML manualmente na BD.

**Decisão:** Estendi a `WHITELIST_TAGS` do exemplo da ficha com `code`, `pre`, `br` e `hr` para suportar blocos de código nos apontamentos técnicos.




## Commit 9 — Classe Tipo para Tecnologias | 28/04/2026

**Commit:** `feat(portfolio): criar entidade Tipo para classificar Tecnologias`

**O que fiz:**
- Criei o modelo `Tipo` com `nome` e `descricao`.
- Mudei `Tecnologia.tipo` de `CharField` para `ForeignKey(Tipo)`.
- Criei migração de dados com os 5 tipos iniciais.

**Dificuldade:** Ao correr `migrate`, deu um `IntegrityError` porque a tecnologia que tinha na BD usava o campo antigo (texto livre como "Linguagem") e o Django não conseguia converter para um ID de Tipo. Resolvi apagando a BD (`db.sqlite3`) e as migrações novas, recriando-as do zero.

**Decisão:** Usei `on_delete=SET_NULL` para que apagar um tipo não apague tecnologias associadas.

**Aprendizagem:** Aprendi a criar **migrações de dados** (`RunPython`). É melhor que criar manualmente no admin porque os dados ficam versionados no código e funcionam em qualquer ambiente.



Falta o 10 (Não esquecer) 



## Commit 11 — Iframe do Vídeo-Tutorial | 29/04/2026

**Commit:** `feat(portfolio): adicionar iframe do vídeo-tutorial na página Sobre`

**O que fiz:**
- Embebi o vídeo-tutorial (https://youtu.be/vkyuVM4F4v4) na secção "Arquitetura MVT" da página "Sobre".
- Configurei o iframe com wrapper responsivo (rácio 16:9) para manter as proporções em qualquer tamanho de ecrã.
- Adicionei link alternativo para abrir o vídeo no YouTube.

**Aprendizagem:** O YouTube exige o formato `embed/VIDEO_ID` para iframes (em vez do `youtu.be/VIDEO_ID` partilhado). Para responsividade, usei a técnica do `padding-bottom: 56.25%` (16:9) num wrapper com `position: relative`, em vez de definir uma altura fixa.

**Marco:** Com este commit, **a Ficha 8 fica completa** ✅ — todos os pontos das secções 2.2, 2.3 e 2.4 foram implementados.



## Commit 12 — Autenticação completa e App Artigos | 09/05/2026

**Commit:** `feat(accounts, artigos): adicionar autenticação e CRUD de artigos`

**O que fiz:**
- Criei a app `accounts` com login, logout, registo e magic link.
- Criei a app `artigos` com CRUD de artigos, likes e comentários.
- Protegi as views de escrita do portfolio com o grupo `gestor-portfolio`.
- Adicionei o link Artigos no menu e mostro o utilizador autenticado.

**Dificuldade:** O magic link estava a aparecer partido no terminal — o Django 6.0.3 aplica `quoted-printable` ao corpo do email, partindo URLs longos com `=` a cada 76 caracteres (ex: `magic-log=in/TOKEN`). Resolvi com uma classe `_Email7bit` que força o encoding `7bit`, mantendo o link inteiro.

**Decisão:** Usei `UniqueConstraint` com `condition=Q(...)` no modelo `Like` para permitir likes de utilizadores anónimos via `session_key`, sem duplicados. Para o grupo `autores`, usei o sinal `post_migrate` em vez de uma migração de dados — corre automaticamente em qualquer ambiente.

**Aprendizagem:** Separar autenticação numa app própria (`accounts`) segue o princípio de responsabilidade única e facilita reutilização noutros projetos. Aprendi também que `UniqueConstraint` condicional permite restrições únicas parciais no SQLite — útil para casos como likes (1 por user OU 1 por sessão).



## Commit 13 — Migração para PostgreSQL na Neon | 10/05/2026

**Commit:** `feat(config): migrar base de dados para PostgreSQL na Neon`

**O que fiz:**
- Configurei o projeto para usar PostgreSQL na cloud (Neon) em vez de SQLite local.
- Usei o `django-environ` para ler a `DATABASE_URL` do ficheiro `.env`.
- Migrei os dados existentes via `dumpdata`/`loaddata`.

**Dificuldade:** O `.env` estava sem o prefixo `DATABASE_URL=`, o que fazia o Django falhar a ler a connection string. Resolvi corrigindo a sintaxe (`CHAVE=valor` numa só linha).

**Decisão:** Adicionei `dados.json` e `.env` ao `.gitignore` por questões de segurança e portabilidade — credenciais nunca devem ir para o repositório.

**Aprendizagem:** A separação **código vs configuração** é uma boa prática. O mesmo código corre em desenvolvimento (SQLite/PostgreSQL local) e produção (Neon) — só muda a variável de ambiente.


## Commit 14 — Migração de media para Cloudinary | 10/05/2026

**Commit:** `feat(config): migrar armazenamento de media para Cloudinary`

**O que fiz:**
- Configurei o `cloudinary_storage` como backend de media no Django.
- Migrei as imagens existentes via script (`migra_ficheiros.py`).
- Removi configuração local (`MEDIA_URL`, `MEDIA_ROOT`, `static()`).

**Dificuldade:** Como o storage padrão já era Cloudinary, o `obj.imagem.path` deixou de funcionar (Cloudinary não tem `path`, só `url`). Resolvi construindo o caminho local manualmente com `os.path.join(MEDIA_ROOT, campo.name)`.

**Decisão:** Mantive as imagens **estáticas** (retrato, diagramas MVT/ER) em `STATIC_ROOT`. O Cloudinary só guarda **media** (uploads dinâmicos). Estáticos são parte do código, não fazem sentido ir para a cloud.

**Aprendizagem:** A separação `MEDIA` vs `STATIC` é importante. `STATIC` é versionado no Git e servido como ficheiro fixo; `MEDIA` é dinâmico (uploads dos utilizadores) e fica em armazenamento externo como Cloudinary ou S3.