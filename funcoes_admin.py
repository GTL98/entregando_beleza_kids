# --- Importar as bibliotecas --- #
import requests
import streamlit as st
from typing import Dict, List

# --- Importar o módulo do cadastro dos produtos --- #
from cadastrar_produtos import cadastrar_produtos

# --- Importar o módulo de visualização/atualização dos produtos (ADM) --- #
from mostrar_produtos_adm import mostrar_produtos_adm

# --- Importar o módulo para a criação dos gráficos --- #
from graficos_adm import Graficos


def atualizar(categorias: List, dic_banco: Dict) -> None:
    """
    Função responsável por mostrar a página da atualização dos produtos na ADM.
    :param categorias: Lista com as categorias dos produtos.
    :param dic_banco: Dicionário com as chaves do banco.
    """
    # --- Seleção do banco de dados --- #
    banco = st.selectbox(
        label='Selecione o banco de dados:',
        placeholder='Selecione o banco de dados',
        options=sorted(categorias),
        index=None,
        key='atualizar'
    )

    # --- Mostrar as informações do banco selecionado --- #
    if banco is not None:
        mostrar_produtos_adm(dic_banco[banco], banco)


def cadastrar(categorias: List, dic_banco: Dict) -> None:
    """
    Função responsável por mostrar a página de cadastro dos produtos na ADM.
    :param categorias: Lista com as categorias dos produtos.
    :param dic_banco: Dicionário com as chaves do banco.
    """
    banco = st.selectbox(
        label='Selecione o banco de dados',
        placeholder='Selecione o banco de dados',
        options=sorted(categorias),
        index=None,
        key='cadastrar'
    )

    # --- Mostrar as informações do banco selecionado --- #
    if banco is not None:
        cadastrar_produtos(dic_banco[banco], banco)


def graficos() -> None:
    """Função responsável por mostrar a página dos gráficos dos produtos na ADM."""
    # --- Acessar o banco de dados --- #
    link = st.secrets['LINK_BD_PRODUTOS']
    dados = requests.get(f'{link}/.json').json()

    # --- Instanciar os gráficos --- #
    grafico = Graficos(dados)
    grafico.barra_precos()
    grafico.barra_estoque()
    grafico.pizza_precos()
    grafico.pizza_estoque()