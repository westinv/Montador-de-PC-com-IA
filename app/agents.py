import google.generativeai as genai
from config import settings

def build_pc_from_components(user_request: str, available_components: str) -> str:
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        safety_settings = {
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE',
        }

        prompt = f"""
        Você é um assistente especialista em montagem de computadores.
        Sua tarefa é montar o melhor PC possível para um cliente, seguindo o pedido dele e usando APENAS a lista de peças disponíveis.

        **Pedido do Cliente:**
        "{user_request}"

        **Regras Obrigatórias:**
        1.  **Orçamento é Rei:** Respeite o orçamento máximo informado no pedido do cliente. A soma dos preços das peças escolhidas NÃO PODE ULTRAPASSAR este valor. Se o pedido não mencionar um orçamento, monte a opção de menor custo que atenda à necessidade.
        2.  **Inventário Limitado:** Use SOMENTE as peças da "Lista de Componentes Disponíveis". Não invente peças ou características. A 'Descrição' é a principal fonte de informação sobre a peça.
        3.  **PC Funcional:** O PC montado deve ser funcional. Ele precisa ter, no mínimo: 1 CPU, 1 Placa-mãe, Memória RAM e 1 Fonte de Alimentação. Adicione uma Placa de Vídeo se o pedido for para jogos ou tarefas gráficas e o orçamento permitir.
        4.  **Compatibilidade:** Verifique a compatibilidade básica entre as peças (ex: processador de um soquete específico com placa-mãe do mesmo soquete).
        5.  **Cálculo Final:** Ao final, liste os componentes escolhidos com seus IDs e descrições, e calcule o preço total somando o preço de cada peça.

        **Lista de Componentes Disponíveis:**
        ---
        {available_components}
        ---

        **Formato da Resposta:**
        Comece com uma breve análise do pedido, explicando por que escolheu as peças para respeitar o orçamento e o objetivo.
        Depois, liste as peças escolhidas e o preço total da seguinte forma:

        Peças Escolhidas:
        - ID: [ID da peça] - Descrição: [Descrição da peça] - Preço: R$[preço]
        - ID: [ID da peça] - Descrição: [Descrição da peça] - Preço: R$[preço]
        ...

        **Preço Total: R$[soma dos preços]**
        """

        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Passamos as configurações de segurança na chamada da API
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings
        )

        return response.text

    except Exception as e:
        print(f"Erro na API do Gemini: {e}")
        raise ConnectionError("Não foi possível obter a recomendação do serviço de IA.")
