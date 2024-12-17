import unittest
from ciasAI import contador_sentiment, positive_tweet, porcentage_sentimento, filtro_tweet

class TestAnaliseSentimento(unittest.TestCase):

    def setUp(self):
        # Dados fictícios para os testes
        self.dados = [
            {'airline_sentiment': 'positive', 'airline': 'Delta'},
            {'airline_sentiment': 'negative', 'airline': 'Delta'},
            {'airline_sentiment': 'positive', 'airline': 'American'},
            {'airline_sentiment': 'neutral', 'airline': 'American'},
            {'airline_sentiment': 'positive', 'airline': 'Delta'}
        ]

    def test_contador_sentiment(self):
        resultado = contador_sentiment(self.dados)
        self.assertEqual(resultado['positive'], 3)
        self.assertEqual(resultado['negative'], 1)
        self.assertEqual(resultado['neutral'], 1)

    def test_positive_tweet(self):
        resultado = positive_tweet(self.dados)
        self.assertEqual(resultado, 'Delta')

    def test_porcentage_sentimento(self):
        resultado = porcentage_sentimento(self.dados)
        self.assertEqual(resultado['Delta']['positive'], 60.0)
        self.assertEqual(resultado['American']['positive'], 50.0)

    def test_filtro_tweet(self):
        resultado = filtro_tweet(self.dados, 'Delta')
        self.assertEqual(len(resultado), 3)

if __name__ == '__main__':
    unittest.main()
