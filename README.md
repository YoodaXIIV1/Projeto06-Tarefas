<div align="center">

# 🍃 MongoDB + Python — 10 Projetos Práticos

### Do primeiro CRUD a uma API REST e a um dashboard de dados

**Material de aula • Código completo • Tutoriais passo a passo • Exercícios • Avaliação**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![PyMongo](https://img.shields.io/badge/PyMongo-4B8BBE?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

![Projetos](https://img.shields.io/badge/PROJETOS-10-009688)
![Níveis](https://img.shields.io/badge/NÍVEIS-3-8A2BE2)
![Idioma](https://img.shields.io/badge/IDIOMA-PT--BR-blue)

> **Objetivo:** aprender a modelar documentos, realizar operações CRUD, criar índices, elaborar consultas e agregações, integrar aplicações Python com MongoDB e construir serviços de dados.

</div>

---

## 🧭 Sumário

- [Instalações e links oficiais](#-instalações-e-links-oficiais)
- [Preparação do ambiente](#-preparação-do-ambiente)
- [Como funciona o MongoDB](#-como-funciona-o-mongodb)
- [Trilha de projetos](#-trilha-de-projetos)
- [Os 10 projetos completos](#-os-10-projetos-completos)
- [Problemas frequentes](#-problemas-frequentes)
- [Critérios de avaliação](#-critérios-de-avaliação)
- [Referências oficiais](#-referências-oficiais)

## 🔗 Instalações e links oficiais

| Ferramenta | Para que serve | Link oficial |
|---|---|---|
| Python 3.11+ | Executar os scripts | [Baixar Python](https://www.python.org/downloads/) |
| MongoDB Community Server | Banco de dados instalado localmente | [Baixar Community Server](https://www.mongodb.com/try/download/community) |
| MongoDB Compass | Interface gráfica para visualizar coleções | [Baixar MongoDB Compass](https://www.mongodb.com/try/download/compass) |
| MongoDB Atlas | Banco de dados hospedado na nuvem (alternativa ao servidor local) | [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) |
| Visual Studio Code | Editor recomendado (opcional) | [Baixar VS Code](https://code.visualstudio.com/) |
| PyMongo | Driver Python oficial do MongoDB | [Documentação PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) |
| FastAPI | Framework da API do projeto 09 | [Documentação FastAPI](https://fastapi.tiangolo.com/) |
| Matplotlib | Gráfico do projeto 10 | [Documentação Matplotlib](https://matplotlib.org/stable/) |

**Importante:** o **MongoDB Compass não é o servidor**. Para os exemplos locais funcionarem, instale e inicie o MongoDB Community Server. Como alternativa, use um cluster no **MongoDB Atlas** e configure sua URI.

## 🛠️ Preparação do ambiente

### Passo 1 — Verificar a instalação do Python

No **Windows (PowerShell)**, execute:

```powershell
py --version
```

No **Linux/macOS**, execute:

```bash
python3 --version
```

Na instalação do Python no Windows, habilite a opção de adicionar o Python ao PATH, caso esteja disponível. Nos próximos comandos, `python` significa o executável do Python dentro do ambiente virtual ativado.

### Passo 2 — Configurar o MongoDB

**Opção A — MongoDB local:** instale o Community Server, configure-o para iniciar como serviço, se aplicável, e teste no Compass a conexão:

```text
mongodb://localhost:27017/
```

**Opção B — MongoDB Atlas:** crie uma implantação, configure um usuário de banco de dados, autorize somente os endereços IP necessários e copie a string em **Connect → Drivers → Python**. Não publique a URI com usuário/senha. Em caso de caracteres especiais na senha, utilize a URI devidamente codificada conforme a documentação.

### Passo 3 — Preparar o projeto e o ambiente virtual

Entre na pasta deste repositório e crie o ambiente:

```bash
python -m venv .venv
```

Ativar no **Windows PowerShell**:

```powershell
.venv\Scripts\Activate.ps1
```

Ativar no **Linux/macOS**:

```bash
source .venv/bin/activate
```

> Se o PowerShell bloquear a ativação, utilize diretamente `.venv\Scripts\python.exe` nos comandos, sem alterar a política de segurança do computador.

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Conteúdo de **`requirements.txt`**:

```text
pymongo>=4.10,<5
python-dotenv>=1,<2
fastapi>=0.110,<1
uvicorn[standard]>=0.29,<1
matplotlib>=3.8,<4
```

### Passo 4 — Configurar a string de conexão

Crie um arquivo **`.env`** na raiz do repositório (pode copiar `.env.example`):

```dotenv
MONGO_URI=mongodb://localhost:27017/
```

Para Atlas, substitua o valor pela URI fornecida no painel do cluster. **Nunca envie `.env` ao GitHub.**

O arquivo **`.gitignore`** deve conter pelo menos:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
*.png
```

### Passo 5 — Criar `conexao.py`

Este arquivo é **compartilhado pelos dez projetos**. Ele lê `.env`, verifica a conexão com `ping` e seleciona o banco didático `laboratorio_python`.
```python
"""Conexao compartilhada: defina MONGO_URI no arquivo .env."""
import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(Path(__file__).with_name('.env'))
uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
cliente.admin.command('ping')  # verifica se o servidor responde
banco = cliente['laboratorio_python']
```
### Passo 6 — Testar a conexão

Com o MongoDB ligado, execute da **raiz do repositório**:

```bash
python -c "from conexao import banco; print('Conectado a:', banco.name)"
```

Resultado esperado:

```text
Conectado a: laboratorio_python
```

### Organização dos arquivos

```text
mongodb-python-lab/
├── README.md
├── requirements.txt
├── .env.example
├── .env                  # somente no seu computador
├── .gitignore
├── conexao.py
├── p01_alunos/main.py
├── p02_biblioteca/main.py
├── p03_estoque/main.py
├── p04_contatos/main.py
├── p05_financas/main.py
├── p06_tarefas/main.py
├── p07_turmas_notas/main.py
├── p08_corretor_provas/main.py
├── p09_api/main.py
└── p10_dashboard/main.py
```

Cada pasta também possui um `__init__.py` vazio, permitindo executar `python -m nome_da_pasta.main` a partir da raiz.

## 🧠 Como funciona o MongoDB

O MongoDB é um banco de dados orientado a **documentos BSON**. Uma coleção contém documentos semelhantes a objetos JSON. Um registro de aluno, por exemplo, pode ter esta estrutura:

```json
{
  "matricula": "2026001",
  "nome": "Ana Silva",
  "curso": "ADS"
}
```

Em cada documento real existe também um campo `_id`, normalmente um `ObjectId` gerado automaticamente. Diferentemente do SQL tradicional, as coleções não exigem uma tabela rígida de colunas, mas **validações e índices continuam importantes**.

| Operação | MongoDB/PyMongo | Exemplo |
|---|---|---|
| Criar | `insert_one()` | Inserir um aluno |
| Ler | `find()` / `find_one()` | Consultar alunos |
| Atualizar | `update_one()` | Alterar um curso |
| Excluir | `delete_one()` | Excluir uma matrícula |
| Agrupar | `aggregate()` | Calcular faturamento |
| Indexar | `create_index()` | Impedir matrícula repetida |

As dez soluções utilizam **o mesmo banco** `laboratorio_python`, mas com **coleções separadas por projeto**, identificadas pelo sufixo `p01`, `p02`, etc. Isso evita misturar dados de exercícios diferentes.

## 🗺️ Trilha de projetos

| Nº | Projeto | Nível | Conteúdo principal |
|:---:|---|---|---|
| 01 | 👨‍🎓 Cadastro de Alunos | 🟢 Iniciante | CRUD |
| 02 | 📚 Biblioteca | 🟢 Iniciante | Índices e empréstimos |
| 03 | 📦 Controle de Estoque | 🟡 Intermediário | Atualização atômica |
| 04 | 📇 Agenda de Contatos | 🟢 Iniciante | Busca e regex |
| 05 | 💰 Controle Financeiro | 🟡 Intermediário | Agregações |
| 06 | ✅ Tarefas e Prazos | 🟡 Intermediário | Datas e filtros |
| 07 | 🏫 Turmas e Boletins | 🟡 Intermediário | `$lookup` |
| 08 | 📝 Corretor de Provas | 🔴 Avançado | Regras de negócio |
| 09 | 🌐 API de Produtos | 🔴 Avançado | FastAPI + HTTP |
| 10 | 📊 Dashboard de Vendas | 🔴 Avançado | Pipeline + gráficos |

> **Como estudar:** leia o objetivo, copie o código para o arquivo indicado, execute, realize o teste proposto e implemente pelo menos um desafio adicional. Todos os códigos também estão disponíveis em suas pastas no pacote do repositório.

---

# 💻 Os 10 projetos completos
## 👨‍🎓 01 — Cadastro de Alunos

**Nível:** Iniciante · **Tema:** CRUD e índice único  
**Objetivo:** Gerenciar matrículas, nomes e cursos; editar curso e excluir um registro.

**Conceitos:** `insert_one`, `find`, `update_one`, `delete_one`, `create_index`.

### Tutorial guiado

1. Execute o script e selecione **1** para cadastrar uma matrícula. 2. Use **2** para listar os documentos. 3. Experimente **3** para alterar o curso e **4** para excluir. 4. Abra a coleção `alunos_p01` no Compass e confira as mudanças.

**Crie o arquivo** `p01_alunos/main.py` com o código abaixo:

```python
"""Projeto 01: CRUD de alunos por matricula."""
from pymongo.errors import DuplicateKeyError
from conexao import banco

alunos = banco['alunos_p01']
alunos.create_index('matricula', unique=True)

while True:
    print('\n[1] Cadastrar [2] Listar [3] Alterar [4] Excluir [0] Sair')
    opcao = input('Opção: ').strip()
    if opcao == '1':
        matricula = input('Matrícula: ').strip()
        nome = input('Nome: ').strip()
        curso = input('Curso: ').strip()
        if not all([matricula, nome, curso]):
            print('Preencha todos os campos.')
            continue
        try:
            alunos.insert_one({'matricula': matricula, 'nome': nome, 'curso': curso})
            print('Aluno cadastrado!')
        except DuplicateKeyError:
            print('Matrícula já cadastrada.')
    elif opcao == '2':
        for aluno in alunos.find({}, {'_id': 0}).sort('nome', 1):
            print(aluno)
    elif opcao == '3':
        matricula = input('Matrícula: ').strip()
        novo_curso = input('Novo curso: ').strip()
        if novo_curso:
            r = alunos.update_one({'matricula': matricula}, {'$set': {'curso': novo_curso}})
            print('Atualizado!' if r.matched_count else 'Aluno não encontrado.')
    elif opcao == '4':
        matricula = input('Matrícula: ').strip()
        r = alunos.delete_one({'matricula': matricula})
        print('Excluído!' if r.deleted_count else 'Aluno não encontrado.')
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p01_alunos.main
```
**Teste obrigatório:** Tente cadastrar duas vezes a mesma matrícula: o índice único deve impedir a duplicação.

**Desafios extras:**
1. Validar formato da matrícula.
2. Adicionar busca por curso.
3. Registrar data de matrícula.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p01`.

---
## 📚 02 — Biblioteca e Empréstimos

**Nível:** Iniciante · **Tema:** Índices e atualização condicional  
**Objetivo:** Cadastrar livros e gerenciar disponibilidade de empréstimo/devolução sem emprestar o mesmo exemplar duas vezes.

**Conceitos:** `create_index`, `find_one_and_update`, `ReturnDocument`.

### Tutorial guiado

1. Cadastre um ISBN com título e autor. 2. Visualize o catálogo. 3. Empreste o livro pelo ISBN e tente emprestá-lo novamente. 4. Devolva e confirme que está disponível.

**Crie o arquivo** `p02_biblioteca/main.py` com o código abaixo:

```python
"""Projeto 02: livros com indice unico e emprestimo atomico."""
from pymongo import ReturnDocument
from pymongo.errors import DuplicateKeyError
from conexao import banco

livros = banco['livros_p02']
livros.create_index('isbn', unique=True)

while True:
    print('\n[1] Novo livro [2] Catálogo [3] Emprestar [4] Devolver [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        isbn, titulo = input('ISBN: ').strip(), input('Título: ').strip()
        autor = input('Autor: ').strip()
        if not all([isbn, titulo, autor]):
            print('Dados incompletos.'); continue
        try:
            livros.insert_one({'isbn': isbn, 'titulo': titulo, 'autor': autor,
                               'disponivel': True})
            print('Livro adicionado.')
        except DuplicateKeyError:
            print('ISBN já existe.')
    elif op == '2':
        for livro in livros.find({}, {'_id': 0}).sort('titulo'):
            print(livro)
    elif op == '3':
        isbn = input('ISBN: ').strip()
        livro = livros.find_one_and_update(
            {'isbn': isbn, 'disponivel': True},
            {'$set': {'disponivel': False}},
            return_document=ReturnDocument.AFTER)
        print('Empréstimo realizado.' if livro else 'Indisponível ou inexistente.')
    elif op == '4':
        isbn = input('ISBN: ').strip()
        livro = livros.find_one_and_update(
            {'isbn': isbn, 'disponivel': False},
            {'$set': {'disponivel': True}},
            return_document=ReturnDocument.AFTER)
        print('Devolução registrada.' if livro else 'Não estava emprestado.')
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p02_biblioteca.main
```
**Teste obrigatório:** A segunda tentativa de empréstimo deve ser recusada até que o livro seja devolvido.

**Desafios extras:**
1. Cadastrar leitor responsável.
2. Registrar data de empréstimo.
3. Criar histórico de devoluções.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p02`.

---
## 📦 03 — Controle de Estoque

**Nível:** Intermediário · **Tema:** Operador `$inc` e atualização atômica  
**Objetivo:** Cadastrar produtos e controlar entradas, saídas e alertas de estoque mínimo com atualização condicional.

**Conceitos:** `$inc`, `$gte`, `$expr`, `update_one`.

### Tutorial guiado

1. Cadastre o SKU `P100`. 2. Registre entrada de 20 unidades. 3. Registre saída de 5 unidades. 4. Tente retirar 50 unidades. 5. Consulte os itens com estoque baixo.

**Crie o arquivo** `p03_estoque/main.py` com o código abaixo:

```python
"""Projeto 03: estoque com entradas e saidas seguras."""
from pymongo.errors import DuplicateKeyError
from conexao import banco

produtos = banco['produtos_p03']
produtos.create_index('sku', unique=True)

def inteiro_positivo(rotulo):
    try:
        n = int(input(rotulo))
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        print('Digite um inteiro maior que zero.')
        return None

while True:
    print('\n[1] Cadastrar [2] Entrada [3] Saída [4] Estoque baixo [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        sku, nome = input('SKU: ').strip(), input('Produto: ').strip()
        minimo = inteiro_positivo('Estoque mínimo (>0): ')
        if not sku or not nome or minimo is None: continue
        try:
            produtos.insert_one({'sku': sku, 'nome': nome, 'quantidade': 0,
                                 'minimo': minimo})
            print('Cadastrado.')
        except DuplicateKeyError:
            print('SKU existente.')
    elif op in ('2', '3'):
        sku = input('SKU: ').strip()
        qtd = inteiro_positivo('Quantidade: ')
        if qtd is None: continue
        filtro = {'sku': sku}
        delta = qtd if op == '2' else -qtd
        if delta < 0:
            filtro['quantidade'] = {'$gte': qtd}
        r = produtos.update_one(filtro, {'$inc': {'quantidade': delta}})
        print('Movimentação realizada.' if r.modified_count else
              'Produto inexistente ou estoque insuficiente.')
    elif op == '4':
        # $expr permite comparar dois campos do mesmo documento.
        for p in produtos.find({'$expr': {'$lte': ['$quantidade', '$minimo']}}):
            print(f"{p['sku']} | {p['nome']} | {p['quantidade']} unidades")
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p03_estoque.main
```
**Teste obrigatório:** A saída acima do saldo deve ser recusada e a quantidade não poderá ficar negativa.

**Desafios extras:**
1. Guardar histórico de movimentações.
2. Criar relatório de valor de estoque.
3. Adicionar categorias.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p03`.

---
## 📇 04 — Agenda de Contatos

**Nível:** Iniciante · **Tema:** Filtros, regex e índices  
**Objetivo:** Criar uma agenda para cadastrar, localizar, atualizar e excluir contatos.

**Conceitos:** `$regex`, `$options`, `re.escape`, índices únicos.

### Tutorial guiado

1. Cadastre dois contatos com nomes diferentes. 2. Busque parte de um nome usando letras minúsculas. 3. Atualize um telefone. 4. Exclua o contato pelo e-mail.

**Crie o arquivo** `p04_contatos/main.py` com o código abaixo:

```python
"""Projeto 04: agenda com filtro por nome e indice unico."""
import re
from pymongo.errors import DuplicateKeyError
from conexao import banco

contatos = banco['contatos_p04']
contatos.create_index('email', unique=True)

while True:
    print('\n[1] Adicionar [2] Buscar [3] Atualizar [4] Remover [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        nome = input('Nome: ').strip()
        email = input('E-mail: ').strip().lower()
        telefone = input('Telefone: ').strip()
        if not all([nome, email, telefone]): continue
        try:
            contatos.insert_one({'nome': nome, 'email': email,
                                 'telefone': telefone})
            print('Contato salvo!')
        except DuplicateKeyError:
            print('E-mail já utilizado.')
    elif op == '2':
        trecho = input('Parte do nome: ').strip()
        if not trecho:
            print('Informe um termo.'); continue
        busca = {'nome': {'$regex': re.escape(trecho), '$options': 'i'}}
        for item in contatos.find(busca, {'_id': 0}).sort('nome'):
            print(item)
    elif op == '3':
        email = input('E-mail do contato: ').strip().lower()
        telefone = input('Novo telefone: ').strip()
        if telefone:
            r = contatos.update_one({'email': email}, {'$set': {'telefone': telefone}})
            print('Atualizado!' if r.matched_count else 'Contato não encontrado.')
    elif op == '4':
        email = input('E-mail: ').strip().lower()
        r = contatos.delete_one({'email': email})
        print('Excluído!' if r.deleted_count else 'Contato não encontrado.')
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p04_contatos.main
```
**Teste obrigatório:** A busca deve ignorar maiúsculas/minúsculas e o índice deve impedir e-mails repetidos.

**Desafios extras:**
1. Adicionar organização/empresa.
2. Validar e-mails corretamente.
3. Exportar contatos em CSV.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p04`.

---
## 💰 05 — Controle Financeiro

**Nível:** Intermediário · **Tema:** Agrupamento e precisão monetária  
**Objetivo:** Registrar receitas/despesas por categoria e produzir relatórios consolidados.

**Conceitos:** `$group`, `$sum`, `$sort`, `Decimal`.

### Tutorial guiado

1. Lance uma receita de 1500,00. 2. Lance duas despesas em categorias distintas. 3. Consulte o extrato. 4. Gere o resumo por categoria e confira o saldo.

**Crie o arquivo** `p05_financas/main.py` com o código abaixo:

```python
"""Projeto 05: receitas, despesas e agregacoes com valores em centavos."""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import datetime, timezone
from conexao import banco

lancamentos = banco['lancamentos_p05']

def centavos(texto):
    try:
        valor = Decimal(texto.replace(',', '.'))
        if not valor.is_finite() or valor <= 0:
            raise ValueError
        return int((valor * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    except (InvalidOperation, ValueError):
        return None

while True:
    print('\n[1] Registrar [2] Extrato [3] Resumo por categoria [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        tipo = input('Tipo (receita/despesa): ').strip().lower()
        categoria = input('Categoria: ').strip()
        valor = centavos(input('Valor (R$): ').strip())
        if tipo not in ('receita', 'despesa') or not categoria or valor is None:
            print('Dados inválidos.'); continue
        lancamentos.insert_one({'tipo': tipo, 'categoria': categoria,
                                'valor_centavos': valor,
                                'criado_em': datetime.now(timezone.utc)})
        print('Lançamento registrado.')
    elif op == '2':
        for item in lancamentos.find().sort('criado_em', -1).limit(30):
            print(f"{item['tipo']} | {item['categoria']} | R$ {item['valor_centavos']/100:.2f}")
    elif op == '3':
        pipeline = [
            {'$group': {'_id': {'tipo': '$tipo', 'categoria': '$categoria'},
                        'total': {'$sum': '$valor_centavos'}}},
            {'$sort': {'_id.tipo': 1, '_id.categoria': 1}}
        ]
        receitas = despesas = 0
        for item in lancamentos.aggregate(pipeline):
            tipo, categoria = item['_id']['tipo'], item['_id']['categoria']
            total = item['total']
            print(f'{tipo} / {categoria}: R$ {total/100:.2f}')
            if tipo == 'receita': receitas += total
            else: despesas += total
        print(f'SALDO: R$ {(receitas - despesas)/100:.2f}')
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p05_financas.main
```
**Teste obrigatório:** O saldo deve corresponder à soma das receitas menos a soma das despesas.

**Desafios extras:**
1. Filtrar por mês.
2. Permitir exclusão de lançamento.
3. Gerar relatório CSV.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p05`.

---
## ✅ 06 — Tarefas e Prazos

**Nível:** Intermediário · **Tema:** Datas e filtros compostos  
**Objetivo:** Cadastrar tarefas com prazo, listar pendências, concluir itens e identificar atrasos.

**Conceitos:** `ObjectId`, índices compostos, filtros por data.

### Tutorial guiado

1. Crie uma tarefa com data de ontem e outra para amanhã. 2. Liste pendências e copie o ID. 3. Conclua uma tarefa. 4. Liste as atrasadas.

**Crie o arquivo** `p06_tarefas/main.py` com o código abaixo:

```python
"""Projeto 06: tarefas com vencimento e filtro por situacao."""
from datetime import datetime, time, timezone, date
from bson import ObjectId
from conexao import banco

tarefas = banco['tarefas_p06']
tarefas.create_index([('concluida', 1), ('prazo', 1)])

while True:
    print('\n[1] Nova [2] Pendentes [3] Concluir [4] Atrasadas [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        titulo = input('Título: ').strip()
        try:
            dia = date.fromisoformat(input('Prazo (AAAA-MM-DD): ').strip())
        except ValueError:
            print('Data inválida.'); continue
        if not titulo: continue
        prazo = datetime.combine(dia, time.max, tzinfo=timezone.utc)
        tarefas.insert_one({'titulo': titulo, 'prazo': prazo, 'concluida': False})
        print('Tarefa cadastrada.')
    elif op == '2':
        for t in tarefas.find({'concluida': False}).sort('prazo', 1):
            print(f"{t['_id']} | {t['titulo']} | até {t['prazo'].date()}")
    elif op == '3':
        texto = input('ID da tarefa: ').strip()
        if not ObjectId.is_valid(texto):
            print('ID inválido.'); continue
        r = tarefas.update_one({'_id': ObjectId(texto)},
                               {'$set': {'concluida': True}})
        print('Concluída!' if r.matched_count else 'Não encontrada.')
    elif op == '4':
        filtro = {'concluida': False, 'prazo': {'$lt': datetime.now(timezone.utc)}}
        for t in tarefas.find(filtro).sort('prazo'):
            print(f"ATRASADA: {t['titulo']} | {t['prazo'].date()}")
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p06_tarefas.main
```
**Teste obrigatório:** A tela de atrasadas deve exibir somente tarefas vencidas que ainda não foram concluídas.

**Desafios extras:**
1. Adicionar prioridades.
2. Editar título e prazo.
3. Notificar tarefas próximas.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p06`.

---
## 🏫 07 — Turmas e Boletins

**Nível:** Intermediário · **Tema:** Relacionamentos e `$lookup`  
**Objetivo:** Cadastrar turmas/alunos, lançar notas por bimestre e calcular médias por estudante.

**Conceitos:** índices compostos, `upsert`, `$lookup`, `$avg`.

### Tutorial guiado

1. Cadastre a turma `ADS-A`. 2. Cadastre alunos nessa turma. 3. Lance notas de 1º e 2º bimestres. 4. Gere o boletim informando `ADS-A`.

**Crie o arquivo** `p07_turmas_notas/main.py` com o código abaixo:

```python
"""Projeto 07: duas colecoes e relatorio com $lookup."""
from pymongo.errors import DuplicateKeyError
from conexao import banco

turmas = banco['turmas_p07']
alunos = banco['alunos_p07']
notas = banco['notas_p07']
turmas.create_index('codigo', unique=True)
alunos.create_index('matricula', unique=True)
notas.create_index([('matricula', 1), ('bimestre', 1)], unique=True)

while True:
    print('\n[1] Turma [2] Aluno [3] Nota [4] Boletim [0] Sair')
    op = input('Opção: ').strip()
    try:
        if op == '1':
            codigo = input('Código da turma: ').strip()
            if codigo:
                turmas.insert_one({'codigo': codigo})
                print('Turma criada.')
        elif op == '2':
            matricula = input('Matrícula: ').strip()
            nome = input('Nome: ').strip()
            codigo = input('Código da turma: ').strip()
            if not all([matricula, nome, codigo]) or not turmas.find_one({'codigo': codigo}):
                print('Dados inválidos ou turma não existe.'); continue
            alunos.insert_one({'matricula': matricula, 'nome': nome, 'turma': codigo})
            print('Aluno cadastrado.')
        elif op == '3':
            matricula = input('Matrícula: ').strip()
            if not alunos.find_one({'matricula': matricula}):
                print('Aluno não existe.'); continue
            bimestre = int(input('Bimestre (1-4): '))
            valor = float(input('Nota (0-10): ').replace(',', '.'))
            if bimestre not in range(1, 5) or not 0 <= valor <= 10:
                print('Bimestre ou nota fora do intervalo.'); continue
            notas.update_one({'matricula': matricula, 'bimestre': bimestre},
                             {'$set': {'valor': valor}}, upsert=True)
            print('Nota salva.')
        elif op == '4':
            codigo = input('Código da turma: ').strip()
            pipeline = [
                {'$match': {'turma': codigo}},
                {'$lookup': {'from': 'notas_p07', 'localField': 'matricula',
                             'foreignField': 'matricula', 'as': 'notas'}},
                {'$project': {'_id': 0, 'matricula': 1, 'nome': 1,
                              'media': {'$avg': '$notas.valor'}}},
                {'$sort': {'nome': 1}}
            ]
            for a in alunos.aggregate(pipeline):
                media = f"{a['media']:.2f}" if a.get('media') is not None else 'sem notas'
                print(f"{a['matricula']} | {a['nome']} | média: {media}")
        elif op == '0':
            break
        else:
            print('Opção inválida.')
    except (ValueError, DuplicateKeyError):
        print('Dados inválidos ou registro duplicado.')
```

**Executar da raiz do repositório:**

```bash
python -m p07_turmas_notas.main
```
**Teste obrigatório:** O relatório deve mostrar a média das notas lançadas; alunos sem notas permanecem sem média.

**Desafios extras:**
1. Calcular média ponderada.
2. Listar aprovados e recuperação.
3. Exportar boletim em CSV.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p07`.

---
## 📝 08 — Corretor de Provas

**Nível:** Avançado · **Tema:** Validação e regras de negócio  
**Objetivo:** Criar gabaritos objetivos de A a E, registrar respostas de alunos e atribuir notas automaticamente.

**Conceitos:** `zip`, `$set`, `upsert`, índices compostos.

### Tutorial guiado

1. Crie a prova `BD01` com o gabarito `ABCDE`. 2. Corrija um aluno informando `ABCXE`. 3. Consulte a nota. 4. Corrija novamente o mesmo aluno e confira se o resultado foi atualizado.

**Crie o arquivo** `p08_corretor_provas/main.py` com o código abaixo:

```python
"""Projeto 08: prova objetiva A-E, gabarito e correcao automatica."""
from conexao import banco

provas = banco['provas_p08']
resultados = banco['resultados_p08']
provas.create_index('codigo', unique=True)
resultados.create_index([('prova', 1), ('aluno', 1)], unique=True)

while True:
    print('\n[1] Criar prova [2] Corrigir aluno [3] Resultados [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        codigo = input('Código da prova: ').strip()
        gabarito = input('Gabarito (ex.: ABCDE): ').strip().upper()
        if not codigo or not gabarito or any(c not in 'ABCDE' for c in gabarito):
            print('Código ou gabarito inválido.'); continue
        if provas.find_one({'codigo': codigo}):
            print('Código já utilizado.'); continue
        provas.insert_one({'codigo': codigo, 'gabarito': gabarito})
        print('Prova criada.')
    elif op == '2':
        codigo = input('Código da prova: ').strip()
        prova = provas.find_one({'codigo': codigo})
        if not prova:
            print('Prova não encontrada.'); continue
        aluno = input('Matrícula do aluno: ').strip()
        respostas = input('Respostas (A-E; X para em branco): ').strip().upper()
        if not aluno or len(respostas) != len(prova['gabarito']) or any(
                c not in 'ABCDEX' for c in respostas):
            print('Respostas inválidas ou quantidade incorreta.'); continue
        acertos = sum(a == b for a, b in zip(respostas, prova['gabarito']))
        nota = round(10 * acertos / len(prova['gabarito']), 2)
        resultados.update_one({'prova': codigo, 'aluno': aluno},
                              {'$set': {'respostas': respostas, 'acertos': acertos,
                                        'nota': nota}}, upsert=True)
        print(f'Resultado: {acertos}/{len(respostas)} | Nota: {nota:.2f}')
    elif op == '3':
        codigo = input('Código da prova: ').strip()
        for r in resultados.find({'prova': codigo}).sort('nota', -1):
            print(f"{r['aluno']} | {r['acertos']} acertos | Nota {r['nota']:.2f}")
    elif op == '0':
        break
    else:
        print('Opção inválida.')
```

**Executar da raiz do repositório:**

```bash
python -m p08_corretor_provas.main
```
**Teste obrigatório:** Com gabarito `ABCDE` e respostas `ABCXE`, a nota esperada é **8,0**.

**Desafios extras:**
1. Criar prova com pesos por questão.
2. Gerar ranking por turma.
3. Importar respostas de CSV.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p08`.

---
## 🌐 09 — API REST de Produtos

**Nível:** Avançado · **Tema:** FastAPI e MongoDB  
**Objetivo:** Expor endpoints REST para cadastrar, consultar, atualizar, listar e excluir produtos.

**Conceitos:** FastAPI, Pydantic, `ObjectId`, códigos HTTP.

### Tutorial guiado

1. Inicie o servidor com o comando da seção abaixo. 2. Acesse `/docs`. 3. Use **POST** para criar um produto. 4. Copie o `id` retornado e teste **GET**, **PUT** e **DELETE**.

**Crie o arquivo** `p09_api/main.py` com o código abaixo:

```python
"""Projeto 09: API REST CRUD de produtos com FastAPI + MongoDB."""
from bson import ObjectId
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from conexao import banco

app = FastAPI(title='API de Produtos - MongoDB', version='1.0')
produtos = banco['produtos_p09']

class ProdutoEntrada(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    preco_centavos: int = Field(ge=0)
    quantidade: int = Field(ge=0)

def serializar(p):
    return {'id': str(p['_id']), 'nome': p['nome'],
            'preco_centavos': p['preco_centavos'], 'quantidade': p['quantidade']}

def buscar(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, 'Identificador inválido')
    p = produtos.find_one({'_id': ObjectId(id)})
    if not p:
        raise HTTPException(404, 'Produto não encontrado')
    return p

@app.post('/produtos', status_code=201)
def criar(p: ProdutoEntrada):
    id = produtos.insert_one(p.model_dump()).inserted_id
    return serializar(produtos.find_one({'_id': id}))

@app.get('/produtos')
def listar(limite: int = Query(default=50, ge=1, le=100)):
    return [serializar(p) for p in produtos.find().limit(limite)]

@app.get('/produtos/{id}')
def consultar(id: str):
    return serializar(buscar(id))

@app.put('/produtos/{id}')
def atualizar(id: str, p: ProdutoEntrada):
    buscar(id)
    produtos.update_one({'_id': ObjectId(id)}, {'$set': p.model_dump()})
    return serializar(buscar(id))

@app.delete('/produtos/{id}', status_code=204)
def excluir(id: str):
    buscar(id)
    produtos.delete_one({'_id': ObjectId(id)})
    return None
```

**Executar da raiz do repositório:**

```bash
uvicorn p09_api.main:app --reload
```
**Abrir documentação interativa:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Use o botão **Try it out** para enviar dados de teste, por exemplo:

```json
{
  "nome": "Teclado mecânico",
  "preco_centavos": 19990,
  "quantidade": 12
}
```

> Para fins didáticos, a API não usa autenticação. **Não exponha este servidor à internet** sem autenticação, autorização, HTTPS e controles adicionais. O parâmetro `--reload` destina-se ao desenvolvimento local.
**Teste obrigatório:** O endpoint `GET /produtos/{id}` deve retornar 404 para IDs válidos que não existem e 400 para IDs malformados.

**Desafios extras:**
1. Adicionar paginação por cursor.
2. Implementar autenticação para escrita.
3. Criar testes com TestClient.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p09`.

---
## 📊 10 — Dashboard de Vendas

**Nível:** Avançado · **Tema:** Aggregation Pipeline e gráficos  
**Objetivo:** Gerar dados didáticos idempotentes, agrupar vendas por categoria e exportar gráfico em PNG.

**Conceitos:** `$group`, `$sum`, `$sort`, `matplotlib`, `upsert`.

### Tutorial guiado

1. Execute o projeto para inserir cinco vendas de exemplo. 2. Leia os totais por categoria no terminal. 3. Abra `p10_dashboard/grafico_vendas.png`. 4. Execute novamente e confirme que não há duplicação dos cinco registros.

**Crie o arquivo** `p10_dashboard/main.py` com o código abaixo:

```python
"""Projeto 10: agregacao de vendas e exportacao de grafico PNG."""
from datetime import datetime, timezone
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from conexao import banco

vendas = banco['vendas_p10']
vendas.create_index('codigo', unique=True)

def adicionar(codigo, categoria, produto, quantidade, preco_centavos):
    vendas.update_one({'codigo': codigo}, {'$setOnInsert': {
        'codigo': codigo, 'categoria': categoria, 'produto': produto,
        'quantidade': quantidade, 'total_centavos': quantidade * preco_centavos,
        'data': datetime.now(timezone.utc)}}, upsert=True)

# Demonstração idempotente: executar duas vezes não duplica estas vendas.
adicionar('V001', 'Informática', 'Teclado', 2, 8990)
adicionar('V002', 'Informática', 'Mouse', 4, 4590)
adicionar('V003', 'Papelaria', 'Caderno', 5, 2490)
adicionar('V004', 'Papelaria', 'Caneta', 20, 350)
adicionar('V005', 'Informática', 'Monitor', 1, 89900)

pipeline = [
    {'$group': {'_id': '$categoria', 'faturamento': {'$sum': '$total_centavos'},
                'unidades': {'$sum': '$quantidade'}}},
    {'$sort': {'faturamento': -1}}
]
dados = list(vendas.aggregate(pipeline))
if not dados:
    print('Sem dados de vendas.'); raise SystemExit(0)

print('RELATÓRIO DE VENDAS POR CATEGORIA')
for item in dados:
    print(f"{item['_id']}: {item['unidades']} unidades | R$ {item['faturamento']/100:.2f}")
print(f"Faturamento geral: R$ {sum(i['faturamento'] for i in dados)/100:.2f}")

plt.figure(figsize=(9, 5))
plt.bar([d['_id'] for d in dados], [d['faturamento']/100 for d in dados])
plt.ylabel('Faturamento (R$)')
plt.title('Vendas por categoria')
plt.tight_layout()
destino = Path(__file__).with_name('grafico_vendas.png')
plt.savefig(destino, dpi=150)
plt.close()
print(f'Gráfico gerado: {destino}')
```

**Executar da raiz do repositório:**

```bash
python -m p10_dashboard.main
```
**Teste obrigatório:** O gráfico deverá conter barras por categoria e o total deverá refletir as vendas armazenadas.

**Desafios extras:**
1. Filtrar vendas por período.
2. Mostrar os cinco produtos mais vendidos.
3. Gerar PDF de relatório.
**Conferência no Compass:** abra `laboratorio_python` e observe a coleção (ou as coleções) cujo nome termina em `p10`.

---
## 🧩 Problemas frequentes

| Situação | Provável causa | O que fazer |
|---|---|---|
| `ServerSelectionTimeoutError` | Servidor MongoDB parado, URI errada ou rede bloqueada | Inicie o Community Server; no Atlas confira IP autorizado e URI |
| `Authentication failed` | Usuário/senha inválidos no Atlas | Revise usuário do banco e credenciais da URI |
| `ModuleNotFoundError: pymongo` | Dependências não instaladas no ambiente ativo | Ative `.venv` e rode `python -m pip install -r requirements.txt` |
| `No module named conexao` | Execução fora da raiz do projeto | Use `python -m p01_alunos.main` estando na raiz |
| `DuplicateKeyError` | Valor duplicado em índice único | Use outro ISBN, matrícula, SKU ou e-mail |
| Porta 8000 ocupada | Outro serviço já usa a porta da API | Execute `uvicorn p09_api.main:app --reload --port 8001` |
| Compass abre, mas não conecta | Compass não inicia o banco sozinho | Confira o serviço MongoDB ou a URI Atlas |

## 📝 Critérios de avaliação

Pontuação total sugerida: **10,0 pontos**.

| Critério | Peso | Nota máxima | O que será observado |
|---|:---:|:---:|---|
| Funcionalidades implementadas | 35% | 3,5 | Operações solicitadas e resultados corretos |
| Modelagem e uso do MongoDB | 25% | 2,5 | Estrutura documental, consultas, índices e integridade |
| Organização do código Python | 20% | 2,0 | Funções, nomes, separação de responsabilidades e legibilidade |
| Testes e tratamento de erros | 10% | 1,0 | Entradas inválidas, falhas de conexão e casos limites |
| Documentação e demonstração | 10% | 1,0 | README, evidências e explicação do funcionamento |
| **Total** | **100%** | **10,0** | |

### Entrega sugerida dos alunos

- [ ] Código executa sem erro de sintaxe.
- [ ] Arquivos e dependências estão organizados.
- [ ] O MongoDB armazena e retorna os dados corretamente.
- [ ] As funcionalidades básicas foram demonstradas.
- [ ] Há evidências de execução (terminal, Compass e/ou API).
- [ ] Pelo menos um desafio extra foi implementado.
- [ ] O `.env` não foi publicado e as credenciais foram protegidas.
- [ ] Foi criado um README breve do projeto com execução e testes.

### Sugestão de relatório individual

1. **Objetivo:** explicar a finalidade do projeto.
2. **Ambiente:** listar Python, MongoDB e bibliotecas.
3. **Modelo de dados:** apresentar exemplo de documento e índices.
4. **Implementação:** descrever as funções e consultas.
5. **Testes:** registrar entradas, saídas e capturas de tela.
6. **Conclusão:** indicar dificuldades, melhorias e aprendizados.

## 🔐 Boas práticas e limites dos exemplos

Estes scripts são **exemplos educacionais**, não sistemas prontos para produção. Para uso real, acrescente autenticação/autorização, limites de acesso, validação robusta, logs apropriados, testes automatizados, backup e monitoramento. Use sempre contas de banco com os privilégios mínimos necessários e evite registrar dados sensíveis nos exercícios. Em especial, o projeto de prova deve usar **dados fictícios** quando não houver controles institucionais para dados de alunos.

## 📚 Referências oficiais

- [Documentação MongoDB](https://www.mongodb.com/docs/)
- [PyMongo — Getting Started](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
- [MongoDB Atlas — Conexão com drivers](https://www.mongodb.com/docs/atlas/driver-connection/)
- [Python — Ambientes virtuais](https://docs.python.org/pt-br/3/tutorial/venv.html)
- [FastAPI — Documentação](https://fastapi.tiangolo.com/)
- [Matplotlib — Documentação](https://matplotlib.org/stable/)

---

<div align="center">

### 🚀 Aprenda construindo, teste com dados reais de exemplo e evolua o código!

**Python + MongoDB = aplicações orientadas a dados.**

⭐ Se este repositório ajudar, deixe uma estrela no GitHub.

</div>
