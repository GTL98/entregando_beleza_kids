# --- Importar as bibliotecas --- #
from PIL import Image
from imagens import *
import streamlit as st

# --- Importar o módulo de login --- #
from login_cliente import login_cliente

# --- Importar o módulo de mostrar os produtos --- #
from mostrar_produtos import mostrar_produtos

# --- Importar o CSS --- #
from menu_css import css

# --- Configurações da página --- #
st.set_page_config(
    page_title='Cuidados da pele',
    page_icon=Image.open(FAVICON),
    layout='wide'
)

# --- CSS --- #
st.html(css)

# --- Logo da sidebar --- #
st.logo(image=LOGO_MENU_ABERTO, icon_image=LOGO_MENU_FECHADO)

# --- Título da página --- #
st.title('Produtos para cuidados da pele')

# --- Mostrar os produtos --- #
mostrar_produtos('cuidados_pele', 'compra')

# --- Compras na sessão do site --- #
if 'compras' not in st.session_state:
    st.session_state.compras = {'produtos': 0}

# --- Verificar se o cliente está logado no site --- #
if 'login' not in st.session_state:
    st.session_state.login = False
if st.session_state.login is False:
    # --- Cadastro do cliente --- #
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
        st.switch_page('./pages/finalizar.py')

    # --- Ir à página da finalização da compra --- #
    perfil = st.sidebar.button('Meu Perfil', width='stretch')
    if perfil:
        st.switch_page('./pages/meu_perfil.py')

# --- Login com admin --- #
if st.session_state.admin:
    st.sidebar.write('Página de administração:')
    administracao = st.sidebar.button('Administração', width='stretch')
    if administracao:
        st.switch_page('./pages/admin.py')