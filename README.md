# Product Price Tracker

Sistema de monitoramento de preços de produtos utilizando web scraping para acompanhar alterações de valores em diferentes lojas online.

## Objetivo

O objetivo do projeto é permitir que produtos de interesse sejam cadastrados e monitorados automaticamente. O sistema realiza consultas periódicas nas páginas dos produtos, coleta informações como nome e preço, armazena o histórico de valores e permite acompanhar variações ao longo do tempo.

A aplicação foi pensada para uso pessoal, funcionando como um rastreador de preços para produtos específicos, evitando a necessidade de verificar manualmente diversas lojas.

---

# Arquitetura

O projeto utiliza uma arquitetura baseada em coleta de dados, processamento e persistência.

Fluxo geral:

```
                    Cron Scheduler

                          |
                          v

                  Scrapy Price Tracker

                          |
                          v

              +-----------------------+
              |                       |
              v                       v

        Product Spider          Data Pipeline

              |                       |
              +-----------+-----------+

                          |

                    Repository Layer

                          |

                          v

                    PostgreSQL Database
```

## Componentes

### Scrapy Spider

Responsável pela coleta das informações dos produtos.

A Spider recebe as URLs dos produtos monitorados e realiza as requisições para as páginas das lojas.

Responsabilidades:

- acessar páginas de produtos;
- extrair informações utilizando seletores CSS/XPath;
- gerar objetos de produto para processamento.

Exemplo de dados coletados:

```
Nome:
Notebook Gamer Lenovo

Preço:
R$ 3999

URL:
https://loja.com/produto
```

---

## Item Pipeline

Camada responsável pelo processamento dos dados coletados.

Responsabilidades:

- validar informações extraídas;
- normalizar dados;
- encaminhar para persistência;
- aplicar regras de negócio.

Fluxo:

```
Spider

   |
   v

Product Item

   |
   v

Pipeline

   |
   v

Database
```

---

## Repository

Camada responsável pela comunicação com o banco de dados.

O objetivo é manter a regra de persistência separada da lógica de scraping.

Responsabilidades:

- salvar produtos;
- registrar histórico de preços;
- consultar produtos monitorados.

---

## Banco de Dados

O sistema utiliza PostgreSQL para armazenar:

### Produtos monitorados

Exemplo:

```
products

id
name
url
store
created_at
```

### Histórico de preços

Exemplo:

```
price_history

id
product_id
price
checked_at
```

O histórico permite analisar alterações de preço ao longo do tempo.

---

# Tecnologias

## Scraping

### Scrapy

Framework utilizado para realizar a coleta de dados das páginas.

Responsável por:

- gerenciamento das spiders;
- requisições HTTP;
- processamento dos itens;
- pipelines;
- controle de execução.

---

## Persistência

### PostgreSQL

Banco de dados relacional utilizado para armazenar produtos e histórico de preços.

---

### SQLAlchemy

ORM utilizado para comunicação entre Python e PostgreSQL.

Responsável por:

- criação dos modelos;
- consultas;
- operações de persistência.

---

# Estrutura do Projeto

```
product_scraper/

├── spiders/
│   ├── product.py
│
├── items.py
│
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
│
└── scrapy.cfg
```

---

# Futuras melhorias

Possíveis evoluções:

- dashboard web para visualizar preços;
- notificações por email ou mensagem;
- suporte para múltiplas lojas;
- gráficos de histórico de preço;
- execução utilizando Docker;

---

## Configuração e Execução

Esta seção descreve como configurar e executar o projeto localmente utilizando Docker, PostgreSQL e Scrapy.

---

# Pré-requisitos

Antes de iniciar, você precisa ter instalado:

- Docker
- Docker Compose
- Python 3.10+
- pip

---

# Subindo o banco de dados (PostgreSQL)

O projeto utiliza Docker para subir o banco de dados.

Execute na raiz do projeto:

```bash
docker compose up -d
```

Isso irá iniciar o container do PostgreSQL com as seguintes configurações:

- Banco: `products`
- Usuário: `scraper`
- Senha: `senha123`
- Porta: `5432`

---

# Variáveis de ambiente

O sistema utiliza variáveis de ambiente para definir quais produtos serão monitorados.

Exemplo:

```bash
export AMAZON_PRODUCT_URLS="https://site1.com/produto,https://site2.com/produto"
```

Cada URL deve ser separada por vírgula.

---

# Executando o scraper

Após configurar o banco e as variáveis de ambiente, execute o crawler:

```bash
scrapy crawl product
```

---

# O que acontece ao executar

Ao rodar o scraper, o fluxo é o seguinte:

```
Variáveis de ambiente (PRODUCT_URLS)
            ↓
      Scrapy Spider
            ↓
   Extração de dados (nome, preço, URL)
            ↓
        Pipeline
            ↓
      Repository (SQLAlchemy)
            ↓
     PostgreSQL (Docker)
```

---

# Persistência dos dados

O sistema armazena dois tipos de informação:

## Produtos monitorados

Tabela `products`:

- id
- name
- url
- store
- created_at

---

## Histórico de preços

Tabela `price_history`:

- id
- product_id
- price
- checked_at

---

# Execução automatizada (Cron)

Para rodar o monitoramento automaticamente diariamente:

```bash
0 8 * * * AMAZON_PRODUCT_URLS="..." scrapy crawl product
```

---

# Exemplo completo de execução

```bash
# 1. subir banco
docker compose up -d

# 2. exportar URLs
export PRODUCT_URLS="https://site.com/produto1,https://site.com/produto2"

# 3. rodar scraper
scrapy crawl product
```

---

# Observações

- O scraper foi projetado para uso pessoal e monitoramento de preços.
- Cada execução cria um registro no histórico de preços.
- O sistema pode ser evoluído para envio de alertas e dashboard web.
