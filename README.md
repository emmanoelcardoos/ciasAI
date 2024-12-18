CiasAI - Análise de Dados e Sentimentos de Companhias Aéreas

CiasAI é um pacote Python desenvolvido por estudantes da UC de
Porgramacao do curso de Inteligência Artificial e Ciência de Dados para
análise de dados de tweets sobre companhias aéreas. Ele oferece
funcionalidades para análise de sentimentos, filtragem de tweets por
companhia, processamento temporal e outras métricas relacionadas a dados
de tweets. O pacote foi desenvolvido como parte de um projeto acadêmico
e pode ser utilizado para análises de dados em outros contextos.

Objetivo

O objetivo do CiasAI é fornecer ferramentas para analisar grandes
volumes de tweets e extrair insights como a quantidade de tweets
positivos ou negativos, a companhia aérea mais mencionada e a análise
temporal dos tweets. Este pacote é útil para analistas de dados,
desenvolvedores e profissionais que necessitam de ferramentas para
processamento e análise de sentimentos de dados de texto.

Funcionalidades

\- Leitura de dados CSV: Carrega dados de um arquivo CSV e converte-os
em um formato utilizável.

\- Análise de Sentimentos: Conta e classifica tweets de acordo com o
sentimento (positivo, negativo, neutro).

\- Filtragem de Tweets: Filtra os tweets com base na companhia aérea.

\- Análise Temporal: Analisa a quantidade de tweets por período de
tempo.

\- Login e Autenticação: Funções básicas de login para validação de
usuário.

Instalação

Para instalar o pacote, siga as instruções abaixo:

1\. Clone o repositório para seu diretório local. O link do repositório
é:
\[https://github.com/emmanoelcardoos/ciasAI
obs: se fizer git clone é preciso usar o caminho absoluto do pacote baixado para executar no jupyter notebook.
exemplo: import sys
sys.path.append('/caminho/absoluto/para/ciasAI') 
from ciasAI.analise_sentimento import contador_sentiment # importacao de uma funcao especifica de um modulo especifico como exempplo


2\. Em seguida, instale as dependências do pacote:

pip install git+ https://github.com/emmanoelcardoos/ciasAI

3 / instale as dependencias do pacote: 

pip install -r requirements.txt

4/ Fazer download do arquivo csv a ser lido pelo programa:

https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment

Agora que já está tudo instalado, siga os passos abaixo para excutar as funcoes do pacote:
 
 1: Abra o Jupyter Notebook
 2: abra uma cédula e introduza "import ciasAI"; se nao correr bem, talvez seja necessario instalar o pacote dentro do diretorio python do seu pc
 3: após a importacao do pacote no jupyter notebook, execiute o seguinte comando:
    file_path = 'caminho do ficheiro csv no seu pc'
    dados = open_file(file_path)
5/ importar 

