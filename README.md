## Este projeto envolve as seguintes partes: Web Scraping, Transformação de dados, Banco de dados (PgAdmin), API.

---

# 📊 Web Scraping

# 📥 Download e Compactação de Arquivos da ANS

Este projeto automatiza o processo de download de anexos do site da ANS (Agência Nacional de Saúde Suplementar) e compacta todos os arquivos em um único `.zip`.

---

## 🚀 O que o script faz

1. Limpa a pasta de destino dos arquivos.
2. Faz web scraping na página da ANS para baixar anexos.
3. Compacta os arquivos baixados em um arquivo `.zip`.

---

## 🛠 Estrutura do Projeto

- `main.py` — script principal com a função `download_compress_files()`.
- `clear_directory.py` — função para limpar diretórios.
- `download_attachments.py` — função que realiza o web scraping e download dos arquivos.
- `compress_files.py` — função que compacta os arquivos em `.zip`.
- `files` - onde os arquivos em PDF são salvos.
- `zip_files` - onde os arquivos são compactados em formato `.zip`.
- `files` - onde está o arquivo `.csv`.

---

## 🛠 Tecnologias utilizadas
 - Python 3
 - pathlib
 - zipfile
 - Selenium
 - selenium.webdriver.chrome.service
 - selenium.webdriver.common.by
 - selenium.webdriver.chrome.options
 - webdriver_manager.chrome
 - time

 ---

# 📃 Extração de Tabelas do PDF da ANS (trasnformação de dados)

 Este script realiza a extração de tabelas contidas no PDF oficial da ANS e salva os dados em um arquivo CSV. Em seguida, o CSV é compactado em um `.zip`.

---

## 🚀 O que o script faz

1. Lê um arquivo PDF com tabelas da ANS.
2. Extrai as tabelas de cada página usando `pdfplumber`.
3. Trata os dados e renomeia algumas colunas.
4. Salva os dados extraídos como `CSV`.
5. Compacta o CSV em um arquivo `.zip`.


---

## 🛠 Estrutura do Projeto

- `main.py` — script principal que faz a extração e compactação.
- `compress_files.py` — função auxiliar para criar arquivos `.zip`.
- `clear_directory.py` — função auxiliar para limpar diretórios.
- `Extracted_tables` - salva o arquivo `.csv`.
- `zip_files` - salva o arquivo em formato `.zip`.

---

# 📃 Banco de dados (pgAdmin, pasta "queries")
Este script em Python realiza a leitura de um arquivo .csv com valores monetários no formato brasileiro (com vírgula como separador decimal), converte esses valores para o formato padrão com ponto decimal (necessário para operações numéricas em Python) e salva um novo arquivo corrigido.

📂 Funcionalidade:

- `generate_convert` :
- Lê um arquivo CSV original com separador ;.

- Converte as colunas VL_SALDO_INICIAL e VL_SALDO_FINAL de string para float, - trocando vírgulas por pontos.

- Salva o resultado em um novo arquivo CSV com os valores numéricos corrigidos.

- `generate_insert`:

Este script em Python realiza a importação de dados de um arquivo .csv para uma tabela existente em um banco de dados PostgreSQL, utilizando a função COPY.

📂 Funcionalidade:

- Conecta-se a um banco PostgreSQL local.

- Lê um arquivo CSV corrigido.

- Importa os dados (ignorando o cabeçalho) diretamente para a tabela definida.

---

## 🚀 API de Busca com FastAPI

Este projeto é uma API simples criada com FastAPI que permite realizar buscas a partir de uma query, utilizando uma função find() localizada em um módulo de repositório.

## 📦 Funcionalidades
- Rota de busca com parâmetro de consulta: /search?query=...

- Suporte a CORS para qualquer origem (útil para integração com front-ends)

- Pronta para rodar localmente com o Uvicorn

 **🛠 Tecnologias utilizadas:**

- Python 3
- FastAPI
- Uvicorn
- psycopg2
- PostgreSQL
- Nodejs
- vue.js



---


## 🧰 Requisitos

- Python 3
- Bibliotecas necessárias (coloque no `requirements.txt`):


## ▶️ Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```
---
Obs:  Não esqueça te ativar sua venv

✍️ Autor :

Jhonatan Sumback — @jholsumback
