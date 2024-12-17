import logging

# Configuração do log para registrar erros em um arquivo
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_erro(msg: str) -> None:
    """
    Registra uma mensagem de erro no arquivo de log.

    Args:
        msg (str): Mensagem de erro a ser registrada.
    """
    logging.error(msg)
