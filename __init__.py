# __init__.py
from .leitor_dados import open_file
from .analise_sentimento import contador_sentiment, positive_tweet, porcentage_sentimento, filtro_tweet
from .analise_cia import realizar_login, total_tweets_por_companhia, listar_companhias, filtrar_tweets_por_companhia, companhia_com_mais_tweets_negativos
from .processamento_temporal import dia_com_mais_tweets, contar_tweets_por_periodo

# Expõe as funções para o uso direto
__all__ = [
    "open_file",
    "contador_sentiment",
    "positive_tweet",
    "porcentage_sentimento",
    "filtro_tweet",
    "realizar_login",
    "total_tweets_por_companhia",
    "listar_companhias",
    "filtrar_tweets_por_companhia",
    "companhia_com_mais_tweets_negativos",
    "dia_com_mais_tweets",
    "contar_tweets_por_periodo"
]



