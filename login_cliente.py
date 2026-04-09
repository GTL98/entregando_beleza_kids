# --- Importar as bibliotecas --- #
import os
import requests
import streamlit as st
from hashlib import sha256
from dotenv import load_dotenv


def login_cliente(usuario: str, senha: str) -> None:
    """
    Função responsável por realizar o login do cliente.
    :param usuario: Nome de usuário do cliente.
    :param senha: Senha do cliente.
    """
    # --- Link do banco de dados --- #
    load_dotenv()
    link = os.getenv('LINK_BD_CLIENTES')

    # --- Obter as chaves de identificação dos clientes --- #
    requisicao = requests.get(f'{link}/.json')
    dic_requisicao = requisicao.json()

    # --- Verificar se o usuário está cadastrado --- #
    usuario_temp = f'{usuario}{senha}'
    usuario_crip = sha256(usuario_temp.encode()).hexdigest()
    if usuario_crip in dic_requisicao.keys():
        st.sidebar.success('Login feito com sucesso!')
        st.session_state.login = True

        # --- Verificaar se é admin ou não --- #
        if dic_requisicao[usuario_crip]['informacoes']['admin']:
            st.session_state.admin = True

        # --- Colocar na sessão a criptografia do cliente --- #
        if 'usuario_crip' not in st.session_state:
            st.session_state.usuario_crip = usuario_crip

    else:
        st.sidebar.warning('Cliente não cadastrado.')
