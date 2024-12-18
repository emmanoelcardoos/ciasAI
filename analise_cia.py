
"""
Módulo para análise de tweets relacionados a companhias aéreas.

Este módulo fornece funções para analisar dados de tweets associados a companhias aéreas, incluindo contagem de tweets por companhia, listagem de companhias únicas, filtragem de tweets por companhia e identificação da companhia com mais tweets negativos.

Funções:
- total_tweets_por_companhia(data): Retorna a contagem de tweets por companhia.
- listar_companhias(data): Retorna uma lista das companhias únicas presentes nos dados.
- filtrar_tweets_por_companhia(data, companhia): Filtra os tweets de uma companhia específica.
- companhia_com_mais_tweets_negativos(data): Retorna a companhia com mais tweets negativos.

Dependências:
- collections.Counter
"""

from collections import Counter

def total_tweets_por_companhia(data):
    """
    Conta o total de tweets associados a cada companhia aérea.

    Args:
        data (list): Lista de dicionários, onde cada dicionário representa um tweet. Cada dicionário deve conter pelo menos a chave 'airline'.

    Returns:
        dict: Um dicionário onde as chaves são os nomes das companhias aéreas e os valores são os totais de tweets de cada uma.
    """
    contagem = Counter(row['airline'] for row in data)
    return dict(contagem)

def listar_companhias(data):
    """
    Retorna uma lista contendo todas as companhias aéreas únicas presentes nos dados.

    Args:
        data (list): Lista de dicionários, onde cada dicionário representa um tweet. Cada dicionário deve conter pelo menos a chave 'airline'.

    Returns:
        list: Uma lista contendo os nomes das companhias aéreas, sem duplicatas.
    """
    companhias = {row['airline'] for row in data}
    return list(companhias)

def filtrar_tweets_por_companhia(data, companhia):
    """
    Filtra os tweets associados a uma companhia aérea específica.

    Args:
        data (list): Lista de dicionários, onde cada dicionário representa um tweet. Cada dicionário deve conter pelo menos a chave 'airline'.
        companhia (str): O nome da companhia aérea cujos tweets devem ser filtrados.

    Returns:
        list: Uma lista contendo os dicionários dos tweets associados à companhia especificada.
    """
    return [row for row in data if row['airline'] == companhia]

def companhia_com_mais_tweets_negativos(data):
    """
    Identifica a companhia aérea que recebeu mais tweets com sentimento negativo.

    Args:
        data (list): Lista de dicionários, onde cada dicionário representa um tweet. Cada dicionário deve conter as chaves:
            - 'airline': Nome da companhia aérea associada ao tweet.
            - 'airline_sentiment': Sentimento associado ao tweet (ex.: 'positive', 'neutral', 'negative').

    Returns:
        str: O nome da companhia aérea com mais tweets negativos. Caso nenhuma companhia tenha tweets negativos, retorna a mensagem:
        "Nenhuma companhia com tweets negativos".
    """
    negativos = [row['airline'] for row in data if row['airline_sentiment'] == 'negative']
    contagem_negativos = Counter(negativos)
    return max(contagem_negativos, key=contagem_negativos.get) if contagem_negativos else "Nenhuma companhia com tweets negativos"