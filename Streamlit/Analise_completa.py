# Bibliotecas usadas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import warnings
import requests
warnings.filterwarnings("ignore")

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from io import StringIO
from datetime import date
from matplotlib.ticker import FuncFormatter



# Título
st.title('Aspectos Macroeconômicos das Exportações de Vinho no Brasil')

st.markdown("<br>", unsafe_allow_html=True)

objetivo = """
Nesta reportagem, você vai ver uma análise da macroeconomia das exportações de vinho do Rio Grande do Sul. O intuito é identificar os principais países importadores do nosso produto, avaliar a influência da taxa de câmbio do dólar sobre as exportações e examinar as condições climáticas que justificam a posição dominante da nossa região, o Rio Grande do Sul, responsável por mais de 90% da produção de vinho no Brasil.
"""
st.write(objetivo)

st.subheader("Análise Econômica")

analise_economica = """
O propósito desta análise é identificar os principais mercados que importam os vinhos do Brasil, destacando as nações que são consideradas nossos principais clientes.
"""
st.write(analise_economica)


# CARREGANDO ARQUIVOS A SEREM UTILIZADOS
url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/ExpVinho.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text), sep=";")

# dados exportados do site da vinícola
# df = pd.read_csv('ExpVinho.csv', sep=";")

# dado demográfico do paraguay - popuplação +20 anos - fonte https://opendata.paho.org/en/core-indicators/core-indicators-dashboard
# Home Core Indicators
# Dash: Country Profile; Dimension: Population aged 20 and over (thousands); Período: 2008 - 2022
url_excel = 'Demografico_Pop_Idade_20_mais.xlsx'
df_demografico_pop_20_mais = pd.read_excel(url_excel, engine='openpyxl')
#df_demografico_pop_20_mais = pd.read_excel(r'Demografico_Pop_Idade_20_mais.csv')

# Carregando o arquivo
# dado demográfico do paraguay - popuplação +20 anos - fonte https://www.paho.org/en/enlace/alcohol-consumption
# Home  ENLACE: Data Portal on Noncommunicable Diseases, Mental Health, and External Causes  Alcohol consumption
# Dash: Level of alcohol consumption; Country: Paraguay and EUA

df_consumo_alcool_litros_paraguay_eua = pd.read_excel("Consumo_Alcool_Paraguay_EUA.xlsx") 

# Comunicado ténico 226 - Vitivinicultura Brasileira: panorama 2021
# fonte https://ainfo.cnptia.embrapa.br/digital/bitstream/doc/1149674/1/Com-Tec-226.pdf

df_br_estado_producao_uvas_ton = pd.read_excel("Viticultura_brasileira.xlsx") 

# dados sobre importação do paraguay de vinho provindo do Brasil - fonte Paraguai2021.pdf

dados_import_vinhos_br = pd.read_excel("import_vinhos_br.xlsx")

# TRATAMENTO DE DADOS
years = list(range(2008, 2023))

# Criando listas vazias
paises_vinho = []
anos_vinho = []
quantidades_vinho = []
valores_vinho = []

# Iterando pelos dados para preencher as listas
for index, row in df.iterrows():
    for year in years:
        paises_vinho.append(row['País'])
        anos_vinho.append(year)
        quantidades_vinho.append(row[str(year)])
        valores_vinho.append(row[str(year) + '.1'])

# Criando o dataframe reformatado
final_data_vinho = pd.DataFrame({
    'País': paises_vinho,
    'Ano': anos_vinho,
    'Quantidade': quantidades_vinho,
    'ValorUSD': valores_vinho
})

# Calculando o valor total exportado e a quantidade para cada país ao longo do período de 15 anos para o novo conjunto de dados
total_vinho_pais = final_data_vinho.groupby('País').agg({'Quantidade': 'sum', 'ValorUSD': 'sum'}).reset_index()

# Ordenando os países pelo VALOR exportado
total_vinho_pais_sorted = total_vinho_pais.sort_values(by='ValorUSD', ascending=False)

# Calculando o valor total exportado e a quantidade para cada país ao longo do período de 15 anos para o novo conjunto de dados
total_vinho_pais = final_data_vinho.groupby('País').agg({'Quantidade': 'sum', 'ValorUSD': 'sum'}).reset_index()

# Ordenando os países pelo VOLUME exportado
total_vinho_pais_sorted_by_volume = total_vinho_pais.sort_values(by='Quantidade', ascending=False)

st.subheader("Valores Acumulados para Exportação em Dólar e Volume (litros)")

valores_acumulados = """
Com o objetivo de identificar os principais destinos das exportações dos produtos vitivinícolas brasileiros, elaborou-se um gráfico que representa o valor consolidado exportado em dólares para diferentes países durante o período de 2008 a 2022. Observa-se que Paraguai, Rússia, Estados Unidos e China destacam-se como os principais destinos, evidenciando a relevância dessas nações para o setor.
"""
st.write(valores_acumulados)

# Configurando o estilo
sns.set_style("whitegrid")

# Criando a visualização no Streamlit
st.subheader('Ranking de Países por Valor Exportado (USD) entre 2008-2022')

# Plotando os 10 principais países por valor de exportação
fig, ax = plt.subplots(figsize=(8, 10))
sns.barplot(x='ValorUSD', y='País', data=total_vinho_pais_sorted.head(20), palette='viridis', ax=ax)
ax.set(xlabel='Valor Total Exportado (USD)', ylabel='País')
ax.xaxis.labelpad = 20

# Formatando o eixo x para mostrar valores com vírgula e sem casas decimais
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.xaxis.set_major_formatter(formatter)

# Adicionando rótulos numéricos para cada barra
for index, value in enumerate(total_vinho_pais_sorted.head(10)['ValorUSD']):
    ax.text(value, index, f'{value:,.0f}', ha='left', va='center', fontsize=10, color='black')

ax.set_xlim(0, 45000000)
ax.set_xticks([0, 10000000, 20000000, 30000000, 40000000])  
plt.xticks(rotation=45)
plt.tight_layout()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

volume_total_exportado = """
Da mesma forma, criou-se um gráfico que apresenta o volume total exportado para cada país, expresso em litros. Nota-se que Rússia, Paraguai, Estados Unidos e China mantêm-se no topo da lista. Dessa maneira, podemos categorizar esses países como os principais clientes, reforçando sua significativa importância no contexto das exportações de produtos vitivinícolas.
"""
st.write(volume_total_exportado)

st.markdown("<br>", unsafe_allow_html=True)

# Configurando o estilo
sns.set_style("whitegrid")

# Criando a visualização no Streamlit
st.subheader('Ranking de Países por Quantidade Exportada (litros) entre 2008-2022')

# Plotando os 10 principais países por valor de exportação
fig, ax = plt.subplots(figsize=(8, 10))
sns.barplot(x='Quantidade', y='País', data=total_vinho_pais_sorted_by_volume.head(20), palette='viridis', ax=ax)
ax.set(xlabel='Valor Total de Exportação (Litros)', ylabel='País')
ax.xaxis.labelpad = 20

# Formatando o eixo x para mostrar valores com vírgula e sem casas decimais
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.xaxis.set_major_formatter(formatter)

