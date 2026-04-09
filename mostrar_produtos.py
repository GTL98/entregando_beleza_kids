# --- Importar as bibliotecas --- #
import os
import requests
import streamlit as st
from dotenv import load_dotenv


def mostrar_produtos(banco: str, tipo: str, kit:bool=False):
    """
    Função responsável por mostrar os produtos na tela.
    :param banco: Banco do produto selecionado.
    :param tipo: Qual tipo de requisição ('compra', 'adm').
    :param kit: Se é para montagem do kit ou não.
    """
    # --- Se o tipo de requisição for de compra --- #
    if tipo == 'compra':
        pass

    # --- Se o tipo de requisição for para administração --- #
    if tipo == 'adm':
        # --- Acessar o banco de dados --- #
        load_dotenv()
        link = os.getenv('LINK_BD_PRODUTOS')

        # --- Obter o dicionário da classe do produto --- #
        requisicao = requests.get(f'{link}/{banco}/.json')
        return requisicao.json()