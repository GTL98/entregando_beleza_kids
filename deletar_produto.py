# --- Importar as bibliotecas --- #
import os
import requests
import streamlit as st


def deletar_produto(banco: str, codigo: int) -> None:
    """
    Função responsável por deletar o produto do banco de dados.
    :param banco: Banco de dados onde está o produto a ser deletado.
    :param codigo: Código do produto a ser deletado.
    """
    # --- Acessar o banco de dados --- #
    link = st.secrets['LINK_BD_PRODUTOS']

    # --- Deletar o produto desejado --- #
    requests.delete(f'{link}/{banco}/{codigo}/.json')