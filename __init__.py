# __init__.py no diretório raiz
from ciasAI.leitor_dados import open_file
from ciasAI.analise_sentimento import (
    contador_sentiment,
    positive_tweet,
    porcentage_sentimento,
    filtro_tweet,
)
from ciasAI.analise_cia import (
    realizar_login,
    total_tweets_por_companhia,
    listar_companhias,
    filtrar_tweets_por_companhia,
    companhia_com_mais_tweets_negativos,
)
from ciasAI.processamento_temporal import dia_com_mais_tweets, contar_tweets_por_periodo

# Expõe as funções para fácil acesso
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
    "contar_tweets_por_periodo",
]





