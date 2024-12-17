from typing import List, Dict, Optional, Tuple
from .leitor_dados import open_file  # Usando open_file para carregar os dados
from datetime import datetime

def carregar_dados() -> Optional[List[Dict[str, str]]]:
    """
    Carrega os dados do arquivo CSV e converte a coluna de datas para objetos datetime.

    Returns:
        Optional[List[Dict[str, str]]]: Dados processados ou None em caso de falha.
    """
    try:
        dados = open_file("")
        if dados:
            for tweet in dados:
                tweet['tweet_created'] = datetime.strptime(tweet['tweet_created'], "%Y-%m-%d %H:%M:%S %z")
        return dados
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def contar_tweets_por_periodo(ano: int, mes: Optional[int] = None) -> int:
    """
    Conta o número de tweets publicados em um ano e opcionalmente em um mês específico.

    Args:
        ano (int): Ano para filtrar os tweets.
        mes (Optional[int]): Mês para filtrar os tweets (opcional).

    Returns:
        int: Total de tweets no período especificado.
    """
    if not ano:
        raise ValueError("Por favor, forneça ao menos o ano para a análise.")

    dados = carregar_dados()
    if dados is None:
        print("Não foi possível carregar os dados.")
        return 0

    total_tweets = 0
    for tweet in dados:
        if tweet['tweet_created'].year == ano:
            if mes:
                if tweet['tweet_created'].month == mes:
                    total_tweets += 1
            else:
                total_tweets += 1

    print(f"Total de tweets no período: {total_tweets}")
    return total_tweets

# processamento_temporal.py

def dia_com_mais_tweets(dados):
    """
    Função para determinar o dia com mais tweets no conjunto de dados
    sem usar pandas, apenas com listas e operações básicas.
    :param dados: Conjunto de dados com as informações carregadas por open_file()
    :return: Data com mais tweets.
    """
    try:
        # Contagem de ocorrências de datas com listas e dicionários
        contagem_datas = {}
        
        # Iterar sobre as linhas dos dados
        for tweet in dados:
            data = tweet.get("data")  # Obtendo o campo de data
            if data:  # Se a data existir
                if data in contagem_datas:
                    contagem_datas[data] += 1
                else:
                    contagem_datas[data] = 1

        # Encontrar a data com maior contagem
        if contagem_datas:
            dia_mais_tweets = max(contagem_datas, key=contagem_datas.get)  # Data com maior número de ocorrências
            return dia_mais_tweets
        else:
            return None
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
        return None



