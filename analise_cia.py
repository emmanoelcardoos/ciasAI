import logging
from collections import Counter
from typing import List, Dict

logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def realizar_login(user: str, password: str) -> bool:
    if user == "main" and password == "123456":
        logging.info(f"Login bem-sucedido para o utilizador: {user}")
        return True
    else:
        logging.info(f"Tentativa de login falhou para o utilizador: {user}")
        return False

def total_tweets_por_companhia(data: List[Dict[str, str]]) -> Dict[str, int]:
    contagem = Counter(row['airline'] for row in data)
    return dict(contagem)

def listar_companhias(data: List[Dict[str, str]]) -> List[str]:
    companhias = {row['airline'] for row in data}
    return list(companhias)

def filtrar_tweets_por_companhia(data: List[Dict[str, str]], companhia: str) -> List[Dict[str, str]]:
    return [row for row in data if row['airline'] == companhia]


def companhia_com_mais_tweets_negativos(data: List[Dict[str, str]]) -> str:
    negativos = [row['airline'] for row in data if row['airline_sentiment'] == 'negative']
    contagem_negativos = Counter(negativos)
    return max(contagem_negativos, key=contagem_negativos.get) if contagem_negativos else "Nenhuma companhia com tweets negativos"
