# --- Importar as bibliotecas --- #
import os
import requests
from dotenv import load_dotenv


def deletar_produto(banco: str, codigo: int) -> None:
    """
    Função responsável por deletar o produto do banco de dados.
    :param banco: Banco de dados onde está o produto a ser deletado.
    :param codigo: Código do produto a ser deletado.
    """
    # --- Acessar o banco de dados --- #
    load_dotenv()
    link = os.getenv('LINK_BD_PRODUTOS')

    # --- Deletar o produto desejado --- #
    requests.delete(f'{link}/{banco}/{codigo}/.json')