# Adicionando rótulos numéricos para cada barra
for index, value in enumerate(total_vinho_pais_sorted_by_volume.head(20)['Quantidade']):
    ax.text(value, index, f'{value:,.0f}', ha='left', va='center', fontsize=10, color='black')

ax.set_xlim(0, 45000000)
ax.set_xticks([0, 10000000, 20000000, 30000000, 40000000])  # Ajuste para os valores desejados no eixo x
ax.legend(loc='upper left', bbox_to_anchor=(0.5, 0))
plt.xticks(rotation=45)
plt.tight_layout()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

montante_acumulado_anual = """
Ao realizar uma análise mais detalhada dos dados relativos aos cinco principais países, com base no ranking de valor exportado em dólares, apresentamos o gráfico a seguir. Este gráfico ilustra o montante acumulado anual exportado em dólares para essas nações. 

Rússia chama a atenção em 2009 e 2013, por ter um pico bem acima dos demais, contudo 2016 e 2019 não houve exportação para esse país.

Já o Paraguai se destaca como o país que consistentemente amplia seu consumo. Ano após ano, observamos um aumento do valor exportado.

Estados Unidos, China e Reino Unido oscilam, mas não demonstram uma taxa de crescimento na exportação.
"""
st.write(montante_acumulado_anual)

# Lista de países
lista_paises = total_vinho_pais_sorted.head(5)['País'].tolist()
top_paises_vinho = lista_paises
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Criando a visualização no Streamlit
st.subheader('Exportação de Vinho Brasileiro para os 5 Principais Países (2008-2022)')

# Plotando a tendência anual para os 3 principais países
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="magma", linewidth=1, ax=ax)
ax.set(xlabel='Ano', ylabel='Valor de Exportação (USD)')
ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20

# Formatando o eixo y para mostrar valores com vírgula e sem casas decimais
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

ax.set_ylim(0, 15500000)
ax.set_yticks(np.arange(0, 15500000, 500000))
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulo apenas para o país "Paraguai"
pais = "Paraguai"
linha = filtro_data_vinho[filtro_data_vinho['País'] == pais]
ultimo_valor = linha['ValorUSD'].iloc[-1]
ax.annotate(f'{pais} - {ultimo_valor:,.0f}', 
            xy=(linha['Ano'].iloc[-1], ultimo_valor),
            xytext=(0, 60), 
            textcoords='offset points',
            ha='left', va='center',
            color=ax.get_lines()[top_paises_vinho.index(pais)].get_c(), rotation=90)

plt.tight_layout()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

analise_volumetrica = """
Realizando uma análise volumétrica, destacamos os mais bem rankeados: China, Estados Unidos, Paraguai, Reino Unido e Rússia. Em particular, nos anos de 2009 e 2013, observamos um notável aumento no consumo de nossos vinhos pela Rússia, coincidindo com o pico no gráfico monetário apresentado anteriormente.

Como na análise monetária anterior, Paraguai se destaca como o único país que consistentemente amplia seu consumo de nossos vinhos. Ano após ano, observamos um aumento na quantidade importada por esse país.
"""
st.write(analise_volumetrica)

# Criando a visualização no Streamlit
st.subheader('Exportação em litros para os Países Selecionados (2008-2022)')

# Selecionando os 5 principais países
lista_paises = total_vinho_pais_sorted.head(5)['País'].tolist()
top_paises_vinho = lista_paises
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Plotando a tendência anual para os 3 principais países
fig, ax = plt.subplots(figsize=(6, 6))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='Quantidade', hue='País', marker="o", palette="magma", linewidth=1, ax=ax)
ax.set(xlabel='Ano', ylabel='Quantidade (L)')
ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20

# Formatando o eixo y para mostrar valores com vírgula e sem casas decimais
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

ax.set_ylim(0, 23000000)
ax.set_yticks(np.arange(0, 23000000, 1000000))
ax.legend(title='País', fontsize=12)

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulo apenas para o país "Paraguai"
pais = "Paraguai"
linha = filtro_data_vinho[filtro_data_vinho['País'] == pais]
ultimo_valor = linha['Quantidade'].iloc[-1]
ax.annotate(f'{pais} - {ultimo_valor:,.0f}', 
            xy=(linha['Ano'].iloc[-1], ultimo_valor),
            xytext=(0, 60), 
            textcoords='offset points',
            ha='left', va='center',
            color=ax.get_lines()[top_paises_vinho.index(pais)].get_c(), rotation=90)

plt.tight_layout()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Um olhar para o top 5 em valor exportado")

st.markdown(
    "<div style='font-size: 23px; font-weight: bold;'>1. Paraguai</div>",
    unsafe_allow_html=True
)

paraguai = """
As exportações para o Paraguai têm aumentado consistentemente ao longo dos anos, com um pico notável em 2021.
Dado o crescimento sustentado nas exportações para o Paraguai, é recomendado fortalecer as relações comerciais e explorar oportunidades para diversificar a oferta de produtos.
"""
st.write(paraguai)

# Supondo que total_vinho_pais_sorted é o seu DataFrame
lista_paises = ["Paraguai"]

top_paises_vinho = lista_paises 
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico no Streamlit 
fig, ax = plt.subplots(figsize=(11, 7))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor de Exportação (USD)', fontsize=14, labelpad=20)
plt.title('Exportações para Paraguai (2008-2022)', fontsize=16)
plt.legend(title='País', fontsize=12, loc='upper left')

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

plt.ylim(0, 10000000)
plt.yticks(np.arange(0, 10000000, 1000000))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulos ponto a ponto
for index, row in filtro_data_vinho.iterrows():
    pais = row['País']
    ano = row['Ano']
    valor = row['ValorUSD']

    # Adicionando o rótulo ao ponto no gráfico com rotação de 45 graus
    plt.annotate(f'{pais}: ${valor:,.0f}', xy=(ano, valor), xytext=(0, 60),
                 textcoords='offset points', fontsize=8, color='black', ha='left', va='center', rotation=90)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='font-size: 23px; font-weight: bold;'>2. Estados Unidos</div>",
    unsafe_allow_html=True
)

estados_unidos = """
As exportações para os EUA têm mostrado uma oscilação, mas não uma tendência de crescimento neste mercado.
O mercado dos EUA tem potencial de crescimento. A recomendação é considerar campanhas de marketing e promoções para aumentar a visibilidade e aceitação do vinho brasileiro nos EUA.
"""
st.write(estados_unidos)

# Supondo que total_vinho_pais_sorted é o seu DataFrame
lista_paises = ["Estados Unidos"]

top_paises_vinho = lista_paises 
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico no Streamlit 
fig, ax = plt.subplots(figsize=(10, 7))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor de Exportação (USD)', fontsize=14, labelpad=20)
plt.title('Exportações para EUA (2008-2022)', fontsize=16)
plt.legend(title='País', fontsize=12, loc='upper left')

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

plt.ylim(0, 4000000)
plt.yticks(np.arange(0, 4000000, 1000000))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulos ponto a ponto
for index, row in filtro_data_vinho.iterrows():
    pais = row['País']
    ano = row['Ano']
    valor = row['ValorUSD']

    # Adicionando o rótulo ao ponto no gráfico com rotação de 45 graus
    plt.annotate(f'{pais}: ${valor:,.0f}', xy=(ano, valor), xytext=(0, 60),
                 textcoords='offset points', fontsize=8, color='black', ha='left', va='center', rotation=90)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='font-size: 23px; font-weight: bold;'>3. Rússia</div>",
    unsafe_allow_html=True
)

