import csv
from typing import List, Dict, Optional

def open_file(file_path: str) -> Optional[List[Dict[str, str]]]:
    """
    Carrega os dados de um arquivo CSV e retorna uma lista de dicionários com os dados.

    Args:
        file_path (str): Caminho para o arquivo CSV.

    Returns:
        Optional[List[Dict[str, str]]]: Lista de dicionários com os dados carregados 
        do arquivo CSV ou None se houver erro.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            dados = [linha for linha in csv_reader]
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None


