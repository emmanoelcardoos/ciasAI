import logging
from collections import Counter, defaultdict
from typing import List, Dict, Optional
import os
import csv
from datetime import datetime
from importlib.resources import files

def get_file_path() -> str:
    try:
        
        file_path = files("ciasAI.dados").joinpath("tweets.csv")
        return str(file_path)
    except Exception as e:
        raise FileNotFoundError(f"Erro ao localizar o arquivo 'tweets.csv': {e}")


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


def contador_sentiment(data: List[Dict[str, str]]) -> Counter:
    sent_count = Counter(row['airline_sentiment'] for row in data)
    return sent_count


def positive_tweet(data: List[Dict[str, str]]) -> str:
    companhia_positivos = Counter(
        row['airline'] for row in data if row['airline_sentiment'] == 'positive'
    )
    return companhia_positivos.most_common(1)[0][0] if companhia_positivos else "Nenhuma companhia com tweets positivos"


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


def carregar_dados(caminho: Optional[str] = None) -> Optional[List[Dict[str, str]]]:
    try:
        if caminho is None:
            caminho = get_file_path()
        dados = open_file(caminho)
        if dados:
            for tweet in dados:
                tweet['tweet_created'] = datetime.strptime(tweet['tweet_created'], "%Y-%m-%d %H:%M:%S %z")
        return dados
    except Exception as e:
        print(f"Erro: {e}")
        return None


if __name__ == "__main__":
   
    file_path = get_file_path()
    dados = carregar_dados(file_path)

    if dados:
        
        print("Contagem de tweets por sentimento:", contador_sentiment(dados))

        
        print("Companhia com mais tweets positivos:", positive_tweet(dados))

        
        print("Percentagem de sentimentos por companhia:", porcentage_sentimento(dados))

        
        companhia_especifica = "Delta"
        tweets_delta = filtrar_tweets_por_companhia(dados, companhia_especifica)
        print(f"Detalhes dos tweets da companhia {companhia_especifica}:", tweets_delta)


# IMPORTANTE NOTA: Com base nas experiencias de trabalho do grupo com este codigo, verificou-se que em muitas das vezes ao copiar e colar este codigo para ser executado, a linha que representa "if __name__ == "__main__":" é alterada. Ao executar este codigo, verifique que esteja assim: if __name__ == "__main__":
