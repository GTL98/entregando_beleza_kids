# --- Importar as bibliotecas --- #
import os
import json
import requests
import streamlit as st
from hashlib import sha256


def cadastrar_cliente(**kwargs) -> None:
    """Função responsável por cadastrar o cliente."""
    # --- Separar as informações do cadastro --- #
    nome_cliente = kwargs['nome_cliente']
    nascimento_cliente = kwargs['nascimento_cliente']
    telefone_cliente = kwargs['telefone_cliente']
    endereco_cliente = kwargs['endereco_cliente']
    numero_endereco_cliente = kwargs['numero_endereco_cliente']
    complemento_endereco = kwargs['complemento_endereco']
    nome_usuario = kwargs['nome_usuario']
    senha_usuario = kwargs['senha_usuario']

    # --- Link do banco de dados --- #
    link = st.secrets('LINK_BD_CLIENTES')

    # --- Criptografar o usuário --- #
    usuario = f'{nome_usuario}{senha_usuario}'
    usuario_crip = sha256(usuario.encode()).hexdigest()

    # --- Verificar se o cliente já está cadastrado no site --- #
    requisicao = requests.get(f'{link}/.json')
    dic_requisicao = requisicao.json()
    if usuario_crip in dic_requisicao.keys():
        st.info('Usuário já cadastrado!')

    else:
        # --- Dicionário com os dados cadastrados --- #
        dados = {
            'informacoes': {
                'admin': False,
                'nome': nome_cliente,
                'nascimento': nascimento_cliente,
                'telefone': telefone_cliente,
                'endereco': endereco_cliente,
                'numero_endereco': numero_endereco_cliente,
                'complemento': complemento_endereco
            },
            'pedidos': {
                'Sem pedidos': 'Sem pedidos'
            }
        }

        # --- Cadastrar o cliente no banco de dados --- #
        requests.patch(f'{link}/{usuario_crip}/.json', data=json.dumps(dados))
        st.success('Seu cadastro foi realizado com sucesso!')
