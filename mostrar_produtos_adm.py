# --- Importar o Streamlit --- #
import streamlit as st

# --- Importar o módulo de mostrar os produtos --- #
from mostrar_produtos import mostrar_produtos

# --- Importar o módulo de atualização dos produtos --- #
from atualizar_produto import atualizar_produto

# --- Importar o módulo de exclusão do produto --- #
from deletar_produto import deletar_produto


def mostrar_produtos_adm(banco: str, titulo: str) -> None:
    """
    Função responsável por mostrar os produtos do banco de dados selecionado
    na página de administração.
    :param banco: Banco selecionado.
    :param titulo: Título do banco.
    """
    # --- Título do banco --- #
    st.header(f'Banco: {titulo}')

    # --- Dicionário com as informações dos produtos --- #
    dic_produtos = mostrar_produtos(banco, 'adm')

    # --- Quantidade de produtos cadastrados --- #
    quantidade_produtos = len(dic_produtos.keys())

    # --- Mostrar a quantidade de produtos cadastrados --- #
    st.subheader(f'Quantidade de produtos: {quantidade_produtos}')

    # --- Mostrar em cada container as informações do produto --- #
    for codigo in dic_produtos.keys():
        conteudo = dic_produtos[codigo]
        with st.container(border=True):
            # --- Foto do produto --- #
            foto = conteudo['foto']
            st.subheader('Foto:')
            st.image(foto, width=300)
            foto_campo = st.text_input(
                label='',
                label_visibility='collapsed',
                value=foto,
                key=f'{codigo}_foto'
            )

            # --- Nome do produto --- #
            nome = conteudo['nome']
            st.subheader('Nome:')
            nome_campo = st.text_input(
                label='',
                label_visibility='collapsed',
                value=nome,
                key=f'{codigo}_nome'
            )

            # --- Preço original --- #
            de = conteudo['de']
            st.subheader('De:')
            de_campo = st.text_input(
                label='',
                label_visibility='collapsed',
                value=de,
                key=f'{codigo}_de'
            )

            # --- Preço com desconto --- #
            preco = conteudo['preco']
            st.subheader('Por:')
            preco_campo = st.text_input(
                label='',
                label_visibility='collapsed',
                value=preco,
                key=f'{codigo}_preco'
            )

            # --- Valor de compra do produto --- #
            compra = conteudo['compra']
            st.subheader('Compra:')
            compra_campo = st.text_input(
                label='',
                label_visibility='collapsed',
                value=compra,
                key=f'{codigo}_compra'
            )

            # --- Estoque do produto --- #
            estoque = conteudo['estoque']
            st.subheader('Estoque:')
            estoque_campo = st.number_input(
                label='',
                label_visibility='collapsed',
                value=estoque,
                min_value=0,
                max_value=100,
                key=f'{codigo}_estoque'
            )

            # --- Descrição do produto --- #
            descricao = conteudo['descricao']
            st.subheader('Descrição:')
            descricao_campo = st.text_area(
                label='',
                label_visibility='collapsed',
                value=descricao,
                key=f'{codigo}_descricao'
            )

            # --- Se está na campanha --- #
            campanha = conteudo['campanha']
            if campanha:
                indice = 0
            else:
                indice = 1
            st.subheader('Está na campanha atual:')
            campanha_radio = st.radio(
                label='',
                label_visibility='collapsed',
                options=['Sim', 'Não'],
                index=indice,
                horizontal=True,
                key=f'{codigo}_campanha'
            )

            # --- Atualizar o produto --- #
            colunas = st.columns(2)
            with colunas[0]:
                atualizar = st.button('Atualizar', width='stretch', key=f'{codigo}_atualizar')
                if atualizar:
                    if campanha_radio == 'Sim':
                        campanha_atual = True
                    else:
                        campanha_atual = False
                    atualizar_produto(
                        banco=banco,
                        foto=foto_campo,
                        nome=nome_campo,
                        codigo=codigo,
                        de=de_campo,
                        preco=preco_campo,
                        compra=compra_campo,
                        estoque=estoque_campo,
                        campanha=campanha_atual,
                        descricao=descricao_campo
                    )

            # --- Deletar o produto --- #
            with colunas[1]:
                deletar = st.button('Deletar', width='stretch', key=f'{codigo}_deletar')
                if deletar:
                    deletar_produto(banco, codigo)