# --- Importar o Streamlit --- #
import streamlit as st

# --- Páginas de navegação --- #
pg = st.navigation(
    [
        st.Page('./pages/home.py', title='Página Inicial'),
        st.Page('./pages/acessorios_utilidades.py', title='Acessórios e utilidades'),
        st.Page('./pages/cabelos.py', title='Cabelos'),
        st.Page('./pages/cuidados_pele.py', title='Cuidados da pele'),
        st.Page('./pages/sabonetes.py', title='Sabonetes'),
        st.Page('./pages/pagina_cadastrar_cliente.py', visibility='hidden'),
        st.Page('./pages/admin.py', visibility='hidden')
     ]
)
pg.run()
