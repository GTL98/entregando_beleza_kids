# --- Importar as bibliotecas --- #
import os
import requests
import streamlit as st


def mostrar_produtos(banco: str, tipo: str, kit:bool=False) -> None:
    """
    Função responsável por mostrar os produtos na tela.
    :param banco: Banco do produto selecionado.
    :param tipo: Qual tipo de requisição ('compra', 'adm').
    :param kit: Se é para montagem do kit ou não.
    """
    # --- Link do banco de dados --- #
    link = st.secrets['LINK_BD_PRODUTOS']

    # --- Se o tipo de requisição for de compra --- #
    if tipo == 'compra':
        # --- Obter o dicionário da categoria --- #
        requisicao = requests.get(f'{link}/{banco}/.json')
        conteudo = requisicao.json()

        # --- Obter os códigos dos produtos --- #
        codigos = list(conteudo.keys())

        # --- Mostrar as informações de cada produto --- #
        for codigo in codigos:
            # --- Estoque dos produtos --- #
            estoque = conteudo[codigo]['estoque']

            # --- Se está na campanha atual --- #
            campanha = conteudo[codigo]['campanha']

            # --- Mostrar somente se o produto estiver na campanha --- #
            if campanha:
                # --- Colcoar os produtos que estão em estoque --- #
                if estoque >= 1:
                    with st.container(border=True):
                        # --- Obter as informações dos produtos --- #
                        foto = conteudo[codigo]['foto']
                        nome = conteudo[codigo]['nome']
                        de = conteudo[codigo]['de']
                        preco = conteudo[codigo]['preco']
                        descricao = conteudo[codigo]['descricao']

                        # --- Colocar as informações no site --- #
                        st.image(foto, width=380)
                        nome_formatado = nome.replace('<b>', '').replace('</b>', '')\
                        .replace('<i>', '').replace('</i>', '').replace('<h3>', '')\
                        .replace('</h3>', '').replace('<h4>', '').replace('</h4>', '')
                        st.write(nome, unsafe_allow_html=True)
                        if descricao:
                            st.write(descricao, unsafe_allow_html=True)
                        if de != '0':
                            st.subheader(f'De: R$ {de}')
                            st.subheader(f'Por: R$ {preco}')
                        else:
                            st.subheader(f'R$: {preco}')

                        # --- Mudar o texto do botão se for kit ou avulso --- #
                        if kit:
                            botao_texto = 'Adicionar ao kit'
                            kit_texto = 'SIM'
                        else:
                            botao_texto = 'Comprar'
                            kit_texto = 'Não'
                        botao_compra = st.button(botao_texto, width='stretch', key=f'botao_{codigo}')

                        # --- Colocar somente 1 vez o produto no carrinho --- #
                        if botao_compra:
                            if codigo not in st.session_state.compras.keys():
                                # --- Colocar o produto na sessão --- #
                                if kit:
                                    nome_produto = f'{nome_formatado} (KIT)'
                                else:
                                    nome_produto = f'{nome_formatado}'
                                st.session_state.compras[codigo] = {
                                    'foto': foto,
                                    'produto': nome_produto,
                                    'preco': preco,
                                    'estoque': estoque,
                                    'codigo': codigo,
                                    'banco': banco,
                                    'kit': kit_texto
                                }

                                # --- Aumentar a quantidade de produtos no carrinho --- #
                                st.session_state.compras['produtos'] += 1

                                # --- Mostrar que o produto foi adicionado ao carrinho --- #
                                st.success(f'O produto {nome_formatado} foi adicionado ao carrinho.')


    # --- Se o tipo de requisição for para administração --- #
    if tipo == 'adm':
        # --- Obter o dicionário da classe do produto --- #
        requisicao = requests.get(f'{link}/{banco}/.json')
        return requisicao.json()