russia = """
As exportações para a Rússia apresentam certa imprevisibilidade. Em 2013, aparentemente estávamos conquistando espaço no mercado, porém a partir de 2014 tivemos resultados ruins.
A partir de 2020 houveram novas importações, porém ainda não muito promissoras.
"""
st.write(russia)

# Supondo que total_vinho_pais_sorted é o seu DataFrame
lista_paises = ["Rússia"]

top_paises_vinho = lista_paises 
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico no Streamlit
fig, ax = plt.subplots(figsize=(13, 10))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Valor de Exportação (USD)', fontsize=14, labelpad=20)
plt.title('Exportações para Rússia (2008-2022)', fontsize=14)
plt.legend(title='País', fontsize=14)

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

plt.ylim(-1000000, 17000000)
plt.yticks(np.arange(0, 17000000, 1000000))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulos ponto a ponto
for index, row in filtro_data_vinho.iterrows():
    pais = row['País']
    ano = row['Ano']
    valor = row['ValorUSD']

    # Adicionando o rótulo ao ponto no gráfico com rotação de 60 graus
    plt.annotate(f'{pais}: ${valor:,.0f}', xy=(ano, valor), xytext=(0, 30),
                 textcoords='offset points', fontsize=8, color='black', ha='left', va='center', rotation=60)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='font-size: 23px; font-weight: bold;'>4. China</div>",
    unsafe_allow_html=True
)

china = """
Exportações para a China demonstração volatilidade e não apresenta tendência de crescimento. É um mercado que nunca passamos de US$ 642.177 (pico em 2012).
Este mercado tem potencial de crescimento. A recomendação é considerar campanhas de marketing e promoções para aumentar a visibilidade e aceitação do vinho brasileiro.
"""
st.write(china)

# Supondo que total_vinho_pais_sorted é o seu DataFrame
lista_paises = ["China"]

top_paises_vinho = lista_paises 
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico no Streamlit
fig, ax = plt.subplots(figsize=(10, 7))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor de Exportação (USD)', fontsize=14, labelpad=20)
plt.title('Exportações para China (2008-2022)', fontsize=12)
plt.legend(title='País', fontsize=12)

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

plt.ylim(0, 1000000)
plt.yticks(np.arange(0, 1000000, 250000))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulos ponto a ponto
for index, row in filtro_data_vinho.iterrows():
    pais = row['País']
    ano = row['Ano']
    valor = row['ValorUSD']

    # Adicionando o rótulo ao ponto no gráfico com rotação de 45 graus
    plt.annotate(f'{pais}: ${valor:,.0f}', xy=(ano, valor), xytext=(0, 50),
                 textcoords='offset points', fontsize=8, color='black', ha='left', va='center', rotation=90)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div style='font-size: 23px; font-weight: bold;'>5. Reino Unido</div>",
    unsafe_allow_html=True
)

reino_unido = """
A análise das exportações do Reino Unido revela uma ausência de tendência de crescimento. Até 2013, alcançamos um patamar superior a 250 mil, atingindo um pico em 2014 com 1,3 milhões. No entanto, nos anos subsequentes, as vendas não mantiveram esse ritmo de crescimento. A partir de 2017, observamos declínios, e de 2019 a 2022 permanecemos abaixo da marca de 250 mil em exportações. 
É um mercado que precisa de estimo de marketing e parcerias comerciais para alavancar mais vendas.
"""
st.write(reino_unido)

# Supondo que total_vinho_pais_sorted é o seu DataFrame
lista_paises = ["Reino Unido"]

top_paises_vinho = lista_paises 
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o gráfico no Streamlit
fig, ax = plt.subplots(figsize=(10, 7))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Valor de Exportação (USD)', fontsize=14, labelpad=20)
plt.title('Exportações para Reino Unido (2008-2022)', fontsize=12)
plt.legend(title='País', fontsize=12)

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

plt.ylim(0, 2500000)
plt.yticks(np.arange(0, 2500000, 250000))

# Ajustando os rótulos do eixo x para mostrar anos de um em um
anos = filtro_data_vinho['Ano'].unique()
ax.set_xticks(anos)
ax.set_xticklabels(anos, rotation=45, ha='right')

# Adicionando rótulos ponto a ponto
for index, row in filtro_data_vinho.iterrows():
    pais = row['País']
    ano = row['Ano']
    valor = row['ValorUSD']

    # Adicionando o rótulo ao ponto no gráfico com rotação de 45 graus
    plt.annotate(f'{pais}: ${valor:,.0f}', xy=(ano, valor), xytext=(0, 50),
                 textcoords='offset points', fontsize=8, color='black', ha='left', va='center', rotation=90)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Um olhar especial para o Paraguai")

top_paises_vinho = ['Paraguai']
dados_paraguai = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

anos = list(range(2015, 2020))
dados_paraguai_anos_15_20 = dados_paraguai[dados_paraguai['Ano'].isin(anos)]

# Criar um dicionário de DataFrames
# dados_import_vinhos_br - USD importados somente do Brasil
dicionario = {'Paraguai': dados_paraguai_anos_15_20, 'DadosImportBR': dados_import_vinhos_br}

# Definir uma função de merge que usa a coluna 'Ano' como chave
def merge_dataframes(left_df, right_df):
    return pd.merge(left_df, right_df, left_on='Ano', right_on='ano', how='inner')

# Inicializar o DataFrame final com um dos DataFrames
dados_paraguai_anos_15_20_import_vinhos_br = dicionario['Paraguai']

# Iterar sobre os outros DataFrames e mesclar com o DataFrame final
for nome_df, df in dicionario.items():
    if nome_df != 'Paraguai':  # Para evitar mesclar consigo mesmo
        dados_paraguai_anos_15_20_import_vinhos_br = merge_dataframes(dados_paraguai_anos_15_20_import_vinhos_br, df)

# O resultado_final agora é um único DataFrame contendo a junção de todos os DataFrames

# Remover a coluna 'ano' inplace
dados_paraguai_anos_15_20_import_vinhos_br.drop(columns=['ano'], inplace=True)
dados_paraguai_anos_15_20_import_vinhos_br.rename(columns={'usd': 'import_br_usd'}, inplace=True)

estudo_mercado_paraguai = """
Um estudo intitulado 'Estudo de Mercado de Vinhos, Espumantes e Sucos de Uva no Paraguai', encomendado pela Embaixada do Brasil em Assunção e conduzido pela consultoria ICA, apresentou dados relativos à quantidade de dólares exportados do Brasil (como país) para o Paraguai em produtos derivados de uva.

Ao analisar os dados fornecidos pela Embrapa, que compila informações de exportação provenientes do Estado do Rio Grande do Sul, foi possível extrair conclusões relevantes. O gráfico evidencia que o montante exportado pelo estado do Rio Grande do Sul segue a tendência das exportações do mercado brasileiro para o Paraguai.

Destaca-se uma correlação extremamente forte, com um coeficiente de correlação de 0.9939 entre as duas variáveis. A pequena distância entre as duas linhas permite concluir que o Paraguai importou predominantemente do estado do Rio Grande do Sul.

Além disso, vemos que a distância entre as curvas é pequena. Podemos concluir que Rio Grande do Sul é o estado que majoritariamente exporta derivados de uva para o Paraguai.
"""
st.write(estudo_mercado_paraguai)

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Definindo as cores
color1 = (128, 0, 128)
color2 = (190, 142, 230)
color1 = tuple(x / 255.0 for x in color1)
color2 = tuple(x / 255.0 for x in color2)

