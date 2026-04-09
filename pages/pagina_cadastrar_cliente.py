# --- Importar as bibliotecas --- #
from PIL import Image
from imagens import *
import streamlit as st
from datetime import date

# --- Importar o CSS --- #
from menu_css import css

# --- Importar o módulo de cadastro do cliente --- #
from cadastrar_cliente import cadastrar_cliente

# --- Configuração da página --- #
st.set_page_config(
    page_title='Cadastro - Entregando Beleza Kids',
    page_icon=Image.open(FAVICON),
    layout='wide'
)

# --- CSS --- #
st.html(css)

# --- Logo da sidebar --- #
st.logo(image=LOGO_MENU_ABERTO, icon_image=LOGO_MENU_FECHADO)

# --- Título da página --- #
st.title('Cadastro')

# --- Formulário para o cadastro --- #
with st.form('cadastro'):
    # --- Nome do cliente --- #
    nome_cliente = st.text_input(
        label='Nome completo:',
        placeholder='Digite o seu nome completo'
    ).strip().upper()

    # --- Data de nascimento do cliente --- #
    nascimento_cliente_bruto = st.date_input(
        label='Data de nascimento:',
        format='DD/MM/YYYY',
        min_value=date(1900, 1, 1),
        value=None
    )

    # --- Telefone do cliente --- #
    telefone_cliente = st.number_input(
        label='Telefone (com DDD):',
        placeholder='(DDD) 99999-9999',
        help='Digite o seu telefone com o DDD, sem parênteses (ex: 41999999999)',
        min_value=900_000_000,
        max_value=99_999_999_999,
        value=None,
        step=1
    )

    # --- Endereço do cliente --- #
    colunas = st.columns((2, 1, 1))
    with colunas[0]:
        endereco_cliente = st.text_input(
            label='Endereço:',
            placeholder='Digite o seu endereço completo'
        ).strip().upper()

    with colunas[1]:
        # --- Número do endereço do cliente --- #
        numero_endereco_cliente = st.number_input(
            label='N° da residência:',
            placeholder='N° da sua residência',
            help='Se tiver letra o número da sua residência, adicione no campo do "Complemento".',
            min_value=1,
            max_value=100_000,
            value=None
        )

    with colunas[2]:
        # --- Complemento do endereço do cliente (opcional) --- #
        complemento_endereco = st.text_input(
            label='Complemento (opcional):',
            placeholder='Complemento do endereço'
        ).strip()

    colunas = st.columns(2)
    with colunas[0]:
        # --- Nome de usuário --- #
        nome_usuario = st.text_input(
            label='Nome de usuário:',
            placeholder='Digite o nome de usuário'
        )

    with colunas[1]:
        # --- Senha --- #
        senha_usuario = st.text_input(
            label='Senha:',
            placeholder='Digite a sua senha',
            type='password'
        )

    # --- Botão de cadastrar o usuário --- #
    cadastrar = st.form_submit_button('Cadastrar', width='stretch')


# --- Verificar se os campos foram preechidos --- #
if cadastrar:
    if (nome_cliente
    and telefone_cliente
    and nascimento_cliente_bruto
    and endereco_cliente
    and numero_endereco_cliente
    and nome_usuario
    and senha_usuario):
        nascimento_cliente_str = str(nascimento_cliente_bruto).split('-')
        nascimento_cliente = f'{nascimento_cliente_str[2]}/{nascimento_cliente_str[1]}/{nascimento_cliente_str[0]}'
        cadastrar_cliente(
            nome_cliente=nome_cliente,
            nascimento_cliente=nascimento_cliente,
            telefone_cliente=telefone_cliente,
            endereco_cliente=endereco_cliente,
            numero_endereco_cliente=numero_endereco_cliente,
            complemento_endereco=complemento_endereco,
            nome_usuario=nome_usuario,
            senha_usuario=senha_usuario
        )
    else:
        st.warning('Digite todas as informações para o cadastro.')