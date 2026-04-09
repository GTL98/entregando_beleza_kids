# --- Importar as bibliotecas --- #
import os
import requests
from json import dumps
import streamlit as st


def atualizar_produto(**kwargs) -> None:
    """Função responsável por atualziar o produto."""
    # --- Separar as informações da atualização --- #
    banco = kwargs['banco']
    foto = kwargs['foto']
    nome = kwargs['nome']
    codigo = kwargs['codigo']
    de = kwargs['de']
    preco = kwargs['preco']
    compra = kwargs['compra']
    estoque = kwargs['estoque']
    campanha = kwargs['campanha']
    descricao = kwargs['descricao']

    # --- Link do banco de dados --- #
    link = st.secrets['LINK_BD_PRODUTOS']

    # --- Obter o dicionário da calsse do produto --- #
    requisicao = requests.get(f'{link}/{banco}/.json')
    dic_requisicao = requisicao.json()
    dic_copia = dic_requisicao

    # --- Atualizar o produto --- #
    dic_copia[str(codigo)]['foto'] = foto
    dic_copia[str(codigo)]['nome'] = nome
    dic_copia[str(codigo)]['codigo'] = codigo
    dic_copia[str(codigo)]['de'] = de
    dic_copia[str(codigo)]['preco'] = preco
    dic_copia[str(codigo)]['compra'] = compra
    dic_copia[str(codigo)]['estoque'] = estoque
    dic_copia[str(codigo)]['campanha'] = campanha
    dic_copia[str(codigo)]['descricao'] = descricao
    requests.patch(f'{link}/{banco}/.json', data=dumps(dic_copia))
