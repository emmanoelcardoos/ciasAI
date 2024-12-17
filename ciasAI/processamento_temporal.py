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
        dados = open_file("/Users/emmanoelcardoso/Desktop/ciasAI/dados/Tweets.csv")
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

def dia_com_mais_tweets() -> Optional[Tuple[datetime.date, int]]:
    """
    Identifica o dia com o maior número de tweets.

    Returns:
        Optional[Tuple[datetime.date, int]]: Dia com mais tweets e o total de tweets ou None em caso de falha.
    """
    dados = carregar_dados()
    if dados is None:
        print("Não foi possível carregar os dados.")
        return None

    contagem_dias = {}
    for tweet in dados:
        # Apenas considerar a data dos tweets
        data_tweet = tweet['tweet_created'].date()
        contagem_dias[data_tweet] = contagem_dias.get(data_tweet, 0) + 1

    if not contagem_dias:
        print("Nenhum dado válido para análise foi encontrado.")
        return None

    dia_mais_tweets = max(contagem_dias, key=contagem_dias.get)
    total_tweets = contagem_dias[dia_mais_tweets]

    print(f"Dia com mais tweets: {dia_mais_tweets}, Total de tweets: {total_tweets}")
    return dia_mais_tweets, total_tweets