# Criando o gráfico no Streamlit com modificações
fig, ax = plt.subplots(figsize=(8, 6))

sns.lineplot(x='Ano', y='import_br_usd', data=dados_paraguai_anos_15_20_import_vinhos_br, label='BR - Exportação Derivados da Uva', color=color1, ax=ax)
sns.lineplot(x='Ano', y='ValorUSD', data=dados_paraguai_anos_15_20_import_vinhos_br, label='RS - Exportação Derivados da Uva', color=color2, ax=ax)

ax.set_xticks(dados_paraguai_anos_15_20_import_vinhos_br['Ano'])
ax.set_xticklabels(dados_paraguai_anos_15_20_import_vinhos_br['Ano'], rotation=45, ha='right')

plt.xlabel('Ano', labelpad=20)
plt.ylabel('Valor de Exportação (USD)', labelpad=20)
plt.title('Exportação de Derivados de Uva do Brasil para o Paraguai (2015-2020)', pad=15)

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

ax.set_ylim(0, 7000000)

ax.legend()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fontes: Embrapa | Consultoria ICA. Estudo de Mercado de Vinhos, Espumantes e Sucos de Uva no Paraguai</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

corr = """
A correlação entre 'Exportação Derivados de Uva do Brasil' e 'Exportação Derivados de Uva do Rio Grande do Sul' é: 0.9939.
"""
st.write(corr)

correlacao = dados_paraguai_anos_15_20_import_vinhos_br['import_br_usd'].corr(dados_paraguai_anos_15_20_import_vinhos_br['ValorUSD'])

correlacao = round(correlacao, 4)

# print("A correlação entre 'Exportação Derivados de Uva do Brasil'")
# print(f"e 'Exportação Derivados de Uva do Rio Grande do Sul' é: {correlacao}")

principal_exportador = """
Confirmamos a conclusão de que o Rio Grande do Sul é o principal estado exportador de derivados de uva no Brasil, conforme evidenciado no gráfico abaixo, que apresenta dados de 2018 a 2021. O estado se destaca em todos os anos, com valores significativamente superiores aos demais.
"""
st.write(principal_exportador)

st.markdown("<br>", unsafe_allow_html=True)

# Configuração da paleta de cores
paleta = sns.color_palette("rocket_r", 24)

# Configuração do tamanho total do gráfico
fig, axes = plt.subplots(2, 2, figsize=(12, 7))

# Loop para criar quatro subplots
anos = ["ANO_2018", "ANO_2019", "ANO_2020", "ANO_2021"]

for i, ano in enumerate(anos):
    row, col = divmod(i, 2)
    ax = axes[row, col]
    
    # Ordenar os dados por produção em ordem decrescente
    sorted_data = df_br_estado_producao_uvas_ton.sort_values(by=ano, ascending=False)
    
    # Plotagem do gráfico de barras
    sns.barplot(data=sorted_data, x="ESTADOS", y=ano, hue="ESTADOS", palette=paleta, errorbar=None, ax=ax)
    
    # Configurações adicionais para melhorar a apresentação
    for bar, valor in zip(ax.patches, sorted_data[ano]):
        color = sns.color_palette("rocket_r", as_cmap=True)(valor / sorted_data[ano].max())
        bar.set_color(color)

    ax.set_title(f"Produção de Uvas por Estado - {ano}")
    ax.set_xlabel("Estados", fontsize=10)
    ax.set_ylabel("Produção (toneladas)", fontsize=10)
    ax.tick_params(axis='x', rotation=90)
    
    # Adiciona formatação de milhar com ponto no eixo y
    formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
    ax.yaxis.set_major_formatter(formatter)

# Ajustes de layout
plt.tight_layout()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Vitivinicultura Brasileira</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Análise de correlação entre taxa de câmbio e valor exportado")

corr_cambio = """
Essa análise econômica tem como objetivo verificar se a taxa de câmbio tem uma correlação com o valor exportado, em dólar, para os três principais países importadores de vinhos do Brasil.

Mostraremos a taxa de câmbio do dólar, frente ao real brasileiro, entre 2008 a 2023, e calcularemos a correlação com o valor exportado de cada respectivo ano para Paraguai, Estados Unidos e Rússia, que são os países que mais importam nossos vinhos.

Para a correlação, será utilizado a média da taxa de câmbio anual.
"""
st.write(corr_cambio)

import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# from io import StringIO
import matplotlib.dates as mdates
from datetime import date

# IMPORTANDO DADOS

dados = pd.read_csv("TAXA_CAMBIO_HISTORICO.csv", encoding='ISO-8859-1', skiprows=0, sep=';', skipfooter=12, thousands='.', decimal=',', engine ="python")
dados_vinho = pd.read_csv("ExpVinho.csv", sep=";") 

# RENOMEANDO COLUNAS
primeira_coluna = dados.columns[0]
dados = dados.rename(columns={primeira_coluna: 'datas'})
segunda_coluna = dados.columns[1]
dados = dados.rename(columns={segunda_coluna: 'cambio'})
dados['datas'] = pd.to_datetime(dados['datas'], format='%d/%m/%Y')

# Filtrando os dados para incluir apenas a partir de 2008
dados_filtrados = dados[dados['datas'].dt.year >= 2008]
# Extrair o ano da coluna 'datas'
dados_filtrados = dados_filtrados.copy()
dados_filtrados['ano'] = dados_filtrados['datas'].dt.year

# Calcular a média da coluna 'cambio' agrupando por ano
# Está escrito mediana_por_ano, mas é média
mediana_por_ano = dados_filtrados.groupby('ano')['cambio'].mean().reset_index()

# CRIANDO UM DATASET PARA TRAZER PAÍS, ANO, QUANTIDADE (L) E VALOR EXPORTADO (USD)
years = list(range(2008, 2023))

# Criando listas vazias
paises_vinho = []
anos_vinho = []
quantidades_vinho = []
valores_vinho = []

# Iterando pelos dados para preencher as listas
for index, row in dados_vinho.iterrows():
    for year in years:
        paises_vinho.append(row['País'])
        anos_vinho.append(year)
        quantidades_vinho.append(row[str(year)])
        valores_vinho.append(row[str(year) + '.1'])

# Criando o dataframe reformatado
final_data_vinho = pd.DataFrame({
    'País': paises_vinho,
    'Ano': anos_vinho,
    'Quantidade': quantidades_vinho,
    'ValorUSD': valores_vinho
})

variacao_cambio = """
No 'Gráfico de Linha - Câmbio ao Longo do Tempo' abaixo mostra o valor da taxa de câmbio entre 2008 e 2023. Através dele podemos acompanhar a valorização do dólar (EUA) frente a moeda brasileira.
"""
st.write(variacao_cambio)

