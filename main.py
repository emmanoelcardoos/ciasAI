import logging
from collections import Counter, defaultdict
from typing import List, Dict, Optional
import os
import csv
from datetime import datetime


# Configuração do logging
logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Função de login
def realizar_login(user: str, password: str) -> bool:
    if user == "main" and password == "123456":
        logging.info(f"Login bem-sucedido para o utilizador: {user}")
        return True
    else:
        logging.info(f"Tentativa de login falhou para o utilizador: {user}")
        return False


# Função para contar o número total de tweets por companhia
def total_tweets_por_companhia(data: List[Dict[str, str]]) -> Dict[str, int]:
    contagem = Counter(row['airline'] for row in data)
    return dict(contagem)


# Função para listar as companhias únicas
def listar_companhias(data: List[Dict[str, str]]) -> List[str]:
    companhias = {row['airline'] for row in data}
    return list(companhias)


# Função para filtrar tweets por companhia
def filtrar_tweets_por_companhia(data: List[Dict[str, str]], companhia: str) -> List[Dict[str, str]]:
    return [row for row in data if row['airline'] == companhia]


# Função para encontrar a companhia com mais tweets negativos
def companhia_com_mais_tweets_negativos(data: List[Dict[str, str]]) -> str:
    negativos = [row['airline'] for row in data if row['airline_sentiment'] == 'negative']
    contagem_negativos = Counter(negativos)
    return max(contagem_negativos, key=contagem_negativos.get) if contagem_negativos else "Nenhuma companhia com tweets negativos"


# Contar os sentimentos
def contador_sentiment(data: List[Dict[str, str]]) -> Counter:
    sent_count = Counter(row['airline_sentiment'] for row in data)
    return sent_count


# Encontrar companhia com mais tweets positivos
def positive_tweet(data: List[Dict[str, str]]) -> str:
    companhia_positivos = Counter(
        row['airline'] for row in data if row['airline_sentiment'] == 'positive'
    )
    return companhia_positivos.most_common(1)[0][0] if companhia_positivos else "Nenhuma companhia com tweets positivos"


# Calcular a percentagem de sentimentos por companhia
def porcentage_sentimento(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
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


# Abrir dados de CSV
def open_file(caminho: str) -> Optional[List[Dict[str, str]]]:
    try:
        if not os.path.isfile(caminho):
            raise FileNotFoundError(f"Erro: Arquivo '{caminho}' não encontrado.")
        with open(caminho, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = [linha for linha in leitor]
        return dados
    except Exception as e:
        print(f"Erro: {e}")
        return None


# Carregar dados e converter datas para objetos datetime
def carregar_dados(caminho: Optional[str] = None) -> Optional[List[Dict[str, str]]]:
    try:
        if caminho is None:
            caminho = os.path.join(os.getcwd(), "dados/Tweets.csv")
        dados = open_file(caminho)
        if dados:
            for tweet in dados:
                tweet['tweet_created'] = datetime.strptime(tweet['tweet_created'], "%Y-%m-%d %H:%M:%S %z")
        return dados
    except Exception as e:
        print(f"Erro: {e}")
        return None


# Contar tweets por período
def contar_tweets_por_periodo(ano: int, mes: Optional[int] = None, caminho: Optional[str] = None) -> int:
    dados = carregar_dados(caminho)
    if not dados:
        print("Não foi possível carregar os dados.")
        return 0

    total_tweets = sum(
        1 for tweet in dados if tweet['tweet_created'].year == ano and (mes is None or tweet['tweet_created'].month == mes)
    )
    print(f"Total de tweets no período: {total_tweets}")
    return total_tweets


# Encontrar dia com mais tweets
def dia_com_mais_tweets(dados: List[Dict[str, str]]) -> Optional[str]:
    contagem_datas = {}
    for tweet in dados:
        data = tweet.get("tweet_created").date()
        if data:
            contagem_datas[data] = contagem_datas.get(data, 0) + 1
    if contagem_datas:
        dia_mais_tweets = max(contagem_datas, key=contagem_datas.get)
        return str(dia_mais_tweets)
    return None


# Execução principal para demonstrar funcionalidades
if __name__ == "__main__":
    # Caminho correto para o arquivo de dados
    file_path = '/Users/emmanoelcardoso/Desktop/ciasAI/dados/Tweets.csv'

    # Carregar dados
    data = carregar_dados(file_path)

    if data:
        # Contagem de sentimentos
        print("Contagem de tweets por sentimento:", contador_sentiment(data))

        # Companhia com mais tweets positivos
        print("Companhia com mais tweets positivos:", positive_tweet(data))

        # Percentual de sentimentos por companhia
        print("Percentagem de sentimentos por companhia:", porcentage_sentimento(data))

        # Filtrar tweets por companhia
        companhia_especifica = "Delta"
        tweets_delta = filtrar_tweets_por_companhia(data, companhia_especifica)
        print(f"Detalhes dos tweets da companhia {companhia_especifica}:", tweets_delta)




