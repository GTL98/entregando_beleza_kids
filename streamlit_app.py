# --- Importar o Streamlit --- #
import streamlit as st

# --- Páginas de navegação --- #
pg = st.navigation(
    [
        st.Page('./pages/home.py', title='Página Inicial'),
        st.Page('./pages/pagina_cadastrar_cliente.py', visibility='hidden'),
        st.Page('./pages/admin.py', visibility='hidden')
     ]
)
pg.run()
