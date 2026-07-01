# 🛒 Product Price Tracker

Sistema de monitoramento de preços de produtos utilizando web scraping para acompanhar variações de valores em diferentes lojas online.

---

# 🎯 Objetivo

O objetivo do projeto é permitir que produtos de interesse sejam cadastrados e monitorados automaticamente.

O sistema realiza consultas periódicas em páginas de produtos previamente cadastradas, coleta informações como nome e preço, armazena o histórico de valores e permite acompanhar variações ao longo do tempo.

A aplicação foi pensada para uso pessoal, funcionando como um rastreador de preços simples e automatizado.

---

# 🏗️ Arquitetura

O projeto segue uma arquitetura baseada em coleta, processamento e persistência de dados.

## 🔁 Fluxo geral

```
                Cron Scheduler
                      |
                      v
                Docker (PostgreSQL)
                      |
                      v
              Scrapy Price Tracker
                      |
          +-----------+-----------+
          |                       |
          v                       v
    Product Spider        Data Pipeline
                                  |
                                  v
                        Repository Layer
                                  |
                                  v
                          PostgreSQL DB
```

---

# 🧩 Componentes

## 🕷️ Scrapy Spider

Responsável pela coleta das informações dos produtos.

A spider recebe uma lista de URLs previamente configuradas e realiza requisições para cada página de produto.

### Responsabilidades:

- Acessar páginas de produtos
- Extrair informações via seletores CSS/XPath
- Criar itens estruturados para processamento

### Exemplo de dados extraídos:

```
Nome: Notebook Gamer Lenovo
Preço: R$ 3.999,90
URL: https://loja.com/produto
```

---

## 🔄 Item Pipeline

Camada responsável pelo processamento dos dados coletados.

### Responsabilidades:

- Validar dados extraídos
- Normalizar valores (ex: preços)
- Encaminhar dados para persistência
- Aplicar regras de negócio

---

## 🗄️ Repository Layer

Camada responsável pela comunicação com o banco de dados.

### Responsabilidades:

- Criar produtos se não existirem
- Registrar histórico de preços
- Consultar produtos monitorados

---

## 🧱 Banco de Dados

O sistema utiliza PostgreSQL para armazenar os dados.

### 📦 Tabela: products

```
id
name
url
store
created_at
```

---

### 📈 Tabela: price_history

```
id
product_id
price
checked_at
```

---

# ⚙️ Tecnologias

## 🕷️ Scraping

### Scrapy

Framework utilizado para coleta de dados.

Responsável por:

- Gerenciamento de spiders
- Requisições HTTP
- Processamento de itens
- Pipelines

---

## 🗄️ Persistência

### PostgreSQL

Banco de dados relacional utilizado para armazenar produtos e histórico de preços.

---

### 🐍 SQLAlchemy

ORM utilizado para integração com o banco.

Responsável por:

- Mapeamento de entidades
- Consultas
- Persistência de dados

---

## 🐳 Infraestrutura

### Docker

Utilizado para subir o ambiente do PostgreSQL de forma isolada e reproduzível.

---

## ⏱️ Automação

### Cron

Utilizado para agendar execuções periódicas do scraper.

---

# 📁 Estrutura do Projeto

```
product_scraper/

├── spiders/
│   └── product.py
│
├── items.py
├── pipelines.py
│
├── services/
│   └── normalizer.py
│
├── storage/
│   ├── database.py
│   ├── models.py
│   └── repository.py
│
├── settings.py
├── scrapy.cfg
```

---

# 🚀 Configuração e Execução

## 📦 Pré-requisitos

- Docker
- Docker Compose
- Python 3.10+
- pip

---

## 🐍 Ambiente virtual

Criação:

```bash
python3 -m venv .venv
```

Ativação:

```bash
source .venv/bin/activate
```

Instalação de dependências:

```bash
pip install -r requirements.txt
```

Dependências:

```
scrapy
sqlalchemy
psycopg2-binary
```

---

## 🐳 Subindo o banco de dados

```bash
docker compose up -d
```

Configuração padrão:

```
Database: products
User: scraper
Password: senha123
Port: 5432
```

---

## 🌐 Variáveis de ambiente

As URLs dos produtos são definidas via variável de ambiente:

```bash
export PRODUCT_URLS="https://site1.com/produto,https://site2.com/produto"
```

---

## ▶️ Execução do scraper

```bash
scrapy crawl product
```

---

## 🔁 Fluxo de execução

```
Variáveis de ambiente (PRODUCT_URLS)
            ↓
      Cron Scheduler
            ↓
   Docker (PostgreSQL)
            ↓
      Scrapy Spider
            ↓
   Extração de dados
            ↓
        Pipeline
            ↓
      Repository (SQLAlchemy)
            ↓
     PostgreSQL
```

---

# 🧠 Observações

- O sistema foi projetado para uso pessoal e monitoramento de preços.
- Não realiza crawling de sites inteiros, apenas coleta dados de URLs previamente cadastradas.
- Cada execução registra um novo histórico de preço.
- O foco do projeto é simplicidade e automação local.
- A infraestrutura pode ser iniciada e finalizada sob demanda via Docker.

---

# 🔮 Futuras melhorias

- Dashboard web para visualização de preços
- Gráficos de histórico de preços
- Sistema de alertas (queda de preço)
- Suporte a múltiplas lojas
- Execução containerizada do scraper
- Sistema de agendamento interno (sem cron externo)

---
