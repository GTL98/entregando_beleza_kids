# --- Importar as bibliotecas --- #
from PIL import Image
from imagens import *
import streamlit as st

# --- Importar o CSS --- #
from menu_css import css

# --- Importar o módulo do cadastro dos produtos --- #
from cadastrar_produtos import cadastrar_produtos

# --- Importar o módulo de visualização/atualização dos produtos (ADM) --- #
from mostrar_produtos_adm import mostrar_produtos_adm

# --- Configurações da página --- #
st.set_page_config(
    page_title='Administração - Entregando Beleza Kids',
    page_icon=Image.open(FAVICON),
    layout='wide',
    initial_sidebar_state='collapsed'
)

# --- CSS --- #
st.html(css)

# --- Logo da sidebar --- #
st.logo(image=LOGO_MENU_ABERTO, icon_image=LOGO_MENU_FECHADO)

if st.session_state.admin:
    # --- Seleção do banco de dados --- #
    categorias = [
        'Cabelos',
        'Sabonetes',
        'Cuidados da pele',
        'Acessórios e Utilidades'
    ]

    # --- Dicionário com o nome correto do banco --- #
    dic_banco = {
        'Cabelos': 'cabelos',
        'Sabonetes': 'sabonetes',
        'Cuidados da pele': 'cuidados_pele',
        'Acessórios e Utilidades': 'acessorios_utilidade'
    }

    # --- Título da página --- #
    st.title('Página de administração')

    # --- Abas da página de administração --- #
    abas = st.tabs(['Clientes', 'Pedidos', 'Atualizar produtos', 'Cadastrar produtos'], on_change='rerun')

    # --- Página dos clientes --- #
    with abas[0]:
        if abas[0].open:
            pass

    # --- Página dos pedidos --- #
    with abas[1]:
        if abas[1].open:
            pass

    # --- Página para atualizar os produtos --- #
    with abas[2]:
        if abas[2].open:
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

    # --- Página para cadastrar os produtos --- #
    with abas[3]:
        if abas[3].open:
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
else:
    st.title('Você não é o administrador, não há nada para ver aqui!')

