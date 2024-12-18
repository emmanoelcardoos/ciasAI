from typing import List, Dict, Optional
from datetime import datetime
import os
import csv


def open_file(caminho: str) -> Optional[List[Dict[str, str]]]:
    """
    Função para abrir e carregar dados de um arquivo CSV.
    :param caminho: Caminho para o arquivo CSV.
    :return: Lista de dicionários com os dados ou None em caso de falha.
    """
    try:
        
        if not os.path.isfile(caminho): 
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

        with open(caminho, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return [linha for linha in leitor]
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None


def carregar_dados(caminho: Optional[str] = None) -> Optional[List[Dict[str, str]]]:
    """
    Carrega os dados do arquivo CSV e converte a coluna de datas para objetos datetime.

    Args:
        caminho (Optional[str]): Caminho para o arquivo CSV.

    Returns:
        Optional[List[Dict[str, str]]]: Dados processados ou None em caso de falha.
    """
    try:
        
        if caminho is None:
            
            caminho = os.path.join(os.path.dirname(__file__), "../../dados/Tweets.csv")

        dados = open_file(caminho)
        if dados:
            for tweet in dados:
                
                tweet['tweet_created'] = datetime.strptime(tweet['tweet_created'], "%Y-%m-%d %H:%M:%S %z")
        return dados
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None


def contar_tweets_por_periodo(ano: int, mes: Optional[int] = None, caminho: Optional[str] = None) -> int:
    """
    Conta o número de tweets publicados em um ano e opcionalmente em um mês específico.

    Args:
        ano (int): Ano para filtrar os tweets.
        mes (Optional[int]): Mês para filtrar os tweets (opcional).
        caminho (Optional[str]): Caminho para o arquivo CSV.

    Returns:
        int: Total de tweets no período especificado.
    """
    if not ano:
        raise ValueError("Por favor, forneça ao menos o ano para a análise.")

    dados = carregar_dados(caminho)
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


def dia_com_mais_tweets(dados: List[Dict[str, str]]) -> Optional[str]:
    """
    Função para determinar o dia com mais tweets no conjunto de dados
    sem usar pandas, apenas com listas e operações básicas.

    Args:
        dados (List[Dict[str, str]]): Conjunto de dados carregados.

    Returns:
        Optional[str]: Data com mais tweets ou None.
    """
    try:
        
        contagem_datas = {}

        
        for tweet in dados:
            data = tweet.get("tweet_created").date()  
            if data:  
                if data in contagem_datas:
                    contagem_datas[data] += 1
                else:
                    contagem_datas[data] = 1

        
        if contagem_datas:
            dia_mais_tweets = max(contagem_datas, key=contagem_datas.get)  
            return str(dia_mais_tweets)  
        else:
            return None
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
        return None

