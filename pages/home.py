# --- Importar as bibliotecas --- #
from PIL import Image
from imagens import *
import streamlit as st

# --- Importar o CSS --- #
from menu_css import css

# --- Importar o módulo de login --- #
from login_cliente import login_cliente

# --- Configurações da página --- #
st.set_page_config(
    page_title='Entregando Beleza Kids',
    page_icon=Image.open(FAVICON),
    layout='wide'
)

# --- CSS --- #
st.html(css)

# --- Banner do site --- #
st.image(BANNER)

# --- Logo da sidebar --- #
st.logo(image=LOGO_MENU_ABERTO, icon_image=LOGO_MENU_FECHADO)

# --- Título da página --- #
st.title('Entregando Beleza Kids')

# --- Compras na sessão do site --- #
if 'compras' not in st.session_state:
    st.session_state.compras = {'produtos': 0}

# --- Informações do cliente na sessão --- #
if 'cliente' not in st.session_state:
    st.session_state.cliente = {}

# --- Usuário e senha do cliente --- #
if 'usuario' not in st.session_state:
    st.session_state.usuario = None
if 'senha' not in st.session_state:
    st.session_state.senha = None

# --- Estado de login do cliente --- #
if 'login' not in st.session_state:
    st.session_state.login = False

# --- Estado do admin --- #
if 'admin' not in st.session_state:
    st.session_state.admin = False

# --- Cadastrar o cliente --- #
if st.session_state.login is False:
    st.sidebar.write('Não tem cadastro? É fácil e rápido!')
    cadastrar = st.sidebar.button('Cadastrar', width='stretch')
    if cadastrar:
        st.switch_page('./pages/pagina_cadastrar_cliente.py')

    # --- Login do cliente --- #
    st.sidebar.write('Já possui cadastro? É só fazer o login!')
    usuario = st.sidebar.text_input('Usuário:')
    senha = st.sidebar.text_input('Senha:', type='password')
    login = st.sidebar.button('Login', width='stretch')
    if login:
        login_cliente(usuario, senha)

# --- Login do cliente --- #
if st.session_state.login:
    # --- Colocar as informações das compras na sidebar --- #
    st.sidebar.subheader('Carrinho:')
    st.sidebar.write(f'Qtde. de produtos: {st.session_state.compras["produtos"]}')
    finalizar = st.sidebar.button('Finalizar compra', width='stretch')

    # --- Ir à página da finalização da compra --- #
    if finalizar:
        pass

    # --- Ir à página da finalização da compra --- #
    perfil = st.sidebar.button('Meu Perfil', width='stretch')
    if perfil:
        pass

# --- Login com admin --- #
if st.session_state.admin:
    st.sidebar.write('Página de administração:')
    administracao = st.sidebar.button('Administração', width='stretch')
    if administracao:
        st.switch_page('./pages/admin.py')
