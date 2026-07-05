# --- Importar as bibliotecas --- #
import streamlit as st
import plotly.express as px


class Graficos:
    def __init__(self, dados):
        self.dados = dados
        self.nomes = ['Acessórios e utilidade', 'Cabelos', 'Cuidados da pele', 'Saboentes']

    def barra_precos(self) -> None:
        """Função responsável por criar o gráfico de barras do preço dos produtos."""
        # --- Obter as chaves dos bancos --- #
        bancos = self.dados.keys()

        # --- Criar para cada banco uma lista vazia --- #
        dic_bancos = {banco: [] for banco in bancos}

        # --- Adicionar o valor de cada produto ao dicionário --- #
        for banco in bancos:
            for codigo in self.dados[banco]:
                preco = round(float(str(self.dados[banco][codigo]['preco']).replace(',', '.')) * self.dados[banco][codigo]['estoque'], 2)
                dic_bancos[banco].append(preco)

        # --- Dicionário com o valor final da soma --- #
        dic_soma = {chave: round(sum(valores), 2) for chave, valores in dic_bancos.items()}

        # --- Eixos do dicionário --- #
        eixo_x = list(dic_soma.keys())
        eixo_y = list(dic_soma.values())

        # --- Preço médio de todos os produtos --- #
        preco_medio = round(sum(eixo_y) / len(eixo_y), 2)

        # --- Criar a figura --- #
        fig = px.bar(
            x=eixo_x,
            y=eixo_y,
            labels={'x': 'Produtos', 'y': 'Valor total (R$)'},
            title='Valor total dos produtos (R$)',
            text_auto=True
        )

        # --- Adicionar a linha com o preço médio --- #
        fig.add_hline(
            y=preco_medio,
            line_dash='dash',
            line_color='red',
            line_width=2,
            annotation_text=f'Preço médio: R$ {preco_medio}',
            annotation_font_size=16,
            annotation_position='top right',
            annotation_font_color='red'
        )

        # --- Atualizar o layout do gráfico --- #
        fig.update_layout(
            hoverlabel=dict(
                bgcolor='white',
                font_size=22,
                font_family='Arial'
            )
        )
        fig.update_xaxes(
            tickvals=eixo_x,
            ticktext=self.nomes,
            tickfont=dict(
                family='Arial',
                size=14
            ),
            title_font=dict(
                size=18,
                family='Arial',
                color='black'
            )
        )

        fig.update_yaxes(
            title_font=dict(
                size=18,
                family='Arial',
                color='black'
            )
        )
        fig.update_traces(
            hovertemplate='<b>%{x}</b><br><br>'+
            'Valor total: R$ %{y}<br>'+
            '<extra></extra>'
        )

        # --- Mostrar o gráfico --- #
        st.plotly_chart(fig)

    def barra_estoque(self) -> None:
        """Função responsável por criar o gráfico de barras do estoque produtos."""
        # --- Obter as chaves dos bancos --- #
        bancos = self.dados.keys()

        # --- Criar para cada banco uma lista vazia --- #
        dic_bancos = {banco: [] for banco in bancos}

        # --- Adicionar o valor de cada produto ao dicionário --- #
        for banco in bancos:
            for codigo in self.dados[banco]:
                dic_bancos[banco].append(self.dados[banco][codigo]['estoque'])

        # --- Dicionário com o valor final da soma --- #
        dic_soma = {chave: sum(valores) for chave, valores in dic_bancos.items()}

        # --- Eixos do dicionário --- #
        eixo_x = list(dic_soma.keys())
        eixo_y = list(dic_soma.values())

        # --- Quantidade média de todos os produtos --- #
        qtde_media = round(sum(eixo_y) / len(eixo_y), 0)

        # --- Criar a figura --- #
        fig = px.bar(
            x=eixo_x,
            y=eixo_y,
            labels={'x': 'Produtos', 'y': 'Quantidade'},
            title='Quantidade de produtos em estoque',
            text_auto=True
        )

        # --- Adicionar a linha com o preço médio --- #
        fig.add_hline(
            y=qtde_media,
            line_dash='dash',
            line_color='red',
            line_width=2,
            annotation_text=f'Qtde. média: {qtde_media:.0f}',
            annotation_font_size=16,
            annotation_position='top right',
            annotation_font_color='red'
        )

        # --- Atualizar o layout do gráfico --- #
        fig.update_layout(
            hoverlabel=dict(
                bgcolor='white',
                font_size=22,
                font_family='Arial'
            )
        )
        fig.update_xaxes(
            tickvals=eixo_x,
            ticktext=self.nomes,
            tickfont=dict(
                family='Arial',
                size=14
            ),
            title_font=dict(
                size=18,
                family='Arial',
                color='black'
            )
        )

        fig.update_yaxes(
            title_font=dict(
                size=18,
                family='Arial',
                color='black'
            )
        )
        fig.update_traces(
            hovertemplate='<b>%{x}</b><br><br>' +
                          'Qtde. em estoque: %{y}<br>' +
                          '<extra></extra>'
        )

        # --- Mostrar o gráfico --- #
        st.plotly_chart(fig)

    def pizza_precos(self) -> None:
        """Função responsável por criar o gráfico de pizza da proporção dos preços dos produtos."""
        # --- Obter as chaves dos bancos --- #
        bancos = self.dados.keys()

        # --- Criar para cada banco uma lista vazia --- #
        dic_bancos = {banco: [] for banco in bancos}

        # --- Adicionar o valor de cada produto ao dicionário --- #
        for banco in bancos:
            for codigo in self.dados[banco]:
                preco = round(
                    float(str(self.dados[banco][codigo]['preco']).replace(',', '.')) * self.dados[banco][codigo][
                        'estoque'], 2)
                dic_bancos[banco].append(preco)

        # --- Valor de cada pedaço --- #
        valores = [sum(valor) for valor in dic_bancos.values()]

        # --- Criar a figura --- #
        fig = px.pie(
            names=self.nomes,
            values=valores,
            title='Proporção do valor de cada categoria'
        )

        # --- Atualizar o layout do gráfico --- #
        fig.update_layout(
            hoverlabel=dict(
                bgcolor='white',
                font_size=22,
                font_family='Arial'
            ),
            width=800,
            height=800
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Valor total: R$ %{value}<br>Proporção: %{percent}<extra></extra>'
        )

        # --- Mostrar o gráfico --- #
        st.plotly_chart(fig)

    def pizza_estoque(self) -> None:
        """Função responsável por criar o gráfico de pizza da proporção do estoque dos produtos."""
        # --- Obter as chaves dos bancos --- #
        bancos = self.dados.keys()

        # --- Criar para cada banco uma lista vazia --- #
        dic_bancos = {banco: [] for banco in bancos}

        # --- Adicionar o valor de cada produto ao dicionário --- #
        for banco in bancos:
            for codigo in self.dados[banco]:
                dic_bancos[banco].append(self.dados[banco][codigo]['estoque'])

                # --- Valor de cada pedaço --- #
            valores = [sum(valor) for valor in dic_bancos.values()]

        # --- Criar a figura --- #
        fig = px.pie(
            names=self.nomes,
            values=valores,
            title='Proporção do estoque de cada categoria'
        )

        # --- Atualizar o layout do gráfico --- #
        fig.update_layout(
            hoverlabel=dict(
                bgcolor='white',
                font_size=22,
                font_family='Arial'
            ),
            width=800,
            height=800
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Qtde. total: %{value}<br>Proporção: %{percent}<extra></extra>'
        )

        # --- Mostrar o gráfico --- #
        st.plotly_chart(fig)