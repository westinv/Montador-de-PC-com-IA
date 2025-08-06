# 🧠 Montador de PC com IA (Prova de Conceito)

Bem-vindo! Esta é uma aplicação de API que utiliza o poder do modelo de linguagem **Google Gemini** para agir como um assistente virtual especialista em hardware.

A partir de uma lista de componentes disponíveis (o seu inventário) e um pedido do cliente, a IA monta o **melhor computador possível**, respeitando as necessidades e o orçamento definidos.

---

## ✨ Funcionalidades

- **🔍 Análise de Linguagem Natural**  
  Compreende pedidos complexos como:  
  _"Quero um PC para streaming de jogos com um orçamento de 10.000 reais"._

- **🧠 Montagem Inteligente**  
  Seleciona componentes compatíveis e com melhor custo-benefício, com base no seu inventário.

- **💰 Orçamento Consciente**  
  A IA respeita rigorosamente o orçamento máximo estipulado no pedido.

- **⚡ API Rápida e Intuitiva**  
  Desenvolvida com **FastAPI**, com documentação interativa automática via Swagger UI.

- **📦 Ambiente Isolado**  
  Containerizada com **Docker**, garantindo execução consistente em qualquer máquina.

---

## 🛠️ Tecnologias Utilizadas

| Componente              | Tecnologia                     |
|-------------------------|--------------------------------|
| **Backend**             | Python 3.10                    |
| **Framework API**       | FastAPI                        |
| **Servidor ASGI**       | Uvicorn                        |
| **IA**                  | Google Gemini 1.5 Flash API    |
| **Manipulação de Dados**| Pandas                         |
| **Containerização**     | Docker                         |

---

## 📊 Estrutura da Planilha (`data/produtos.xlsx`)

A aplicação espera uma planilha com os seguintes campos obrigatórios:

| cf      | descricao                                                          | preco   |
|---------|---------------------------------------------------------------------|---------|
| 885086  | Ssd Kingston Pcie Nv3, 2tb, Nvme, Leitura 6000mb/S                  | 500.00  |
| 42456356| Fonte Gamer Redragon Rgps 600w, 80 Plus, Bronze                     | 800.50  |
| 708330  | Memória Ram Kingston Fury Beast, 16gb, 6000mt/S, Ddr5               | 700.00  |
| ...     | ...                                                                 | ...     |

- `cf`: ID ou identificador único do produto  
- `descricao`: Descrição completa do componente (utilizada pela IA)  
- `preco`: Preço em formato numérico (ex: `500` ou `800.50`)

> **Observação**: Os nomes das colunas são tratados de forma flexível quanto a maiúsculas/minúsculas e acentuação.

---

## 🚀 Como Executar Localmente

### ✅ Pré-requisitos

- [Docker](https://www.docker.com/) instalado e em execução  
- [Git](https://git-scm.com/) instalado  
- Uma **chave de API do Google Gemini** (crie via [Google AI Studio](https://makersuite.google.com/app))

🚀 Execute o container
docker run --rm -p 8000:8000 --env-file .env montador-pc-ia

Após isso, sua API estará disponível em:
👉 http://localhost:8000

E a documentação Swagger em:
👉 http://localhost:8000/docs
