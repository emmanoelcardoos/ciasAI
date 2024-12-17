import unittest
from ciasAI import realizar_login, total_tweets_por_companhia, listar_companhias, filtrar_tweets_por_companhia, companhia_com_mais_tweets_negativos

class TestAnaliseCias(unittest.TestCase):

    def setUp(self):
        self.dados = [
            {'airline_sentiment': 'positive', 'airline': 'Delta', 'tweet_created': '2024-01-01'},
            {'airline_sentiment': 'negative', 'airline': 'Delta', 'tweet_created': '2024-01-02'},
            {'airline_sentiment': 'positive', 'airline': 'American', 'tweet_created': '2024-01-03'},
            {'airline_sentiment': 'negative', 'airline': 'American', 'tweet_created': '2024-01-04'},
            {'airline_sentiment': 'negative', 'airline': 'Delta', 'tweet_created': '2024-01-05'}
        ]

    def test_realizar_login_sucesso(self):
        resultado = realizar_login("main", "123456")
        self.assertTrue(resultado)

    def test_realizar_login_falha(self):
        resultado = realizar_login("user", "wrongpass")
        self.assertFalse(resultado)

    def test_total_tweets_por_companhia(self):
        resultado = total_tweets_por_companhia(self.dados)
        self.assertEqual(resultado['Delta'], 3)
        self.assertEqual(resultado['American'], 2)

    def test_listar_companhias(self):
        resultado = listar_companhias(self.dados)
        self.assertIn('Delta', resultado)
        self.assertIn('American', resultado)

    def test_filtrar_tweets_por_companhia(self):
        resultado = filtrar_tweets_por_companhia(self.dados, 'Delta')
        self.assertEqual(len(resultado), 3)

    def test_companhia_com_mais_tweets_negativos(self):
        resultado = companhia_com_mais_tweets_negativos(self.dados)
        self.assertEqual(resultado, 'Delta')

if __name__ == '__main__':
    unittest.main()
