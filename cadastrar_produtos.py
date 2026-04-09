# --- Importar as bibliotecas --- #
import os
import requests
from json import dumps
import streamlit as st
from dotenv import load_dotenv


def cadastrar_produtos(banco: str, titulo: str) -> None:
    """
    Função responsável por cadastrar os produtos no banco de dados.
    :param banco: Qual banco terá um produto cadastrado.
    :param titulo: Nome do banco quando selecionado.
    """
    # --- Link do banco de dados --- #
    load_dotenv()
    link = os.getenv('LINK_BD_PRODUTOS')

    # --- Dados do produto --- #
    with st.form('cadastrar_produto'):
        # --- Título do banco --- #
        st.header(f'Banco de dados: {titulo}')

        # --- Nome do produto --- #
        st.subheader('Nome:')
        nome = st.text_input(
            label='',
            placeholder='Digite o nome do produto',
            label_visibility='collapsed'
        )

        # --- Código do produto --- #
        st.subheader('Código:')
        codigo = st.number_input(
            label='',
            placeholder='Difite o código do produto',
            min_value=0,
            max_value=999_999,
            value=None,
            label_visibility='collapsed'
        )

        # --- Preço de compra --- #
        st.subheader('Compra:')
        compra = st.text_input(
            label='',
            placeholder='Digite o preço de compra',
            help='Não adicione R$ ao valor. Você pode separar por vírgula ou ponto os centavos.',
            label_visibility='collapsed'
        )

        # --- Preço original --- #
        st.subheader('De:')
        de = st.text_input(
            label='',
            placeholder='Digite o preço original',
            help='Não adicione R$ ao valor. Você pode separar por vírgula ou ponto os centavos.',
            label_visibility='collapsed'
        )

        # --- Preço com desconto --- #
        st.subheader('Preço:')
        preco = st.text_input(
            label='',
            placeholder='Digite o preço com desconto',
            help='Não adicione R$ ao valor. Você pode separar por vírgula ou ponto os centavos.',
            label_visibility='collapsed'
        )

        # -- Quantidade no estoque --- #
        st.subheader('Estoque:')
        estoque = st.number_input(
            label='',
            placeholder='Digite a quantidade em estoque',
            label_visibility='collapsed',
            min_value=0,
            max_value=100,
            step=1,
            value=None
        )

        # --- Foto do produto --- #
        st.subheader('Foto:')
        foto = st.text_input(
            label='',
            placeholder='Link da foto',
            label_visibility='collapsed'
        )

        # --- Descrição do produto --- #
        st.subheader('Descrição:')
        descricao = st.text_area(
            label='',
            placeholder='Digite a descrição do produto',
            label_visibility='collapsed'
        )

        # --- Se o produto estiver na campanha --- #
        st.subheader('O produto está na campanha:')
        campanha_str = st.radio(
            label='',
            options=['Sim', 'Não'],
            horizontal=True,
            label_visibility='collapsed'
        )
        if campanha_str == 'Sim':
            camapanha = True
        else:
            campanha = False

        # --- Enviar ao banco de dados o produto cadastrado --- #
        enviar = st.form_submit_button(
            label='Enviar',
            width='stretch'
        )

        if enviar:
            if codigo and foto:
                # --- Dicionário com os dados do produto cadastrado --- #
                dados = {
                    codigo: {
                        'campanha': camapanha,
                        'codigo': codigo,
                        'de': de,
                        'foto': foto,
                        'nome': nome,
                        'preco': preco,
                        'estoque': estoque,
                        'descricao': descricao,
                        'compra': compra
                    }
                }

                # --- Cadastrar o produto no banco de dados --- #
                requests.patch(f'{link}/{banco}/.json', data=dumps(dados))

                # --- Informar que o produto foi cadastrado com sucesso --- #
                st.success(f'O produto {nome} foi cadastrado com sucesso!')
            else:
                st.warning('Por favor, informe ao menos o código e a foto do produto.')
