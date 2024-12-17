from ciasAI import open_file, contador_sentiment, positive_tweet, porcentage_sentimento, filtro_tweet
from ciasAI import realizar_login, total_tweets_por_companhia, listar_companhias, filtrar_tweets_por_companhia
from ciasAI import dia_com_mais_tweets, contar_tweets_por_periodo, carregar_dados


def exemplo_open_file():
    file_path = "dados/Tweets.csv"  # Caminho relativo para o arquivo
    data = open_file(file_path)
    if data:
        print("Dados carregados com sucesso!")


def exemplo_contador_sentiment():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(contador_sentiment(data))


def exemplo_positive_tweet():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(positive_tweet(data))


def exemplo_porcentage_sentimento():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(porcentage_sentimento(data))


def exemplo_filtro_tweet():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(filtro_tweet(data, "Delta"))


def exemplo_realizar_login():
    if realizar_login("main", "123456"):
        print("Login bem-sucedido!")


def exemplo_total_tweets_por_companhia():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(total_tweets_por_companhia(data))


def exemplo_listar_companhias():
    file_path = "dados/Tweets.csv"
    data = open_file(file_path)
    if data:
        print(listar_companhias(data))


def exemplo_dia_com_mais_tweets():
    dados = carregar_dados("dados/Tweets.csv")
    if dados:
        print(dia_com_mais_tweets(dados))


def exemplo_contar_tweets_por_periodo():
    print(contar_tweets_por_periodo(2024, 1))


if __name__ == "__main__":
    exemplo_open_file()
    exemplo_contador_sentiment()
    exemplo_positive_tweet()
    exemplo_porcentage_sentimento()
    exemplo_filtro_tweet()
    exemplo_realizar_login()
    exemplo_total_tweets_por_companhia()
    exemplo_listar_companhias()
    exemplo_dia_com_mais_tweets()
    exemplo_contar_tweets_por_periodo()


