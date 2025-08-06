Montador de PC com IA (POC)
Bem-vindo esta é uma aplicação API que utiliza o poder do modelo de linguagem Google Gemini para agir como um assistente virtual especialista em hardware. A partir de uma lista de componentes disponíveis (o seu inventário) e um pedido do cliente, a IA monta o melhor computador possível, respeitando as necessidades e o orçamento definidos.

✨ Funcionalidades
Análise de Linguagem Natural: Entende pedidos complexos dos utilizadores, como "Quero um PC para streaming de jogos com um orçamento de 10.000 reais".

Montagem Inteligente: Seleciona componentes de uma lista pré-definida, considerando compatibilidade básica e otimizando o custo-benefício.

Orçamento Consciente: A IA é instruída a respeitar rigorosamente o orçamento máximo estipulado no pedido.

API Robusta: Construída com FastAPI, oferece uma interface RESTful rápida, com documentação interativa automática (Swagger UI).

Ambiente Isolado: Totalmente containerizada com Docker, garantindo que a aplicação funcione de forma consistente em qualquer ambiente.

🛠️ Tecnologias Utilizadas
Backend: Python 3.10

Framework API: FastAPI

Servidor ASGI: Uvicorn

Inteligência Artificial: Google Gemini 1.5 Flash API

Manipulação de Dados: Pandas

Containerização: Docker

📊 Estrutura da Planilha (produtos.xlsx)
Para que a aplicação funcione corretamente, a sua planilha de inventário, localizada em data/produtos.xlsx, deve ter a seguinte estrutura. O código é flexível quanto a maiúsculas/minúsculas e acentos nos cabeçalhos, mas a presença das três colunas é obrigatória.

cf

descricao

preco

885086

Ssd Kingston Pcie Nv3, 2tb, Nvme, Leitura 6000mb/S

500.00

42456356

Fonte Gamer Redragon Rgps 600w, 80 Plus, Bronze

800.50

708330

Memória Ram Kingston Fury Beast, 16gb, 6000mt/S, Ddr5

700.00

...

...

...

cf: ID ou qualquer identificador único do produto.

descricao: Uma descrição clara e completa do componente. A IA usa esta coluna como principal fonte de informação sobre a peça.

preco: O preço do componente, em formato numérico (ex: 500 ou 800.50).

🚀 Como Executar
Siga estes passos para colocar a aplicação a funcionar localmente.

1. Pré-requisitos
   Docker instalado e em execução.

Git instalado.

Uma chave de API do Google AI Studio.

2. Clone o Repositório
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

3. Crie o Ficheiro de Ambiente
   Crie um ficheiro chamado .env na raiz do projeto. Este ficheiro guardará a sua chave de API de forma segura.

# .env

GEMINI_API_KEY="SUA_CHAVE_API_AQUI"

Substitua "SUA_CHAVE_API_AQUI" pela sua chave real da API do Gemini.

4. Construa a Imagem Docker
   Execute o seguinte comando na raiz do projeto. Ele irá ler o Dockerfile e construir a imagem da sua aplicação.

docker build -t montador-pc-ia .

5. Execute o Container
   Agora, inicie um container a partir da imagem que acabou de criar.

docker run --rm -p 8000:8000 --env-file .env montador-pc-ia

--rm: Remove o container automaticamente quando ele é parado.

-p 8000:8000: Mapeia a porta 8000 da sua máquina para a porta 8000 do container.

--env-file .env: Carrega as variáveis de ambiente (a sua chave de API) do ficheiro .env.

A sua API está agora em execução e acessível em http://localhost:8000.

🤖 Uso da API
Você pode interagir com a API de duas formas:

Documentação Interativa (Swagger UI): Abra o seu browser e navegue para http://localhost:8000/docs.

Cliente de API (Insomnia, Postman, cURL):

Endpoint: POST /build-pc

URL: http://localhost:8000/build-pc

Body (JSON):

{
"user_request": "Monte um PC para rodar Call of Duty Warzone com um orçamento de 10.000 reais"
}

Exemplo com cURL:

curl -X 'POST' \
 'http://localhost:8000/build-pc' \
 -H 'Content-Type: application/json' \
 -d '{
"user_request": "Monte um PC para rodar Call of Duty Warzone com um orçamento de 10.000 reais"
}'

⚠️ Notas Importantes
Timeout do Cliente: A chamada para a API do Gemini pode demorar vários segundos. Clientes de API como o Insomnia podem ter um timeout padrão baixo (ex: 30 segundos). Se receber erros de timeout, aumente o tempo de espera nas configurações do seu cliente.

Limites da API Gemini: Se estiver a usar o plano gratuito, existem limites de requisições por dia (ex: 50). Se receber um erro 429 Quota Exceeded, significa que atingiu o seu limite diário.
