import os
from collections import Counter, defaultdict
from ciasAI.leitor_dados import open_file  
from typing import List, Dict

def contador_sentiment(data: List[Dict[str, str]]) -> Counter:
    """
    Conta a quantidade de tweets para cada sentimento.

    Args:
        data (list): Lista de dicionários com os tweets.

    Returns:
        Counter: Contagem de tweets por sentimento.
    """
    sent_count = Counter(row['airline_sentiment'] for row in data)
    return sent_count

def positive_tweet(data: List[Dict[str, str]]) -> str:
    """
    Encontra a companhia com mais tweets positivos.

    Args:
        data (list): Lista de dicionários com os tweets.

    Returns:
        str: Nome da companhia com mais tweets positivos.
    """
    companhia_positivos = Counter(
        row['airline'] for row in data if row['airline_sentiment'] == 'positive'
    )
    return companhia_positivos.most_common(1)[0][0] if companhia_positivos else "Nenhuma companhia com tweets positivos"

def porcentage_sentimento(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    """
    Calcula a percentagem de sentimentos para cada companhia.

    Args:
        data (list): Lista de dicionários com os tweets.

    Returns:
        dict: Percentagens de sentimentos por companhia.
    """
    companhia_sentimentos = defaultdict(lambda: Counter())

    for row in data:
        companhia = row['airline']
        sentimento = row['airline_sentiment']
        companhia_sentimentos[companhia][sentimento] += 1

    percentagens = {}
    for companhia, contagens in companhia_sentimentos.items():
        total = sum(contagens.values())
        percentagens[companhia] = {
            sentimento: (count / total) * 100 for sentimento, count in contagens.items()
        }

    return percentagens

def filtro_tweet(data: List[Dict[str, str]], companhia: str) -> List[Dict[str, str]]:
    """
    Filtra tweets por companhia.

    Args:
        data (list): Lista de dicionários com os tweets.
        companhia (str): Nome da companhia para filtrar os tweets.

    Returns:
        list: Lista de tweets filtrados pela companhia.
    """
    return [row for row in data if row['airline'] == companhia]

if __name__ == "__main__":
    
    current_dir = os.getcwd()  
    file_path = os.path.join(current_dir, "Desktop", "ciasAI", "dados", "Tweets.csv")


    
    data = open_file(file_path)

    if data:
        
        print("Contagem de tweets por sentimento:", contador_sentiment(data))

        
        print("Companhia com mais tweets positivos:", positive_tweet(data))

        
        print("Percentagem de sentimentos por companhia:", porcentage_sentimento(data))

        
        companhia_especifica = "Delta"  
        tweets_delta = filtro_tweet(data, companhia_especifica)
        print(f"Detalhes dos tweets da companhia {companhia_especifica}:", tweets_delta)
    else:
        print("Erro ao carregar os dados.")
        
        
#Ao executar este código tenha em conta que o arquivo ciasAI encontra-se no desktop
