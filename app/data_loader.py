import pandas as pd
import unicodedata
from typing import Optional

DATA_FILE_PATH = "data/produtos.xlsx"

def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return str(text)
    
    nfkd_form = unicodedata.normalize('NFKD', text)
    text = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    return text.lower().strip()


def get_available_components_as_text() -> Optional[str]:
    try:
        df = pd.read_excel(DATA_FILE_PATH)

        df.columns = [normalize_text(col) for col in df.columns]

        required_columns = ['cf', 'descricao', 'preco']
        if not all(col in df.columns for col in required_columns):
            print(f"ERRO CRÍTICO: A planilha deve conter as colunas: {required_columns}. Colunas encontradas: {list(df.columns)}")
            return None

        component_list = []
        for index, row in df.iterrows():
            component_str = (
                f"ID: {str(row['cf']).strip()}, "
                f"Descrição: {str(row['descricao']).strip()}, "
                f"Preço: R${float(row['preco']):.2f}"
            )
            component_list.append(component_str)

        if not component_list:
            return ""

        return "\n".join(component_list)

    except FileNotFoundError:
        print(f"ERRO CRÍTICO: Arquivo de dados não encontrado em '{DATA_FILE_PATH}'")
        return None
    except Exception as e:
        print(f"ERRO ao ler a planilha de componentes: {e}")
        return None
