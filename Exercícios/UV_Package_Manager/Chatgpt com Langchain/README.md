# ChatGPT com LangChain e `uv`

Este é um projeto simples que utiliza o modelo `gpt-4o` da OpenAI via `LangChain`, com gerenciamento de dependências feito pelo poderoso gerenciador de pacotes [`uv`](https://docs.astral.sh/uv/).

---

## Sobre o Projeto

O script realiza uma pergunta via terminal ao usuário e envia essa entrada para o modelo `gpt-4o`, retornando uma resposta gerada por IA.

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

pergunta = input("O Que deseja saber?: ")
resposta = llm.invoke(str(pergunta))

print(resposta.content)
````

---

## Requisitos

* Python 3.8+
* Git Bash (ou outro terminal compatível no Windows)
* Conexão com a internet
* Uma chave de API da OpenAI (armazenada em um arquivo `.env`)

---

## Instalação do `uv`

[`uv`](https://docs.astral.sh/uv/) é um gerenciador de pacotes moderno, rápido e eficiente criado pela [Astral](https://astral.sh). Ele substitui `pip`, `virtualenv` e `pip-tools` com uma única ferramenta.

### 1. Instalar o `uv`

No terminal (ex: Git Bash), execute:

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

Se necessário, adicione `uv` ao seu PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verifique se funcionou:

```bash
uv --version
```

---

### 2. Inicializar o projeto com `uv`

Crie o ambiente virtual e configure o projeto:

```bash
uv init .
```

---

### 3. Adicionar as dependências

Adicione os pacotes necessários:

```bash
uv add python-dotenv
uv add langchain-openai
```

> Obs: `python-dotenv` carrega variáveis do `.env`; `langchain-openai` integra com a API da OpenAI.

---

### 4. Criar o arquivo `.env`

Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 5. Rodar o projeto

Execute o script com:

```bash
uv run main.py
```

---

## 📄 Documentação oficial do `uv`

Acesse a documentação completa aqui:
🔗 [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## 🧠 Exemplos de uso

```bash
$ uv add requests
$ uv remove numpy
$ uv sync
$ uv pip freeze
```

---

## ✅ Benefícios de usar `uv`

* ⚡ Ultra-rápido (usa Rust)
* 🛠️ Substitui `pip`, `venv` e `pip-tools`
* 🔄 Sincronização automática de ambientes
* 📦 Cache inteligente de pacotes