# Criando o gráfico de linha usando o SeabornNO '
fig, ax = plt.subplots(figsize=(8, 4))  
sns.lineplot(x='datas', y='cambio', data=dados_filtrados, label="Valor do Dólar", ax=ax)
ax.xaxis.set_major_locator(mdates.YearLocator())

# Configurar os tiques do eixo x para mostrar todos os anos e rotacioná-los em 45 graus
plt.xticks(rotation=45)

# Adicione rótulos e título ao gráfico
plt.xlabel('Data', labelpad=20)
plt.ylabel('Valor do Dólar', labelpad=20)
plt.title('Gráfico de Linha - Câmbio ao Longo do Tempo')

plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, 7)
plt.legend()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: IPEA Data</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

tendencia_anual = """
No 'Tendência Anual de Exportação de Vinho Brasileiro' vemos a tendência anual do valor exportado em dólar para os três principais importadores de produtos da viticultura brasileira: Estados Unidos, Paraguai e Rússia. Paraguai se destaca porque a partir de 2015 começa uma crescente de importação. Ano a ano há uma aumento, exceto em 2019 e 2020. Devido essa tendência crescente Paraguai é o nosso principal cliente.
"""
st.write(tendencia_anual)

top_paises_vinho = ['Paraguai', 'Rússia', 'Estados Unidos']
filtro_data_vinho = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# Plotando a tendência anual para os 3 principais países
fig, ax = plt.subplots(figsize=(5, 4))
sns.lineplot(data=filtro_data_vinho, x='Ano', y='ValorUSD', hue='País', marker="o", palette="viridis", linewidth=2.5, ax=ax)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Valor de Exportação (USD)', fontsize=12)
ax.tick_params(axis='x', labelrotation=45) 
ax.set_title('Tendência Anual de Exportação de Vinho Brasileiro', fontsize=12)
ax.legend(title='País', fontsize=12)
plt.tight_layout()

formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

ax.set_ylim(-2000000, 17000000)

# Adicionar linhas de grade
ax.grid(True, linestyle='--', alpha=0.7)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fonte: Embrapa</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Filtrar os dados para incluir apenas linhas onde a coluna 'País' é 
final_data_vinho_paraguai = final_data_vinho[final_data_vinho['País'] == 'Paraguai']
final_data_vinho_russia = final_data_vinho[final_data_vinho['País'] == 'Rússia']
final_data_vinho_eua = final_data_vinho[final_data_vinho['País'] == 'Estados Unidos']

# Renomear a coluna 'ano' em 'mediana_por_ano' para 'Ano' para coincidir com o nome da coluna em 'final_data_vinho_paraguai'
mediana_por_ano = mediana_por_ano.rename(columns={'ano': 'Ano'})

# Merge dos DataFrames com base na coluna 'Ano'
final_data_vinho_paraguai_dolar = pd.merge(final_data_vinho_paraguai, mediana_por_ano, on='Ano')
final_data_vinho_russia_dolar = pd.merge(final_data_vinho_russia, mediana_por_ano, on='Ano')
final_data_vinho_eua_dolar = pd.merge(final_data_vinho_eua, mediana_por_ano, on='Ano')

valor_medio_anual_dolar = "Fazendo uma correlação do valor médio anual do dólar com gŕafico 'Tendência Anual de Exportação de Vinho Brasileiro', para cada país, temos os seguintes valores."
st.write(valor_medio_anual_dolar)

correlacao_paraguai = final_data_vinho_paraguai_dolar['ValorUSD'].corr(final_data_vinho_paraguai_dolar['cambio'])
correlacao_russia = final_data_vinho_russia_dolar['ValorUSD'].corr(final_data_vinho_russia_dolar['cambio'])
correlacao_eua = final_data_vinho_eua_dolar['ValorUSD'].corr(final_data_vinho_eua_dolar['cambio'])

correlacao_paraguai = round(correlacao_paraguai, 4)
correlacao_russia = round(correlacao_russia, 4)
correlacao_eua = round(correlacao_eua, 4)
# print(f"CORR Paraguai: {correlacao_paraguai}")
# print(f"CORR Rússia: {correlacao_russia}")
# print(f"CORR EUA: {correlacao_eua}")

# Valores das correlações
dados_tabela = {
    'País': ['Paraguai', 'Rússia', 'EUA'],
    'Correlação': [0.8693, -0.3513, -0.2901]
}

df = pd.DataFrame(dados_tabela)

st.markdown(
    "<div style='text-align: center; font-size: 20px;'><b>Correlação Anual: Dólar vs Exportação de Vinho Brasileiro<b></div>",
    unsafe_allow_html=True
)

# Exibir a tabela no Streamlit
st.table(df)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fontes análise de câmbio: Embrapa | GPEstatistica | Consultoria ICA | Vitivinicultura Brasileira: Panorama 2021</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

GPEstatistica = """
De acordo com o GPEstatística, uma correlação é considerada forte quando o coeficiente (r) é superior a 0,6 e igual ou inferior a 0,9. Ao analisarmos os dados, observamos que o valor do dólar não exerce uma influência significativa sobre as exportações para a Rússia e os Estados Unidos, pois sua correlação é bastante reduzida.

Entretanto, ao examinarmos as relações com o Paraguai, identificamos uma correlação de 0,8693, indicando uma associação forte entre a taxa de câmbio e o valor exportado. Nesse contexto, a valorização do dólar está diretamente relacionada ao aumento das exportações em dólares para esse país. Torna-se evidente que o valor exportado é sensível às flutuações cambiais.

Essa informação revela-se valiosa para compreender quais fatores impactam nossos lucros, fornecendo insights cruciais para a gestão estratégica dos negócios.
"""
st.write(GPEstatistica)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Análise Demográfica - Paraguai")

consumo_2015_2019 = """
Foi estimado a quantidade de litros consumido de bebidas alcoólicas da população do Paraguai. A quantidade estimada de consumo alcoólico foi através da multiplicação entre quantidade de pessoas maiores de 20 anos e a quantidade de álcool consumido nos respectivos anos, entre 2015 e 2019.
O gráfico abaixo mostra o estimado de consumo alcoólico do Paraguai e o valor em litros exportado pelo estado do Rio Grande do Sul, entre 2015 a 2019.
A diferença entre os valores é muito grande, porém é possível verificar que a quantidade exportada segue a tendência do consumo alcoólico do país.
"""
st.write(consumo_2015_2019)

corr_retas = """
A correlação entre essas duas retas é de: **0,9041**.

Esse crescente consumo de bebidas álcoolicas benefíciou a exportação de derivados de uva do Brasil. A população do Paraguai demandou mais bebidas álcoolicas e nossas vinícolas supriram em parte essa demanda.
"""
st.write(corr_retas)

# corr_ConsumoVsExportado = df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'].corr(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'])

# corr_ConsumoVsExportado = round(corr_ConsumoVsExportado,4)

# print(f"CORR: {corr_ConsumoVsExportado}")

df_consumo_alcool_litros_paraguay_2015_over = df_consumo_alcool_litros_paraguay_eua.query('Sex == "Both sexes" and Country == "Paraguay" and Year >= 2015')

dados_paraguai_anos_15_20_import_vinhos_br_2015_over = dados_paraguai_anos_15_20_import_vinhos_br.query('País == "Paraguai" and Ano >= 2015')

