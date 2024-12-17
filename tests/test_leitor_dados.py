import unittest
from unittest.mock import patch, mock_open
from ciasAI import open_file  # Alterando para a função correta

class TestLeitorDados(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="airline_sentiment,airline,tweet_created\npositive,Delta,2024-01-01 10:00:00\nnegative,Delta,2024-01-02 11:00:00")
    def test_open_file(self, mock_file):  # Alterando o nome do teste para open_file
        dados = open_file("mocked_file.csv")  # Usando open_file ao invés de carregar_dados_tweets
        self.assertIsNotNone(dados)
        self.assertEqual(len(dados), 2)
        self.assertEqual(dados[0]['airline'], 'Delta')
        self.assertEqual(dados[0]['airline_sentiment'], 'positive')

    @patch("builtins.open", new_callable=mock_open)
    def test_open_file_vazio(self, mock_file):  # Alterando o nome do teste para open_file
        mock_file.return_value.read.return_value = ""
        dados = open_file("mocked_file.csv")  # Usando open_file ao invés de carregar_dados_tweets
        self.assertIsNone(dados)

if __name__ == '__main__':
    unittest.main()
