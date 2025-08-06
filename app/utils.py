import pandas as pd
from typing import List, Dict

def ler_planilha_produtos(caminho_arquivo: str) -> List[Dict]:
    try:
        df = pd.read_excel(caminho_arquivo)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        return []