correlacao_importacaoUSD_pessoasOver20 = dados_paraguai_anos_15_20_import_vinhos_br['import_br_usd'].corr(df_demografico_pop_20_mais['People'])

# Mesclar os DataFrames com base na coluna 'Year'
df_consumo_alcool_litros_paraguay_2015_over_with_people = pd.merge(
    df_consumo_alcool_litros_paraguay_2015_over,
    df_demografico_pop_20_mais[['Year', 'People']],
    on='Year',
    how='left'  # Use 'left' para preservar todas as linhas do DataFrame de consumo
)

df_consumo_alcool_litros_paraguay_2015_over_with_people['Liters_Total'] = df_consumo_alcool_litros_paraguay_2015_over_with_people['Liters'] * df_consumo_alcool_litros_paraguay_2015_over_with_people['People']

dados_paraguai_anos_15_20_import_vinhos_br_2015_over = dados_paraguai_anos_15_20_import_vinhos_br_2015_over.rename(columns={'Ano': 'Year'})
dados_paraguai_anos_15_20_import_vinhos_br_2015_over

df_consumo_alcool_litros_paraguay_2015_over_with_people_2 = pd.merge(
    df_consumo_alcool_litros_paraguay_2015_over_with_people,
    dados_paraguai_anos_15_20_import_vinhos_br_2015_over[['Year', 'Quantidade']],
    on='Year',
    how='left'  # Use 'left' para preservar todas as linhas do DataFrame de consumo
)

# Configuração do tamanho da figura
fig, ax = plt.subplots(figsize=(10, 8))

# Definição de cores
color1 = (128, 0, 128)
color2 = (190, 142, 230)

# Normalizar os valores RGB para o intervalo [0, 1]
color1 = tuple(x / 255.0 for x in color1)
color2 = tuple(x / 255.0 for x in color2)

# Plotar as linhas e adicionar rótulos nos pontos
plot1 = sns.lineplot(x='Year', y='Liters_Total', data=df_consumo_alcool_litros_paraguay_2015_over_with_people_2, label='Consumo estimado de bebidas alcoólicas', color=color1)
plot2 = sns.lineplot(x='Year', y='Quantidade', data=df_consumo_alcool_litros_paraguay_2015_over_with_people_2, label='Exportação do Rio Grande do Sul', color=color2)

# Adicionar rótulos nos pontos para o plot1
for line in range(0, df_consumo_alcool_litros_paraguay_2015_over_with_people_2.shape[0]):
    plot1.text(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'][line], 
               df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'][line], 
               f"{df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'][line]:,.0f}", 
               ha='center', va='bottom', rotation=45)

# Adicionar rótulos nos pontos para o plot2
for line in range(0, df_consumo_alcool_litros_paraguay_2015_over_with_people_2.shape[0]):
    plot2.text(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'][line], 
               df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'][line], 
               f"{df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'][line]:,.0f}", 
               ha='center', va='bottom')

# Configurações adicionais do gráfico
plt.xticks(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'])

# Formate a escala do eixo y para incluir separador de milhar com ponto
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
plt.gca().yaxis.set_major_formatter(formatter)

# Coloque um limite para o valor y. Pegue o maior valor e coloque 20% a mais.
plt.ylim(0, 40000000)

# Adicione rótulos e título ao gráfico
plt.xlabel('Ano', fontsize=14, labelpad=15)
plt.ylabel('Quantidade (litros)', fontsize=14, labelpad=15)
plt.title('Paraguai - Consumo de bebidas alcoólicas x Quantidade Exportada', fontsize=16, pad=20)

# Ajustando o layout para evitar cortes
plt.tight_layout()

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Fontes da análise demográfica: População Maior de 20 anos do Paraguai | Consumo de álcool no Paraguai | Exportação do Rio Grande do Sul</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Bibliotecas utilizadas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, MonthLocator, YearLocator
import sys
import warnings
warnings.filterwarnings("ignore")

# Título
st.title('O Rio Grande do Sul Destaca-se como o Principal Cultivador de Videiras no Brasil')

st.markdown("<br>", unsafe_allow_html=True)

RS = """
O Rio Grande do Sul é o maior produtor nacional de uva, contribuindo significativamente com aproximadamente 90% da produção nacional de uvas destinadas ao processamento. A Serra Gaúcha emerge como a principal zona produtora, responsável por cerca de 85% da produção de uvas no estado. Além disso, as regiões da Campanha Gaúcha, Serra do Sudeste, Campos de Cima da Serra e Vale Central também desempenham papéis proeminentes na atividade vitivinícola. Devido à magnitude da produção no Rio Grande do Sul, os dados desse estado são considerados como a principal base de referência para representação e análise do setor vitivinícola em âmbito nacional.

A produção de uva é destinada não apenas ao consumo de mesa, mas também à elaboração de sucos e vinhos, tanto de forma artesanal quanto industrial. Abaixo, segue uma imagem representando as Indicações Geográficas (IG) no território nacional.
"""
st.write(RS)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Indicações Geográficas (IG) de Vinhos do Brasil e Associações de Produtores")

# Adicionando a imagem
st.image("indicacoes_geograficas.jpg", caption="Fonte: https://www.embrapa.br/uva-e-vinho/indicacoes-geograficas-de-vinhos-do-brasil", use_column_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Influência da temperatura na videira
temperatura_videira = """
A atividade fotossintética da videira é fortemente influenciada pela temperatura do ar. O comportamento da cultura da videira é significativamente afetado pela temperatura, sendo este o fator ambiental mais significante. A temperatura do ar influencia a atividade fotossintética das plantas, sendo que as reações da fotossíntese são menos intensas em temperaturas abaixo de 20°C, atingindo o máximo entre 25 e 30°C, e diminuindo novamente quando a temperatura se aproxima de 45°C.

A faixa de temperatura média considerada ideal para a produção de uvas de mesa situa-se entre 20°C e 30°C. Nesse intervalo, as condições são propícias para o desenvolvimento da videira e para a produção de uvas de mesa, passas e vinhos doces.

A temperatura da região de cultivo também afeta a composição química da uva. Em regiões com temperaturas mais elevadas, dentro dos limites críticos, há maior concentração de açúcar e menor concentração de ácido málico nos frutos. Isso favorece a produção de uva de mesa, passas e vinhos doces. Em regiões mais frias, as condições são mais propícias para a produção de vinhos secos, devido ao maior teor de ácido nos frutos.

O zoneamento agroclimático é uma ferramenta utilizada para delimitar regiões propícias ao cultivo da videira. Esse zoneamento considera variáveis como temperatura, umidade, precipitação e evapotranspiração. Em algumas regiões, como o Submédio São Francisco, as condições climáticas são favoráveis ao crescimento da videira.
"""
st.write(temperatura_videira)

# Análise climática
st.subheader("Análise Climática nas Regiões Produtoras: Estudo Detalhado de Precipitação e Temperatura no Rio Grande do Sul")

analise_climatica = """
Exploramos os registros da base de dados do Instituto Nacional de Meteorologia -
INMET e adquirimos dados sobre chuva e temperatura de forma mensal, abrangendo o
período de 2007 a 2022. A produção de uvas no Rio Grande do Sul é predominante, representando 90% do total nacional. Optamos por avaliar as condições climáticas em cidades cruciais no cultivo de uvas, como Erechim, Alegrete, Rio Grande, Bento Gonçalves e Bagé.

Para conduzir a análise, adotamos os seguintes procedimentos: realizamos a limpeza
dos dados e organizamos a temperatura e a precipitação em gráficos para uma
inspeção visual em busca de padrões.

A seguir, apresentamos uma análise exploratória com estatística descritiva,
destacando as variáveis de temperatura (em graus Celsius) e precipitação (em
milímetros) nas cinco cidades consideradas. As tabelas contêm dados do número total
de observações, média, desvio padrão, valor mínimo, primeiro quartil (25%), mediana
(50%), terceiro quartil (75%) e valor máximo para cada variável, abrangendo todas as
regiões analisadas. Seguem as tabelas:
"""
st.write(analise_climatica)

# Leitura dos dados
analise_mediana_mensal = pd.read_csv("analise_mediana_mensal.csv", parse_dates=["Data de Referência"])
analise_precipitacao_mensal = pd.read_csv("analise_precipitacao_mensal.csv", parse_dates=["Data de Referência"])

# Lista de cidades
cidades = ['Bento Gonçalves', 'Alegrete', 'Bagé', 'Rio Grande', 'Erechim']

def gerar_tabela_descritiva(analise_mediana_mensal, analise_precipitacao_mensal):
    # Selecionando as cinco cidades
    df_temp_mediana = analise_mediana_mensal[analise_mediana_mensal['Cidade'].isin(cidades)]
    df_temp_precipitacao = analise_precipitacao_mensal[analise_precipitacao_mensal['Cidade'].isin(cidades)]

    # Convertendo as datas para o formato datetime
    df_temp_mediana['Data de Referência'] = pd.to_datetime(df_temp_mediana['Data de Referência'])
    df_temp_precipitacao['Data de Referência'] = pd.to_datetime(df_temp_precipitacao['Data de Referência'])

    # Calculando estatísticas descritivas para temperatura mediana
    desc_temp_mediana = df_temp_mediana.groupby('Cidade')['Temperatura Mediana (°C)'].describe().round(2)

    # Calculando estatísticas descritivas para precipitação
    desc_precipitacao = df_temp_precipitacao.groupby('Cidade')['Precipitação (mm)'].describe().round(2)

    return desc_temp_mediana, desc_precipitacao

# Chamando a função nas tabelas
tabela_temp_mediana, tabela_precipitacao = gerar_tabela_descritiva(analise_mediana_mensal, analise_precipitacao_mensal)

# Exibindo as tabelas centralizadas
st.subheader("Estatística Descritiva - Temperatura (C°):")
st.dataframe(tabela_temp_mediana.style.format("{:.2f}").set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'center'}))

