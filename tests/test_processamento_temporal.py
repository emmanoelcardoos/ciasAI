import unittest
from datetime import datetime
from ciasAI import dia_com_mais_tweets, contar_tweets_por_periodo

class TestProcessamentoTemporal(unittest.TestCase):

    def setUp(self):
        self.dados = [
            {'airline_sentiment': 'positive', 'airline': 'Delta', 'tweet_created': datetime(2024, 1, 1, 10, 0)},
            {'airline_sentiment': 'negative', 'airline': 'Delta', 'tweet_created': datetime(2024, 1, 1, 11, 0)},
            {'airline_sentiment': 'positive', 'airline': 'American', 'tweet_created': datetime(2024, 1, 2, 12, 0)},
            {'airline_sentiment': 'negative', 'airline': 'American', 'tweet_created': datetime(2024, 1, 3, 13, 0)},
            {'airline_sentiment': 'positive', 'airline': 'Delta', 'tweet_created': datetime(2024, 1, 3, 14, 0)}
        ]

    def test_dia_com_mais_tweets(self):
        resultado = dia_com_mais_tweets()
        self.assertEqual(resultado[0], datetime(2024, 1, 1).date())
        self.assertEqual(resultado[1], 2)

    def test_contar_tweets_por_periodo(self):
        resultado_ano = contar_tweets_por_periodo(2024)
        self.assertEqual(resultado_ano, 5)

        resultado_mes = contar_tweets_por_periodo(2024, 1)
        self.assertEqual(resultado_mes, 5)

if __name__ == '__main__':
    unittest.main()