st.subheader("Estatística Descritiva - Precipitação (mm):")
st.dataframe(tabela_precipitacao.style.format("{:.2f}").set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'center'}))

st.markdown("<br>", unsafe_allow_html=True)

# Análise Exploratória: Estatísticas Descritivas de Temperatura e Precipitação
st.subheader("Análise Exploratória: Estatísticas Descritivas de Temperatura e Precipitação")

st.markdown("<br>", unsafe_allow_html=True)

tabela_temp_mediana = tabela_temp_mediana.reset_index()
tabela_precipitacao = tabela_precipitacao.reset_index()

# Criando a função para gerar as tabelas com o Matplotlib
def criar_tabela_matplotlib(titulo, dados):
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis('off')

    rotulos = ['Cidade', 'Número total de observações', 'Média', 'Desvio Padrão', 'Valor Mínimo', 'Primeiro Quartil (25%)', 'Mediana (50%)', 'Terceiro Quartil (75%)', 'Valor Máximo']

    # Criando a tabela diretamente a partir dos dados
    tabela_matplotlib = ax.table(cellText=dados.values,
                                 colLabels=rotulos,
                                 loc='center',
                                 cellLoc='center')
    tabela_matplotlib.auto_set_font_size(False)
    tabela_matplotlib.set_fontsize(12)  
    tabela_matplotlib.auto_set_column_width([0] + list(range(1, len(rotulos)))) 
    tabela_matplotlib.scale(1.7, 2.7) 

    titulo_table = ax.text(0.5, 1.6, titulo, va='center', ha='center', fontsize=15)

    # Exibindo a tabela
    st.pyplot(fig)

# Exibindo as tabelas no Streamlit
criar_tabela_matplotlib("Estatística Descritiva - Temperatura (C°)", tabela_temp_mediana)
criar_tabela_matplotlib("Estatística Descritiva - Precipitação (mm)", tabela_precipitacao)

st.markdown("<br>", unsafe_allow_html=True)

analise_cinco_cidades = """
Finalizamos com uma análise exploratória abrangente que conectou as cinco
cidades, explorando as relações entre temperatura mediana durante o período
de 2007 a 2023. A seguir, apresentamos o gráfico correspondente:
"""
st.write(analise_cinco_cidades)

st.markdown("<br>", unsafe_allow_html=True)

# Criando o gráfico
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(15, 7))

for cidade in cidades:
    cidade_data = analise_mediana_mensal[analise_mediana_mensal['Cidade'] == cidade]
    sns.lineplot(data=cidade_data, x='Data de Referência', y='Temperatura Mediana (°C)', label=cidade)

ax.set(xlabel='Data de Referência', ylabel='Temperatura (°C)')
locator = MonthLocator(bymonthday=1, interval=6)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.set_xticks(pd.date_range(start='2007-01-01', end='2023-01-01', freq='6MS'))
plt.xticks(rotation=65, ha='right')
ax.set_ylim(0, 30)
ax.legend(title='Cidade', bbox_to_anchor=(1.05, 0.5), loc='center left', ncol=1, borderaxespad=-3.5)

# Exibindo o gráfico
st.pyplot(fig)
st.markdown(
    "<div style='text-align: center; font-size: 12px;'>Gráfico 11: Variação da Temperatura Mediana Mensal das cinco cidades (2007-2023)</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

influencia_El_Nino = """
As elevadas temperaturas não tiveram um impacto adverso direto na
produção. Houve períodos em que as temperaturas estavam
consideravelmente acima da média, como evidenciado em 2022. No entanto,
apesar dessas condições, a produção foi robusta nesse ano, sugerindo que as
altas temperaturas não exercem uma influência determinante nas condições
das safras. Ao analisar as temperaturas de forma ordenada, da estação mais
quente para a mais fria, não foi possível identificar um padrão visual claro que
permitisse fazer afirmações conclusivas. Além de 2022, o ano de 2011 também
se destacou como um dos mais quentes, correlacionado a um aumento
significativo na produção. Em resumo, as oscilações de temperatura estiveram
presentes tanto nos picos quanto nos declínios na produção.

A influência do fenômeno El Niño nas chuvas pode ser significativa para a
produção e safra das uvas ao longo dos anos de 2007 a 2022. O El Niño,
caracterizado pelo aquecimento anômalo das águas do Oceano Pacífico, tem
potencial para alterar os padrões climáticos em diversas regiões do mundo,
inclusive afetando as condições meteorológicas em áreas vitivinícolas.

Durante os anos em que o El Niño esteve presente, é possível observar
variações nas chuvas que podem impactar diretamente a produção de uvas.
Eventos climáticos extremos, como chuvas intensas ou períodos de seca
prolongados associados ao El Niño, podem influenciar o ciclo de crescimento
das vinhas, afetando a qualidade e quantidade da safra.

Notamos que nos anos de ocorrência do fenômeno El Niño, há uma correlação
com reduções significativas, sejam sutis ou extremas, na produção de vinhos,
especialmente os tintos, tanto os de mesa quanto os finos, que são
comercializados em grande escala. A previsão de um El Niño para 2024 destaca a importância de os agricultores estarem atentos às suas safras neste
ano específico, considerando os potenciais impactos adversos nas condições
climáticas.
"""
st.write(influencia_El_Nino)

st.markdown("<br>", unsafe_allow_html=True)

conclusao_impactos_climaticos = """Conclusão"""
st.subheader(conclusao_impactos_climaticos)

conclusao = """
Investir no setor vitivinícola brasileiro, especialmente no estado do Rio Grande do Sul, apresenta-se como uma oportunidade estratégica e promissora para os investidores. Destacamos as razões fundamentais que respaldam essa recomendação:

**1. Crescimento Sustentável:**
   - As exportações de vinho do Brasil têm registrado um crescimento sustentável, com destaque para mercados-chave como Paraguai, Rússia, Estados Unidos e China.
   - O Paraguai, em particular, emerge como um mercado em ascensão constante, oferecendo oportunidades de expansão e diversificação.

**2. Mercados Estratégicos:**
   - A diversificação dos destinos de exportação, com ênfase em países como Rússia e China, abre portas para mercados estratégicos e amplia o alcance internacional do setor.

**3. Estabilidade no Rio Grande do Sul:**
   - O Rio Grande do Sul, responsável por mais de 90% da produção nacional, destaca-se como o principal estado exportador de derivados de uva no Brasil.
   - Condições climáticas favoráveis, com temperaturas ideais entre 20°C e 30°C, contribuem para uma produção consistente e de alta qualidade.

**4. Correlação Positiva com o Paraguai:**
   - A forte correlação entre as exportações do Rio Grande do Sul e o mercado paraguaio ressalta a confiabilidade e a liderança desse estado no cenário vitivinícola brasileiro.

**5. Análise de Riscos:**
   - A análise climática indica a resiliência do Rio Grande do Sul frente a fenômenos climáticos passados, como o El Niño, não comprometendo significativamente a produção.
   - Monitoramento constante e práticas agrícolas eficientes contribuem para mitigar riscos climáticos.

**6. Recomendações de Marketing:**
   - Recomenda-se estratégias de marketing e promoção para consolidar e expandir a presença em mercados como Estados Unidos e Rússia, aproveitando seu potencial de crescimento.

**Em síntese, investir no setor vitivinícola brasileiro, com ênfase no Rio Grande do Sul, oferece aos investidores a perspectiva de participar de um mercado em expansão, impulsionado por exportações consistentes e favoráveis condições de produção. A resiliência demonstrada diante de desafios climáticos passados e as estratégias de crescimento sustentável posicionam o setor como uma escolha confiável para investimentos sólidos e de longo prazo.**
"""
st.write(conclusao)

st.subheader("Referências")

referencias = """
***EMBRAPA. Dados da Vitivinicultura.***
Disponível em: https://www.cnpuv.embrapa.br/vitibrazil/index.php?opcao=opt_01 - Acesso em 02 de novembro de 2024.

***IPEA Data. Taxa de câmbio comercial para compra.***
Disponível em: http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M - Acesso em 02 de novembro de 2023.

***GPEstatistica. Coeficiente de Correlação de Pearson.***
Disponível em: https://gpestatistica.netlify.app/blog/correlacao - Acesso em 06 de janeiro de 2024.

***Consultoria ICA. Estudo de Mercado de Vinhos, Espumantes e Sucos de Uva no Paraguai.***
Disponível em: https://www.gov.br/empresas-e-negocios/pt-br/invest-export-brasil/exportar/conheca-os-mercados/pesquisas-de-mercado/estudo-de-mercado.pdf/Paraguai2021.pdf - Acesso em 20 de janeiro de 2024.

***Vitivinicultura Brasileira: Panorama 2021.***
Disponível em: https://ainfo.cnptia.embrapa.br/digital/bitstream/doc/1149674/1/Com-Tec-226.pdf - Acesso em 20 de janeiro de 2024.

***População Maior de 20 anos do Paraguai.***
Disponível em: https://opendata.paho.org/en/core-indicators/core-indicators-dashboard - Acesso em 20 de janeiro de 2024.

***Consumo de Álcool no Paraguai.***
Disponível em: https://www.paho.org/en/enlace/alcohol-consumption - Acesso em 20 de janeiro de 2024.

***Exportação do Rio Grande do Sul.***
Disponível em: https://www.cnpuv.embrapa.br/vitibrazil/index.php?opcao=opt_01 - Acesso em 20 de janeiro de 2024.

***INMET - Instituto Nacional de Meteorologia.***
Disponível em:
https://portal.inmet.gov.br/dadoshistoricos - Acesso em 28/11/2023.

***BASF Brasil | Agricultura.***
Disponível em:
https://agriculture.basf.com/br/pt/conteudos/cultivos-e-sementes/uva/qual-e-a-temperatura-ideal-para-o-cultivo-de-videiras-tropicais.html - Acesso em 06/01/2024.

***Vinícula Aliança.***
Disponível em:
https://vinicolaalianca.com.br/blog/3/suco-de-uva-alianca/69/voce-sabe-quanto-tempo-a-videira-leva-para-dar-uvas-confira-aqui - Acesso em 06/01/2024.

***Veja.***
Disponível em:
https://veja.abril.com.br/ciencia/el-nino-deve-durar-pelo-menos-ate-abril-de-2024-diz-agencia-da-onu - Acesso em 07/01/2024.

***g1 | Meio Ambiente.***
Disponível em:
https://g1.globo.com/meio-ambiente/noticia/2023/11/08/el-nino-deve-durar-ao-menos-ate-abril-de-2024-aponta-organizacao-meteorologica-mundial.ghtml - Acesso em 07/01/2024.

***Embrapa.***
Disponível em:
https://www.embrapa.br/cim-uva-e-vinho/a-viticultura-no-brasil - Acesso em 08/01/2024.\n
http://www.cpatsa.embrapa.br:8080/sistema_producao/spuva/clima.html - Acesso em 08/01/2024.\n
https://www.embrapa.br/uva-e-vinho/indicacoes-geograficas-de-vinhos-do-brasil - Acesso em 08/01/2024.\n

***Visão analítica da viticultura sul-rio-grandense – Conab***. 
Compêndio de estudos Conab V.19, 2019 - Acesso em 09/01/2024.

***Atlas Socioeconômico Rio Grande do Sul.***
Disponível em:
https://atlassocioeconomico.rs.gov.br/uva-e-maca#:~:text=O%20cultivo%20de%20uva%20no,de%2052%25%20da%20produ%C3%A7%C3%A3o%20nacional. - Acesso em 09/01/2024.

***Revista Brasileira de Engenharia Agrícola e Ambiental.***
Disponível em:
https://www.scielo.br/j/rbeaa/a/mDNzxqwJj3qZ3VrzwsMLNwL/? - Acesso em 10/01/2024.
"""
st.write(referencias)
