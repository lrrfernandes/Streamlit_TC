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
import numpy as np
from io import StringIO
from datetime import date
from matplotlib.ticker import FuncFormatter

import os
import requests

titulo_principal = """
<h1 style="color: #5e9ca0;"><span style="background-color: #ffffff; color: #993366;">Clube Wine S.A.</span></h1>
<h2><span style="background-color: #ffffff; color: #993366;">Departamento de Ci&ecirc;ncia de Dados</span></h2>
<h2><span style="background-color: #ffffff; color: #993366;">_________________________________</span></h2>
<p>&nbsp;</p>
<h1 style="color: #5e9ca0;"><span style="text-decoration: underline;">&Aacute;rea do Investidor</span> - An&aacute;lise da Viticultura do Rio Grande do Sul</h1>
<p>&nbsp;</p>
<pre style="color: #2e6c80;">Cientistas de Dados: Wellington, Andr&eacute;, Raphael, David, Lucas</pre>
"""
st.markdown(titulo_principal, unsafe_allow_html=True)

# Título
st.title('Aspectos Macroeconômicos das Exportações de Vinho no Brasil')

st.markdown("<br>", unsafe_allow_html=True)

objetivo = """
Nesta análise, você vai ver a macroeconomia das exportações de vinho do Rio Grande do Sul. O intuito é identificar os principais países importadores do nosso produto, avaliar a influência da taxa de câmbio do dólar sobre as exportações e examinar as condições climáticas que justificam a posição dominante da nossa região, o Rio Grande do Sul, responsável por mais de 90% da produção de vinho no Brasil.
Por fim, responder: É ainda interessante investir em vinho no Brasil?
"""
st.write(objetivo)

st.subheader("Análise Econômica")

analise_economica = """
O propósito desta análise é identificar os principais mercados que importam os vinhos do Brasil, destacando as nações que são consideradas nossos principais clientes.
"""
st.write(analise_economica)


# CARREGANDO ARQUIVOS A SEREM UTILIZADOS
# url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/ExpVinho.csv"
# response = requests.get(url)
# df = pd.read_csv(StringIO(response.text), sep=";")

# filename = "/mount/src/streamlit_tc/Streamlit/ExpVinho.csv"
df = pd.read_csv('EXP_VINHO.csv', sep=';')
# df = pd.read_csv(filename, sep=";")
st.dataframe(df)

# dados exportados do site da vinícola
# df = pd.read_csv('ExpVinho.csv', sep=";")

# dado demográfico do paraguay - popuplação +20 anos - fonte https://opendata.paho.org/en/core-indicators/core-indicators-dashboard
# Home Core Indicators
# Dash: Country Profile; Dimension: Population aged 20 and over (thousands); Período: 2008 - 2022

text_io = """
Dimension;sub_dimension;Indicator;Year;People
Sociodemographic;Demographic;Population_aged_20_and_over;2008;3094000
Sociodemographic;Demographic;Population_aged_20_and_over;2009;3164000
Sociodemographic;Demographic;Population_aged_20_and_over;2010;324000
Sociodemographic;Demographic;Population_aged_20_and_over;2011;3322000
Sociodemographic;Demographic;Population_aged_20_and_over;2012;3407000
Sociodemographic;Demographic;Population_aged_20_and_over;2013;3493000
Sociodemographic;Demographic;Population_aged_20_and_over;2014;3579000
Sociodemographic;Demographic;Population_aged_20_and_over;2015;3666000
Sociodemographic;Demographic;Population_aged_20_and_over;2016;3752000
Sociodemographic;Demographic;Population_aged_20_and_over;2017;3837000
Sociodemographic;Demographic;Population_aged_20_and_over;2018;3921000
Sociodemographic;Demographic;Population_aged_20_and_over;2019;4003000
Sociodemographic;Demographic;Population_aged_20_and_over;2020;4084000
Sociodemographic;Demographic;Population_aged_20_and_over;2021;4159000
Sociodemographic;Demographic;Population_aged_20_and_over;2022;4225000
"""
text = StringIO(text_io)
df_demografico_pop_20_mais = pd.read_csv(text, sep=";")
text_io = """
"""
text = """
"""
# st.dataframe(df_demografico_pop_20_mais)

# url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/Demografico_Pop_Idade_20_mais.csv"
# response = requests.get(url)
# df_demografico_pop_20_mais = pd.read_csv(StringIO(response.text), sep=";")

# df_demografico_pop_20_mais = pd.read_excel(r'Demografico_Pop_Idade_20_mais.csv')

# Carregando o arquivo
# dado demográfico do paraguay - popuplação +20 anos - fonte https://www.paho.org/en/enlace/alcohol-consumption
# Home  ENLACE: Data Portal on Noncommunicable Diseases, Mental Health, and External Causes  Alcohol consumption
# Dash: Level of alcohol consumption; Country: Paraguay and EUA

text_io = """
Country;Year;Sex;Liters
Paraguay;2000;Male;9,82
Paraguay;2001;Male;9,82
Paraguay;2002;Male;9,16
Paraguay;2003;Male;9,01
Paraguay;2004;Male;9,49
Paraguay;2005;Male;10,43
Paraguay;2006;Male;11,00
Paraguay;2007;Male;11,92
Paraguay;2008;Male;12,06
Paraguay;2009;Male;12,27
Paraguay;2010;Male;11,85
Paraguay;2011;Male;11,74
Paraguay;2012;Male;11,36
Paraguay;2013;Male;10,92
Paraguay;2014;Male;10,58
Paraguay;2015;Male;10,43
Paraguay;2016;Male;10,54
Paraguay;2017;Male;10,80
Paraguay;2018;Male;10,96
Paraguay;2019;Male;10,96
Paraguay;2000;Female;2,63
Paraguay;2001;Female;2,63
Paraguay;2002;Female;2,45
Paraguay;2003;Female;2,41
Paraguay;2004;Female;2,54
Paraguay;2005;Female;2,79
Paraguay;2006;Female;2,95
Paraguay;2007;Female;3,21
Paraguay;2008;Female;3,25
Paraguay;2009;Female;3,31
Paraguay;2010;Female;3,19
Paraguay;2011;Female;3,16
Paraguay;2012;Female;3,06
Paraguay;2013;Female;2,94
Paraguay;2014;Female;2,85
Paraguay;2015;Female;2,81
Paraguay;2016;Female;2,83
Paraguay;2017;Female;2,90
Paraguay;2018;Female;2,94
Paraguay;2019;Female;2,94
Paraguay;2000;Both sexes;6,27
Paraguay;2001;Both sexes;6,27
Paraguay;2002;Both sexes;5,84
Paraguay;2003;Both sexes;5,74
Paraguay;2004;Both sexes;6,05
Paraguay;2005;Both sexes;6,66
Paraguay;2006;Both sexes;7,03
Paraguay;2007;Both sexes;7,62
Paraguay;2008;Both sexes;7,71
Paraguay;2009;Both sexes;7,85
Paraguay;2010;Both sexes;7,59
Paraguay;2011;Both sexes;7,52
Paraguay;2012;Both sexes;7,28
Paraguay;2013;Both sexes;7,00
Paraguay;2014;Both sexes;6,78
Paraguay;2015;Both sexes;6,68
Paraguay;2016;Both sexes;6,74
Paraguay;2017;Both sexes;6,91
Paraguay;2018;Both sexes;7,01
Paraguay;2019;Both sexes;7,01
United States of America;2000;Male;14,66
United States of America;2001;Male;14,66
United States of America;2002;Male;14,68
United States of America;2003;Male;14,71
United States of America;2004;Male;14,74
United States of America;2005;Male;14,77
United States of America;2006;Male;14,82
United States of America;2007;Male;14,84
United States of America;2008;Male;14,79
United States of America;2009;Male;14,61
United States of America;2010;Male;14,54
United States of America;2011;Male;14,68
United States of America;2012;Male;14,91
United States of America;2013;Male;15,07
United States of America;2014;Male;15,13
United States of America;2015;Male;15,24
United States of America;2016;Male;15,33
United States of America;2017;Male;15,41
United States of America;2018;Male;15,44
United States of America;2019;Male;15,44
United States of America;2000;Female;4,39
United States of America;2001;Female;4,39
United States of America;2002;Female;4,40
United States of America;2003;Female;4,43
United States of America;2004;Female;4,45
United States of America;2005;Female;4,47
United States of America;2006;Female;4,50
United States of America;2007;Female;4,50
United States of America;2008;Female;4,47
United States of America;2009;Female;4,41
United States of America;2010;Female;4,38
United States of America;2011;Female;4,43
United States of America;2012;Female;4,51
United States of America;2013;Female;4,56
United States of America;2014;Female;4,58
United States of America;2015;Female;4,62
United States of America;2016;Female;4,65
United States of America;2017;Female;4,68
United States of America;2018;Female;4,69
United States of America;2019;Female;4,69
United States of America;2000;Both sexes;9,40
United States of America;2001;Both sexes;9,40
United States of America;2002;Both sexes;9,42
United States of America;2003;Both sexes;9,45
United States of America;2004;Both sexes;9,47
United States of America;2005;Both sexes;9,50
United States of America;2006;Both sexes;9,54
United States of America;2007;Both sexes;9,56
United States of America;2008;Both sexes;9,52
United States of America;2009;Both sexes;9,40
United States of America;2010;Both sexes;9,36
United States of America;2011;Both sexes;9,45
United States of America;2012;Both sexes;9,60
United States of America;2013;Both sexes;9,71
United States of America;2014;Both sexes;9,76
United States of America;2015;Both sexes;9,83
United States of America;2016;Both sexes;9,89
United States of America;2017;Both sexes;9,95
United States of America;2018;Both sexes;9,97
United States of America;2019;Both sexes;9,97
"""
text = StringIO(text_io)
df_consumo_alcool_litros_paraguay_eua = pd.read_csv(text, sep=";")
text_io = """
"""
text = """
"""

# url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/Consumo_Alcool_Paraguay_EUA.csv"
# response = requests.get(url)
# df_consumo_alcool_litros_paraguay_eua = pd.read_csv(StringIO(response.text), sep=";")
# df_consumo_alcool_litros_paraguay_eua = pd.read_excel("Consumo_Alcool_Paraguay_EUA.xlsx") 

# Comunicado ténico 226 - Vitivinicultura Brasileira: panorama 2021
# fonte https://ainfo.cnptia.embrapa.br/digital/bitstream/doc/1149674/1/Com-Tec-226.pdf

text_io = """
ESTADOS;ANO_2018;ANO_2019;ANO_2020;ANO_2021
Acre;0;0;0;0
Alagoas;0;0;0;0
Amapá;0;0;0;0
Amazonas;0;0;0;0
Bahia;75378;74142;45342;61274
Ceará;422;564;763;521
Distrito Federal;1425;1235;1267;1309
Espírito Santo;3090;3207;3370;3040
Goiás;2121;1656;1411;1496
Maranhão;0;0;0;0
Mato Grosso;1297;1304;1287;1290
Mato Grosso do Sul;72;72;59;57
Minas Gerais;15763;17307;18723;19571
Pará;0;0;0;0
Paraíba;2600;2600;2600;2600
Paraná;54000;48000;57556;57000
Pernambuco;423382;420830;338837;390640
Piauí;51;24;120;96
Rio de Janeiro;170;206;191;86
Rio Grande do Norte;0;0;0;0
Rio Grande do Sul;822689;666423;735358;951567
Rondônia;187;219;197;124
Roraima;0;0;0;0
Santa Catarina;61256;59525;60388;59638
São Paulo;128327;148379;148919;147359
Sergipe;0;0;0;0
Tocantins;12;12;12;12
"""
text = StringIO(text_io)
df_br_estado_producao_uvas_ton = pd.read_csv(text, sep=";")
text_io = """
"""
text = """
"""

# url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/Viticultura_brasileira.csv"
# response = requests.get(url)
# df_br_estado_producao_uvas_ton = pd.read_csv(StringIO(response.text), sep=";")
# df_br_estado_producao_uvas_ton = pd.read_excel("Viticultura_brasileira.xlsx") 

# dados sobre importação do paraguay de vinho provindo do Brasil - fonte Paraguai2021.pdf

text_io = """
ano;usd
2015;928224,00
2016;1894680,00
2017;4786678,00
2018;6035132,00
2019;4798148,00
"""
text = StringIO(text_io)
dados_import_vinhos_br = pd.read_csv(text, sep=";")
text_io = """
"""
text = """
"""

# url = "https://github.com/lrrfernandes/Streamlit_TC/blob/main/Streamlit/import_vinhos_br.csv"
# response = requests.get(url)
# dados_import_vinhos_br = pd.read_csv(StringIO(response.text), sep=";")
# dados_import_vinhos_br = pd.read_excel("import_vinhos_br.xlsx")

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

st.subheader("Um olhar especial para o Rio Grande do Sul")

# top_paises_vinho = ['Paraguai']
# dados_paraguai = final_data_vinho[final_data_vinho['País'].isin(top_paises_vinho)]

# anos = list(range(2015, 2020))
# dados_paraguai_anos_15_20 = dados_paraguai[dados_paraguai['Ano'].isin(anos)]

# Criar um dicionário de DataFrames
# dados_import_vinhos_br - USD importados somente do Brasil
# dicionario = {'Paraguai': dados_paraguai_anos_15_20, 'DadosImportBR': dados_import_vinhos_br}

# Definir uma função de merge que usa a coluna 'Ano' como chave
# def merge_dataframes(left_df, right_df):
#     return pd.merge(left_df, right_df, left_on='Ano', right_on='ano', how='inner')

# Inicializar o DataFrame final com um dos DataFrames
# dados_paraguai_anos_15_20_import_vinhos_br = dicionario['Paraguai']

# Iterar sobre os outros DataFrames e mesclar com o DataFrame final
# for nome_df, df in dicionario.items():
#     if nome_df != 'Paraguai':  # Para evitar mesclar consigo mesmo
#         dados_paraguai_anos_15_20_import_vinhos_br = merge_dataframes(dados_paraguai_anos_15_20_import_vinhos_br, df)

# O resultado_final agora é um único DataFrame contendo a junção de todos os DataFrames

# Remover a coluna 'ano' inplace
# dados_paraguai_anos_15_20_import_vinhos_br.drop(columns=['ano'], inplace=True)
# dados_paraguai_anos_15_20_import_vinhos_br.rename(columns={'usd': 'import_br_usd'}, inplace=True)

# estudo_mercado_paraguai = """
# Um estudo intitulado 'Estudo de Mercado de Vinhos, Espumantes e Sucos de Uva no Paraguai', encomendado pela Embaixada do Brasil em Assunção e conduzido pela consultoria ICA, apresentou dados relativos à quantidade de dólares exportados do Brasil (como país) para o Paraguai em produtos derivados de uva.

# Ao analisar os dados fornecidos pela Embrapa, que compila informações de exportação provenientes do Estado do Rio Grande do Sul, foi possível extrair conclusões relevantes. O gráfico evidencia que o montante exportado pelo estado do Rio Grande do Sul segue a tendência das exportações do mercado brasileiro para o Paraguai.

# Destaca-se uma correlação extremamente forte, com um coeficiente de correlação de 0.9939 entre as duas variáveis. A pequena distância entre as duas linhas permite concluir que o Paraguai importou predominantemente do estado do Rio Grande do Sul.

# Além disso, vemos que a distância entre as curvas é pequena. Podemos concluir que Rio Grande do Sul é o estado que majoritariamente exporta derivados de uva para o Paraguai.
# """
# st.write(estudo_mercado_paraguai)

# Configurando o estilo do Seaborn
# sns.set(style="whitegrid")

# Definindo as cores
# color1 = (128, 0, 128)
# color2 = (190, 142, 230)
# color1 = tuple(x / 255.0 for x in color1)
# color2 = tuple(x / 255.0 for x in color2)

# Criando o gráfico no Streamlit com modificações
# fig, ax = plt.subplots(figsize=(8, 6))

# sns.lineplot(x='Ano', y='import_br_usd', data=dados_paraguai_anos_15_20_import_vinhos_br, label='BR - Exportação Derivados da Uva', color=color1, ax=ax)
# sns.lineplot(x='Ano', y='ValorUSD', data=dados_paraguai_anos_15_20_import_vinhos_br, label='RS - Exportação Derivados da Uva', color=color2, ax=ax)

# ax.set_xticks(dados_paraguai_anos_15_20_import_vinhos_br['Ano'])
# ax.set_xticklabels(dados_paraguai_anos_15_20_import_vinhos_br['Ano'], rotation=45, ha='right')

# plt.xlabel('Ano', labelpad=20)
# plt.ylabel('Valor de Exportação (USD)', labelpad=20)
# plt.title('Exportação de Derivados de Uva do Brasil para o Paraguai (2015-2020)', pad=15)

# formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
# ax.yaxis.set_major_formatter(formatter)

# ax.set_ylim(0, 7000000)

# ax.legend()

# Exibindo o gráfico
# st.pyplot(fig)
# st.markdown(
#     "<div style='text-align: center; font-size: 13px;'>Fontes: Embrapa | Consultoria ICA. Estudo de Mercado de Vinhos, Espumantes e Sucos de Uva no Paraguai</div>",
#     unsafe_allow_html=True
# )

st.markdown("<br>", unsafe_allow_html=True)

# corr = """
# A correlação entre 'Exportação Derivados de Uva do Brasil' e 'Exportação Derivados de Uva do Rio Grande do Sul' é: 0.9939.
# """
# st.write(corr)

# correlacao = dados_paraguai_anos_15_20_import_vinhos_br['import_br_usd'].corr(dados_paraguai_anos_15_20_import_vinhos_br['ValorUSD'])

# correlacao = round(correlacao, 4)

# print("A correlação entre 'Exportação Derivados de Uva do Brasil'")
# print(f"e 'Exportação Derivados de Uva do Rio Grande do Sul' é: {correlacao}")

principal_exportador = """
O Rio Grande do Sul é o principal estado exportador de derivados de uva no Brasil, conforme evidenciado no gráfico abaixo, que apresenta dados de 2018 a 2021. O estado se destaca em todos os anos, com valores significativamente superiores aos demais.
"""
st.write(principal_exportador)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; font-size: 13px;'>Clique na seta para expandir.</div>",
    unsafe_allow_html=True
)

# Configuração da paleta de cores
paleta = sns.color_palette("rocket_r", 24)

# Configuração do tamanho total do gráfico
fig, axes = plt.subplots(2, 2, figsize=(30, 12))

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

import matplotlib.dates as mdates

# IMPORTANDO DADOS
text_io = """
Data;Cambio
01/11/2023;5,0188
31/10/2023;5,0569
30/10/2023;5,0068
27/10/2023;4,9474
26/10/2023;5,0049
25/10/2023;4,9975
24/10/2023;5,0059
23/10/2023;5,0158
20/10/2023;5,0522
19/10/2023;5,0534
18/10/2023;5,0562
17/10/2023;5,0378
16/10/2023;5,0612
13/10/2023;5,0619
11/10/2023;5,0490
10/10/2023;5,0856
09/10/2023;5,1660
06/10/2023;5,1912
05/10/2023;5,1707
04/10/2023;5,1520
03/10/2023;5,1094
02/10/2023;5,0673
29/09/2023;5,0070
28/09/2023;5,0469
27/09/2023;5,0283
26/09/2023;4,9711
25/09/2023;4,9600
22/09/2023;4,9125
21/09/2023;4,9223
20/09/2023;4,8481
19/09/2023;4,8569
18/09/2023;4,8529
15/09/2023;4,8683
14/09/2023;4,8745
13/09/2023;4,9165
12/09/2023;4,9499
11/09/2023;4,9360
08/09/2023;4,9829
06/09/2023;4,9756
05/09/2023;4,9699
04/09/2023;4,9170
01/09/2023;4,9312
31/08/2023;4,9213
30/08/2023;4,8647
29/08/2023;4,8700
28/08/2023;4,8933
25/08/2023;4,8766
24/08/2023;4,8742
23/08/2023;4,8971
22/08/2023;4,9425
21/08/2023;4,9841
18/08/2023;4,9718
17/08/2023;4,9810
16/08/2023;4,9765
15/08/2023;4,9806
14/08/2023;4,9475
11/08/2023;4,8912
10/08/2023;4,8512
09/08/2023;4,9009
08/08/2023;4,9211
07/08/2023;4,9004
04/08/2023;4,8603
03/08/2023;4,8791
02/08/2023;4,8077
01/08/2023;4,7746
31/07/2023;4,7409
28/07/2023;4,7247
27/07/2023;4,7196
26/07/2023;4,7362
25/07/2023;4,7490
24/07/2023;4,7451
21/07/2023;4,7726
20/07/2023;4,7882
19/07/2023;4,7994
18/07/2023;4,8034
17/07/2023;4,8296
14/07/2023;4,7951
13/07/2023;4,8032
12/07/2023;4,8052
11/07/2023;4,8943
10/07/2023;4,8729
07/07/2023;4,8793
06/07/2023;4,8971
05/07/2023;4,8571
04/07/2023;4,8050
03/07/2023;4,7870
30/06/2023;4,8186
29/06/2023;4,8578
28/06/2023;4,8557
27/06/2023;4,7897
26/06/2023;4,7692
23/06/2023;4,7793
22/06/2023;4,7744
21/06/2023;4,7789
20/06/2023;4,7924
19/06/2023;4,7797
16/06/2023;4,8280
15/06/2023;4,8216
14/06/2023;4,8456
13/06/2023;4,8527
12/06/2023;4,8826
09/06/2023;4,8916
07/06/2023;4,9113
06/06/2023;4,9286
05/06/2023;4,9230
02/06/2023;4,9552
01/06/2023;5,0344
31/05/2023;5,0953
30/05/2023;5,0587
29/05/2023;4,9948
26/05/2023;5,0108
25/05/2023;4,9984
24/05/2023;4,9468
23/05/2023;4,9668
22/05/2023;4,9674
19/05/2023;4,9852
18/05/2023;4,9641
17/05/2023;4,9507
16/05/2023;4,9116
15/05/2023;4,9097
12/05/2023;4,9228
11/05/2023;4,9690
10/05/2023;4,9541
09/05/2023;5,0001
08/05/2023;4,9690
05/05/2023;4,9690
04/05/2023;5,0100
03/05/2023;5,0221
02/05/2023;5,0329
28/04/2023;5,0001
27/04/2023;5,0144
26/04/2023;5,0579
25/04/2023;5,0607
24/04/2023;5,0589
20/04/2023;5,0491
19/04/2023;5,0461
18/04/2023;4,9672
17/04/2023;4,9415
14/04/2023;4,9449
13/04/2023;4,9091
12/04/2023;4,9490
11/04/2023;5,0122
10/04/2023;5,0828
06/04/2023;5,0677
05/04/2023;5,0441
04/04/2023;5,0756
03/04/2023;5,0631
31/03/2023;5,0798
30/03/2023;5,1248
29/03/2023;5,1487
28/03/2023;5,1727
27/03/2023;5,2300
24/03/2023;5,2915
23/03/2023;5,2626
22/03/2023;5,2642
21/03/2023;5,2438
20/03/2023;5,2461
17/03/2023;5,2673
16/03/2023;5,2886
15/03/2023;5,2975
14/03/2023;5,2356
13/03/2023;5,2394
10/03/2023;5,1816
09/03/2023;5,1347
08/03/2023;5,1381
07/03/2023;5,1895
06/03/2023;5,1964
03/03/2023;5,2031
02/03/2023;5,2074
01/03/2023;5,2064
28/02/2023;5,2072
27/02/2023;5,1954
24/02/2023;5,1785
23/02/2023;5,1324
22/02/2023;5,1724
17/02/2023;5,2006
16/02/2023;5,2426
15/02/2023;5,2237
14/02/2023;5,1501
13/02/2023;5,1828
10/02/2023;5,2520
09/02/2023;5,2309
08/02/2023;5,2030
07/02/2023;5,1689
06/02/2023;5,1757
03/02/2023;5,1024
02/02/2023;4,9895
01/02/2023;5,0715
31/01/2023;5,0987
30/01/2023;5,0953
27/01/2023;5,0761
26/01/2023;5,0945
25/01/2023;5,1036
24/01/2023;5,1690
23/01/2023;5,1916
20/01/2023;5,1980
19/01/2023;5,2138
18/01/2023;5,0903
17/01/2023;5,1197
16/01/2023;5,1109
13/01/2023;5,1140
12/01/2023;5,1394
11/01/2023;5,2014
10/01/2023;5,2389
09/01/2023;5,2961
06/01/2023;5,2849
05/01/2023;5,4020
04/01/2023;5,4453
03/01/2023;5,3753
02/01/2023;5,3430
30/12/2022;5,2171
29/12/2022;5,2171
28/12/2022;5,2730
27/12/2022;5,2826
26/12/2022;5,1866
23/12/2022;5,1439
22/12/2022;5,1865
21/12/2022;5,2025
20/12/2022;5,2421
19/12/2022;5,3154
16/12/2022;5,2801
15/12/2022;5,3177
14/12/2022;5,3400
13/12/2022;5,2663
12/12/2022;5,3060
09/12/2022;5,2390
08/12/2022;5,2085
07/12/2022;5,2202
06/12/2022;5,2390
05/12/2022;5,2457
02/12/2022;5,1968
01/12/2022;5,1942
30/11/2022;5,2935
29/11/2022;5,3070
28/11/2022;5,3791
25/11/2022;5,3502
24/11/2022;5,3143
23/11/2022;5,3924
22/11/2022;5,3333
21/11/2022;5,3253
18/11/2022;5,3471
17/11/2022;5,4649
16/11/2022;5,3198
14/11/2022;5,3007
11/11/2022;5,3045
10/11/2022;5,3058
09/11/2022;5,1623
08/11/2022;5,1738
07/11/2022;5,0880
04/11/2022;5,0354
03/11/2022;5,1343
01/11/2022;5,1494
31/10/2022;5,2564
28/10/2022;5,3449
27/10/2022;5,2997
26/10/2022;5,3242
25/10/2022;5,3085
24/10/2022;5,2738
21/10/2022;5,1913
20/10/2022;5,2170
19/10/2022;5,2802
18/10/2022;5,2691
17/10/2022;5,2707
14/10/2022;5,2818
13/10/2022;5,3011
11/10/2022;5,2061
10/10/2022;5,1935
07/10/2022;5,2215
06/10/2022;5,2002
05/10/2022;5,2138
04/10/2022;5,1405
03/10/2022;5,1996
30/09/2022;5,4060
29/09/2022;5,3910
28/09/2022;5,3588
27/09/2022;5,3502
26/09/2022;5,3542
23/09/2022;5,2251
22/09/2022;5,1671
21/09/2022;5,1686
20/09/2022;5,1699
19/09/2022;5,2361
16/09/2022;5,2876
15/09/2022;5,2205
14/09/2022;5,1768
13/09/2022;5,1788
12/09/2022;5,1177
09/09/2022;5,1627
08/09/2022;5,2149
06/09/2022;5,2222
05/09/2022;5,1680
02/09/2022;5,1872
01/09/2022;5,2001
31/08/2022;5,1784
30/08/2022;5,0611
29/08/2022;5,0423
26/08/2022;5,0897
25/08/2022;5,1167
24/08/2022;5,1044
23/08/2022;5,1024
22/08/2022;5,1703
19/08/2022;5,1955
18/08/2022;5,1767
17/08/2022;5,1779
16/08/2022;5,1334
15/08/2022;5,0919
12/08/2022;5,1017
11/08/2022;5,1121
10/08/2022;5,0491
09/08/2022;5,1218
08/08/2022;5,1241
05/08/2022;5,2159
04/08/2022;5,2403
03/08/2022;5,2840
02/08/2022;5,2323
01/08/2022;5,1600
29/07/2022;5,1878
28/07/2022;5,2143
27/07/2022;5,3068
26/07/2022;5,3602
25/07/2022;5,4138
22/07/2022;5,4516
21/07/2022;5,4744
20/07/2022;5,4282
19/07/2022;5,3898
18/07/2022;5,3669
15/07/2022;5,4008
14/07/2022;5,4562
13/07/2022;5,3987
12/07/2022;5,4114
11/07/2022;5,3471
08/07/2022;5,3080
07/07/2022;5,3634
06/07/2022;5,4315
05/07/2022;5,3893
04/07/2022;5,3032
01/07/2022;5,3136
30/06/2022;5,2374
29/06/2022;5,2262
28/06/2022;5,2173
27/06/2022;5,2208
24/06/2022;5,2328
23/06/2022;5,1827
22/06/2022;5,1503
21/06/2022;5,1456
20/06/2022;5,1635
17/06/2022;5,1307
15/06/2022;5,1113
14/06/2022;5,1197
13/06/2022;5,1027
10/06/2022;4,9830
09/06/2022;4,8945
08/06/2022;4,8705
07/06/2022;4,8903
06/06/2022;4,7833
03/06/2022;4,7950
02/06/2022;4,7873
01/06/2022;4,7759
31/05/2022;4,7283
30/05/2022;4,7210
27/05/2022;4,7428
26/05/2022;4,7961
25/05/2022;4,8353
24/05/2022;4,8100
23/05/2022;4,7967
20/05/2022;4,8771
19/05/2022;4,9192
18/05/2022;4,9586
17/05/2022;4,9670
16/05/2022;5,0660
13/05/2022;5,1069
12/05/2022;5,1476
11/05/2022;5,1238
10/05/2022;5,1384
09/05/2022;5,1334
06/05/2022;5,0744
05/05/2022;5,0045
04/05/2022;5,0087
03/05/2022;5,0161
02/05/2022;5,0260
29/04/2022;4,9185
28/04/2022;5,0104
27/04/2022;5,0161
26/04/2022;4,9660
25/04/2022;4,8812
22/04/2022;4,7320
20/04/2022;4,6391
19/04/2022;4,6658
18/04/2022;4,6740
14/04/2022;4,7152
13/04/2022;4,6805
12/04/2022;4,6477
11/04/2022;4,7019
08/04/2022;4,7507
07/04/2022;4,7416
06/04/2022;4,6961
05/04/2022;4,6394
04/04/2022;4,6169
01/04/2022;4,6978
31/03/2022;4,7372
30/03/2022;4,7491
29/03/2022;4,7480
28/03/2022;4,7899
25/03/2022;4,7776
24/03/2022;4,8061
23/03/2022;4,8698
22/03/2022;4,9202
21/03/2022;4,9660
18/03/2022;5,0405
17/03/2022;5,0758
16/03/2022;5,1281
15/03/2022;5,1308
14/03/2022;5,0641
11/03/2022;5,0249
10/03/2022;5,0507
09/03/2022;5,0088
08/03/2022;5,0897
07/03/2022;5,0573
04/03/2022;5,0752
03/03/2022;5,0473
02/03/2022;5,1341
25/02/2022;5,1388
24/02/2022;5,1168
23/02/2022;5,0137
22/02/2022;5,0605
21/02/2022;5,0991
18/02/2022;5,1333
17/02/2022;5,1559
16/02/2022;5,1624
15/02/2022;5,1875
14/02/2022;5,2100
11/02/2022;5,1981
10/02/2022;5,2095
09/02/2022;5,2729
01/02/2022;5,2804
31/01/2022;5,3568
28/01/2022;5,3948
27/01/2022;5,3806
26/01/2022;5,4318
25/01/2022;5,4965
24/01/2022;5,4904
21/01/2022;5,4395
20/01/2022;5,4160
19/01/2022;5,4972
18/01/2022;5,5207
17/01/2022;5,5052
14/01/2022;5,5343
13/01/2022;5,5240
12/01/2022;5,5605
11/01/2022;5,6345
10/01/2022;5,6730
07/01/2022;5,6747
06/01/2022;5,7036
05/01/2022;5,6622
04/01/2022;5,6770
03/01/2022;5,6303
31/12/2021;5,5799
30/12/2021;5,5799
29/12/2021;5,6613
28/12/2021;5,6432
27/12/2021;5,6644
24/12/2021;5,6541
23/12/2021;5,6904
22/12/2021;5,7195
21/12/2021;5,7367
20/12/2021;5,7049
17/12/2021;5,6953
16/12/2021;5,6957
15/12/2021;5,7121
14/12/2021;5,6455
13/12/2021;5,6351
10/12/2021;5,5925
09/12/2021;5,5558
08/12/2021;5,5773
07/12/2021;5,6405
06/12/2021;5,6871
03/12/2021;5,6426
02/12/2021;5,6339
01/12/2021;5,6162
30/11/2021;5,6193
29/11/2021;5,6112
26/11/2021;5,5859
25/11/2021;5,5734
24/11/2021;5,6021
23/11/2021;5,6450
22/11/2021;5,5835
19/11/2021;5,5578
18/11/2021;5,5464
17/11/2021;5,4987
16/11/2021;5,4766
12/11/2021;5,4193
11/11/2021;5,4165
10/11/2021;5,4584
09/11/2021;5,4951
08/11/2021;5,5621
05/11/2021;5,5449
04/11/2021;5,5936
03/11/2021;5,6666
01/11/2021;5,6688
29/10/2021;5,6424
28/10/2021;5,6118
27/10/2021;5,5661
26/10/2021;5,5794
25/10/2021;5,5967
22/10/2021;5,7111
21/10/2021;5,6417
20/10/2021;5,5565
19/10/2021;5,5515
18/10/2021;5,5187
15/10/2021;5,4504
14/10/2021;5,4982
13/10/2021;5,5464
11/10/2021;5,5155
08/10/2021;5,5078
07/10/2021;5,5134
06/10/2021;5,5091
05/10/2021;5,4605
04/10/2021;5,4198
01/10/2021;5,3905
30/09/2021;5,4388
29/09/2021;5,4167
28/09/2021;5,4200
27/09/2021;5,3472
24/09/2021;5,3429
23/09/2021;5,2885
22/09/2021;5,2777
21/09/2021;5,3038
20/09/2021;5,3326
17/09/2021;5,3097
16/09/2021;5,2588
15/09/2021;5,2570
14/09/2021;5,2254
13/09/2021;5,2184
10/09/2021;5,2152
09/09/2021;5,2819
08/09/2021;5,2518
06/09/2021;5,1767
03/09/2021;5,1679
02/09/2021;5,1729
01/09/2021;5,1570
31/08/2021;5,1427
30/08/2021;5,1946
27/08/2021;5,2194
26/08/2021;5,2423
25/08/2021;5,2459
24/08/2021;5,3011
23/08/2021;5,3680
20/08/2021;5,4268
19/08/2021;5,4174
18/08/2021;5,3019
17/08/2021;5,2579
16/08/2021;5,2489
13/08/2021;5,2468
12/08/2021;5,2345
11/08/2021;5,2007
10/08/2021;5,2211
09/08/2021;5,2768
06/08/2021;5,2404
05/08/2021;5,1459
04/08/2021;5,2085
03/08/2021;5,2458
02/08/2021;5,1373
30/07/2021;5,1210
29/07/2021;5,0676
28/07/2021;5,1521
27/07/2021;5,1663
26/07/2021;5,1857
23/07/2021;5,1695
22/07/2021;5,1972
21/07/2021;5,2510
20/07/2021;5,2459
19/07/2021;5,1972
16/07/2021;5,0935
15/07/2021;5,0994
14/07/2021;5,0874
13/07/2021;5,1764
12/07/2021;5,2233
09/07/2021;5,2370
08/07/2021;5,2581
07/07/2021;5,2322
06/07/2021;5,1639
05/07/2021;5,0743
02/07/2021;5,0287
01/07/2021;5,0049
30/06/2021;5,0016
28/06/2021;4,9414
25/06/2021;4,9200
24/06/2021;4,9271
23/06/2021;4,9513
18/06/2021;5,0314
17/06/2021;5,0359
16/06/2021;5,0207
15/06/2021;5,0874
14/06/2021;5,0707
11/06/2021;5,1190
10/06/2021;5,0635
09/06/2021;5,0533
08/06/2021;5,0489
07/06/2021;5,0498
04/06/2021;5,0666
02/06/2021;5,1147
01/06/2021;5,1636
31/05/2021;5,2322
28/05/2021;5,2281
27/05/2021;5,2840
26/05/2021;5,3164
25/05/2021;5,3143
24/05/2021;5,3198
21/05/2021;5,3027
20/05/2021;5,2905
19/05/2021;5,2822
18/05/2021;5,2588
17/05/2021;5,2749
14/05/2021;5,2695
13/05/2021;5,2809
12/05/2021;5,2347
11/05/2021;5,2397
10/05/2021;5,2221
07/05/2021;5,2211
06/05/2021;5,2891
05/05/2021;5,3866
04/05/2021;5,4499
03/05/2021;5,4081
30/04/2021;5,4030
29/04/2021;5,3656
28/04/2021;5,3999
27/04/2021;5,4418
26/04/2021;5,4560
23/04/2021;5,4781
22/04/2021;5,4964
20/04/2021;5,5260
19/04/2021;5,5744
16/04/2021;5,6322
15/04/2021;5,6228
14/04/2021;5,6930
13/04/2021;5,7058
12/04/2021;5,6576
09/04/2021;5,6439
08/04/2021;5,5811
07/04/2021;5,5858
06/04/2021;5,6257
05/04/2021;5,6573
01/04/2021;5,6843
31/03/2021;5,6967
30/03/2021;5,7636
29/03/2021;5,7919
26/03/2021;5,7036
25/03/2021;5,6579
24/03/2021;5,5324
23/03/2021;5,4945
22/03/2021;5,5263
19/03/2021;5,5076
18/03/2021;5,5468
17/03/2021;5,6573
16/03/2021;5,5845
15/03/2021;5,6290
12/03/2021;5,5634
11/03/2021;5,5884
10/03/2021;5,7443
09/03/2021;5,8391
08/03/2021;5,7337
05/03/2021;5,6864
04/03/2021;5,6002
03/03/2021;5,7336
02/03/2021;5,6838
01/03/2021;5,5826
26/02/2021;5,5296
25/02/2021;5,4594
24/02/2021;5,4176
23/02/2021;5,4484
22/02/2021;5,5038
19/02/2021;5,3918
18/02/2021;5,4232
17/02/2021;5,4132
12/02/2021;5,3809
11/02/2021;5,3620
10/02/2021;5,4018
09/02/2021;5,4210
08/02/2021;5,3664
05/02/2021;5,3878
04/02/2021;5,3904
03/02/2021;5,3417
02/02/2021;5,3869
01/02/2021;5,4602
29/01/2021;5,4753
28/01/2021;5,4276
27/01/2021;5,3818
26/01/2021;5,3859
25/01/2021;5,5074
22/01/2021;5,4295
21/01/2021;5,3160
20/01/2021;5,3027
19/01/2021;5,2939
18/01/2021;5,2782
15/01/2021;5,2708
14/01/2021;5,2611
13/01/2021;5,3064
12/01/2021;5,4631
11/01/2021;5,4960
08/01/2021;5,3677
07/01/2021;5,3427
06/01/2021;5,3176
05/01/2021;5,3263
04/01/2021;5,1620
31/12/2020;5,1961
30/12/2020;5,1961
29/12/2020;5,1936
28/12/2020;5,2384
24/12/2020;5,1785
23/12/2020;5,1734
22/12/2020;5,1467
21/12/2020;5,1566
18/12/2020;5,0980
17/12/2020;5,0606
16/12/2020;5,1051
15/12/2020;5,0962
14/12/2020;5,0572
11/12/2020;5,0685
10/12/2020;5,0846
09/12/2020;5,1103
08/12/2020;5,0914
07/12/2020;5,1012
04/12/2020;5,1700
03/12/2020;5,1619
02/12/2020;5,2261
01/12/2020;5,2783
30/11/2020;5,3311
27/11/2020;5,3488
26/11/2020;5,3195
25/11/2020;5,3502
24/11/2020;5,4031
23/11/2020;5,3822
20/11/2020;5,3499
19/11/2020;5,3324
18/11/2020;5,2926
17/11/2020;5,3962
16/11/2020;5,4192
13/11/2020;5,4848
12/11/2020;5,4088
11/11/2020;5,4014
10/11/2020;5,3690
09/11/2020;5,2815
06/11/2020;5,5307
05/11/2020;5,5618
04/11/2020;5,6926
03/11/2020;5,6889
30/10/2020;5,7712
29/10/2020;5,7797
28/10/2020;5,7319
27/10/2020;5,6484
26/10/2020;5,6322
23/10/2020;5,6114
22/10/2020;5,5814
21/10/2020;5,6000
20/10/2020;5,5824
19/10/2020;5,6017
16/10/2020;5,6220
15/10/2020;5,6166
14/10/2020;5,5669
13/10/2020;5,5854
09/10/2020;5,5387
08/10/2020;5,6194
07/10/2020;5,6012
06/10/2020;5,5199
05/10/2020;5,6293
02/10/2020;5,6458
01/10/2020;5,6435
30/09/2020;5,6401
29/09/2020;5,6521
28/09/2020;5,5852
25/09/2020;5,5661
24/09/2020;5,5708
23/09/2020;5,5305
22/09/2020;5,4323
21/09/2020;5,4434
18/09/2020;5,2883
17/09/2020;5,2587
16/09/2020;5,2526
15/09/2020;5,2722
14/09/2020;5,2978
11/09/2020;5,2848
10/09/2020;5,2930
09/09/2020;5,3018
08/09/2020;5,3692
04/09/2020;5,2842
03/09/2020;5,3073
02/09/2020;5,3735
01/09/2020;5,3726
31/08/2020;5,4707
28/08/2020;5,4673
27/08/2020;5,5950
26/08/2020;5,5674
25/08/2020;5,5991
24/08/2020;5,5948
21/08/2020;5,6058
20/08/2020;5,6504
19/08/2020;5,4900
18/08/2020;5,4653
17/08/2020;5,4491
14/08/2020;5,3846
13/08/2020;5,3795
12/08/2020;5,4545
11/08/2020;5,4279
10/08/2020;5,3927
07/08/2020;5,4221
06/08/2020;5,3425
05/08/2020;5,2754
04/08/2020;5,3323
03/08/2020;5,3069
31/07/2020;5,2027
30/07/2020;5,1831
29/07/2020;5,1389
28/07/2020;5,1771
27/07/2020;5,1883
24/07/2020;5,2140
23/07/2020;5,1641
22/07/2020;5,1105
21/07/2020;5,2277
20/07/2020;5,3629
17/07/2020;5,3504
16/07/2020;5,3554
15/07/2020;5,3485
14/07/2020;5,4282
13/07/2020;5,3480
10/07/2020;5,3434
09/07/2020;5,2972
08/07/2020;5,3476
07/07/2020;5,3312
06/07/2020;5,3079
03/07/2020;5,3368
02/07/2020;5,3022
01/07/2020;5,3646
30/06/2020;5,4754
29/06/2020;5,4410
26/06/2020;5,4623
25/06/2020;5,3281
24/06/2020;5,2429
23/06/2020;5,1699
22/06/2020;5,2220
19/06/2020;5,3460
18/06/2020;5,3462
17/06/2020;5,2492
16/06/2020;5,1279
15/06/2020;5,1877
12/06/2020;5,0367
10/06/2020;4,8888
09/06/2020;4,9051
08/06/2020;4,9325
05/06/2020;4,9769
04/06/2020;5,1035
03/06/2020;5,0510
02/06/2020;5,2595
01/06/2020;5,3633
29/05/2020;5,4257
28/05/2020;5,3399
27/05/2020;5,2986
26/05/2020;5,3701
25/05/2020;5,4766
22/05/2020;5,5802
21/05/2020;5,6013
20/05/2020;5,6962
19/05/2020;5,7210
18/05/2020;5,7369
15/05/2020;5,8223
14/05/2020;5,9366
13/05/2020;5,9016
12/05/2020;5,7717
11/05/2020;5,7948
08/05/2020;5,7647
07/05/2020;5,8359
06/05/2020;5,6670
05/05/2020;5,5348
04/05/2020;5,5811
30/04/2020;5,4264
29/04/2020;5,4285
28/04/2020;5,5677
27/04/2020;5,6352
24/04/2020;5,6504
23/04/2020;5,4461
22/04/2020;5,3841
20/04/2020;5,2831
17/04/2020;5,2567
16/04/2020;5,2371
15/04/2020;5,2573
14/04/2020;5,1852
13/04/2020;5,1818
09/04/2020;5,0773
08/04/2020;5,2117
07/04/2020;5,2211
06/04/2020;5,2465
03/04/2020;5,2991
02/04/2020;5,2645
01/04/2020;5,2399
31/03/2020;5,1981
30/03/2020;5,1588
27/03/2020;5,1103
26/03/2020;5,0004
25/03/2020;5,0700
24/03/2020;5,0707
23/03/2020;5,0798
20/03/2020;5,0241
19/03/2020;5,1437
18/03/2020;5,1101
17/03/2020;5,0489
16/03/2020;4,9464
13/03/2020;4,7355
12/03/2020;4,8825
11/03/2020;4,6732
10/03/2020;4,6687
09/03/2020;4,7373
06/03/2020;4,6453
05/03/2020;4,6201
04/03/2020;4,5252
03/03/2020;4,4877
02/03/2020;4,4940
28/02/2020;4,4981
27/02/2020;4,4758
26/02/2020;4,4353
21/02/2020;4,3918
20/02/2020;4,3867
19/02/2020;4,3722
18/02/2020;4,3465
17/02/2020;4,3151
14/02/2020;4,3157
13/02/2020;4,3383
12/02/2020;4,3360
11/02/2020;4,3142
10/02/2020;4,3189
07/02/2020;4,3070
06/02/2020;4,2471
05/02/2020;4,2443
04/02/2020;4,2375
03/02/2020;4,2469
31/01/2020;4,2689
30/01/2020;4,2517
29/01/2020;4,2007
28/01/2020;4,2058
27/01/2020;4,2190
24/01/2020;4,1763
23/01/2020;4,1656
22/01/2020;4,1883
21/01/2020;4,2008
20/01/2020;4,1823
17/01/2020;4,1831
16/01/2020;4,1720
15/01/2020;4,1616
14/01/2020;4,1437
13/01/2020;4,1303
10/01/2020;4,0739
09/01/2020;4,0738
08/01/2020;4,0666
07/01/2020;4,0835
06/01/2020;4,0548
03/01/2020;4,0516
02/01/2020;4,0207
31/12/2019;4,0301
30/12/2019;4,0301
27/12/2019;4,0539
26/12/2019;4,0595
24/12/2019;4,0793
23/12/2019;4,0751
20/12/2019;4,0771
19/12/2019;4,0627
18/12/2019;4,0542
17/12/2019;4,0681
16/12/2019;4,0795
13/12/2019;4,0943
12/12/2019;4,1086
11/12/2019;4,1147
10/12/2019;4,1421
09/12/2019;4,1497
06/12/2019;4,1777
05/12/2019;4,2130
04/12/2019;4,1920
03/12/2019;4,2002
02/12/2019;4,2255
29/11/2019;4,2234
28/11/2019;4,2474
27/11/2019;4,2596
26/11/2019;4,2553
25/11/2019;4,2083
22/11/2019;4,1826
21/11/2019;4,2006
20/11/2019;4,2027
19/11/2019;4,2078
18/11/2019;4,1821
14/11/2019;4,1825
13/11/2019;4,1761
12/11/2019;4,1750
11/11/2019;4,1553
08/11/2019;4,1359
07/11/2019;4,0921
06/11/2019;4,0345
05/11/2019;4,0037
04/11/2019;3,9916
01/11/2019;3,9780
31/10/2019;4,0035
30/10/2019;4,0180
29/10/2019;3,9940
28/10/2019;3,9786
25/10/2019;4,0127
24/10/2019;4,0083
23/10/2019;4,0715
22/10/2019;4,0852
21/10/2019;4,1313
18/10/2019;4,1370
17/10/2019;4,1452
16/10/2019;4,1708
15/10/2019;4,1482
14/10/2019;4,1257
11/10/2019;4,1054
10/10/2019;4,1139
09/10/2019;4,0948
08/10/2019;4,0862
07/10/2019;4,0682
04/10/2019;4,0604
03/10/2019;4,1006
02/10/2019;4,1540
01/10/2019;4,1734
30/09/2019;4,1638
27/09/2019;4,1581
26/09/2019;4,1463
25/09/2019;4,1821
24/09/2019;4,1715
23/09/2019;4,1728
20/09/2019;4,1681
19/09/2019;4,1387
18/09/2019;4,0966
17/09/2019;4,0992
16/09/2019;4,0866
13/09/2019;4,0610
12/09/2019;4,0488
11/09/2019;4,0625
10/09/2019;4,1102
09/09/2019;4,0760
06/09/2019;4,0644
05/09/2019;4,0853
04/09/2019;4,1243
03/09/2019;4,1651
02/09/2019;4,1575
30/08/2019;4,1379
29/08/2019;4,1674
28/08/2019;4,1553
27/08/2019;4,1551
26/08/2019;4,1361
23/08/2019;4,0845
22/08/2019;4,0438
21/08/2019;4,0248
20/08/2019;4,0419
19/08/2019;4,0268
16/08/2019;3,9927
15/08/2019;4,0182
14/08/2019;4,0068
13/08/2019;3,9730
12/08/2019;3,9960
09/08/2019;3,9356
08/08/2019;3,9403
07/08/2019;3,9844
06/08/2019;3,9637
05/08/2019;3,9398
02/08/2019;3,8733
01/08/2019;3,8290
31/07/2019;3,7643
30/07/2019;3,7894
29/07/2019;3,7903
26/07/2019;3,7735
25/07/2019;3,7843
24/07/2019;3,7590
23/07/2019;3,7615
22/07/2019;3,7394
19/07/2019;3,7402
18/07/2019;3,7483
17/07/2019;3,7612
16/07/2019;3,7618
15/07/2019;3,7457
12/07/2019;3,7446
11/07/2019;3,7527
10/07/2019;3,7691
09/07/2019;3,7846
08/07/2019;3,8059
05/07/2019;3,8198
04/07/2019;3,7934
03/07/2019;3,8469
02/07/2019;3,8558
01/07/2019;3,8187
28/06/2019;3,8316
27/06/2019;3,8636
26/06/2019;3,8435
25/06/2019;3,8297
24/06/2019;3,8228
21/06/2019;3,8249
19/06/2019;3,8717
18/06/2019;3,8602
17/06/2019;3,8889
14/06/2019;3,8807
13/06/2019;3,8423
12/06/2019;3,8431
11/06/2019;3,8658
10/06/2019;3,8784
07/06/2019;3,8565
06/06/2019;3,8720
05/06/2019;3,8605
04/06/2019;3,8704
03/06/2019;3,8997
31/05/2019;3,9401
30/05/2019;3,9714
29/05/2019;3,9959
28/05/2019;4,0269
27/05/2019;4,0204
24/05/2019;4,0316
23/05/2019;4,0507
22/05/2019;4,0222
21/05/2019;4,0804
20/05/2019;4,1050
17/05/2019;4,0838
16/05/2019;4,0132
15/05/2019;4,0025
14/05/2019;3,9782
13/05/2019;3,9884
10/05/2019;3,9572
09/05/2019;3,9667
08/05/2019;3,9338
07/05/2019;3,9874
06/05/2019;3,9618
03/05/2019;3,9382
02/05/2019;3,9644
30/04/2019;3,9447
29/04/2019;3,9358
26/04/2019;3,9347
25/04/2019;3,9719
24/04/2019;3,9624
23/04/2019;3,9430
22/04/2019;3,9224
18/04/2019;3,9364
17/04/2019;3,9219
16/04/2019;3,8907
15/04/2019;3,8724
12/04/2019;3,8679
11/04/2019;3,8393
10/04/2019;3,8339
09/04/2019;3,8557
08/04/2019;3,8652
05/04/2019;3,8616
04/04/2019;3,8707
03/04/2019;3,8430
02/04/2019;3,8655
01/04/2019;3,8676
29/03/2019;3,8961
28/03/2019;3,9676
27/03/2019;3,9383
26/03/2019;3,8640
25/03/2019;3,8764
22/03/2019;3,8809
21/03/2019;3,7961
20/03/2019;3,7891
19/03/2019;3,7756
18/03/2019;3,8105
15/03/2019;3,8338
14/03/2019;3,8321
13/03/2019;3,8259
12/03/2019;3,8123
11/03/2019;3,8455
08/03/2019;3,8672
07/03/2019;3,8481
06/03/2019;3,8297
01/03/2019;3,7826
28/02/2019;3,7379
27/02/2019;3,7345
26/02/2019;3,7589
25/02/2019;3,7279
22/02/2019;3,7424
21/02/2019;3,7589
20/02/2019;3,7094
19/02/2019;3,7200
18/02/2019;3,7310
15/02/2019;3,7149
14/02/2019;3,7750
13/02/2019;3,7271
12/02/2019;3,7290
11/02/2019;3,7385
08/02/2019;3,7178
07/02/2019;3,7187
06/02/2019;3,7013
05/02/2019;3,6735
04/02/2019;3,6750
01/02/2019;3,6688
31/01/2019;3,6513
30/01/2019;3,7145
29/01/2019;3,7364
28/01/2019;3,7670
25/01/2019;3,7613
24/01/2019;3,7809
23/01/2019;3,7988
22/01/2019;3,7609
21/01/2019;3,7699
18/01/2019;3,7480
17/01/2019;3,7585
16/01/2019;3,7191
15/01/2019;3,7043
14/01/2019;3,7255
11/01/2019;3,7135
10/01/2019;3,6863
09/01/2019;3,6925
08/01/2019;3,7202
07/01/2019;3,7056
04/01/2019;3,7621
03/01/2019;3,7677
02/01/2019;3,8589
31/12/2018;3,8742
28/12/2018;3,8742
27/12/2018;3,9324
26/12/2018;3,9252
24/12/2018;3,8839
21/12/2018;3,8665
20/12/2018;3,8437
19/12/2018;3,8901
18/12/2018;3,8991
17/12/2018;3,9115
14/12/2018;3,9084
13/12/2018;3,8784
12/12/2018;3,8623
11/12/2018;3,9007
10/12/2018;3,9104
07/12/2018;3,8958
06/12/2018;3,9172
05/12/2018;3,8555
04/12/2018;3,8307
03/12/2018;3,8279
30/11/2018;3,8627
29/11/2018;3,8562
28/11/2018;3,8625
27/11/2018;3,8919
26/11/2018;3,8649
23/11/2018;3,8075
22/11/2018;3,8097
21/11/2018;3,7866
20/11/2018;3,7574
19/11/2018;3,7547
16/11/2018;3,7519
14/11/2018;3,7918
13/11/2018;3,7786
12/11/2018;3,7472
09/11/2018;3,7500
08/11/2018;3,7385
07/11/2018;3,7586
06/11/2018;3,7486
05/11/2018;3,7042
01/11/2018;3,6968
31/10/2018;3,7171
30/10/2018;3,7013
29/10/2018;3,6362
26/10/2018;3,6746
25/10/2018;3,7008
24/10/2018;3,7054
23/10/2018;3,7074
22/10/2018;3,6897
19/10/2018;3,7073
18/10/2018;3,6957
17/10/2018;3,7002
16/10/2018;3,7073
15/10/2018;3,7326
11/10/2018;3,7454
10/10/2018;3,7504
09/10/2018;3,7385
08/10/2018;3,7582
05/10/2018;3,8693
04/10/2018;3,9041
03/10/2018;3,8536
02/10/2018;3,9499
01/10/2018;4,0267
28/09/2018;4,0033
27/09/2018;4,0086
26/09/2018;4,0564
25/09/2018;4,1280
24/09/2018;4,0588
21/09/2018;4,0722
20/09/2018;4,0991
19/09/2018;4,1345
18/09/2018;4,1363
17/09/2018;4,1689
14/09/2018;4,1873
13/09/2018;4,1631
12/09/2018;4,1253
11/09/2018;4,1635
10/09/2018;4,1001
06/09/2018;4,1454
05/09/2018;4,1603
04/09/2018;4,1646
03/09/2018;4,1273
31/08/2018;4,1347
30/08/2018;4,1806
29/08/2018;4,1347
28/08/2018;4,1186
27/08/2018;4,0681
24/08/2018;4,0848
23/08/2018;4,0721
22/08/2018;4,0734
21/08/2018;3,9867
20/08/2018;3,9424
17/08/2018;3,9383
16/08/2018;3,8804
15/08/2018;3,9128
14/08/2018;3,8806
13/08/2018;3,8982
10/08/2018;3,8466
09/08/2018;3,8024
08/08/2018;3,7513
07/08/2018;3,7112
06/08/2018;3,7208
03/08/2018;3,7195
02/08/2018;3,7639
01/08/2018;3,7485
31/07/2018;3,7543
30/07/2018;3,7149
27/07/2018;3,7158
26/07/2018;3,7237
25/07/2018;3,7114
24/07/2018;3,7453
23/07/2018;3,7909
20/07/2018;3,7787
19/07/2018;3,8841
18/07/2018;3,8468
17/07/2018;3,8665
16/07/2018;3,8573
13/07/2018;3,8739
12/07/2018;3,8558
11/07/2018;3,8411
10/07/2018;3,8446
09/07/2018;3,8680
06/07/2018;3,9258
05/07/2018;3,9186
04/07/2018;3,9052
03/07/2018;3,8914
02/07/2018;3,9049
29/06/2018;3,8552
28/06/2018;3,8515
27/06/2018;3,8352
26/06/2018;3,7715
25/06/2018;3,7754
22/06/2018;3,7657
21/06/2018;3,7888
20/06/2018;3,7329
19/06/2018;3,7560
18/06/2018;3,7537
15/06/2018;3,7732
14/06/2018;3,7051
13/06/2018;3,7048
12/06/2018;3,7038
11/06/2018;3,6907
08/06/2018;3,7853
07/06/2018;3,8994
06/06/2018;3,8187
05/06/2018;3,7746
04/06/2018;3,7418
01/06/2018;3,7407
30/05/2018;3,7364
29/05/2018;3,7283
28/05/2018;3,7086
25/05/2018;3,6581
24/05/2018;3,6430
23/05/2018;3,6501
22/05/2018;3,6496
21/05/2018;3,7066
18/05/2018;3,7497
17/05/2018;3,6868
16/05/2018;3,6797
15/05/2018;3,6747
14/05/2018;3,6091
11/05/2018;3,5710
10/05/2018;3,5561
09/05/2018;3,5937
08/05/2018;3,5782
07/05/2018;3,5452
04/05/2018;3,5302
03/05/2018;3,5478
02/05/2018;3,5418
30/04/2018;3,4805
27/04/2018;3,4670
26/04/2018;3,4971
25/04/2018;3,5034
24/04/2018;3,4661
23/04/2018;3,4415
20/04/2018;3,4096
19/04/2018;3,3971
18/04/2018;3,3838
17/04/2018;3,4035
16/04/2018;3,4257
13/04/2018;3,4099
12/04/2018;3,3852
11/04/2018;3,4046
10/04/2018;3,4189
09/04/2018;3,3897
06/04/2018;3,3660
05/04/2018;3,3190
04/04/2018;3,3532
03/04/2018;3,3133
02/04/2018;3,3098
29/03/2018;3,3232
28/03/2018;3,3374
27/03/2018;3,3250
26/03/2018;3,3028
23/03/2018;3,3035
22/03/2018;3,3027
21/03/2018;3,2915
20/03/2018;3,2975
19/03/2018;3,2905
16/03/2018;3,2899
15/03/2018;3,2853
14/03/2018;3,2578
13/03/2018;3,2486
12/03/2018;3,2600
09/03/2018;3,2490
08/03/2018;3,2512
07/03/2018;3,2312
06/03/2018;3,2240
05/03/2018;3,2576
02/03/2018;3,2608
01/03/2018;3,2614
28/02/2018;3,2443
27/02/2018;3,2377
26/02/2018;3,2345
23/02/2018;3,2411
22/02/2018;3,2592
21/02/2018;3,2549
20/02/2018;3,2501
19/02/2018;3,2341
16/02/2018;3,2375
15/02/2018;3,2202
14/02/2018;3,2531
09/02/2018;3,2815
08/02/2018;3,2686
07/02/2018;3,2461
06/02/2018;3,2607
05/02/2018;3,2349
02/02/2018;3,2054
01/02/2018;3,1724
31/01/2018;3,1618
30/01/2018;3,1655
29/01/2018;3,1648
26/01/2018;3,1444
25/01/2018;3,1380
24/01/2018;3,1964
23/01/2018;3,2243
22/01/2018;3,1928
19/01/2018;3,2081
18/01/2018;3,2123
17/01/2018;3,2318
16/01/2018;3,2213
15/01/2018;3,1957
12/01/2018;3,2192
11/01/2018;3,2295
10/01/2018;3,2461
09/01/2018;3,2391
08/01/2018;3,2351
05/01/2018;3,2403
04/01/2018;3,2312
03/01/2018;3,2529
02/01/2018;3,2691
29/12/2017;3,3074
28/12/2017;3,3074
27/12/2017;3,3024
26/12/2017;3,3194
22/12/2017;3,3203
21/12/2017;3,3039
20/12/2017;3,2903
19/12/2017;3,2877
18/12/2017;3,2875
15/12/2017;3,3176
14/12/2017;3,3326
13/12/2017;3,3030
12/12/2017;3,3143
11/12/2017;3,2839
08/12/2017;3,2805
07/12/2017;3,2886
06/12/2017;3,2348
05/12/2017;3,2316
04/12/2017;3,2500
01/12/2017;3,2630
30/11/2017;3,2610
29/11/2017;3,2130
28/11/2017;3,2226
27/11/2017;3,2212
24/11/2017;3,2294
23/11/2017;3,2365
22/11/2017;3,2555
21/11/2017;3,2585
20/11/2017;3,2608
17/11/2017;3,2782
16/11/2017;3,2802
14/11/2017;3,2828
13/11/2017;3,2867
10/11/2017;3,2655
09/11/2017;3,2509
08/11/2017;3,2503
07/11/2017;3,2727
06/11/2017;3,2845
03/11/2017;3,2914
01/11/2017;3,2730
31/10/2017;3,2763
30/10/2017;3,2541
27/10/2017;3,2795
26/10/2017;3,2438
25/10/2017;3,2381
24/10/2017;3,2464
23/10/2017;3,1997
20/10/2017;3,1827
19/10/2017;3,1727
18/10/2017;3,1667
17/10/2017;3,1763
16/10/2017;3,1601
13/10/2017;3,1567
11/10/2017;3,1633
10/10/2017;3,1682
09/10/2017;3,1764
06/10/2017;3,1642
05/10/2017;3,1341
04/10/2017;3,1309
03/10/2017;3,1496
02/10/2017;3,1636
29/09/2017;3,1674
28/09/2017;3,1865
27/09/2017;3,1926
26/09/2017;3,1668
25/09/2017;3,1406
22/09/2017;3,1279
21/09/2017;3,1341
20/09/2017;3,1275
19/09/2017;3,1317
18/09/2017;3,1233
15/09/2017;3,1249
14/09/2017;3,1348
13/09/2017;3,1337
12/09/2017;3,1138
11/09/2017;3,0846
08/09/2017;3,0902
06/09/2017;3,1127
05/09/2017;3,1197
04/09/2017;3,1383
01/09/2017;3,1327
31/08/2017;3,1465
30/08/2017;3,1632
29/08/2017;3,1689
28/08/2017;3,1557
25/08/2017;3,1456
24/08/2017;3,1398
23/08/2017;3,1563
22/08/2017;3,1533
21/08/2017;3,1437
18/08/2017;3,1648
17/08/2017;3,1597
16/08/2017;3,1664
15/08/2017;3,1970
14/08/2017;3,1882
11/08/2017;3,1689
10/08/2017;3,1537
09/08/2017;3,1458
08/08/2017;3,1314
07/08/2017;3,1261
04/08/2017;3,1218
03/08/2017;3,1188
02/08/2017;3,1262
01/08/2017;3,1154
31/07/2017;3,1301
28/07/2017;3,1451
27/07/2017;3,1507
26/07/2017;3,1651
25/07/2017;3,1550
24/07/2017;3,1453
21/07/2017;3,1250
20/07/2017;3,1396
19/07/2017;3,1527
18/07/2017;3,1662
17/07/2017;3,1815
14/07/2017;3,1893
13/07/2017;3,2102
12/07/2017;3,2258
11/07/2017;3,2516
10/07/2017;3,2644
07/07/2017;3,2889
06/07/2017;3,3058
05/07/2017;3,3187
04/07/2017;3,3044
03/07/2017;3,3009
30/06/2017;3,3076
29/06/2017;3,2946
28/06/2017;3,3024
27/06/2017;3,3166
26/06/2017;3,3122
23/06/2017;3,3336
22/06/2017;3,3356
21/06/2017;3,3241
20/06/2017;3,3139
19/06/2017;3,2969
16/06/2017;3,2886
14/06/2017;3,2830
13/06/2017;3,3202
12/06/2017;3,2980
09/06/2017;3,2734
08/06/2017;3,2832
07/06/2017;3,2741
06/06/2017;3,2811
05/06/2017;3,2814
02/06/2017;3,2395
01/06/2017;3,2301
31/05/2017;3,2431
30/05/2017;3,2653
29/05/2017;3,2703
26/05/2017;3,2608
25/05/2017;3,2818
24/05/2017;3,2623
23/05/2017;3,2648
22/05/2017;3,2857
19/05/2017;3,2872
18/05/2017;3,3756
17/05/2017;3,1070
16/05/2017;3,0918
15/05/2017;3,1005
12/05/2017;3,1284
11/05/2017;3,1553
10/05/2017;3,1600
09/05/2017;3,1851
08/05/2017;3,1932
05/05/2017;3,1758
04/05/2017;3,1774
03/05/2017;3,1483
02/05/2017;3,1718
28/04/2017;3,1978
27/04/2017;3,1757
26/04/2017;3,1841
25/04/2017;3,1571
24/04/2017;3,1245
20/04/2017;3,1447
19/04/2017;3,1288
18/04/2017;3,0952
17/04/2017;3,1030
13/04/2017;3,1263
12/04/2017;3,1457
11/04/2017;3,1418
10/04/2017;3,1403
07/04/2017;3,1296
06/04/2017;3,1154
05/04/2017;3,0917
04/04/2017;3,1225
03/04/2017;3,1161
31/03/2017;3,1678
30/03/2017;3,1241
29/03/2017;3,1223
28/03/2017;3,1297
27/03/2017;3,1250
24/03/2017;3,1276
23/03/2017;3,1242
22/03/2017;3,0933
21/03/2017;3,0759
20/03/2017;3,0892
17/03/2017;3,1069
16/03/2017;3,1074
15/03/2017;3,1623
14/03/2017;3,1633
13/03/2017;3,1535
10/03/2017;3,1617
09/03/2017;3,1729
08/03/2017;3,1471
07/03/2017;3,1179
06/03/2017;3,1105
03/03/2017;3,1358
02/03/2017;3,1132
01/03/2017;3,0970
24/02/2017;3,0987
23/02/2017;3,0632
22/02/2017;3,0818
21/02/2017;3,0964
20/02/2017;3,0912
17/02/2017;3,0944
16/02/2017;3,0504
15/02/2017;3,0773
14/02/2017;3,0998
13/02/2017;3,1169
10/02/2017;3,1149
09/02/2017;3,1179
08/02/2017;3,1248
07/02/2017;3,1298
06/02/2017;3,1173
03/02/2017;3,1235
02/02/2017;3,1190
01/02/2017;3,1473
31/01/2017;3,1264
30/01/2017;3,1310
27/01/2017;3,1590
26/01/2017;3,1798
25/01/2017;3,1679
24/01/2017;3,1643
23/01/2017;3,1603
20/01/2017;3,1912
19/01/2017;3,2107
18/01/2017;3,2205
17/01/2017;3,2094
16/01/2017;3,2228
13/01/2017;3,2028
12/01/2017;3,1655
11/01/2017;3,2148
10/01/2017;3,1912
09/01/2017;3,2091
06/01/2017;3,2051
05/01/2017;3,2123
04/01/2017;3,2327
03/01/2017;3,2626
02/01/2017;3,2723
30/12/2016;3,2585
29/12/2016;3,2585
28/12/2016;3,2768
27/12/2016;3,2770
26/12/2016;3,2695
23/12/2016;3,2690
22/12/2016;3,3296
21/12/2016;3,3291
20/12/2016;3,3580
19/12/2016;3,3772
16/12/2016;3,3706
15/12/2016;3,3824
14/12/2016;3,3097
13/12/2016;3,3334
12/12/2016;3,3691
09/12/2016;3,3852
08/12/2016;3,4002
07/12/2016;3,3889
06/12/2016;3,4348
05/12/2016;3,4592
02/12/2016;3,4644
01/12/2016;3,4356
30/11/2016;3,3961
29/11/2016;3,4054
28/11/2016;3,3990
25/11/2016;3,4273
24/11/2016;3,3981
23/11/2016;3,3921
22/11/2016;3,3470
21/11/2016;3,3511
18/11/2016;3,3911
17/11/2016;3,4046
16/11/2016;3,4177
14/11/2016;3,4440
11/11/2016;3,4371
10/11/2016;3,3098
09/11/2016;3,2252
08/11/2016;3,2018
07/11/2016;3,2018
04/11/2016;3,2443
03/11/2016;3,2304
01/11/2016;3,2047
31/10/2016;3,1805
28/10/2016;3,1809
27/10/2016;3,1423
26/10/2016;3,1213
25/10/2016;3,1187
24/10/2016;3,1305
21/10/2016;3,1587
20/10/2016;3,1599
19/10/2016;3,1794
18/10/2016;3,1868
17/10/2016;3,1957
14/10/2016;3,1858
13/10/2016;3,2081
11/10/2016;3,2130
10/10/2016;3,2119
07/10/2016;3,2128
06/10/2016;3,2304
05/10/2016;3,2353
04/10/2016;3,2197
03/10/2016;3,2332
30/09/2016;3,2456
29/09/2016;3,2229
28/09/2016;3,2470
27/09/2016;3,2352
26/09/2016;3,2394
23/09/2016;3,2236
22/09/2016;3,2009
21/09/2016;3,2402
20/09/2016;3,2534
19/09/2016;3,2630
16/09/2016;3,2998
15/09/2016;3,3320
14/09/2016;3,3256
13/09/2016;3,2966
12/09/2016;3,2848
09/09/2016;3,2632
08/09/2016;3,1928
06/09/2016;3,2446
05/09/2016;3,2715
02/09/2016;3,2425
01/09/2016;3,2466
31/08/2016;3,2397
30/08/2016;3,2519
29/08/2016;3,2607
26/08/2016;3,2147
25/08/2016;3,2313
24/08/2016;3,2366
23/08/2016;3,2047
22/08/2016;3,2157
19/08/2016;3,2261
18/08/2016;3,2209
17/08/2016;3,2242
16/08/2016;3,1743
15/08/2016;3,1666
12/08/2016;3,1596
11/08/2016;3,1358
10/08/2016;3,1296
09/08/2016;3,1497
08/08/2016;3,1765
05/08/2016;3,1853
04/08/2016;3,2177
03/08/2016;3,2727
02/08/2016;3,2484
01/08/2016;3,2656
29/07/2016;3,2384
26/07/2016;3,2784
25/07/2016;3,2813
22/07/2016;3,2848
21/07/2016;3,2579
20/07/2016;3,2506
19/07/2016;3,2795
18/07/2016;3,2628
15/07/2016;3,2650
14/07/2016;3,2305
13/07/2016;3,2890
12/07/2016;3,2744
11/07/2016;3,3025
08/07/2016;3,2962
07/07/2016;3,3382
06/07/2016;3,3236
05/07/2016;3,2898
04/07/2016;3,2474
01/07/2016;3,2292
30/06/2016;3,2092
29/06/2016;3,2429
28/06/2016;3,3261
27/06/2016;3,3928
24/06/2016;3,3766
23/06/2016;3,3527
22/06/2016;3,3877
21/06/2016;3,3891
20/06/2016;3,3829
17/06/2016;3,4366
16/06/2016;3,4898
15/06/2016;3,4762
14/06/2016;3,4833
13/06/2016;3,4527
10/06/2016;3,4255
09/06/2016;3,3811
08/06/2016;3,3892
07/06/2016;3,4739
06/06/2016;3,5092
03/06/2016;3,5403
02/06/2016;3,5955
01/06/2016;3,6120
31/05/2016;3,5945
30/05/2016;3,5991
27/05/2016;3,6162
25/05/2016;3,5798
24/05/2016;3,5485
23/05/2016;3,5654
20/05/2016;3,5413
19/05/2016;3,5997
18/05/2016;3,5362
17/05/2016;3,5031
16/05/2016;3,5029
13/05/2016;3,5035
12/05/2016;3,4871
11/05/2016;3,4639
10/05/2016;3,4766
09/05/2016;3,5380
06/05/2016;3,5356
05/05/2016;3,5290
04/05/2016;3,5391
03/05/2016;3,5544
02/05/2016;3,4985
29/04/2016;3,4502
28/04/2016;3,4986
27/04/2016;3,5289
26/04/2016;3,5294
25/04/2016;3,5466
22/04/2016;3,5823
20/04/2016;3,5497
19/04/2016;3,5532
18/04/2016;3,5898
15/04/2016;3,5270
14/04/2016;3,5120
13/04/2016;3,5423
12/04/2016;3,5400
11/04/2016;3,5278
08/04/2016;3,6379
07/04/2016;3,6915
06/04/2016;3,6743
05/04/2016;3,6575
04/04/2016;3,5865
01/04/2016;3,5793
31/03/2016;3,5583
30/03/2016;3,6110
29/03/2016;3,6681
28/03/2016;3,6401
24/03/2016;3,6942
23/03/2016;3,6525
22/03/2016;3,6067
21/03/2016;3,6223
18/03/2016;3,6140
17/03/2016;3,6439
16/03/2016;3,8073
15/03/2016;3,7110
14/03/2016;3,6232
11/03/2016;3,6265
10/03/2016;3,6694
09/03/2016;3,7031
08/03/2016;3,7807
07/03/2016;3,7708
04/03/2016;3,7182
03/03/2016;3,8498
02/03/2016;3,9110
01/03/2016;3,9907
29/02/2016;3,9790
26/02/2016;3,9571
25/02/2016;3,9394
24/02/2016;3,9894
23/02/2016;3,9678
22/02/2016;3,9612
19/02/2016;4,0486
18/02/2016;4,0084
17/02/2016;4,0312
16/02/2016;4,0207
15/02/2016;3,9879
12/02/2016;3,9884
11/02/2016;3,9636
10/02/2016;3,9406
05/02/2016;3,8969
04/02/2016;3,8646
03/02/2016;3,9552
02/02/2016;3,9913
01/02/2016;3,9979
29/01/2016;4,0422
28/01/2016;4,0832
27/01/2016;4,0441
26/01/2016;4,0961
25/01/2016;4,0991
22/01/2016;4,1226
21/01/2016;4,1552
20/01/2016;4,0855
19/01/2016;4,0297
18/01/2016;4,0358
15/01/2016;4,0396
14/01/2016;4,0217
13/01/2016;3,9857
12/01/2016;4,0293
11/01/2016;4,0147
08/01/2016;4,0244
07/01/2016;4,0469
06/01/2016;4,0297
05/01/2016;4,0108
04/01/2016;4,0380
31/12/2015;3,9042
30/12/2015;3,9042
29/12/2015;3,8486
28/12/2015;3,9180
24/12/2015;3,9511
23/12/2015;3,9626
22/12/2015;3,9764
21/12/2015;3,9825
18/12/2015;3,9056
17/12/2015;3,8923
16/12/2015;3,9351
15/12/2015;3,8697
14/12/2015;3,9017
11/12/2015;3,8541
10/12/2015;3,7679
09/12/2015;3,7573
08/12/2015;3,7915
07/12/2015;3,7470
04/12/2015;3,7569
03/12/2015;3,7964
02/12/2015;3,8539
01/12/2015;3,8739
30/11/2015;3,8499
27/11/2015;3,7392
26/11/2015;3,7600
25/11/2015;3,7682
24/11/2015;3,7075
23/11/2015;3,7224
20/11/2015;3,7000
19/11/2015;3,7435
18/11/2015;3,7915
17/11/2015;3,8045
16/11/2015;3,8330
13/11/2015;3,8016
12/11/2015;3,7990
11/11/2015;3,7320
10/11/2015;3,7975
09/11/2015;3,7922
06/11/2015;3,8053
05/11/2015;3,7887
04/11/2015;3,7680
03/11/2015;3,8120
30/10/2015;3,8582
29/10/2015;3,9321
28/10/2015;3,8791
27/10/2015;3,9108
26/10/2015;3,8575
23/10/2015;3,8982
22/10/2015;3,9354
21/10/2015;3,9380
20/10/2015;3,8650
19/10/2015;3,9009
16/10/2015;3,8432
15/10/2015;3,8337
14/10/2015;3,8501
13/10/2015;3,8243
09/10/2015;3,7380
08/10/2015;3,8511
07/10/2015;3,8053
06/10/2015;3,8561
05/10/2015;3,9135
02/10/2015;4,0003
01/10/2015;3,9788
30/09/2015;3,9722
29/09/2015;4,1165
28/09/2015;4,0093
25/09/2015;3,9472
24/09/2015;4,1942
23/09/2015;4,1034
22/09/2015;4,0419
21/09/2015;3,9815
18/09/2015;3,9015
17/09/2015;3,8915
16/09/2015;3,8361
15/09/2015;3,8593
14/09/2015;3,8647
11/09/2015;3,8692
10/09/2015;3,8691
09/09/2015;3,7864
08/09/2015;3,8021
04/09/2015;3,7980
03/09/2015;3,7753
02/09/2015;3,7307
01/09/2015;3,6719
31/08/2015;3,6461
28/08/2015;3,5784
27/08/2015;3,5549
26/08/2015;3,6320
25/08/2015;3,5339
24/08/2015;3,5488
21/08/2015;3,4890
20/08/2015;3,4745
19/08/2015;3,4843
18/08/2015;3,4805
17/08/2015;3,4739
14/08/2015;3,4755
13/08/2015;3,5068
12/08/2015;3,4820
11/08/2015;3,4919
10/08/2015;3,4903
07/08/2015;3,5175
06/08/2015;3,5341
05/08/2015;3,4844
04/08/2015;3,4669
03/08/2015;3,4419
31/07/2015;3,3934
30/07/2015;3,3646
29/07/2015;3,3413
28/07/2015;3,3808
27/07/2015;3,3551
24/07/2015;3,3248
23/07/2015;3,2844
22/07/2015;3,2088
21/07/2015;3,1807
20/07/2015;3,2143
17/07/2015;3,1826
16/07/2015;3,1369
15/07/2015;3,1526
14/07/2015;3,1224
13/07/2015;3,1588
10/07/2015;3,1891
09/07/2015;3,2152
08/07/2015;3,2275
07/07/2015;3,1803
06/07/2015;3,1425
03/07/2015;3,1265
02/07/2015;3,1166
01/07/2015;3,1185
30/06/2015;3,1019
29/06/2015;3,1383
26/06/2015;3,1265
25/06/2015;3,1009
24/06/2015;3,0846
23/06/2015;3,1036
22/06/2015;3,0751
19/06/2015;3,0782
18/06/2015;3,0466
17/06/2015;3,0983
16/06/2015;3,1076
15/06/2015;3,1030
12/06/2015;3,1101
11/06/2015;3,1508
10/06/2015;3,0837
09/06/2015;3,0985
08/06/2015;3,1184
05/06/2015;3,1677
03/06/2015;3,1178
02/06/2015;3,1437
01/06/2015;3,1783
29/05/2015;3,1781
28/05/2015;3,1741
27/05/2015;3,1734
26/05/2015;3,1345
25/05/2015;3,1206
22/05/2015;3,0647
21/05/2015;3,0289
20/05/2015;3,0340
19/05/2015;3,0278
18/05/2015;3,0139
15/05/2015;2,9887
14/05/2015;3,0026
13/05/2015;3,0096
12/05/2015;3,0382
11/05/2015;3,0169
08/05/2015;2,9959
07/05/2015;3,0415
06/05/2015;3,0414
05/05/2015;3,0619
04/05/2015;3,0748
30/04/2015;2,9930
29/04/2015;2,9369
28/04/2015;2,8937
27/04/2015;2,9229
24/04/2015;2,9739
23/04/2015;3,0077
22/04/2015;3,0180
20/04/2015;3,0467
17/04/2015;3,0538
16/04/2015;3,0243
15/04/2015;3,0675
14/04/2015;3,0874
13/04/2015;3,1005
10/04/2015;3,0789
09/04/2015;3,0459
08/04/2015;3,0828
07/04/2015;3,1225
06/04/2015;3,0920
02/04/2015;3,1486
01/04/2015;3,1549
31/03/2015;3,2074
30/03/2015;3,2595
27/03/2015;3,2253
26/03/2015;3,1909
25/03/2015;3,1469
24/03/2015;3,1304
23/03/2015;3,1793
20/03/2015;3,2417
19/03/2015;3,2635
18/03/2015;3,2512
17/03/2015;3,2677
16/03/2015;3,2251
13/03/2015;3,2258
12/03/2015;3,1165
11/03/2015;3,1156
10/03/2015;3,1293
09/03/2015;3,1012
06/03/2015;3,0360
05/03/2015;2,9925
04/03/2015;2,9798
03/03/2015;2,9045
02/03/2015;2,8649
27/02/2015;2,8777
26/02/2015;2,8721
25/02/2015;2,8640
24/02/2015;2,8643
23/02/2015;2,8805
20/02/2015;2,8694
19/02/2015;2,8539
18/02/2015;2,8424
13/02/2015;2,8385
12/02/2015;2,8619
11/02/2015;2,8570
10/02/2015;2,8069
09/02/2015;2,7867
06/02/2015;2,7635
05/02/2015;2,7380
04/02/2015;2,7142
03/02/2015;2,7053
02/02/2015;2,6888
30/01/2015;2,6617
29/01/2015;2,5954
28/01/2015;2,5791
27/01/2015;2,5803
26/01/2015;2,5960
23/01/2015;2,5850
22/01/2015;2,5748
21/01/2015;2,5961
20/01/2015;2,6241
19/01/2015;2,6237
16/01/2015;2,6187
15/01/2015;2,6116
14/01/2015;2,6216
13/01/2015;2,6479
12/01/2015;2,6569
09/01/2015;2,6577
08/01/2015;2,6913
07/01/2015;2,6801
06/01/2015;2,7016
05/01/2015;2,7101
02/01/2015;2,6923
31/12/2014;2,6556
30/12/2014;2,6556
29/12/2014;2,6777
26/12/2014;2,6806
24/12/2014;2,6822
23/12/2014;2,6769
22/12/2014;2,6520
19/12/2014;2,6480
18/12/2014;2,6669
17/12/2014;2,7240
16/12/2014;2,7397
15/12/2014;2,6711
12/12/2014;2,6552
11/12/2014;2,6265
10/12/2014;2,5925
09/12/2014;2,6010
08/12/2014;2,5917
05/12/2014;2,5882
04/12/2014;2,5791
03/12/2014;2,5601
02/12/2014;2,5658
01/12/2014;2,5618
28/11/2014;2,5595
27/11/2014;2,5059
26/11/2014;2,5097
25/11/2014;2,5230
24/11/2014;2,5276
21/11/2014;2,5384
20/11/2014;2,5540
19/11/2014;2,5843
18/11/2014;2,5961
17/11/2014;2,6029
14/11/2014;2,6129
13/11/2014;2,5719
12/11/2014;2,5544
11/11/2014;2,5638
10/11/2014;2,5384
07/11/2014;2,5715
06/11/2014;2,5319
05/11/2014;2,5162
04/11/2014;2,5189
03/11/2014;2,4833
31/10/2014;2,4436
30/10/2014;2,4113
29/10/2014;2,4340
28/10/2014;2,4863
27/10/2014;2,5335
24/10/2014;2,4799
23/10/2014;2,4998
22/10/2014;2,4775
21/10/2014;2,4791
20/10/2014;2,4548
17/10/2014;2,4470
16/10/2014;2,4763
15/10/2014;2,4310
14/10/2014;2,3985
13/10/2014;2,3917
10/10/2014;2,4096
09/10/2014;2,3908
08/10/2014;2,4065
07/10/2014;2,4032
06/10/2014;2,4092
03/10/2014;2,4926
02/10/2014;2,4779
01/10/2014;2,4617
30/09/2014;2,4504
29/09/2014;2,4516
26/09/2014;2,4304
25/09/2014;2,4078
24/09/2014;2,4064
23/09/2014;2,4020
22/09/2014;2,3864
19/09/2014;2,3650
18/09/2014;2,3661
17/09/2014;2,3378
16/09/2014;2,3345
15/09/2014;2,3395
12/09/2014;2,3244
11/09/2014;2,2874
10/09/2014;2,2961
09/09/2014;2,2807
08/09/2014;2,2485
05/09/2014;2,2410
04/09/2014;2,2350
03/09/2014;2,2313
02/09/2014;2,2515
01/09/2014;2,2358
29/08/2014;2,2390
28/08/2014;2,2493
27/08/2014;2,2585
26/08/2014;2,2742
25/08/2014;2,2802
22/08/2014;2,2772
21/08/2014;2,2576
20/08/2014;2,2544
19/08/2014;2,2581
18/08/2014;2,2589
15/08/2014;2,2684
14/08/2014;2,2697
13/08/2014;2,2686
12/08/2014;2,2764
11/08/2014;2,2773
08/08/2014;2,2980
07/08/2014;2,2796
06/08/2014;2,2784
05/08/2014;2,2750
04/08/2014;2,2571
01/08/2014;2,2600
31/07/2014;2,2668
30/07/2014;2,2441
29/07/2014;2,2272
28/07/2014;2,2296
25/07/2014;2,2287
24/07/2014;2,2198
23/07/2014;2,2196
22/07/2014;2,2123
21/07/2014;2,2232
18/07/2014;2,2356
17/07/2014;2,2397
16/07/2014;2,2187
15/07/2014;2,2189
14/07/2014;2,2170
11/07/2014;2,2222
10/07/2014;2,2231
09/07/2014;2,2128
08/07/2014;2,2144
07/07/2014;2,2195
04/07/2014;2,2143
03/07/2014;2,2275
02/07/2014;2,2127
01/07/2014;2,2048
30/06/2014;2,2019
27/06/2014;2,1969
26/06/2014;2,2083
25/06/2014;2,2046
24/06/2014;2,2211
23/06/2014;2,2189
20/06/2014;2,2374
18/06/2014;2,2528
17/06/2014;2,2480
16/06/2014;2,2307
13/06/2014;2,2341
12/06/2014;2,2298
11/06/2014;2,2301
10/06/2014;2,2290
09/06/2014;2,2330
06/06/2014;2,2439
05/06/2014;2,2689
04/06/2014;2,2796
03/06/2014;2,2648
02/06/2014;2,2634
30/05/2014;2,2384
29/05/2014;2,2245
28/05/2014;2,2399
27/05/2014;2,2348
26/05/2014;2,2203
23/05/2014;2,2181
22/05/2014;2,2125
21/05/2014;2,2105
20/05/2014;2,2150
19/05/2014;2,2105
16/05/2014;2,2104
15/05/2014;2,2160
14/05/2014;2,2123
13/05/2014;2,2095
12/05/2014;2,2158
09/05/2014;2,2186
08/05/2014;2,2101
07/05/2014;2,2276
06/05/2014;2,2316
05/05/2014;2,2280
02/05/2014;2,2215
30/04/2014;2,2354
29/04/2014;2,2193
28/04/2014;2,2364
25/04/2014;2,2319
24/04/2014;2,2223
23/04/2014;2,2420
22/04/2014;2,2443
17/04/2014;2,2476
16/04/2014;2,2336
15/04/2014;2,2251
14/04/2014;2,2090
11/04/2014;2,2053
10/04/2014;2,1982
09/04/2014;2,2105
08/04/2014;2,1968
07/04/2014;2,2230
04/04/2014;2,2414
03/04/2014;2,2805
02/04/2014;2,2705
01/04/2014;2,2614
31/03/2014;2,2624
28/03/2014;2,2597
27/03/2014;2,2824
26/03/2014;2,3113
25/03/2014;2,3118
24/03/2014;2,3242
21/03/2014;2,3239
20/03/2014;2,3414
19/03/2014;2,3333
18/03/2014;2,3516
17/03/2014;2,3513
14/03/2014;2,3631
13/03/2014;2,3480
12/03/2014;2,3643
11/03/2014;2,3455
10/03/2014;2,3404
07/03/2014;2,3376
06/03/2014;2,3088
05/03/2014;2,3234
28/02/2014;2,3327
27/02/2014;2,3431
26/02/2014;2,3448
25/02/2014;2,3361
24/02/2014;2,3385
21/02/2014;2,3619
20/02/2014;2,3793
19/02/2014;2,3980
18/02/2014;2,3977
17/02/2014;2,3864
14/02/2014;2,3919
13/02/2014;2,4232
12/02/2014;2,4080
11/02/2014;2,4070
10/02/2014;2,3930
07/02/2014;2,3811
06/02/2014;2,4035
05/02/2014;2,4101
04/02/2014;2,4171
03/02/2014;2,4084
31/01/2014;2,4257
30/01/2014;2,4218
29/01/2014;2,4390
28/01/2014;2,4159
27/01/2014;2,4038
24/01/2014;2,4123
23/01/2014;2,3755
22/01/2014;2,3595
21/01/2014;2,3602
20/01/2014;2,3329
17/01/2014;2,3595
16/01/2014;2,3677
15/01/2014;2,3465
14/01/2014;2,3611
13/01/2014;2,3485
10/01/2014;2,3813
09/01/2014;2,3954
08/01/2014;2,3773
07/01/2014;2,3628
06/01/2014;2,3783
03/01/2014;2,3734
02/01/2014;2,3969
31/12/2013;2,3420
30/12/2013;2,3420
27/12/2013;2,3532
26/12/2013;2,3501
24/12/2013;2,3543
23/12/2013;2,3700
20/12/2013;2,3811
19/12/2013;2,3522
18/12/2013;2,3268
17/12/2013;2,3215
16/12/2013;2,3249
13/12/2013;2,3348
12/12/2013;2,3333
11/12/2013;2,3256
10/12/2013;2,3096
09/12/2013;2,3218
06/12/2013;2,3519
05/12/2013;2,3741
04/12/2013;2,3740
03/12/2013;2,3552
02/12/2013;2,3443
29/11/2013;2,3243
28/11/2013;2,3202
27/11/2013;2,3052
26/11/2013;2,3034
25/11/2013;2,2865
22/11/2013;2,2906
21/11/2013;2,3061
20/11/2013;2,2713
19/11/2013;2,2656
18/11/2013;2,2822
14/11/2013;2,3283
13/11/2013;2,3228
12/11/2013;2,3356
11/11/2013;2,3136
08/11/2013;2,3164
07/11/2013;2,2819
06/11/2013;2,2779
05/11/2013;2,2741
04/11/2013;2,2420
01/11/2013;2,2462
31/10/2013;2,2020
30/10/2013;2,1882
29/10/2013;2,1798
28/10/2013;2,1840
25/10/2013;2,1842
24/10/2013;2,1997
23/10/2013;2,1821
22/10/2013;2,1754
21/10/2013;2,1732
18/10/2013;2,1610
17/10/2013;2,1605
16/10/2013;2,1623
15/10/2013;2,1812
14/10/2013;2,1811
11/10/2013;2,1815
10/10/2013;2,1844
09/10/2013;2,2048
08/10/2013;2,2010
07/10/2013;2,2081
04/10/2013;2,2045
03/10/2013;2,2063
02/10/2013;2,2082
01/10/2013;2,2118
30/09/2013;2,2294
27/09/2013;2,2565
26/09/2013;2,2279
25/09/2013;2,2218
24/09/2013;2,2025
23/09/2013;2,2026
20/09/2013;2,2047
19/09/2013;2,2029
18/09/2013;2,2483
17/09/2013;2,2611
16/09/2013;2,2643
13/09/2013;2,2779
12/09/2013;2,2763
11/09/2013;2,2941
10/09/2013;2,2773
09/09/2013;2,2862
06/09/2013;2,2973
05/09/2013;2,3308
04/09/2013;2,3532
03/09/2013;2,3891
02/09/2013;2,3637
30/08/2013;2,3719
29/08/2013;2,3572
28/08/2013;2,3509
27/08/2013;2,3992
26/08/2013;2,3699
23/08/2013;2,3862
22/08/2013;2,4451
21/08/2013;2,4163
20/08/2013;2,3937
19/08/2013;2,3974
16/08/2013;2,3559
15/08/2013;2,3428
14/08/2013;2,3112
13/08/2013;2,3029
12/08/2013;2,2716
09/08/2013;2,2743
08/08/2013;2,2876
07/08/2013;2,3022
06/08/2013;2,2949
05/08/2013;2,3004
02/08/2013;2,2927
01/08/2013;2,2908
31/07/2013;2,2897
30/07/2013;2,2729
29/07/2013;2,2603
26/07/2013;2,2483
25/07/2013;2,2491
24/07/2013;2,2342
23/07/2013;2,2261
22/07/2013;2,2380
19/07/2013;2,2358
18/07/2013;2,2291
17/07/2013;2,2366
16/07/2013;2,2347
15/07/2013;2,2543
12/07/2013;2,2664
11/07/2013;2,2666
10/07/2013;2,2691
09/07/2013;2,2615
08/07/2013;2,2577
05/07/2013;2,2639
04/07/2013;2,2589
03/07/2013;2,2628
02/07/2013;2,2407
01/07/2013;2,2292
28/06/2013;2,2150
27/06/2013;2,1840
26/06/2013;2,1969
25/06/2013;2,2180
24/06/2013;2,2509
21/06/2013;2,2642
20/06/2013;2,2517
19/06/2013;2,1738
18/06/2013;2,1700
17/06/2013;2,1532
14/06/2013;2,1361
13/06/2013;2,1441
12/06/2013;2,1415
11/06/2013;2,1515
10/06/2013;2,1501
07/06/2013;2,1367
06/06/2013;2,1244
05/06/2013;2,1229
04/06/2013;2,1276
03/06/2013;2,1349
31/05/2013;2,1314
29/05/2013;2,0888
28/05/2013;2,0610
27/05/2013;2,0521
24/05/2013;2,0489
23/05/2013;2,0531
22/05/2013;2,0381
21/05/2013;2,0396
20/05/2013;2,0328
17/05/2013;2,0348
16/05/2013;2,0249
15/05/2013;2,0227
14/05/2013;2,0057
13/05/2013;2,0144
10/05/2013;2,0225
09/05/2013;2,0046
08/05/2013;2,0024
07/05/2013;2,0104
06/05/2013;2,0137
03/05/2013;2,0088
02/05/2013;2,0089
30/04/2013;2,0011
29/04/2013;1,9993
26/04/2013;1,9995
25/04/2013;2,0114
24/04/2013;2,0238
23/04/2013;2,0164
22/04/2013;2,0148
19/04/2013;2,0084
18/04/2013;2,0146
17/04/2013;1,9933
16/04/2013;1,9897
15/04/2013;1,9784
12/04/2013;1,9755
11/04/2013;1,9731
10/04/2013;1,9804
09/04/2013;1,9855
08/04/2013;1,9897
05/04/2013;2,0029
04/04/2013;2,0195
03/04/2013;2,0233
02/04/2013;2,0173
01/04/2013;2,0180
28/03/2013;2,0132
27/03/2013;2,0179
26/03/2013;2,0081
25/03/2013;2,0134
22/03/2013;2,0120
21/03/2013;1,9925
20/03/2013;1,9862
19/03/2013;1,9824
18/03/2013;1,9865
15/03/2013;1,9743
14/03/2013;1,9671
13/03/2013;1,9614
12/03/2013;1,9579
11/03/2013;1,9546
08/03/2013;1,9522
07/03/2013;1,9636
06/03/2013;1,9668
05/03/2013;1,9688
04/03/2013;1,9822
01/03/2013;1,9843
28/02/2013;1,9749
27/02/2013;1,9801
26/02/2013;1,9812
25/02/2013;1,9670
22/02/2013;1,9699
21/02/2013;1,9715
20/02/2013;1,9564
19/02/2013;1,9591
18/02/2013;1,9670
15/02/2013;1,9594
14/02/2013;1,9660
13/02/2013;1,9665
08/02/2013;1,9630
07/02/2013;1,9783
06/02/2013;1,9878
05/02/2013;1,9875
04/02/2013;1,9888
01/02/2013;1,9838
31/01/2013;1,9877
30/01/2013;1,9894
29/01/2013;1,9906
28/01/2013;2,0235
25/01/2013;2,0277
24/01/2013;2,0338
23/01/2013;2,0388
22/01/2013;2,0466
21/01/2013;2,0415
18/01/2013;2,0435
17/01/2013;2,0405
16/01/2013;2,0403
15/01/2013;2,0368
14/01/2013;2,0328
11/01/2013;2,0335
10/01/2013;2,0352
09/01/2013;2,0411
08/01/2013;2,0280
07/01/2013;2,0306
04/01/2013;2,0419
03/01/2013;2,0458
02/01/2013;2,0409
31/12/2012;2,0429
28/12/2012;2,0429
27/12/2012;2,0477
26/12/2012;2,0563
24/12/2012;2,0767
21/12/2012;2,0751
20/12/2012;2,0620
19/12/2012;2,0785
18/12/2012;2,0960
17/12/2012;2,0896
14/12/2012;2,0834
13/12/2012;2,0745
12/12/2012;2,0795
11/12/2012;2,0737
10/12/2012;2,0804
07/12/2012;2,0798
06/12/2012;2,0831
05/12/2012;2,1040
04/12/2012;2,1072
03/12/2012;2,1115
30/11/2012;2,1068
29/11/2012;2,0986
28/11/2012;2,0907
27/11/2012;2,0746
26/11/2012;2,0782
23/11/2012;2,0980
22/11/2012;2,0907
21/11/2012;2,0918
20/11/2012;2,0827
19/11/2012;2,0740
16/11/2012;2,0706
14/11/2012;2,0624
13/11/2012;2,0609
12/11/2012;2,0470
09/11/2012;2,0507
08/11/2012;2,0352
07/11/2012;2,0324
06/11/2012;2,0336
05/11/2012;2,0344
01/11/2012;2,0306
31/10/2012;2,0308
30/10/2012;2,0318
29/10/2012;2,0291
26/10/2012;2,0257
25/10/2012;2,0256
24/10/2012;2,0257
23/10/2012;2,0281
22/10/2012;2,0260
19/10/2012;2,0266
18/10/2012;2,0290
17/10/2012;2,0330
16/10/2012;2,0345
15/10/2012;2,0377
11/10/2012;2,0363
10/10/2012;2,0373
09/10/2012;2,0331
08/10/2012;2,0307
05/10/2012;2,0240
04/10/2012;2,0218
03/10/2012;2,0260
02/10/2012;2,0260
01/10/2012;2,0254
28/09/2012;2,0300
27/09/2012;2,0305
26/09/2012;2,0335
25/09/2012;2,0245
24/09/2012;2,0267
21/09/2012;2,0235
20/09/2012;2,0257
19/09/2012;2,0230
18/09/2012;2,0268
17/09/2012;2,0306
14/09/2012;2,0133
13/09/2012;2,0249
12/09/2012;2,0198
11/09/2012;2,0192
10/09/2012;2,0235
06/09/2012;2,0375
05/09/2012;2,0380
04/09/2012;2,0386
03/09/2012;2,0329
31/08/2012;2,0366
30/08/2012;2,0507
29/08/2012;2,0503
28/08/2012;2,0427
27/08/2012;2,0287
24/08/2012;2,0250
23/08/2012;2,0236
22/08/2012;2,0204
21/08/2012;2,0167
20/08/2012;2,0203
17/08/2012;2,0176
16/08/2012;2,0208
15/08/2012;2,0228
14/08/2012;2,0252
13/08/2012;2,0260
10/08/2012;2,0169
09/08/2012;2,0177
08/08/2012;2,0267
07/08/2012;2,0276
06/08/2012;2,0273
03/08/2012;2,0307
02/08/2012;2,0470
01/08/2012;2,0426
31/07/2012;2,0494
30/07/2012;2,0308
27/07/2012;2,0167
26/07/2012;2,0249
25/07/2012;2,0397
24/07/2012;2,0413
23/07/2012;2,0406
20/07/2012;2,0220
19/07/2012;2,0233
18/07/2012;2,0253
17/07/2012;2,0343
16/07/2012;2,0375
13/07/2012;2,0332
12/07/2012;2,0465
11/07/2012;2,0304
10/07/2012;2,0327
09/07/2012;2,0303
06/07/2012;2,0287
05/07/2012;2,0287
04/07/2012;2,0195
03/07/2012;1,9882
02/07/2012;1,9887
29/06/2012;2,0207
28/06/2012;2,0897
27/06/2012;2,0758
26/06/2012;2,0737
25/06/2012;2,0712
22/06/2012;2,0549
21/06/2012;2,0357
20/06/2012;2,0287
19/06/2012;2,0433
18/06/2012;2,0628
15/06/2012;2,0437
14/06/2012;2,0685
13/06/2012;2,0597
12/06/2012;2,0558
11/06/2012;2,0342
08/06/2012;2,0347
06/06/2012;2,0176
05/06/2012;2,0259
04/06/2012;2,0404
01/06/2012;2,0344
31/05/2012;2,0217
30/05/2012;2,0072
29/05/2012;1,9938
28/05/2012;1,9772
25/05/2012;2,0026
24/05/2012;2,0378
23/05/2012;2,0809
22/05/2012;2,0487
21/05/2012;2,0368
18/05/2012;2,0088
17/05/2012;1,9967
16/05/2012;1,9968
15/05/2012;1,9941
14/05/2012;1,9860
11/05/2012;1,9507
10/05/2012;1,9576
09/05/2012;1,9571
08/05/2012;1,9360
07/05/2012;1,9262
04/05/2012;1,9204
03/05/2012;1,9271
02/05/2012;1,9143
30/04/2012;1,8912
27/04/2012;1,8846
26/04/2012;1,8864
25/04/2012;1,8801
24/04/2012;1,8774
23/04/2012;1,8858
20/04/2012;1,8780
19/04/2012;1,8861
18/04/2012;1,8688
17/04/2012;1,8447
16/04/2012;1,8367
13/04/2012;1,8358
12/04/2012;1,8264
11/04/2012;1,8297
10/04/2012;1,8311
09/04/2012;1,8254
05/04/2012;1,8295
04/04/2012;1,8310
03/04/2012;1,8250
02/04/2012;1,8308
30/03/2012;1,8215
29/03/2012;1,8327
28/03/2012;1,8217
27/03/2012;1,8129
26/03/2012;1,8137
23/03/2012;1,8188
22/03/2012;1,8244
21/03/2012;1,8261
20/03/2012;1,8253
19/03/2012;1,8084
16/03/2012;1,8012
15/03/2012;1,8000
14/03/2012;1,8140
13/03/2012;1,8096
12/03/2012;1,8151
09/03/2012;1,7761
08/03/2012;1,7691
07/03/2012;1,7685
06/03/2012;1,7550
05/03/2012;1,7308
02/03/2012;1,7239
01/03/2012;1,7146
29/02/2012;1,7086
28/02/2012;1,7017
27/02/2012;1,7082
24/02/2012;1,7091
23/02/2012;1,7033
22/02/2012;1,7069
17/02/2012;1,7130
16/02/2012;1,7320
15/02/2012;1,7151
14/02/2012;1,7167
13/02/2012;1,7162
10/02/2012;1,7254
09/02/2012;1,7219
08/02/2012;1,7189
07/02/2012;1,7255
06/02/2012;1,7243
03/02/2012;1,7216
02/02/2012;1,7320
01/02/2012;1,7370
31/01/2012;1,7385
30/01/2012;1,7502
27/01/2012;1,7429
26/01/2012;1,7382
25/01/2012;1,7623
24/01/2012;1,7643
23/01/2012;1,7521
20/01/2012;1,7664
19/01/2012;1,7642
18/01/2012;1,7785
17/01/2012;1,7754
16/01/2012;1,7830
13/01/2012;1,7846
12/01/2012;1,7867
11/01/2012;1,8041
10/01/2012;1,8036
09/01/2012;1,8435
06/01/2012;1,8442
05/01/2012;1,8365
04/01/2012;1,8265
03/01/2012;1,8450
02/01/2012;1,8676
29/12/2011;1,8751
28/12/2011;1,8626
27/12/2011;1,8578
26/12/2011;1,8559
23/12/2011;1,8554
22/12/2011;1,8571
21/12/2011;1,8550
20/12/2011;1,8501
19/12/2011;1,8608
16/12/2011;1,8458
15/12/2011;1,8602
14/12/2011;1,8721
13/12/2011;1,8403
12/12/2011;1,8211
09/12/2011;1,8123
08/12/2011;1,7934
07/12/2011;1,7974
06/12/2011;1,7906
05/12/2011;1,7823
02/12/2011;1,7836
01/12/2011;1,7922
30/11/2011;1,8102
29/11/2011;1,8478
28/11/2011;1,8590
25/11/2011;1,8930
24/11/2011;1,8652
23/11/2011;1,8434
22/11/2011;1,8062
21/11/2011;1,8053
18/11/2011;1,7716
17/11/2011;1,7767
16/11/2011;1,7765
14/11/2011;1,7642
11/11/2011;1,7540
10/11/2011;1,7603
09/11/2011;1,7510
08/11/2011;1,7446
07/11/2011;1,7486
04/11/2011;1,7408
03/11/2011;1,7262
01/11/2011;1,7499
31/10/2011;1,6878
28/10/2011;1,6979
27/10/2011;1,7316
26/10/2011;1,7599
25/10/2011;1,7541
24/10/2011;1,7761
21/10/2011;1,7796
20/10/2011;1,7819
19/10/2011;1,7597
18/10/2011;1,7717
17/10/2011;1,7481
14/10/2011;1,7369
13/10/2011;1,7529
11/10/2011;1,7652
10/10/2011;1,7471
07/10/2011;1,7659
06/10/2011;1,8109
05/10/2011;1,8449
04/10/2011;1,8848
03/10/2011;1,8804
30/09/2011;1,8536
29/09/2011;1,8283
28/09/2011;1,8123
27/09/2011;1,8000
26/09/2011;1,8437
23/09/2011;1,8727
22/09/2011;1,9008
21/09/2011;1,8272
20/09/2011;1,7862
19/09/2011;1,7755
16/09/2011;1,7114
15/09/2011;1,7098
14/09/2011;1,7280
13/09/2011;1,7119
12/09/2011;1,6891
09/09/2011;1,6766
08/09/2011;1,6558
06/09/2011;1,6575
05/09/2011;1,6514
02/09/2011;1,6335
01/09/2011;1,6032
31/08/2011;1,5864
30/08/2011;1,5896
29/08/2011;1,5966
26/08/2011;1,6106
25/08/2011;1,6146
24/08/2011;1,6031
23/08/2011;1,6028
22/08/2011;1,6001
19/08/2011;1,5952
18/08/2011;1,6054
17/08/2011;1,5822
16/08/2011;1,5910
15/08/2011;1,5948
12/08/2011;1,6149
11/08/2011;1,6298
10/08/2011;1,6175
09/08/2011;1,6326
08/08/2011;1,5991
05/08/2011;1,5887
04/08/2011;1,5744
03/08/2011;1,5643
02/08/2011;1,5648
01/08/2011;1,5543
29/07/2011;1,5555
28/07/2011;1,5643
27/07/2011;1,5631
26/07/2011;1,5337
25/07/2011;1,5441
22/07/2011;1,5539
21/07/2011;1,5559
20/07/2011;1,5643
19/07/2011;1,5683
18/07/2011;1,5820
15/07/2011;1,5735
14/07/2011;1,5721
13/07/2011;1,5754
12/07/2011;1,5765
11/07/2011;1,5788
08/07/2011;1,5626
07/07/2011;1,5573
06/07/2011;1,5654
05/07/2011;1,5629
04/07/2011;1,5572
01/07/2011;1,5591
30/06/2011;1,5603
29/06/2011;1,5722
28/06/2011;1,5825
27/06/2011;1,5961
24/06/2011;1,5980
22/06/2011;1,5869
21/06/2011;1,5902
20/06/2011;1,5961
17/06/2011;1,5971
16/06/2011;1,6100
15/06/2011;1,5952
14/06/2011;1,5813
13/06/2011;1,5880
10/06/2011;1,5930
09/06/2011;1,5869
08/06/2011;1,5812
07/06/2011;1,5756
06/06/2011;1,5802
03/06/2011;1,5736
02/06/2011;1,5797
01/06/2011;1,5870
31/05/2011;1,5791
30/05/2011;1,5950
27/05/2011;1,6030
26/05/2011;1,6188
25/05/2011;1,6289
24/05/2011;1,6248
23/05/2011;1,6331
20/05/2011;1,6161
19/05/2011;1,6157
18/05/2011;1,6158
17/05/2011;1,6282
16/05/2011;1,6309
13/05/2011;1,6320
12/05/2011;1,6199
11/05/2011;1,6170
10/05/2011;1,6061
09/05/2011;1,6191
06/05/2011;1,6103
05/05/2011;1,6211
04/05/2011;1,6022
03/05/2011;1,5882
02/05/2011;1,5739
29/04/2011;1,5725
28/04/2011;1,5845
27/04/2011;1,5697
26/04/2011;1,5646
25/04/2011;1,5712
20/04/2011;1,5714
19/04/2011;1,5784
18/04/2011;1,5904
15/04/2011;1,5768
14/04/2011;1,5834
13/04/2011;1,5856
12/04/2011;1,5862
11/04/2011;1,5797
08/04/2011;1,5754
07/04/2011;1,5919
06/04/2011;1,6089
05/04/2011;1,6079
04/04/2011;1,6102
01/04/2011;1,6186
31/03/2011;1,6279
30/03/2011;1,6352
29/03/2011;1,6538
28/03/2011;1,6606
25/03/2011;1,6573
24/03/2011;1,6585
23/03/2011;1,6594
22/03/2011;1,6630
21/03/2011;1,6644
18/03/2011;1,6712
17/03/2011;1,6749
16/03/2011;1,6666
15/03/2011;1,6684
14/03/2011;1,6623
11/03/2011;1,6641
10/03/2011;1,6604
09/03/2011;1,6551
04/03/2011;1,6454
03/03/2011;1,6537
02/03/2011;1,6602
01/03/2011;1,6619
28/02/2011;1,6604
25/02/2011;1,6617
24/02/2011;1,6641
23/02/2011;1,6712
22/02/2011;1,6686
21/02/2011;1,6659
18/02/2011;1,6669
17/02/2011;1,6696
16/02/2011;1,6696
15/02/2011;1,6674
14/02/2011;1,6673
11/02/2011;1,6671
10/02/2011;1,6672
09/02/2011;1,6635
08/02/2011;1,6703
07/02/2011;1,6768
04/02/2011;1,6730
03/02/2011;1,6689
02/02/2011;1,6663
01/02/2011;1,6623
31/01/2011;1,6726
28/01/2011;1,6774
27/01/2011;1,6712
26/01/2011;1,6684
25/01/2011;1,6737
24/01/2011;1,6723
21/01/2011;1,6715
20/01/2011;1,6707
19/01/2011;1,6706
18/01/2011;1,6737
17/01/2011;1,6810
14/01/2011;1,6835
13/01/2011;1,6693
12/01/2011;1,6879
11/01/2011;1,6879
10/01/2011;1,6904
07/01/2011;1,6853
06/01/2011;1,6849
05/01/2011;1,6705
04/01/2011;1,6548
03/01/2011;1,6502
31/12/2010;1,6654
30/12/2010;1,6654
29/12/2010;1,6780
28/12/2010;1,6858
27/12/2010;1,6914
24/12/2010;1,6895
23/12/2010;1,6976
22/12/2010;1,6938
21/12/2010;1,6966
20/12/2010;1,7074
17/12/2010;1,7090
16/12/2010;1,7020
15/12/2010;1,6980
14/12/2010;1,6941
13/12/2010;1,7019
10/12/2010;1,7109
09/12/2010;1,7016
08/12/2010;1,6884
07/12/2010;1,6731
06/12/2010;1,6828
02/12/2010;1,7021
01/12/2010;1,7036
30/11/2010;1,7153
29/11/2010;1,7263
26/11/2010;1,7290
25/11/2010;1,7198
24/11/2010;1,7239
23/11/2010;1,7328
22/11/2010;1,7227
19/11/2010;1,7181
18/11/2010;1,7135
17/11/2010;1,7290
16/11/2010;1,7287
12/11/2010;1,7190
11/11/2010;1,7170
10/11/2010;1,7062
09/11/2010;1,6962
08/11/2010;1,6962
05/11/2010;1,6793
04/11/2010;1,6811
03/11/2010;1,6929
01/11/2010;1,7036
29/10/2010;1,7006
28/10/2010;1,7104
27/10/2010;1,7069
26/10/2010;1,7037
25/10/2010;1,7018
22/10/2010;1,6989
21/10/2010;1,6889
20/10/2010;1,6727
19/10/2010;1,6860
18/10/2010;1,6678
15/10/2010;1,6596
14/10/2010;1,6588
13/10/2010;1,6546
11/10/2010;1,6640
08/10/2010;1,6796
07/10/2010;1,6769
06/10/2010;1,6750
05/10/2010;1,6800
04/10/2010;1,6874
01/10/2010;1,6804
30/09/2010;1,6934
29/09/2010;1,7045
28/09/2010;1,7085
27/09/2010;1,7092
24/09/2010;1,7112
23/09/2010;1,7186
22/09/2010;1,7176
21/09/2010;1,7247
20/09/2010;1,7208
17/09/2010;1,7158
16/09/2010;1,7176
15/09/2010;1,7161
14/09/2010;1,7060
13/09/2010;1,7166
10/09/2010;1,7178
09/09/2010;1,7230
08/09/2010;1,7223
06/09/2010;1,7251
03/09/2010;1,7273
02/09/2010;1,7359
01/09/2010;1,7433
31/08/2010;1,7552
30/08/2010;1,7583
27/08/2010;1,7536
26/08/2010;1,7588
25/08/2010;1,7660
24/08/2010;1,7719
23/08/2010;1,7579
20/08/2010;1,7589
19/08/2010;1,7576
18/08/2010;1,7505
17/08/2010;1,7520
16/08/2010;1,7631
13/08/2010;1,7708
12/08/2010;1,7723
11/08/2010;1,7655
10/08/2010;1,7568
09/08/2010;1,7529
06/08/2010;1,7558
05/08/2010;1,7527
04/08/2010;1,7555
03/08/2010;1,7586
02/08/2010;1,7481
30/07/2010;1,7564
29/07/2010;1,7635
28/07/2010;1,7642
27/07/2010;1,7650
26/07/2010;1,7661
23/07/2010;1,7609
22/07/2010;1,7621
21/07/2010;1,7758
20/07/2010;1,7792
19/07/2010;1,7846
16/07/2010;1,7784
15/07/2010;1,7682
14/07/2010;1,7649
13/07/2010;1,7517
12/07/2010;1,7636
09/07/2010;1,7564
08/07/2010;1,7644
07/07/2010;1,7711
06/07/2010;1,7657
05/07/2010;1,7747
02/07/2010;1,7777
01/07/2010;1,7998
30/06/2010;1,8007
29/06/2010;1,8068
28/06/2010;1,7818
25/06/2010;1,7773
24/06/2010;1,7899
23/06/2010;1,7900
22/06/2010;1,7672
21/06/2010;1,7655
18/06/2010;1,7753
17/06/2010;1,7809
16/06/2010;1,7885
15/06/2010;1,7963
14/06/2010;1,8022
11/06/2010;1,8117
10/06/2010;1,8177
09/06/2010;1,8415
08/06/2010;1,8650
07/06/2010;1,8626
04/06/2010;1,8393
02/06/2010;1,8354
01/06/2010;1,8247
31/05/2010;1,8159
28/05/2010;1,8221
27/05/2010;1,8320
26/05/2010;1,8453
25/05/2010;1,8803
24/05/2010;1,8514
21/05/2010;1,8702
20/05/2010;1,8669
19/05/2010;1,8358
18/05/2010;1,7913
17/05/2010;1,8037
14/05/2010;1,7959
13/05/2010;1,7729
12/05/2010;1,7715
11/05/2010;1,7835
10/05/2010;1,7825
07/05/2010;1,8335
06/05/2010;1,8345
05/05/2010;1,7854
04/05/2010;1,7549
03/05/2010;1,7307
30/04/2010;1,7298
29/04/2010;1,7313
28/04/2010;1,7550
27/04/2010;1,7584
26/04/2010;1,7438
23/04/2010;1,7616
22/04/2010;1,7618
20/04/2010;1,7489
19/04/2010;1,7580
16/04/2010;1,7550
15/04/2010;1,7475
14/04/2010;1,7438
13/04/2010;1,7576
12/04/2010;1,7600
09/04/2010;1,7722
08/04/2010;1,7798
07/04/2010;1,7654
06/04/2010;1,7597
05/04/2010;1,7565
01/04/2010;1,7693
31/03/2010;1,7802
30/03/2010;1,7944
29/03/2010;1,8056
26/03/2010;1,8223
25/03/2010;1,8000
24/03/2010;1,7896
23/03/2010;1,7805
22/03/2010;1,8022
19/03/2010;1,7946
18/03/2010;1,7840
17/03/2010;1,7632
16/03/2010;1,7658
15/03/2010;1,7636
12/03/2010;1,7629
11/03/2010;1,7685
10/03/2010;1,7708
09/03/2010;1,7891
08/03/2010;1,7818
05/03/2010;1,7816
04/03/2010;1,7880
03/03/2010;1,7838
02/03/2010;1,7843
01/03/2010;1,7992
26/02/2010;1,8102
25/02/2010;1,8356
24/02/2010;1,8195
23/02/2010;1,8178
22/02/2010;1,8038
19/02/2010;1,8108
18/02/2010;1,8258
17/02/2010;1,8305
12/02/2010;1,8662
11/02/2010;1,8508
10/02/2010;1,8475
09/02/2010;1,8542
08/02/2010;1,8722
05/02/2010;1,8745
04/02/2010;1,8707
03/02/2010;1,8329
02/02/2010;1,8355
01/02/2010;1,8765
29/01/2010;1,8740
28/01/2010;1,8552
27/01/2010;1,8505
26/01/2010;1,8359
25/01/2010;1,8186
22/01/2010;1,8179
21/01/2010;1,7895
20/01/2010;1,7846
19/01/2010;1,7739
18/01/2010;1,7713
15/01/2010;1,7703
14/01/2010;1,7640
13/01/2010;1,7434
12/01/2010;1,7431
11/01/2010;1,7315
08/01/2010;1,7382
07/01/2010;1,7405
06/01/2010;1,7329
05/01/2010;1,7219
04/01/2010;1,7232
30/12/2009;1,7404
29/12/2009;1,7413
28/12/2009;1,7390
24/12/2009;1,7519
23/12/2009;1,7755
22/12/2009;1,7817
21/12/2009;1,7779
18/12/2009;1,7871
17/12/2009;1,7815
16/12/2009;1,7510
15/12/2009;1,7449
14/12/2009;1,7475
11/12/2009;1,7513
10/12/2009;1,7619
09/12/2009;1,7603
08/12/2009;1,7474
07/12/2009;1,7294
04/12/2009;1,7123
03/12/2009;1,7088
02/12/2009;1,7193
01/12/2009;1,7285
30/11/2009;1,7497
27/11/2009;1,7435
26/11/2009;1,7401
25/11/2009;1,7264
24/11/2009;1,7274
23/11/2009;1,7237
19/11/2009;1,7348
18/11/2009;1,7095
17/11/2009;1,7145
16/11/2009;1,7119
13/11/2009;1,7282
12/11/2009;1,7242
11/11/2009;1,7104
10/11/2009;1,7088
09/11/2009;1,7016
06/11/2009;1,7171
05/11/2009;1,7232
04/11/2009;1,7263
03/11/2009;1,7580
30/10/2009;1,7432
29/10/2009;1,7428
28/10/2009;1,7439
27/10/2009;1,7334
26/10/2009;1,7149
23/10/2009;1,7105
22/10/2009;1,7296
21/10/2009;1,7432
20/10/2009;1,7442
19/10/2009;1,7122
16/10/2009;1,7127
15/10/2009;1,7029
14/10/2009;1,7091
13/10/2009;1,7290
09/10/2009;1,7381
08/10/2009;1,7404
07/10/2009;1,7587
06/10/2009;1,7525
05/10/2009;1,7665
02/10/2009;1,7836
01/10/2009;1,7786
30/09/2009;1,7773
29/09/2009;1,7920
28/09/2009;1,7902
25/09/2009;1,8009
24/09/2009;1,7909
23/09/2009;1,7908
22/09/2009;1,8053
21/09/2009;1,8164
18/09/2009;1,8041
17/09/2009;1,8086
16/09/2009;1,7976
15/09/2009;1,8079
14/09/2009;1,8189
11/09/2009;1,8171
10/09/2009;1,8253
09/09/2009;1,8272
08/09/2009;1,8246
04/09/2009;1,8493
03/09/2009;1,8694
02/09/2009;1,9030
01/09/2009;1,8821
31/08/2009;1,8856
28/08/2009;1,8732
27/08/2009;1,8661
26/08/2009;1,8662
25/08/2009;1,8411
24/08/2009;1,8331
21/08/2009;1,8289
20/08/2009;1,8426
19/08/2009;1,8425
18/08/2009;1,8566
17/08/2009;1,8674
14/08/2009;1,8377
13/08/2009;1,8317
12/08/2009;1,8378
11/08/2009;1,8449
10/08/2009;1,8404
07/08/2009;1,8224
06/08/2009;1,8340
05/08/2009;1,8173
04/08/2009;1,8264
03/08/2009;1,8361
31/07/2009;1,8718
30/07/2009;1,8803
29/07/2009;1,8974
28/07/2009;1,8811
27/07/2009;1,8829
24/07/2009;1,8952
23/07/2009;1,8914
22/07/2009;1,9021
21/07/2009;1,9035
20/07/2009;1,9060
17/07/2009;1,9282
16/07/2009;1,9332
15/07/2009;1,9412
14/07/2009;1,9696
13/07/2009;1,9887
10/07/2009;2,0139
09/07/2009;1,9913
08/07/2009;1,9974
07/07/2009;1,9633
06/07/2009;1,9703
03/07/2009;1,9466
02/07/2009;1,9461
01/07/2009;1,9334
30/06/2009;1,9508
29/06/2009;1,9479
26/06/2009;1,9388
25/06/2009;1,9554
24/06/2009;1,9716
23/06/2009;2,0011
22/06/2009;2,0066
19/06/2009;1,9584
18/06/2009;1,9701
17/06/2009;1,9776
16/06/2009;1,9453
15/06/2009;1,9450
12/06/2009;1,9293
10/06/2009;1,9466
09/06/2009;1,9377
08/06/2009;1,9696
05/06/2009;1,9526
04/06/2009;1,9489
03/06/2009;1,9592
02/06/2009;1,9362
01/06/2009;1,9432
29/05/2009;1,9722
28/05/2009;2,0136
27/05/2009;2,0087
26/05/2009;2,0253
25/05/2009;2,0226
22/05/2009;2,0271
21/05/2009;2,0256
20/05/2009;2,0191
19/05/2009;2,0480
18/05/2009;2,0776
15/05/2009;2,0754
14/05/2009;2,0921
13/05/2009;2,0984
12/05/2009;2,0641
11/05/2009;2,0571
08/05/2009;2,0742
07/05/2009;2,0976
06/05/2009;2,2105
05/05/2009;2,1468
04/05/2009;2,1361
30/04/2009;2,1775
29/04/2009;2,1830
28/04/2009;2,2029
27/04/2009;2,2157
24/04/2009;2,1925
23/04/2009;2,2099
22/04/2009;2,2120
20/04/2009;2,2342
17/04/2009;2,1856
16/04/2009;2,1783
15/04/2009;2,1984
14/04/2009;2,1868
13/04/2009;2,1691
09/04/2009;2,1758
08/04/2009;2,2006
07/04/2009;2,2241
06/04/2009;2,2244
03/04/2009;2,2064
02/04/2009;2,2347
01/04/2009;2,2891
31/03/2009;2,3144
30/03/2009;2,3289
27/03/2009;2,2737
26/03/2009;2,2367
25/03/2009;2,2427
24/03/2009;2,2559
23/03/2009;2,2497
20/03/2009;2,2559
19/03/2009;2,2371
18/03/2009;2,2798
17/03/2009;2,2825
16/03/2009;2,2697
13/03/2009;2,3004
12/03/2009;2,3150
11/03/2009;2,3358
10/03/2009;2,3507
09/03/2009;2,3773
06/03/2009;2,3760
05/03/2009;2,3814
04/03/2009;2,3909
03/03/2009;2,4210
02/03/2009;2,4113
27/02/2009;2,3776
26/02/2009;2,3495
25/02/2009;2,3806
20/02/2009;2,3908
19/02/2009;2,3241
18/02/2009;2,3388
17/02/2009;2,3123
16/02/2009;2,2711
13/02/2009;2,2672
12/02/2009;2,2901
11/02/2009;2,2862
10/02/2009;2,2520
09/02/2009;2,2438
06/02/2009;2,2650
05/02/2009;2,3057
04/02/2009;2,2986
03/02/2009;2,3136
02/02/2009;2,3467
30/01/2009;2,3154
29/01/2009;2,2753
28/01/2009;2,2974
27/01/2009;2,3101
26/01/2009;2,3141
23/01/2009;2,3560
22/01/2009;2,3291
21/01/2009;2,3536
20/01/2009;2,3540
19/01/2009;2,3298
16/01/2009;2,3240
15/01/2009;2,3795
14/01/2009;2,3333
13/01/2009;2,3075
12/01/2009;2,2961
09/01/2009;2,2859
08/01/2009;2,2675
07/01/2009;2,2166
06/01/2009;2,1881
05/01/2009;2,2772
02/01/2009;2,3290
30/12/2008;2,3362
29/12/2008;2,3948
26/12/2008;2,3605
23/12/2008;2,3743
22/12/2008;2,3732
19/12/2008;2,3851
18/12/2008;2,3564
17/12/2008;2,3568
16/12/2008;2,3775
15/12/2008;2,3682
12/12/2008;2,3912
11/12/2008;2,3389
10/12/2008;2,4675
09/12/2008;2,4821
08/12/2008;2,4681
05/12/2008;2,4996
04/12/2008;2,4897
03/12/2008;2,4205
02/12/2008;2,3449
01/12/2008;2,3557
28/11/2008;2,3323
27/11/2008;2,2649
26/11/2008;2,3213
25/11/2008;2,3048
24/11/2008;2,3492
21/11/2008;2,4269
20/11/2008;2,3954
19/11/2008;2,3758
18/11/2008;2,2988
17/11/2008;2,2932
14/11/2008;2,2792
13/11/2008;2,3306
12/11/2008;2,2624
11/11/2008;2,2002
10/11/2008;2,1327
07/11/2008;2,1605
06/11/2008;2,1585
05/11/2008;2,1202
04/11/2008;2,1219
03/11/2008;2,1810
31/10/2008;2,1145
30/10/2008;2,1143
29/10/2008;2,1312
28/10/2008;2,1692
27/10/2008;2,2516
24/10/2008;2,3104
23/10/2008;2,3139
22/10/2008;2,3642
21/10/2008;2,1933
20/10/2008;2,1166
17/10/2008;2,1012
16/10/2008;2,1846
15/10/2008;2,1543
14/10/2008;2,0781
13/10/2008;2,1554
10/10/2008;2,2872
09/10/2008;2,1810
08/10/2008;2,3916
07/10/2008;2,1875
06/10/2008;2,1761
03/10/2008;2,0532
02/10/2008;2,0073
01/10/2008;1,9205
30/09/2008;1,9135
29/09/2008;1,9551
26/09/2008;1,8547
25/09/2008;1,8269
24/09/2008;1,8437
23/09/2008;1,8234
22/09/2008;1,7981
19/09/2008;1,8390
18/09/2008;1,9151
17/09/2008;1,8652
16/09/2008;1,8402
15/09/2008;1,8117
12/09/2008;1,7904
11/09/2008;1,8247
10/09/2008;1,7850
09/09/2008;1,7536
08/09/2008;1,7274
05/09/2008;1,7297
04/09/2008;1,7002
03/09/2008;1,6720
02/09/2008;1,6594
01/09/2008;1,6439
29/08/2008;1,6336
28/08/2008;1,6254
27/08/2008;1,6205
26/08/2008;1,6367
25/08/2008;1,6267
22/08/2008;1,6209
21/08/2008;1,6135
20/08/2008;1,6199
19/08/2008;1,6335
18/08/2008;1,6341
15/08/2008;1,6381
14/08/2008;1,6196
13/08/2008;1,6203
12/08/2008;1,6153
11/08/2008;1,6140
08/08/2008;1,6128
07/08/2008;1,5835
06/08/2008;1,5774
05/08/2008;1,5724
04/08/2008;1,5651
01/08/2008;1,5585
31/07/2008;1,5658
30/07/2008;1,5633
29/07/2008;1,5722
28/07/2008;1,5746
25/07/2008;1,5737
24/07/2008;1,5773
23/07/2008;1,5826
22/07/2008;1,5803
21/07/2008;1,5810
18/07/2008;1,5930
17/07/2008;1,5905
16/07/2008;1,5952
15/07/2008;1,5902
14/07/2008;1,5934
11/07/2008;1,6024
10/07/2008;1,6139
09/07/2008;1,6084
08/07/2008;1,6019
07/07/2008;1,6033
04/07/2008;1,6092
03/07/2008;1,6081
02/07/2008;1,5985
01/07/2008;1,6053
30/06/2008;1,5911
27/06/2008;1,6069
26/06/2008;1,5943
25/06/2008;1,5993
24/06/2008;1,6038
23/06/2008;1,6109
20/06/2008;1,6034
19/06/2008;1,6043
18/06/2008;1,6105
17/06/2008;1,6119
16/06/2008;1,6269
13/06/2008;1,6360
12/06/2008;1,6392
11/06/2008;1,6420
10/06/2008;1,6384
09/06/2008;1,6257
06/06/2008;1,6274
05/06/2008;1,6254
04/06/2008;1,6299
03/06/2008;1,6270
02/06/2008;1,6290
30/05/2008;1,6286
29/05/2008;1,6488
28/05/2008;1,6622
27/05/2008;1,6673
26/05/2008;1,6602
23/05/2008;1,6539
21/05/2008;1,6484
20/05/2008;1,6562
19/05/2008;1,6452
16/05/2008;1,6426
15/05/2008;1,6593
14/05/2008;1,6633
13/05/2008;1,6575
12/05/2008;1,6735
09/05/2008;1,6941
08/05/2008;1,6928
07/05/2008;1,6733
06/05/2008;1,6607
05/05/2008;1,6570
02/05/2008;1,6498
30/04/2008;1,6864
29/04/2008;1,7050
28/04/2008;1,6756
25/04/2008;1,6680
24/04/2008;1,6679
23/04/2008;1,6574
22/04/2008;1,6567
18/04/2008;1,6685
17/04/2008;1,6580
16/04/2008;1,6691
15/04/2008;1,6814
14/04/2008;1,6859
11/04/2008;1,6868
10/04/2008;1,6814
09/04/2008;1,6870
08/04/2008;1,7030
07/04/2008;1,6982
04/04/2008;1,7109
03/04/2008;1,7244
02/04/2008;1,7265
01/04/2008;1,7526
31/03/2008;1,7483
28/03/2008;1,7448
27/03/2008;1,7337
26/03/2008;1,7280
25/03/2008;1,7333
24/03/2008;1,7399
20/03/2008;1,7416
19/03/2008;1,7037
18/03/2008;1,6999
17/03/2008;1,7240
14/03/2008;1,6939
13/03/2008;1,6963
12/03/2008;1,6788
11/03/2008;1,6939
10/03/2008;1,6988
07/03/2008;1,6833
06/03/2008;1,6712
05/03/2008;1,6692
04/03/2008;1,6722
03/03/2008;1,6808
29/02/2008;1,6825
28/02/2008;1,6715
27/02/2008;1,6707
26/02/2008;1,6874
25/02/2008;1,7054
22/02/2008;1,7032
21/02/2008;1,7096
20/02/2008;1,7343
19/02/2008;1,7321
18/02/2008;1,7386
15/02/2008;1,7533
14/02/2008;1,7461
13/02/2008;1,7451
12/02/2008;1,7470
11/02/2008;1,7593
08/02/2008;1,7673
07/02/2008;1,7619
06/02/2008;1,7523
01/02/2008;1,7443
31/01/2008;1,7595
30/01/2008;1,7794
29/01/2008;1,7754
28/01/2008;1,7898
25/01/2008;1,7904
24/01/2008;1,7875
23/01/2008;1,8139
22/01/2008;1,8033
21/01/2008;1,8293
18/01/2008;1,7842
17/01/2008;1,7679
16/01/2008;1,7622
15/01/2008;1,7442
14/01/2008;1,7406
11/01/2008;1,7528
10/01/2008;1,7620
09/01/2008;1,7683
08/01/2008;1,7546
07/01/2008;1,7667
04/01/2008;1,7566
03/01/2008;1,7561
02/01/2008;1,7714
31/12/2007;1,7705
28/12/2007;1,7705
27/12/2007;1,7663
26/12/2007;1,7787
24/12/2007;1,7901
21/12/2007;1,7958
20/12/2007;1,8024
19/12/2007;1,8011
18/12/2007;1,8083
17/12/2007;1,8115
14/12/2007;1,7951
13/12/2007;1,7738
12/12/2007;1,7616
11/12/2007;1,7642
10/12/2007;1,7612
07/12/2007;1,7608
06/12/2007;1,7865
05/12/2007;1,7948
04/12/2007;1,8225
03/12/2007;1,7880
30/11/2007;1,7829
29/11/2007;1,7897
28/11/2007;1,8010
27/11/2007;1,8493
26/11/2007;1,8102
23/11/2007;1,7954
22/11/2007;1,7739
21/11/2007;1,7858
20/11/2007;1,7639
19/11/2007;1,7585
16/11/2007;1,7406
14/11/2007;1,7370
13/11/2007;1,7674
12/11/2007;1,7732
09/11/2007;1,7482
08/11/2007;1,7346
07/11/2007;1,7392
06/11/2007;1,7317
05/11/2007;1,7548
01/11/2007;1,7452
31/10/2007;1,7432
30/10/2007;1,7544
29/10/2007;1,7587
26/10/2007;1,7744
25/10/2007;1,7888
24/10/2007;1,7961
23/10/2007;1,7999
22/10/2007;1,8198
19/10/2007;1,7956
18/10/2007;1,8063
17/10/2007;1,8130
16/10/2007;1,8234
15/10/2007;1,8070
11/10/2007;1,7912
10/10/2007;1,8040
09/10/2007;1,8100
08/10/2007;1,8125
05/10/2007;1,8084
04/10/2007;1,8276
03/10/2007;1,8266
02/10/2007;1,8227
01/10/2007;1,8217
28/09/2007;1,8381
27/09/2007;1,8401
26/09/2007;1,8485
25/09/2007;1,8648
24/09/2007;1,8686
21/09/2007;1,8610
20/09/2007;1,8629
19/09/2007;1,8631
18/09/2007;1,8952
17/09/2007;1,9115
14/09/2007;1,9023
13/09/2007;1,8983
12/09/2007;1,9117
11/09/2007;1,9296
10/09/2007;1,9583
06/09/2007;1,9537
05/09/2007;1,9632
04/09/2007;1,9520
03/09/2007;1,9539
31/08/2007;1,9612
30/08/2007;1,9769
29/08/2007;1,9856
28/08/2007;1,9841
27/08/2007;1,9481
24/08/2007;1,9847
23/08/2007;1,9931
22/08/2007;2,0165
21/08/2007;2,0377
20/08/2007;2,0272
17/08/2007;2,0368
16/08/2007;2,1116
15/08/2007;2,0035
14/08/2007;1,9801
13/08/2007;1,9403
10/08/2007;1,9542
09/08/2007;1,9183
08/08/2007;1,8858
07/08/2007;1,9069
06/08/2007;1,9098
03/08/2007;1,8806
02/08/2007;1,8721
01/08/2007;1,8848
31/07/2007;1,8768
30/07/2007;1,8801
27/07/2007;1,9061
26/07/2007;1,9046
25/07/2007;1,8635
24/07/2007;1,8517
23/07/2007;1,8440
20/07/2007;1,8598
19/07/2007;1,8528
18/07/2007;1,8601
17/07/2007;1,8613
16/07/2007;1,8639
13/07/2007;1,8676
12/07/2007;1,8759
11/07/2007;1,8892
10/07/2007;1,8939
09/07/2007;1,8984
06/07/2007;1,9025
05/07/2007;1,9149
04/07/2007;1,9091
03/07/2007;1,9114
02/07/2007;1,9168
29/06/2007;1,9254
28/06/2007;1,9248
27/06/2007;1,9491
26/06/2007;1,9480
25/06/2007;1,9371
22/06/2007;1,9326
21/06/2007;1,9189
20/06/2007;1,9190
19/06/2007;1,9100
18/06/2007;1,9000
15/06/2007;1,9089
14/06/2007;1,9295
13/06/2007;1,9434
12/06/2007;1,9412
11/06/2007;1,9465
08/06/2007;1,9630
06/06/2007;1,9609
05/06/2007;1,9387
04/06/2007;1,9207
01/06/2007;1,9048
31/05/2007;1,9281
30/05/2007;1,9460
29/05/2007;1,9453
28/05/2007;1,9433
25/05/2007;1,9512
24/05/2007;1,9645
23/05/2007;1,9481
22/05/2007;1,9401
21/05/2007;1,9427
18/05/2007;1,9622
17/05/2007;1,9565
16/05/2007;1,9578
15/05/2007;1,9914
14/05/2007;2,0130
11/05/2007;2,0186
10/05/2007;2,0209
09/05/2007;2,0214
08/05/2007;2,0218
07/05/2007;2,0258
04/05/2007;2,0301
03/05/2007;2,0231
02/05/2007;2,0260
30/04/2007;2,0331
27/04/2007;2,0313
26/04/2007;2,0244
25/04/2007;2,0228
24/04/2007;2,0377
23/04/2007;2,0282
20/04/2007;2,0254
19/04/2007;2,0304
18/04/2007;2,0357
17/04/2007;2,0340
16/04/2007;2,0332
13/04/2007;2,0223
12/04/2007;2,0363
11/04/2007;2,0325
10/04/2007;2,0274
09/04/2007;2,0228
05/04/2007;2,0325
04/04/2007;2,0313
03/04/2007;2,0364
02/04/2007;2,0470
30/03/2007;2,0496
29/03/2007;2,0537
28/03/2007;2,0708
27/03/2007;2,0629
26/03/2007;2,0593
23/03/2007;2,0644
22/03/2007;2,0594
21/03/2007;2,0668
20/03/2007;2,0755
19/03/2007;2,0784
16/03/2007;2,0907
15/03/2007;2,0901
14/03/2007;2,1036
13/03/2007;2,0954
12/03/2007;2,0894
09/03/2007;2,0975
08/03/2007;2,1046
07/03/2007;2,1113
06/03/2007;2,1201
05/03/2007;2,1380
02/03/2007;2,1266
01/03/2007;2,1252
28/02/2007;2,1174
27/02/2007;2,1091
26/02/2007;2,0855
23/02/2007;2,0860
22/02/2007;2,0758
21/02/2007;2,0794
16/02/2007;2,0905
15/02/2007;2,0888
14/02/2007;2,0992
13/02/2007;2,1080
12/02/2007;2,1132
09/02/2007;2,1025
08/02/2007;2,0943
07/02/2007;2,0844
06/02/2007;2,0825
05/02/2007;2,0956
02/02/2007;2,0974
01/02/2007;2,1085
31/01/2007;2,1239
30/01/2007;2,1321
29/01/2007;2,1352
26/01/2007;2,1352
25/01/2007;2,1273
24/01/2007;2,1278
23/01/2007;2,1360
22/01/2007;2,1319
19/01/2007;2,1399
18/01/2007;2,1321
17/01/2007;2,1342
16/01/2007;2,1436
15/01/2007;2,1399
12/01/2007;2,1413
11/01/2007;2,1457
10/01/2007;2,1548
09/01/2007;2,1498
08/01/2007;2,1497
05/01/2007;2,1466
04/01/2007;2,1421
03/01/2007;2,1364
02/01/2007;2,1334
29/12/2006;2,1372
28/12/2006;2,1372
27/12/2006;2,1489
26/12/2006;2,1429
22/12/2006;2,1510
20/12/2006;2,1552
19/12/2006;2,1564
18/12/2006;2,1462
15/12/2006;2,1462
14/12/2006;2,1452
13/12/2006;2,1451
12/12/2006;2,1473
11/12/2006;2,1376
08/12/2006;2,1434
07/12/2006;2,1420
06/12/2006;2,1520
05/12/2006;2,1552
04/12/2006;2,1685
01/12/2006;2,1664
30/11/2006;2,1660
29/11/2006;2,1775
28/11/2006;2,1862
27/11/2006;2,1792
24/11/2006;2,1692
23/11/2006;2,1675
22/11/2006;2,1615
21/11/2006;2,1630
20/11/2006;2,1614
17/11/2006;2,1585
16/11/2006;2,1509
14/11/2006;2,1529
13/11/2006;2,1612
10/11/2006;2,1481
09/11/2006;2,1404
08/11/2006;2,1456
07/11/2006;2,1345
06/11/2006;2,1370
03/11/2006;2,1412
01/11/2006;2,1402
31/10/2006;2,1422
30/10/2006;2,1448
27/10/2006;2,1370
26/10/2006;2,1355
25/10/2006;2,1502
24/10/2006;2,1459
23/10/2006;2,1383
20/10/2006;2,1449
19/10/2006;2,1379
18/10/2006;2,1331
17/10/2006;2,1353
16/10/2006;2,1323
13/10/2006;2,1411
11/10/2006;2,1538
10/10/2006;2,1489
09/10/2006;2,1580
06/10/2006;2,1621
05/10/2006;2,1621
04/10/2006;2,1668
03/10/2006;2,1647
02/10/2006;2,1615
29/09/2006;2,1734
28/09/2006;2,1785
27/09/2006;2,1852
26/09/2006;2,1972
25/09/2006;2,2180
22/09/2006;2,2169
21/09/2006;2,1961
20/09/2006;2,1682
19/09/2006;2,1510
18/09/2006;2,1445
15/09/2006;2,1532
14/09/2006;2,1585
13/09/2006;2,1692
12/09/2006;2,1724
11/09/2006;2,1743
08/09/2006;2,1574
06/09/2006;2,1435
05/09/2006;2,1280
04/09/2006;2,1274
01/09/2006;2,1460
31/08/2006;2,1380
30/08/2006;2,1322
29/08/2006;2,1411
28/08/2006;2,1465
25/08/2006;2,1563
24/08/2006;2,1515
23/08/2006;2,1346
22/08/2006;2,1347
21/08/2006;2,1353
18/08/2006;2,1448
17/08/2006;2,1357
16/08/2006;2,1321
15/08/2006;2,1472
14/08/2006;2,1597
11/08/2006;2,1608
10/08/2006;2,1620
09/08/2006;2,1679
08/08/2006;2,1831
07/08/2006;2,1785
04/08/2006;2,1712
03/08/2006;2,1827
02/08/2006;2,1813
01/08/2006;2,1897
31/07/2006;2,1754
28/07/2006;2,1792
27/07/2006;2,1891
26/07/2006;2,1976
25/07/2006;2,1985
24/07/2006;2,1908
21/07/2006;2,1927
20/07/2006;2,1887
19/07/2006;2,1802
18/07/2006;2,1954
17/07/2006;2,2118
14/07/2006;2,2122
13/07/2006;2,2098
12/07/2006;2,1907
11/07/2006;2,1851
10/07/2006;2,1742
07/07/2006;2,1757
06/07/2006;2,1832
05/07/2006;2,1947
04/07/2006;2,1638
03/07/2006;2,1693
30/06/2006;2,1635
29/06/2006;2,2055
28/06/2006;2,2254
27/06/2006;2,2307
26/06/2006;2,2251
23/06/2006;2,2454
22/06/2006;2,2383
21/06/2006;2,2370
20/06/2006;2,2498
19/06/2006;2,2396
16/06/2006;2,2513
14/06/2006;2,2837
13/06/2006;2,3010
12/06/2006;2,2699
09/06/2006;2,2607
08/06/2006;2,2693
07/06/2006;2,2492
06/06/2006;2,2678
05/06/2006;2,2549
02/06/2006;2,2587
01/06/2006;2,2705
31/05/2006;2,2997
30/05/2006;2,3227
29/05/2006;2,2558
26/05/2006;2,2512
25/05/2006;2,3142
24/05/2006;2,3703
23/05/2006;2,2593
22/05/2006;2,2875
19/05/2006;2,1922
18/05/2006;2,1825
17/05/2006;2,1818
16/05/2006;2,1395
15/05/2006;2,1766
12/05/2006;2,1299
11/05/2006;2,0873
10/05/2006;2,0578
09/05/2006;2,0634
08/05/2006;2,0643
05/05/2006;2,0579
04/05/2006;2,0659
03/05/2006;2,0698
02/05/2006;2,0710
28/04/2006;2,0884
27/04/2006;2,1128
26/04/2006;2,1216
25/04/2006;2,1225
24/04/2006;2,1174
20/04/2006;2,1228
19/04/2006;2,1135
18/04/2006;2,1284
17/04/2006;2,1335
13/04/2006;2,1428
12/04/2006;2,1328
11/04/2006;2,1412
10/04/2006;2,1514
07/04/2006;2,1401
06/04/2006;2,1291
05/04/2006;2,1336
04/04/2006;2,1285
03/04/2006;2,1534
31/03/2006;2,1716
30/03/2006;2,1944
29/03/2006;2,2220
28/03/2006;2,2230
27/03/2006;2,1796
24/03/2006;2,1620
23/03/2006;2,1498
22/03/2006;2,1545
21/03/2006;2,1583
20/03/2006;2,1378
17/03/2006;2,1180
16/03/2006;2,1059
15/03/2006;2,1207
14/03/2006;2,1261
13/03/2006;2,1341
10/03/2006;2,1439
09/03/2006;2,1607
08/03/2006;2,1770
07/03/2006;2,1674
06/03/2006;2,1253
03/03/2006;2,1147
02/03/2006;2,1126
01/03/2006;2,1173
24/02/2006;2,1347
23/02/2006;2,1345
22/02/2006;2,1476
21/02/2006;2,1289
20/02/2006;2,1174
17/02/2006;2,1178
16/02/2006;2,1169
15/02/2006;2,1367
14/02/2006;2,1427
13/02/2006;2,1613
10/02/2006;2,1567
09/02/2006;2,1770
08/02/2006;2,1948
07/02/2006;2,1858
06/02/2006;2,1869
03/02/2006;2,2194
02/02/2006;2,2202
01/02/2006;2,2209
31/01/2006;2,2152
30/01/2006;2,2108
27/01/2006;2,2144
26/01/2006;2,2374
25/01/2006;2,2425
24/01/2006;2,2432
23/01/2006;2,2601
20/01/2006;2,2748
19/01/2006;2,3217
18/01/2006;2,3268
17/01/2006;2,2916
16/01/2006;2,2754
13/01/2006;2,2739
12/01/2006;2,2721
11/01/2006;2,2671
10/01/2006;2,2630
09/01/2006;2,2624
06/01/2006;2,2862
05/01/2006;2,2817
04/01/2006;2,3058
03/01/2006;2,3452
02/01/2006;2,3362
30/12/2005;2,3399
29/12/2005;2,3399
28/12/2005;2,3475
27/12/2005;2,3518
26/12/2005;2,3317
23/12/2005;2,3319
22/12/2005;2,3246
21/12/2005;2,3160
20/12/2005;2,3489
19/12/2005;2,3727
16/12/2005;2,3348
15/12/2005;2,2949
14/12/2005;2,2771
13/12/2005;2,2557
12/12/2005;2,2626
09/12/2005;2,2438
08/12/2005;2,2119
07/12/2005;2,1792
06/12/2005;2,1799
05/12/2005;2,1960
02/12/2005;2,2053
01/12/2005;2,2169
30/11/2005;2,2062
29/11/2005;2,1972
28/11/2005;2,2086
25/11/2005;2,2321
24/11/2005;2,2362
23/11/2005;2,2372
22/11/2005;2,2503
21/11/2005;2,2173
18/11/2005;2,2179
17/11/2005;2,1858
16/11/2005;2,1966
14/11/2005;2,1982
11/11/2005;2,1625
10/11/2005;2,1749
09/11/2005;2,1709
08/11/2005;2,2024
07/11/2005;2,2005
04/11/2005;2,2223
03/11/2005;2,2328
01/11/2005;2,2508
31/10/2005;2,2535
28/10/2005;2,2783
27/10/2005;2,2843
26/10/2005;2,2738
25/10/2005;2,2610
24/10/2005;2,2615
21/10/2005;2,2538
20/10/2005;2,2435
19/10/2005;2,2527
18/10/2005;2,2397
17/10/2005;2,2344
14/10/2005;2,2503
13/10/2005;2,2619
11/10/2005;2,2343
10/10/2005;2,2376
07/10/2005;2,2622
06/10/2005;2,2878
05/10/2005;2,2677
04/10/2005;2,2416
03/10/2005;2,2331
30/09/2005;2,2214
29/09/2005;2,2236
28/09/2005;2,2425
27/09/2005;2,2525
26/09/2005;2,2575
23/09/2005;2,2674
22/09/2005;2,2744
21/09/2005;2,2819
20/09/2005;2,2940
19/09/2005;2,2897
16/09/2005;2,2929
15/09/2005;2,3004
14/09/2005;2,3292
13/09/2005;2,3261
12/09/2005;2,3189
09/09/2005;2,3167
08/09/2005;2,3190
06/09/2005;2,3254
05/09/2005;2,3287
02/09/2005;2,3421
01/09/2005;2,3615
31/08/2005;2,3629
30/08/2005;2,3853
29/08/2005;2,3979
26/08/2005;2,4121
25/08/2005;2,4195
24/08/2005;2,4227
23/08/2005;2,4089
22/08/2005;2,4020
19/08/2005;2,4308
18/08/2005;2,3629
17/08/2005;2,3484
16/08/2005;2,3434
15/08/2005;2,3414
12/08/2005;2,3750
11/08/2005;2,3161
10/08/2005;2,2759
09/08/2005;2,3143
08/08/2005;2,3092
05/08/2005;2,2978
04/08/2005;2,3046
03/08/2005;2,3143
02/08/2005;2,3522
01/08/2005;2,3777
29/07/2005;2,3897
28/07/2005;2,4203
27/07/2005;2,4431
26/07/2005;2,4648
25/07/2005;2,4279
22/07/2005;2,3753
21/07/2005;2,3397
20/07/2005;2,3514
19/07/2005;2,3426
18/07/2005;2,3296
15/07/2005;2,3419
14/07/2005;2,3425
13/07/2005;2,3474
12/07/2005;2,3345
11/07/2005;2,3494
08/07/2005;2,3675
07/07/2005;2,3882
06/07/2005;2,3893
05/07/2005;2,3660
04/07/2005;2,3707
01/07/2005;2,3451
30/06/2005;2,3496
29/06/2005;2,3541
28/06/2005;2,3686
27/06/2005;2,3822
24/06/2005;2,3869
23/06/2005;2,3924
22/06/2005;2,3695
21/06/2005;2,3764
20/06/2005;2,3847
17/06/2005;2,3865
16/06/2005;2,4153
15/06/2005;2,4447
14/06/2005;2,4367
13/06/2005;2,4555
10/06/2005;2,4743
09/06/2005;2,4883
08/06/2005;2,4456
07/06/2005;2,4624
06/06/2005;2,4568
03/06/2005;2,4021
02/06/2005;2,4194
01/06/2005;2,4278
31/05/2005;2,4030
30/05/2005;2,3776
27/05/2005;2,3926
25/05/2005;2,4305
24/05/2005;2,4305
23/05/2005;2,4291
20/05/2005;2,4485
19/05/2005;2,4450
18/05/2005;2,4628
17/05/2005;2,4771
16/05/2005;2,4764
13/05/2005;2,4707
12/05/2005;2,4640
11/05/2005;2,4711
10/05/2005;2,4642
09/05/2005;2,4530
06/05/2005;2,4586
05/05/2005;2,4679
04/05/2005;2,4757
03/05/2005;2,4999
02/05/2005;2,5138
29/04/2005;2,5305
28/04/2005;2,5209
27/04/2005;2,5187
26/04/2005;2,5347
25/04/2005;2,5300
22/04/2005;2,5384
20/04/2005;2,5637
19/04/2005;2,5817
18/04/2005;2,6149
15/04/2005;2,5963
14/04/2005;2,5739
13/04/2005;2,5590
12/04/2005;2,5891
11/04/2005;2,5775
08/04/2005;2,5934
07/04/2005;2,6011
06/04/2005;2,6059
05/04/2005;2,6247
04/04/2005;2,6590
01/04/2005;2,6542
31/03/2005;2,6654
30/03/2005;2,6800
29/03/2005;2,7032
28/03/2005;2,7377
24/03/2005;2,7295
23/03/2005;2,7395
22/03/2005;2,7052
21/03/2005;2,7280
18/03/2005;2,7155
17/03/2005;2,7514
16/03/2005;2,7562
15/03/2005;2,7613
14/03/2005;2,7515
11/03/2005;2,7013
10/03/2005;2,7311
09/03/2005;2,7105
08/03/2005;2,6926
07/03/2005;2,6616
04/03/2005;2,6607
03/03/2005;2,6690
02/03/2005;2,6360
01/03/2005;2,6003
28/02/2005;2,5942
25/02/2005;2,6312
24/02/2005;2,6090
23/02/2005;2,5849
22/02/2005;2,5929
21/02/2005;2,5754
18/02/2005;2,5613
17/02/2005;2,5729
16/02/2005;2,5918
15/02/2005;2,5754
14/02/2005;2,5826
11/02/2005;2,6165
10/02/2005;2,6114
09/02/2005;2,6070
04/02/2005;2,6022
03/02/2005;2,6026
02/02/2005;2,6232
01/02/2005;2,6122
31/01/2005;2,6240
28/01/2005;2,6579
27/01/2005;2,6637
26/01/2005;2,6740
25/01/2005;2,6786
24/01/2005;2,6772
21/01/2005;2,6786
20/01/2005;2,7214
19/01/2005;2,7177
18/01/2005;2,7131
17/01/2005;2,6999
14/01/2005;2,7066
13/01/2005;2,7003
12/01/2005;2,7105
11/01/2005;2,7098
10/01/2005;2,6965
07/01/2005;2,7024
06/01/2005;2,7199
05/01/2005;2,7088
04/01/2005;2,6879
03/01/2005;2,6674
31/12/2004;2,6536
30/12/2004;2,6536
29/12/2004;2,6828
28/12/2004;2,6887
27/12/2004;2,6975
24/12/2004;2,6904
23/12/2004;2,7059
22/12/2004;2,6982
21/12/2004;2,6884
20/12/2004;2,6919
17/12/2004;2,7239
16/12/2004;2,7285
15/12/2004;2,7500
14/12/2004;2,7572
13/12/2004;2,7689
10/12/2004;2,7859
09/12/2004;2,7736
08/12/2004;2,7656
07/12/2004;2,7314
06/12/2004;2,7178
03/12/2004;2,7087
02/12/2004;2,7231
01/12/2004;2,7137
30/11/2004;2,7299
29/11/2004;2,7394
26/11/2004;2,7324
25/11/2004;2,7503
24/11/2004;2,7477
23/11/2004;2,7438
22/11/2004;2,7672
19/11/2004;2,7629
18/11/2004;2,7595
17/11/2004;2,7666
16/11/2004;2,7848
12/11/2004;2,7983
11/11/2004;2,8192
10/11/2004;2,8201
09/11/2004;2,8279
08/11/2004;2,8291
05/11/2004;2,8178
04/11/2004;2,8203
03/11/2004;2,8296
01/11/2004;2,8582
29/10/2004;2,8557
28/10/2004;2,8647
27/10/2004;2,8577
26/10/2004;2,8721
25/10/2004;2,8809
22/10/2004;2,8481
21/10/2004;2,8527
20/10/2004;2,8839
19/10/2004;2,8698
18/10/2004;2,8539
15/10/2004;2,8615
14/10/2004;2,8623
13/10/2004;2,8366
11/10/2004;2,8310
08/10/2004;2,8243
07/10/2004;2,8510
06/10/2004;2,8354
05/10/2004;2,8233
04/10/2004;2,8257
01/10/2004;2,8505
30/09/2004;2,8578
29/09/2004;2,8594
28/09/2004;2,8684
27/09/2004;2,8720
24/09/2004;2,8727
23/09/2004;2,8717
22/09/2004;2,8669
21/09/2004;2,8729
20/09/2004;2,8668
17/09/2004;2,8736
16/09/2004;2,8884
15/09/2004;2,9034
14/09/2004;2,9117
13/09/2004;2,9052
10/09/2004;2,8980
09/09/2004;2,9020
08/09/2004;2,9006
06/09/2004;2,9134
03/09/2004;2,9281
02/09/2004;2,9353
01/09/2004;2,9290
31/08/2004;2,9330
30/08/2004;2,9480
27/08/2004;2,9563
26/08/2004;2,9533
25/08/2004;2,9504
24/08/2004;2,9568
23/08/2004;2,9679
20/08/2004;2,9734
19/08/2004;2,9785
18/08/2004;2,9914
17/08/2004;2,9981
16/08/2004;3,0138
13/08/2004;3,0227
12/08/2004;3,0299
11/08/2004;3,0384
10/08/2004;3,0277
09/08/2004;3,0388
06/08/2004;3,0481
05/08/2004;3,0629
04/08/2004;3,0571
03/08/2004;3,0542
02/08/2004;3,0458
30/07/2004;3,0260
29/07/2004;3,0366
28/07/2004;3,0549
27/07/2004;3,0662
26/07/2004;3,0565
23/07/2004;3,0457
22/07/2004;3,0384
21/07/2004;3,0239
20/07/2004;3,0033
19/07/2004;2,9931
16/07/2004;3,0013
15/07/2004;3,0207
14/07/2004;3,0276
13/07/2004;3,0412
12/07/2004;3,0363
09/07/2004;3,0420
08/07/2004;3,0467
07/07/2004;3,0359
06/07/2004;3,0410
05/07/2004;3,0308
02/07/2004;3,0494
01/07/2004;3,0739
30/06/2004;3,1067
29/06/2004;3,1175
28/06/2004;3,1239
25/06/2004;3,1088
24/06/2004;3,1022
23/06/2004;3,1250
22/06/2004;3,1333
21/06/2004;3,1290
18/06/2004;3,1380
17/06/2004;3,1272
16/06/2004;3,1397
15/06/2004;3,1372
14/06/2004;3,1643
11/06/2004;3,1394
09/06/2004;3,1158
08/06/2004;3,1147
07/06/2004;3,1111
04/06/2004;3,1327
03/06/2004;3,1435
02/06/2004;3,1294
01/06/2004;3,1559
31/05/2004;3,1283
28/05/2004;3,0953
27/05/2004;3,1516
26/05/2004;3,1562
25/05/2004;3,1568
24/05/2004;3,1790
21/05/2004;3,2043
20/05/2004;3,1805
19/05/2004;3,1051
18/05/2004;3,1161
17/05/2004;3,1212
14/05/2004;3,0974
13/05/2004;3,1271
12/05/2004;3,1203
11/05/2004;3,1043
10/05/2004;3,1241
07/05/2004;3,0496
06/05/2004;2,9891
05/05/2004;2,9608
04/05/2004;2,9688
03/05/2004;2,9561
30/04/2004;2,9439
29/04/2004;2,9514
28/04/2004;2,9327
27/04/2004;2,9153
26/04/2004;2,9077
23/04/2004;2,9165
22/04/2004;2,9297
20/04/2004;2,9178
19/04/2004;2,9093
16/04/2004;2,9145
15/04/2004;2,9056
14/04/2004;2,8948
13/04/2004;2,8851
12/04/2004;2,8847
08/04/2004;2,8794
07/04/2004;2,8765
06/04/2004;2,8735
05/04/2004;2,8843
02/04/2004;2,8922
01/04/2004;2,8896
31/03/2004;2,9078
30/03/2004;2,9208
29/03/2004;2,9357
26/03/2004;2,9402
25/03/2004;2,9329
24/03/2004;2,9256
23/03/2004;2,9136
22/03/2004;2,9099
19/03/2004;2,8992
18/03/2004;2,9127
17/03/2004;2,9062
16/03/2004;2,8993
15/03/2004;2,9005
12/03/2004;2,9055
11/03/2004;2,9124
10/03/2004;2,8883
09/03/2004;2,8750
08/03/2004;2,8744
05/03/2004;2,8782
04/03/2004;2,8870
03/03/2004;2,8804
02/03/2004;2,9078
01/03/2004;2,8937
27/02/2004;2,9130
26/02/2004;2,9361
25/02/2004;2,9395
20/02/2004;2,9870
19/02/2004;2,9501
18/02/2004;2,9288
17/02/2004;2,9117
16/02/2004;2,9058
13/02/2004;2,9077
12/02/2004;2,9034
11/02/2004;2,9245
10/02/2004;2,9190
09/02/2004;2,9333
06/02/2004;2,9492
05/02/2004;2,9327
04/02/2004;2,9098
03/02/2004;2,9318
02/02/2004;2,9478
30/01/2004;2,9401
29/01/2004;2,9228
28/01/2004;2,8777
27/01/2004;2,8579
26/01/2004;2,8423
23/01/2004;2,8427
22/01/2004;2,8409
21/01/2004;2,8409
20/01/2004;2,8374
19/01/2004;2,8411
16/01/2004;2,8176
15/01/2004;2,8118
14/01/2004;2,8134
13/01/2004;2,8014
12/01/2004;2,8155
09/01/2004;2,8414
08/01/2004;2,8580
07/01/2004;2,8715
06/01/2004;2,8500
05/01/2004;2,8619
02/01/2004;2,8854
31/12/2003;2,8884
30/12/2003;2,8884
29/12/2003;2,8875
26/12/2003;2,8986
24/12/2003;2,9074
23/12/2003;2,9167
22/12/2003;2,9231
19/12/2003;2,9270
18/12/2003;2,9333
17/12/2003;2,9373
16/12/2003;2,9312
15/12/2003;2,9285
12/12/2003;2,9412
11/12/2003;2,9426
10/12/2003;2,9421
09/12/2003;2,9342
08/12/2003;2,9414
05/12/2003;2,9390
04/12/2003;2,9395
03/12/2003;2,9308
02/12/2003;2,9265
01/12/2003;2,9333
28/11/2003;2,9486
27/11/2003;2,9469
26/11/2003;2,9353
25/11/2003;2,9238
24/11/2003;2,9262
21/11/2003;2,9293
20/11/2003;2,9472
19/11/2003;2,9499
18/11/2003;2,9413
17/11/2003;2,9538
14/11/2003;2,9410
13/11/2003;2,9188
12/11/2003;2,9104
11/11/2003;2,8947
10/11/2003;2,8799
07/11/2003;2,8691
06/11/2003;2,8700
05/11/2003;2,8588
04/11/2003;2,8599
03/11/2003;2,8551
31/10/2003;2,8554
30/10/2003;2,8432
29/10/2003;2,8529
28/10/2003;2,8667
27/10/2003;2,8720
24/10/2003;2,8687
23/10/2003;2,8690
22/10/2003;2,8594
21/10/2003;2,8634
20/10/2003;2,8831
17/10/2003;2,8627
16/10/2003;2,8401
15/10/2003;2,8260
14/10/2003;2,8417
13/10/2003;2,8363
10/10/2003;2,8393
09/10/2003;2,8414
08/10/2003;2,8436
07/10/2003;2,8693
06/10/2003;2,8745
03/10/2003;2,8867
02/10/2003;2,8981
01/10/2003;2,9026
30/09/2003;2,9226
29/09/2003;2,9366
26/09/2003;2,9365
25/09/2003;2,9298
24/09/2003;2,9236
23/09/2003;2,9137
22/09/2003;2,9013
19/09/2003;2,9057
18/09/2003;2,8967
17/09/2003;2,8959
16/09/2003;2,8959
15/09/2003;2,8890
12/09/2003;2,8951
11/09/2003;2,8983
10/09/2003;2,9117
09/09/2003;2,9298
08/09/2003;2,9147
05/09/2003;2,9208
04/09/2003;2,9410
03/09/2003;2,9560
02/09/2003;2,9781
01/09/2003;2,9832
29/08/2003;2,9657
28/08/2003;2,9523
27/08/2003;2,9726
26/08/2003;2,9888
25/08/2003;2,9887
22/08/2003;2,9918
21/08/2003;3,0024
20/08/2003;3,0002
19/08/2003;2,9965
18/08/2003;2,9840
15/08/2003;2,9922
14/08/2003;3,0132
13/08/2003;3,0301
12/08/2003;3,0229
11/08/2003;2,9937
08/08/2003;2,9884
07/08/2003;3,0061
06/08/2003;3,0382
05/08/2003;3,0358
04/08/2003;3,0732
01/08/2003;2,9998
31/07/2003;2,9647
30/07/2003;2,9465
29/07/2003;2,9147
28/07/2003;2,8957
25/07/2003;2,8877
24/07/2003;2,8953
23/07/2003;2,8870
22/07/2003;2,8818
21/07/2003;2,8820
18/07/2003;2,8766
17/07/2003;2,8555
16/07/2003;2,8669
15/07/2003;2,8546
14/07/2003;2,8745
11/07/2003;2,9021
10/07/2003;2,8914
09/07/2003;2,8663
08/07/2003;2,8815
07/07/2003;2,8686
04/07/2003;2,8291
03/07/2003;2,8324
02/07/2003;2,8211
01/07/2003;2,8435
30/06/2003;2,8712
27/06/2003;2,8804
26/06/2003;2,8932
25/06/2003;2,8551
24/06/2003;2,8608
23/06/2003;2,8780
20/06/2003;2,8925
18/06/2003;2,8894
17/06/2003;2,8736
16/06/2003;2,8500
13/06/2003;2,8562
12/06/2003;2,8612
11/06/2003;2,8684
10/06/2003;2,8595
09/06/2003;2,8674
06/06/2003;2,8483
05/06/2003;2,8921
04/06/2003;2,9104
03/06/2003;2,9632
02/06/2003;2,9772
30/05/2003;2,9648
29/05/2003;2,9480
28/05/2003;3,0132
27/05/2003;3,0249
26/05/2003;2,9557
23/05/2003;2,9437
22/05/2003;2,9834
21/05/2003;3,0101
20/05/2003;3,0133
19/05/2003;2,9807
16/05/2003;2,9723
15/05/2003;2,9294
14/05/2003;2,8894
13/05/2003;2,8645
12/05/2003;2,8749
09/05/2003;2,8794
08/05/2003;2,9169
07/05/2003;2,9631
06/05/2003;3,0269
05/05/2003;2,9837
02/05/2003;2,9151
30/04/2003;2,8890
29/04/2003;2,9243
28/04/2003;2,9907
25/04/2003;3,0115
24/04/2003;3,0021
23/04/2003;3,0139
22/04/2003;3,0631
17/04/2003;3,0281
16/04/2003;3,0744
15/04/2003;3,1146
14/04/2003;3,1810
11/04/2003;3,2139
10/04/2003;3,2149
09/04/2003;3,1849
08/04/2003;3,1641
07/04/2003;3,1715
04/04/2003;3,2461
03/04/2003;3,2555
02/04/2003;3,2787
01/04/2003;3,3351
31/03/2003;3,3523
28/03/2003;3,3749
27/03/2003;3,4023
26/03/2003;3,3739
25/03/2003;3,3884
24/03/2003;3,4062
21/03/2003;3,4454
20/03/2003;3,4822
19/03/2003;3,4568
18/03/2003;3,4300
17/03/2003;3,4434
14/03/2003;3,3950
13/03/2003;3,4285
12/03/2003;3,4755
11/03/2003;3,5053
10/03/2003;3,5273
07/03/2003;3,5002
06/03/2003;3,5252
05/03/2003;3,5629
28/02/2003;3,5624
27/02/2003;3,5842
26/02/2003;3,5809
25/02/2003;3,6005
24/02/2003;3,5862
21/02/2003;3,6089
20/02/2003;3,6059
19/02/2003;3,5927
18/02/2003;3,5881
17/02/2003;3,6224
14/02/2003;3,6572
13/02/2003;3,6351
12/02/2003;3,5995
11/02/2003;3,5729
10/02/2003;3,6034
07/02/2003;3,5794
06/02/2003;3,6037
05/02/2003;3,5837
04/02/2003;3,5398
03/02/2003;3,4922
31/01/2003;3,5250
30/01/2003;3,5688
29/01/2003;3,6409
28/01/2003;3,6304
27/01/2003;3,6615
24/01/2003;3,5915
23/01/2003;3,4893
22/01/2003;3,5181
21/01/2003;3,4394
20/01/2003;3,4095
17/01/2003;3,3624
16/01/2003;3,2929
15/01/2003;3,2975
14/01/2003;3,2750
13/01/2003;3,2948
10/01/2003;3,2910
09/01/2003;3,3289
08/01/2003;3,3116
07/01/2003;3,3415
06/01/2003;3,3656
03/01/2003;3,4690
02/01/2003;3,5216
31/12/2002;3,5325
30/12/2002;3,5325
27/12/2002;3,5405
26/12/2002;3,5243
24/12/2002;3,5002
23/12/2002;3,4939
20/12/2002;3,4270
19/12/2002;3,5039
18/12/2002;3,5308
17/12/2002;3,5819
16/12/2002;3,6310
13/12/2002;3,7334
12/12/2002;3,7527
11/12/2002;3,7946
10/12/2002;3,7677
09/12/2002;3,7972
06/12/2002;3,7518
05/12/2002;3,7506
04/12/2002;3,7041
03/12/2002;3,6617
02/12/2002;3,6152
29/11/2002;3,6357
28/11/2002;3,6022
27/11/2002;3,5890
26/11/2002;3,5864
25/11/2002;3,5484
22/11/2002;3,5608
21/11/2002;3,5095
20/11/2002;3,5138
19/11/2002;3,5539
18/11/2002;3,5881
14/11/2002;3,6789
13/11/2002;3,6334
12/11/2002;3,5519
11/11/2002;3,5027
08/11/2002;3,5263
07/11/2002;3,6210
06/11/2002;3,5968
05/11/2002;3,5617
04/11/2002;3,5410
01/11/2002;3,6105
31/10/2002;3,6442
30/10/2002;3,7435
29/10/2002;3,8203
28/10/2002;3,7398
25/10/2002;3,8007
24/10/2002;3,8609
23/10/2002;3,8696
22/10/2002;3,9544
21/10/2002;3,9117
18/10/2002;3,8751
17/10/2002;3,9237
16/10/2002;3,8736
15/10/2002;3,8559
14/10/2002;3,8605
11/10/2002;3,9227
10/10/2002;3,9220
09/10/2002;3,8512
08/10/2002;3,7009
07/10/2002;3,6957
04/10/2002;3,6585
03/10/2002;3,6944
02/10/2002;3,5928
01/10/2002;3,7459
30/09/2002;3,8941
27/09/2002;3,8533
26/09/2002;3,7508
25/09/2002;3,7249
24/09/2002;3,6208
23/09/2002;3,5440
20/09/2002;3,4269
19/09/2002;3,3835
18/09/2002;3,3232
17/09/2002;3,2240
16/09/2002;3,1876
13/09/2002;3,1498
12/09/2002;3,1231
11/09/2002;3,1145
10/09/2002;3,1298
09/09/2002;3,1304
06/09/2002;3,1775
05/09/2002;3,1504
04/09/2002;3,1317
03/09/2002;3,0890
02/09/2002;3,0278
30/08/2002;3,0215
29/08/2002;3,1231
28/08/2002;3,1211
27/08/2002;3,0941
26/08/2002;3,0780
23/08/2002;3,1128
22/08/2002;3,1409
21/08/2002;3,0786
20/08/2002;3,0915
19/08/2002;3,1134
16/08/2002;3,1612
15/08/2002;3,1904
14/08/2002;3,1957
13/08/2002;3,2086
12/08/2002;3,0971
09/08/2002;2,9956
08/08/2002;2,8875
07/08/2002;3,0590
06/08/2002;3,2062
05/08/2002;3,0724
02/08/2002;3,0294
01/08/2002;3,3267
31/07/2002;3,4277
30/07/2002;3,2684
29/07/2002;3,1441
26/07/2002;3,0169
25/07/2002;2,9814
24/07/2002;2,9471
23/07/2002;2,9124
22/07/2002;2,8808
19/07/2002;2,8663
18/07/2002;2,8764
17/07/2002;2,8775
16/07/2002;2,8663
15/07/2002;2,8447
12/07/2002;2,8139
11/07/2002;2,8224
10/07/2002;2,8533
09/07/2002;2,8543
08/07/2002;2,8703
05/07/2002;2,8738
04/07/2002;2,8473
03/07/2002;2,8609
02/07/2002;2,9133
01/07/2002;2,8587
28/06/2002;2,8436
27/06/2002;2,8585
26/06/2002;2,8576
25/06/2002;2,7987
24/06/2002;2,8261
21/06/2002;2,7902
20/06/2002;2,7497
19/06/2002;2,7022
18/06/2002;2,6692
17/06/2002;2,6815
14/06/2002;2,7173
13/06/2002;2,6914
12/06/2002;2,7478
11/06/2002;2,6656
10/06/2002;2,6359
07/06/2002;2,6700
06/06/2002;2,6410
05/06/2002;2,6078
04/06/2002;2,5689
03/06/2002;2,5405
31/05/2002;2,5212
29/05/2002;2,5193
28/05/2002;2,5240
27/05/2002;2,5220
24/05/2002;2,5232
23/05/2002;2,5288
22/05/2002;2,5008
21/05/2002;2,4779
20/05/2002;2,4729
17/05/2002;2,4755
16/05/2002;2,4791
15/05/2002;2,5109
14/05/2002;2,5146
13/05/2002;2,4944
10/05/2002;2,4830
09/05/2002;2,4511
08/05/2002;2,4333
07/05/2002;2,4166
06/05/2002;2,4319
03/05/2002;2,4141
02/05/2002;2,3762
30/04/2002;2,3617
29/04/2002;2,3681
26/04/2002;2,3550
25/04/2002;2,3658
24/04/2002;2,3560
23/04/2002;2,3479
22/04/2002;2,3339
19/04/2002;2,3261
18/04/2002;2,3319
17/04/2002;2,3157
16/04/2002;2,3164
15/04/2002;2,3172
12/04/2002;2,2980
11/04/2002;2,2701
10/04/2002;2,2720
09/04/2002;2,2834
08/04/2002;2,2899
05/04/2002;2,2916
04/04/2002;2,3110
03/04/2002;2,2969
02/04/2002;2,3014
01/04/2002;2,3212
28/03/2002;2,3228
27/03/2002;2,3363
26/03/2002;2,3494
25/03/2002;2,3633
22/03/2002;2,3500
21/03/2002;2,3467
20/03/2002;2,3372
19/03/2002;2,3424
18/03/2002;2,3398
15/03/2002;2,3534
14/03/2002;2,3433
13/03/2002;2,3360
12/03/2002;2,3488
11/03/2002;2,3479
08/03/2002;2,3574
07/03/2002;2,3655
06/03/2002;2,3512
05/03/2002;2,3243
04/03/2002;2,3424
01/03/2002;2,3588
28/02/2002;2,3474
27/02/2002;2,3819
26/02/2002;2,3939
25/02/2002;2,4054
22/02/2002;2,4265
21/02/2002;2,4233
20/02/2002;2,4276
19/02/2002;2,4241
18/02/2002;2,4276
15/02/2002;2,4372
14/02/2002;2,4241
13/02/2002;2,4224
08/02/2002;2,4683
07/02/2002;2,4510
06/02/2002;2,4198
05/02/2002;2,4206
04/02/2002;2,4220
01/02/2002;2,4153
31/01/2002;2,4175
30/01/2002;2,4376
29/01/2002;2,4226
28/01/2002;2,4220
25/01/2002;2,4038
24/01/2002;2,3973
23/01/2002;2,3796
22/01/2002;2,3659
21/01/2002;2,3734
18/01/2002;2,3744
17/01/2002;2,3633
16/01/2002;2,3859
15/01/2002;2,3697
14/01/2002;2,4064
11/01/2002;2,4160
10/01/2002;2,3888
09/01/2002;2,3786
08/01/2002;2,3446
07/01/2002;2,3420
04/01/2002;2,3093
03/01/2002;2,2924
02/01/2002;2,3058
31/12/2001;2,3196
28/12/2001;2,3196
27/12/2001;2,3207
26/12/2001;2,3137
24/12/2001;2,3370
21/12/2001;2,3303
20/12/2001;2,3194
19/12/2001;2,2922
18/12/2001;2,3422
17/12/2001;2,3572
14/12/2001;2,3832
13/12/2001;2,3839
12/12/2001;2,3543
11/12/2001;2,3409
10/12/2001;2,3571
07/12/2001;2,3997
06/12/2001;2,4427
05/12/2001;2,4298
04/12/2001;2,4281
03/12/2001;2,4664
30/11/2001;2,5279
29/11/2001;2,5064
28/11/2001;2,4849
27/11/2001;2,4596
26/11/2001;2,4886
23/11/2001;2,5126
22/11/2001;2,5375
21/11/2001;2,5403
20/11/2001;2,5342
19/11/2001;2,5146
16/11/2001;2,5384
14/11/2001;2,5291
13/11/2001;2,5262
12/11/2001;2,5494
09/11/2001;2,5339
08/11/2001;2,5563
07/11/2001;2,6047
06/11/2001;2,5995
05/11/2001;2,6200
01/11/2001;2,6812
31/10/2001;2,7063
30/10/2001;2,7223
29/10/2001;2,7238
26/10/2001;2,7282
25/10/2001;2,7420
24/10/2001;2,7430
23/10/2001;2,7160
22/10/2001;2,7168
19/10/2001;2,7565
18/10/2001;2,7417
17/10/2001;2,7203
16/10/2001;2,7518
15/10/2001;2,7782
11/10/2001;2,7791
10/10/2001;2,7776
09/10/2001;2,7789
08/10/2001;2,7820
05/10/2001;2,7532
04/10/2001;2,7318
03/10/2001;2,7279
02/10/2001;2,7030
01/10/2001;2,6858
28/09/2001;2,6705
27/09/2001;2,7042
26/09/2001;2,7256
25/09/2001;2,7125
24/09/2001;2,7667
21/09/2001;2,7999
20/09/2001;2,7314
19/09/2001;2,7057
18/09/2001;2,6785
17/09/2001;2,6671
14/09/2001;2,6978
13/09/2001;2,6970
12/09/2001;2,6733
11/09/2001;2,6361
10/09/2001;2,6005
06/09/2001;2,5919
05/09/2001;2,5661
04/09/2001;2,5634
03/09/2001;2,5582
31/08/2001;2,5509
30/08/2001;2,5395
29/08/2001;2,5466
28/08/2001;2,5556
27/08/2001;2,5577
24/08/2001;2,5492
23/08/2001;2,5274
22/08/2001;2,5223
21/08/2001;2,5345
20/08/2001;2,5298
17/08/2001;2,5227
16/08/2001;2,4869
15/08/2001;2,4997
14/08/2001;2,5132
13/08/2001;2,4902
10/08/2001;2,4834
09/08/2001;2,4660
08/08/2001;2,4696
07/08/2001;2,4455
06/08/2001;2,4682
03/08/2001;2,4876
02/08/2001;2,4869
01/08/2001;2,4927
31/07/2001;2,4305
30/07/2001;2,4326
27/07/2001;2,4963
26/07/2001;2,4828
25/07/2001;2,4906
24/07/2001;2,4239
23/07/2001;2,4100
20/07/2001;2,4565
19/07/2001;2,5024
18/07/2001;2,4688
17/07/2001;2,5296
16/07/2001;2,5971
13/07/2001;2,5530
12/07/2001;2,5415
11/07/2001;2,5292
10/07/2001;2,4794
09/07/2001;2,4540
06/07/2001;2,4935
05/07/2001;2,4105
04/07/2001;2,3899
03/07/2001;2,3387
02/07/2001;2,3241
29/06/2001;2,3041
28/06/2001;2,2915
27/06/2001;2,3228
26/06/2001;2,3131
25/06/2001;2,2989
22/06/2001;2,3288
21/06/2001;2,4046
20/06/2001;2,4740
19/06/2001;2,4667
18/06/2001;2,4578
15/06/2001;2,4071
13/06/2001;2,4070
12/06/2001;2,3898
11/06/2001;2,3714
08/06/2001;2,3611
07/06/2001;2,3872
06/06/2001;2,3813
05/06/2001;2,3887
04/06/2001;2,3621
01/06/2001;2,3825
31/05/2001;2,3592
30/05/2001;2,3588
29/05/2001;2,3417
28/05/2001;2,3257
25/05/2001;2,3395
24/05/2001;2,3486
23/05/2001;2,3419
22/05/2001;2,3054
21/05/2001;2,3270
18/05/2001;2,2933
17/05/2001;2,3028
16/05/2001;2,3211
15/05/2001;2,3376
14/05/2001;2,3054
11/05/2001;2,2855
10/05/2001;2,2687
09/05/2001;2,2578
08/05/2001;2,2311
07/05/2001;2,1949
04/05/2001;2,2179
03/05/2001;2,2345
02/05/2001;2,2231
30/04/2001;2,1839
27/04/2001;2,2172
26/04/2001;2,2533
25/04/2001;2,3003
24/04/2001;2,2530
23/04/2001;2,2578
20/04/2001;2,2356
19/04/2001;2,1874
18/04/2001;2,1742
17/04/2001;2,1880
16/04/2001;2,1817
12/04/2001;2,1565
11/04/2001;2,1376
10/04/2001;2,1414
09/04/2001;2,1634
06/04/2001;2,1513
05/04/2001;2,1581
04/04/2001;2,1624
03/04/2001;2,1724
02/04/2001;2,1576
30/03/2001;2,1608
29/03/2001;2,1361
28/03/2001;2,1162
27/03/2001;2,1228
26/03/2001;2,1365
23/03/2001;2,1578
22/03/2001;2,1411
21/03/2001;2,0992
20/03/2001;2,0921
19/03/2001;2,1269
16/03/2001;2,1209
15/03/2001;2,0856
14/03/2001;2,0755
13/03/2001;2,0614
12/03/2001;2,0544
09/03/2001;2,0591
08/03/2001;2,0377
07/03/2001;2,0383
06/03/2001;2,0200
05/03/2001;2,0224
02/03/2001;2,0347
01/03/2001;2,0420
28/02/2001;2,0444
23/02/2001;2,0428
22/02/2001;2,0360
21/02/2001;2,0232
20/02/2001;2,0055
19/02/2001;2,0019
16/02/2001;1,9932
15/02/2001;1,9804
14/02/2001;1,9886
13/02/2001;1,9795
12/02/2001;1,9805
09/02/2001;1,9876
08/02/2001;1,9951
07/02/2001;2,0037
06/02/2001;1,9972
05/02/2001;1,9937
02/02/2001;1,9926
01/02/2001;1,9731
31/01/2001;1,9703
30/01/2001;1,9706
29/01/2001;1,9745
26/01/2001;1,9732
25/01/2001;1,9730
24/01/2001;1,9587
23/01/2001;1,9578
22/01/2001;1,9563
19/01/2001;1,9545
18/01/2001;1,9519
17/01/2001;1,9493
16/01/2001;1,9508
15/01/2001;1,9467
12/01/2001;1,9500
11/01/2001;1,9455
10/01/2001;1,9421
09/01/2001;1,9433
08/01/2001;1,9516
05/01/2001;1,9476
04/01/2001;1,9349
03/01/2001;1,9414
02/01/2001;1,9376
29/12/2000;1,9546
28/12/2000;1,9546
27/12/2000;1,9600
26/12/2000;1,9570
22/12/2000;1,9516
21/12/2000;1,9570
20/12/2000;1,9551
19/12/2000;1,9548
18/12/2000;1,9531
15/12/2000;1,9670
14/12/2000;1,9627
13/12/2000;1,9615
12/12/2000;1,9668
11/12/2000;1,9640
08/12/2000;1,9687
07/12/2000;1,9690
06/12/2000;1,9649
05/12/2000;1,9640
04/12/2000;1,9839
01/12/2000;1,9787
30/11/2000;1,9588
29/11/2000;1,9602
28/11/2000;1,9770
27/11/2000;1,9563
24/11/2000;1,9552
23/11/2000;1,9405
22/11/2000;1,9314
21/11/2000;1,9092
20/11/2000;1,9357
17/11/2000;1,9601
16/11/2000;1,9478
14/11/2000;1,9433
13/11/2000;1,9571
10/11/2000;1,9558
09/11/2000;1,9675
08/11/2000;1,9495
07/11/2000;1,9565
06/11/2000;1,9454
03/11/2000;1,9278
01/11/2000;1,9091
31/10/2000;1,9082
30/10/2000;1,9176
27/10/2000;1,9232
26/10/2000;1,9332
25/10/2000;1,9274
24/10/2000;1,8973
23/10/2000;1,8910
20/10/2000;1,8788
19/10/2000;1,8706
18/10/2000;1,8787
17/10/2000;1,8659
16/10/2000;1,8696
13/10/2000;1,8756
11/10/2000;1,8595
10/10/2000;1,8533
09/10/2000;1,8566
06/10/2000;1,8512
05/10/2000;1,8493
04/10/2000;1,8521
03/10/2000;1,8490
02/10/2000;1,8475
29/09/2000;1,8429
28/09/2000;1,8471
27/09/2000;1,8484
26/09/2000;1,8498
25/09/2000;1,8412
22/09/2000;1,8586
21/09/2000;1,8509
20/09/2000;1,8538
19/09/2000;1,8530
18/09/2000;1,8550
15/09/2000;1,8430
14/09/2000;1,8309
13/09/2000;1,8312
12/09/2000;1,8271
11/09/2000;1,8191
08/09/2000;1,8216
06/09/2000;1,8199
05/09/2000;1,8286
04/09/2000;1,8247
01/09/2000;1,8210
31/08/2000;1,8226
30/08/2000;1,8251
29/08/2000;1,8341
28/08/2000;1,8269
25/08/2000;1,8205
24/08/2000;1,8196
23/08/2000;1,8178
22/08/2000;1,8161
21/08/2000;1,8191
18/08/2000;1,8166
17/08/2000;1,8088
16/08/2000;1,8062
15/08/2000;1,8048
14/08/2000;1,8013
11/08/2000;1,7951
10/08/2000;1,7954
09/08/2000;1,7942
08/08/2000;1,7984
07/08/2000;1,7953
04/08/2000;1,7911
03/08/2000;1,8071
02/08/2000;1,7908
01/08/2000;1,7872
31/07/2000;1,7740
28/07/2000;1,7820
27/07/2000;1,7839
26/07/2000;1,7917
25/07/2000;1,7890
24/07/2000;1,7948
21/07/2000;1,7913
20/07/2000;1,8007
19/07/2000;1,8036
18/07/2000;1,7962
17/07/2000;1,7971
14/07/2000;1,8098
13/07/2000;1,8096
12/07/2000;1,8026
11/07/2000;1,7964
10/07/2000;1,7998
07/07/2000;1,7964
06/07/2000;1,7962
05/07/2000;1,8039
04/07/2000;1,8113
03/07/2000;1,8072
30/06/2000;1,7992
29/06/2000;1,8164
28/06/2000;1,8187
27/06/2000;1,8227
26/06/2000;1,8274
23/06/2000;1,8195
21/06/2000;1,8113
20/06/2000;1,7983
19/06/2000;1,8022
16/06/2000;1,8065
15/06/2000;1,8071
14/06/2000;1,8099
13/06/2000;1,8092
12/06/2000;1,8032
09/06/2000;1,7991
08/06/2000;1,7940
07/06/2000;1,8028
06/06/2000;1,7891
05/06/2000;1,7925
02/06/2000;1,8096
01/06/2000;1,8194
31/05/2000;1,8258
30/05/2000;1,8297
29/05/2000;1,8380
26/05/2000;1,8447
25/05/2000;1,8384
24/05/2000;1,8529
23/05/2000;1,8529
22/05/2000;1,8460
19/05/2000;1,8446
18/05/2000;1,8297
17/05/2000;1,8284
16/05/2000;1,8190
15/05/2000;1,8374
12/05/2000;1,8258
11/05/2000;1,8154
10/05/2000;1,8161
09/05/2000;1,8071
08/05/2000;1,8050
05/05/2000;1,8110
04/05/2000;1,8136
03/05/2000;1,8154
02/05/2000;1,8000
28/04/2000;1,8059
27/04/2000;1,8075
26/04/2000;1,7977
25/04/2000;1,7880
24/04/2000;1,7908
20/04/2000;1,7776
19/04/2000;1,7654
18/04/2000;1,7688
17/04/2000;1,7865
14/04/2000;1,7825
13/04/2000;1,7625
12/04/2000;1,7463
11/04/2000;1,7440
10/04/2000;1,7379
07/04/2000;1,7431
06/04/2000;1,7415
05/04/2000;1,7524
04/04/2000;1,7417
03/04/2000;1,7399
31/03/2000;1,7465
30/03/2000;1,7514
29/03/2000;1,7371
28/03/2000;1,7448
27/03/2000;1,7354
24/03/2000;1,7226
23/03/2000;1,7234
22/03/2000;1,7297
21/03/2000;1,7373
20/03/2000;1,7380
17/03/2000;1,7399
16/03/2000;1,7349
15/03/2000;1,7423
14/03/2000;1,7364
13/03/2000;1,7494
10/03/2000;1,7378
09/03/2000;1,7335
08/03/2000;1,7490
03/03/2000;1,7503
02/03/2000;1,7592
01/03/2000;1,7670
29/02/2000;1,7677
28/02/2000;1,7780
25/02/2000;1,7733
24/02/2000;1,7771
23/02/2000;1,7878
22/02/2000;1,7817
21/02/2000;1,7776
18/02/2000;1,7697
17/02/2000;1,7732
16/02/2000;1,7724
15/02/2000;1,7756
14/02/2000;1,7691
11/02/2000;1,7639
10/02/2000;1,7687
09/02/2000;1,7624
08/02/2000;1,7646
07/02/2000;1,7651
04/02/2000;1,7777
03/02/2000;1,7771
02/02/2000;1,7892
01/02/2000;1,7924
31/01/2000;1,8016
28/01/2000;1,7867
27/01/2000;1,7745
26/01/2000;1,7761
25/01/2000;1,7733
24/01/2000;1,7644
21/01/2000;1,7776
20/01/2000;1,7793
19/01/2000;1,7976
18/01/2000;1,7916
17/01/2000;1,7949
14/01/2000;1,7989
13/01/2000;1,8185
12/01/2000;1,8306
11/01/2000;1,8211
10/01/2000;1,8153
07/01/2000;1,8273
06/01/2000;1,8453
05/01/2000;1,8536
04/01/2000;1,8329
03/01/2000;1,8003
31/12/1999;1,7882
30/12/1999;1,7882
29/12/1999;1,8162
28/12/1999;1,8281
27/12/1999;1,8259
24/12/1999;1,8282
23/12/1999;1,8278
22/12/1999;1,8196
21/12/1999;1,8226
20/12/1999;1,8040
17/12/1999;1,8170
16/12/1999;1,8399
15/12/1999;1,8493
14/12/1999;1,8455
13/12/1999;1,8556
10/12/1999;1,8659
09/12/1999;1,8660
08/12/1999;1,8619
07/12/1999;1,8586
06/12/1999;1,8661
03/12/1999;1,8766
02/12/1999;1,8942
01/12/1999;1,9213
30/11/1999;1,9219
29/11/1999;1,9205
26/11/1999;1,9255
25/11/1999;1,9292
24/11/1999;1,9287
23/11/1999;1,9320
22/11/1999;1,9314
19/11/1999;1,9305
18/11/1999;1,9282
17/11/1999;1,9319
16/11/1999;1,9323
12/11/1999;1,9323
11/11/1999;1,9280
10/11/1999;1,9340
09/11/1999;1,9233
08/11/1999;1,9258
05/11/1999;1,9147
04/11/1999;1,9287
03/11/1999;1,9406
01/11/1999;1,9423
29/10/1999;1,9522
28/10/1999;1,9781
27/10/1999;1,9946
26/10/1999;1,9861
25/10/1999;1,9769
22/10/1999;1,9826
21/10/1999;1,9928
20/10/1999;2,0017
19/10/1999;1,9925
18/10/1999;1,9821
15/10/1999;1,9786
14/10/1999;1,9640
13/10/1999;1,9579
11/10/1999;1,9542
08/10/1999;1,9422
07/10/1999;1,9331
06/10/1999;1,9592
05/10/1999;1,9517
04/10/1999;1,9380
01/10/1999;1,9557
30/09/1999;1,9215
29/09/1999;1,9216
28/09/1999;1,9385
27/09/1999;1,9166
24/09/1999;1,9136
23/09/1999;1,8906
22/09/1999;1,8898
21/09/1999;1,8783
20/09/1999;1,8737
17/09/1999;1,8853
16/09/1999;1,8786
15/09/1999;1,8771
14/09/1999;1,8915
13/09/1999;1,8814
10/09/1999;1,8613
09/09/1999;1,8727
08/09/1999;1,8975
06/09/1999;1,9051
03/09/1999;1,9032
02/09/1999;1,9236
01/09/1999;1,9209
31/08/1999;1,9151
30/08/1999;1,9428
27/08/1999;1,9235
26/08/1999;1,9079
25/08/1999;1,9303
24/08/1999;1,9018
23/08/1999;1,8698
20/08/1999;1,9489
19/08/1999;1,9163
18/08/1999;1,8919
17/08/1999;1,8812
16/08/1999;1,8760
13/08/1999;1,8703
12/08/1999;1,8503
11/08/1999;1,8622
10/08/1999;1,8721
09/08/1999;1,8446
06/08/1999;1,8485
05/08/1999;1,8468
04/08/1999;1,8209
03/08/1999;1,8270
02/08/1999;1,8107
30/07/1999;1,7884
29/07/1999;1,7931
28/07/1999;1,7907
27/07/1999;1,8165
26/07/1999;1,8195
23/07/1999;1,8139
22/07/1999;1,8163
21/07/1999;1,8163
20/07/1999;1,7974
19/07/1999;1,7921
16/07/1999;1,8099
15/07/1999;1,8273
14/07/1999;1,8101
13/07/1999;1,8384
12/07/1999;1,8182
09/07/1999;1,8036
08/07/1999;1,7903
07/07/1999;1,7807
06/07/1999;1,7746
05/07/1999;1,7655
02/07/1999;1,7698
01/07/1999;1,7567
30/06/1999;1,7687
29/06/1999;1,7664
28/06/1999;1,7892
25/06/1999;1,7896
24/06/1999;1,7995
23/06/1999;1,7840
22/06/1999;1,7680
21/06/1999;1,7628
18/06/1999;1,7477
17/06/1999;1,7597
16/06/1999;1,7667
15/06/1999;1,7884
14/06/1999;1,7775
11/06/1999;1,7722
10/06/1999;1,7589
09/06/1999;1,7483
08/06/1999;1,7471
07/06/1999;1,7404
04/06/1999;1,7357
02/06/1999;1,7534
01/06/1999;1,7328
31/05/1999;1,7232
28/05/1999;1,7303
27/05/1999;1,7129
26/05/1999;1,7178
25/05/1999;1,7472
24/05/1999;1,6977
21/05/1999;1,6955
20/05/1999;1,6826
19/05/1999;1,6628
18/05/1999;1,6651
17/05/1999;1,6662
14/05/1999;1,6562
13/05/1999;1,6502
12/05/1999;1,6606
11/05/1999;1,6460
10/05/1999;1,6510
07/05/1999;1,6704
06/05/1999;1,6721
05/05/1999;1,6839
04/05/1999;1,6726
03/05/1999;1,6727
30/04/1999;1,6599
29/04/1999;1,6668
28/04/1999;1,6955
27/04/1999;1,7061
26/04/1999;1,6970
23/04/1999;1,6843
22/04/1999;1,7006
20/04/1999;1,7093
19/04/1999;1,6713
16/04/1999;1,6692
15/04/1999;1,6680
14/04/1999;1,6567
13/04/1999;1,6712
12/04/1999;1,7046
09/04/1999;1,7082
08/04/1999;1,7198
07/04/1999;1,7287
06/04/1999;1,7306
05/04/1999;1,7243
31/03/1999;1,7212
30/03/1999;1,7326
29/03/1999;1,7647
26/03/1999;1,7742
25/03/1999;1,8092
24/03/1999;1,8420
23/03/1999;1,8508
22/03/1999;1,8607
19/03/1999;1,8499
18/03/1999;1,8588
17/03/1999;1,8769
16/03/1999;1,8513
15/03/1999;1,8817
12/03/1999;1,9043
11/03/1999;1,8776
10/03/1999;1,8623
09/03/1999;1,9048
08/03/1999;1,9700
05/03/1999;1,9926
04/03/1999;2,1014
03/03/1999;2,1639
02/03/1999;2,1300
01/03/1999;2,0276
26/02/1999;2,0640
25/02/1999;2,0343
24/02/1999;2,0025
23/02/1999;2,0120
22/02/1999;1,9348
19/02/1999;1,9200
18/02/1999;1,9021
17/02/1999;1,9171
12/02/1999;1,8976
11/02/1999;1,8860
10/02/1999;1,8945
09/02/1999;1,9325
08/02/1999;1,8601
05/02/1999;1,8309
04/02/1999;1,8132
03/02/1999;1,7701
02/02/1999;1,7972
01/02/1999;1,9630
29/01/1999;1,9824
28/01/1999;1,9198
27/01/1999;1,8878
26/01/1999;1,8762
25/01/1999;1,7598
22/01/1999;1,7041
21/01/1999;1,6594
20/01/1999;1,5727
19/01/1999;1,5572
18/01/1999;1,5376
15/01/1999;1,4651
14/01/1999;1,3186
13/01/1999;1,3185
12/01/1999;1,2106
11/01/1999;1,2101
08/01/1999;1,2096
07/01/1999;1,2093
06/01/1999;1,2088
05/01/1999;1,2077
04/01/1999;1,2070
31/12/1998;1,2079
30/12/1998;1,2075
29/12/1998;1,2076
28/12/1998;1,2076
24/12/1998;1,2071
23/12/1998;1,2070
22/12/1998;1,2066
21/12/1998;1,2061
18/12/1998;1,2060
17/12/1998;1,2057
16/12/1998;1,2045
15/12/1998;1,2044
14/12/1998;1,2040
11/12/1998;1,2032
10/12/1998;1,2026
09/12/1998;1,2029
08/12/1998;1,2027
07/12/1998;1,2021
04/12/1998;1,2018
03/12/1998;1,2015
02/12/1998;1,2005
01/12/1998;1,2008
30/11/1998;1,2004
27/11/1998;1,1995
26/11/1998;1,1984
25/11/1998;1,1974
24/11/1998;1,1970
23/11/1998;1,1966
20/11/1998;1,1942
19/11/1998;1,1924
18/11/1998;1,1905
17/11/1998;1,1901
16/11/1998;1,1901
13/11/1998;1,1907
12/11/1998;1,1905
11/11/1998;1,1900
10/11/1998;1,1903
09/11/1998;1,1891
06/11/1998;1,1876
05/11/1998;1,1897
04/11/1998;1,1908
03/11/1998;1,1921
30/10/1998;1,1924
29/10/1998;1,1914
28/10/1998;1,1916
27/10/1998;1,1914
26/10/1998;1,1905
23/10/1998;1,1903
22/10/1998;1,1897
21/10/1998;1,1891
20/10/1998;1,1888
19/10/1998;1,1891
16/10/1998;1,1878
15/10/1998;1,1878
14/10/1998;1,1880
13/10/1998;1,1869
09/10/1998;1,1859
08/10/1998;1,1838
07/10/1998;1,1823
06/10/1998;1,1841
05/10/1998;1,1852
02/10/1998;1,1829
01/10/1998;1,1799
30/09/1998;1,1848
29/09/1998;1,1842
28/09/1998;1,1841
25/09/1998;1,1840
24/09/1998;1,1827
23/09/1998;1,1830
22/09/1998;1,1822
21/09/1998;1,1808
18/09/1998;1,1800
17/09/1998;1,1793
16/09/1998;1,1788
15/09/1998;1,1790
14/09/1998;1,1795
11/09/1998;1,1785
10/09/1998;1,1786
09/09/1998;1,1784
08/09/1998;1,1761
04/09/1998;1,1776
03/09/1998;1,1772
02/09/1998;1,1766
01/09/1998;1,1764
31/08/1998;1,1761
28/08/1998;1,1755
27/08/1998;1,1745
26/08/1998;1,1720
25/08/1998;1,1739
24/08/1998;1,1742
21/08/1998;1,1745
20/08/1998;1,1730
19/08/1998;1,1734
18/08/1998;1,1731
17/08/1998;1,1722
14/08/1998;1,1708
13/08/1998;1,1708
12/08/1998;1,1692
11/08/1998;1,1681
10/08/1998;1,1684
07/08/1998;1,1675
06/08/1998;1,1673
05/08/1998;1,1663
04/08/1998;1,1651
03/08/1998;1,1635
31/07/1998;1,1626
30/07/1998;1,1616
29/07/1998;1,1624
28/07/1998;1,1627
27/07/1998;1,1653
24/07/1998;1,1647
23/07/1998;1,1639
22/07/1998;1,1612
21/07/1998;1,1602
20/07/1998;1,1599
17/07/1998;1,1609
16/07/1998;1,1613
15/07/1998;1,1607
14/07/1998;1,1626
13/07/1998;1,1611
10/07/1998;1,1604
09/07/1998;1,1604
08/07/1998;1,1589
07/07/1998;1,1581
06/07/1998;1,1575
03/07/1998;1,1567
02/07/1998;1,1564
01/07/1998;1,1564
30/06/1998;1,1561
29/06/1998;1,1558
26/06/1998;1,1556
25/06/1998;1,1553
24/06/1998;1,1551
23/06/1998;1,1547
22/06/1998;1,1546
19/06/1998;1,1554
18/06/1998;1,1549
17/06/1998;1,1545
16/06/1998;1,1541
15/06/1998;1,1543
12/06/1998;1,1545
10/06/1998;1,1538
09/06/1998;1,1528
08/06/1998;1,1521
05/06/1998;1,1516
04/06/1998;1,1509
03/06/1998;1,1510
02/06/1998;1,1509
01/06/1998;1,1512
29/05/1998;1,1497
28/05/1998;1,1492
27/05/1998;1,1512
26/05/1998;1,1523
25/05/1998;1,1508
22/05/1998;1,1507
21/05/1998;1,1489
20/05/1998;1,1481
19/05/1998;1,1480
18/05/1998;1,1467
15/05/1998;1,1464
14/05/1998;1,1465
13/05/1998;1,1466
12/05/1998;1,1455
11/05/1998;1,1451
08/05/1998;1,1447
07/05/1998;1,1443
06/05/1998;1,1444
05/05/1998;1,1441
04/05/1998;1,1434
30/04/1998;1,1435
29/04/1998;1,1445
28/04/1998;1,1441
27/04/1998;1,1433
24/04/1998;1,1427
23/04/1998;1,1420
22/04/1998;1,1417
20/04/1998;1,1410
17/04/1998;1,1406
16/04/1998;1,1401
15/04/1998;1,1399
14/04/1998;1,1396
13/04/1998;1,1389
08/04/1998;1,1386
07/04/1998;1,1380
06/04/1998;1,1380
03/04/1998;1,1376
02/04/1998;1,1367
01/04/1998;1,1367
31/03/1998;1,1366
30/03/1998;1,1357
27/03/1998;1,1356
26/03/1998;1,1352
25/03/1998;1,1350
24/03/1998;1,1344
23/03/1998;1,1341
20/03/1998;1,1338
19/03/1998;1,1336
18/03/1998;1,1336
17/03/1998;1,1327
16/03/1998;1,1327
13/03/1998;1,1326
12/03/1998;1,1320
11/03/1998;1,1317
10/03/1998;1,1316
09/03/1998;1,1315
06/03/1998;1,1307
05/03/1998;1,1306
04/03/1998;1,1306
03/03/1998;1,1298
02/03/1998;1,1297
27/02/1998;1,1296
26/02/1998;1,1290
25/02/1998;1,1289
20/02/1998;1,1287
19/02/1998;1,1284
18/02/1998;1,1278
17/02/1998;1,1276
16/02/1998;1,1266
13/02/1998;1,1268
12/02/1998;1,1260
11/02/1998;1,1257
10/02/1998;1,1256
09/02/1998;1,1247
06/02/1998;1,1246
05/02/1998;1,1237
04/02/1998;1,1237
03/02/1998;1,1236
02/02/1998;1,1228
30/01/1998;1,1229
29/01/1998;1,1222
28/01/1998;1,1219
27/01/1998;1,1216
26/01/1998;1,1208
23/01/1998;1,1207
22/01/1998;1,1198
21/01/1998;1,1199
20/01/1998;1,1197
19/01/1998;1,1193
16/01/1998;1,1197
15/01/1998;1,1198
14/01/1998;1,1182
13/01/1998;1,1179
12/01/1998;1,1184
09/01/1998;1,1176
08/01/1998;1,1172
07/01/1998;1,1167
06/01/1998;1,1161
05/01/1998;1,1157
02/01/1998;1,1157
31/12/1997;1,1156
30/12/1997;1,1156
29/12/1997;1,1149
26/12/1997;1,1143
24/12/1997;1,1142
23/12/1997;1,1142
22/12/1997;1,1143
19/12/1997;1,1140
18/12/1997;1,1136
17/12/1997;1,1133
16/12/1997;1,1126
15/12/1997;1,1135
12/12/1997;1,1154
11/12/1997;1,1143
10/12/1997;1,1121
09/12/1997;1,1114
08/12/1997;1,1111
05/12/1997;1,1097
04/12/1997;1,1098
03/12/1997;1,1096
02/12/1997;1,1088
01/12/1997;1,1088
28/11/1997;1,1090
27/11/1997;1,1081
26/11/1997;1,1096
25/11/1997;1,1096
24/11/1997;1,1089
21/11/1997;1,1086
20/11/1997;1,1073
19/11/1997;1,1073
18/11/1997;1,1058
17/11/1997;1,1059
14/11/1997;1,1074
13/11/1997;1,1062
12/11/1997;1,1056
11/11/1997;1,1042
10/11/1997;1,1045
07/11/1997;1,1074
06/11/1997;1,1061
05/11/1997;1,1033
04/11/1997;1,1033
03/11/1997;1,1022
31/10/1997;1,1023
30/10/1997;1,1055
29/10/1997;1,1016
28/10/1997;1,1056
27/10/1997;1,1019
24/10/1997;1,1004
23/10/1997;1,1001
22/10/1997;1,1000
21/10/1997;1,0996
20/10/1997;1,0995
17/10/1997;1,0992
16/10/1997;1,0988
15/10/1997;1,0986
14/10/1997;1,0980
13/10/1997;1,0977
10/10/1997;1,0977
09/10/1997;1,0974
08/10/1997;1,0971
07/10/1997;1,0969
06/10/1997;1,0966
03/10/1997;1,0963
02/10/1997;1,0962
01/10/1997;1,0959
30/09/1997;1,0956
29/09/1997;1,0954
26/09/1997;1,0953
25/09/1997;1,0947
24/09/1997;1,0946
23/09/1997;1,0944
22/09/1997;1,0941
19/09/1997;1,0935
18/09/1997;1,0934
17/09/1997;1,0930
16/09/1997;1,0924
15/09/1997;1,0919
12/09/1997;1,0917
11/09/1997;1,0914
10/09/1997;1,0910
09/09/1997;1,0907
08/09/1997;1,0908
05/09/1997;1,0921
04/09/1997;1,0917
03/09/1997;1,0917
02/09/1997;1,0914
01/09/1997;1,0906
29/08/1997;1,0908
28/08/1997;1,0908
27/08/1997;1,0914
26/08/1997;1,0917
25/08/1997;1,0912
22/08/1997;1,0904
21/08/1997;1,0880
20/08/1997;1,0882
19/08/1997;1,0886
18/08/1997;1,0877
15/08/1997;1,0865
14/08/1997;1,0856
13/08/1997;1,0855
12/08/1997;1,0851
11/08/1997;1,0850
08/08/1997;1,0850
07/08/1997;1,0843
06/08/1997;1,0837
05/08/1997;1,0835
04/08/1997;1,0827
01/08/1997;1,0827
31/07/1997;1,0826
30/07/1997;1,0826
29/07/1997;1,0825
28/07/1997;1,0819
25/07/1997;1,0816
24/07/1997;1,0814
23/07/1997;1,0815
22/07/1997;1,0809
21/07/1997;1,0807
18/07/1997;1,0808
17/07/1997;1,0804
16/07/1997;1,0803
15/07/1997;1,0800
14/07/1997;1,0798
11/07/1997;1,0795
10/07/1997;1,0789
09/07/1997;1,0788
08/07/1997;1,0782
07/07/1997;1,0773
04/07/1997;1,0771
03/07/1997;1,0770
02/07/1997;1,0765
01/07/1997;1,0763
30/06/1997;1,0761
27/06/1997;1,0764
26/06/1997;1,0760
25/06/1997;1,0761
24/06/1997;1,0762
23/06/1997;1,0761
20/06/1997;1,0769
19/06/1997;1,0749
18/06/1997;1,0742
17/06/1997;1,0733
16/06/1997;1,0733
13/06/1997;1,0737
12/06/1997;1,0730
11/06/1997;1,0726
10/06/1997;1,0721
09/06/1997;1,0722
06/06/1997;1,0720
05/06/1997;1,0720
04/06/1997;1,0718
03/06/1997;1,0707
02/06/1997;1,0701
30/05/1997;1,0709
28/05/1997;1,0724
27/05/1997;1,0720
26/05/1997;1,0713
23/05/1997;1,0701
22/05/1997;1,0690
21/05/1997;1,0681
20/05/1997;1,0677
19/05/1997;1,0672
16/05/1997;1,0669
15/05/1997;1,0670
14/05/1997;1,0675
13/05/1997;1,0672
12/05/1997;1,0665
09/05/1997;1,0652
08/05/1997;1,0643
07/05/1997;1,0645
06/05/1997;1,0642
05/05/1997;1,0639
02/05/1997;1,0635
30/04/1997;1,0630
29/04/1997;1,0625
28/04/1997;1,0624
25/04/1997;1,0624
24/04/1997;1,0623
23/04/1997;1,0625
22/04/1997;1,0621
18/04/1997;1,0610
17/04/1997;1,0605
16/04/1997;1,0603
15/04/1997;1,0598
14/04/1997;1,0592
11/04/1997;1,0587
10/04/1997;1,0581
09/04/1997;1,0582
08/04/1997;1,0580
07/04/1997;1,0582
04/04/1997;1,0577
03/04/1997;1,0576
02/04/1997;1,0590
01/04/1997;1,0586
31/03/1997;1,0585
26/03/1997;1,0601
25/03/1997;1,0604
24/03/1997;1,0607
21/03/1997;1,0603
20/03/1997;1,0594
19/03/1997;1,0597
18/03/1997;1,0581
17/03/1997;1,0574
14/03/1997;1,0546
13/03/1997;1,0549
12/03/1997;1,0536
11/03/1997;1,0531
10/03/1997;1,0524
07/03/1997;1,0524
06/03/1997;1,0522
05/03/1997;1,0518
04/03/1997;1,0509
03/03/1997;1,0507
28/02/1997;1,0507
27/02/1997;1,0507
26/02/1997;1,0509
25/02/1997;1,0503
24/02/1997;1,0499
21/02/1997;1,0500
20/02/1997;1,0497
19/02/1997;1,0496
18/02/1997;1,0487
17/02/1997;1,0483
14/02/1997;1,0487
13/02/1997;1,0479
12/02/1997;1,0468
07/02/1997;1,0472
06/02/1997;1,0464
05/02/1997;1,0462
04/02/1997;1,0455
03/02/1997;1,0449
31/01/1997;1,0453
30/01/1997;1,0449
29/01/1997;1,0448
28/01/1997;1,0441
27/01/1997;1,0433
24/01/1997;1,0433
23/01/1997;1,0430
22/01/1997;1,0428
21/01/1997;1,0427
20/01/1997;1,0424
17/01/1997;1,0431
16/01/1997;1,0428
15/01/1997;1,0418
14/01/1997;1,0414
13/01/1997;1,0412
10/01/1997;1,0406
09/01/1997;1,0407
08/01/1997;1,0402
07/01/1997;1,0397
06/01/1997;1,0397
03/01/1997;1,0390
02/01/1997;1,0387
31/12/1996;1,0386
30/12/1996;1,0386
27/12/1996;1,0392
26/12/1996;1,0381
24/12/1996;1,0382
23/12/1996;1,0380
20/12/1996;1,0379
19/12/1996;1,0376
18/12/1996;1,0375
17/12/1996;1,0399
16/12/1996;1,0381
13/12/1996;1,0373
12/12/1996;1,0368
11/12/1996;1,0361
10/12/1996;1,0351
09/12/1996;1,0342
06/12/1996;1,0343
05/12/1996;1,0338
04/12/1996;1,0330
03/12/1996;1,0323
02/12/1996;1,0323
29/11/1996;1,0324
28/11/1996;1,0320
27/11/1996;1,0316
26/11/1996;1,0312
25/11/1996;1,0303
22/11/1996;1,0303
21/11/1996;1,0303
20/11/1996;1,0300
19/11/1996;1,0295
18/11/1996;1,0296
14/11/1996;1,0297
13/11/1996;1,0301
12/11/1996;1,0303
11/11/1996;1,0289
08/11/1996;1,0287
07/11/1996;1,0280
06/11/1996;1,0272
05/11/1996;1,0272
04/11/1996;1,0272
01/11/1996;1,0272
31/10/1996;1,0268
30/10/1996;1,0267
29/10/1996;1,0277
28/10/1996;1,0271
25/10/1996;1,0264
24/10/1996;1,0256
23/10/1996;1,0262
22/10/1996;1,0255
21/10/1996;1,0246
18/10/1996;1,0244
17/10/1996;1,0242
16/10/1996;1,0245
15/10/1996;1,0243
14/10/1996;1,0239
11/10/1996;1,0246
10/10/1996;1,0239
09/10/1996;1,0225
08/10/1996;1,0217
07/10/1996;1,0217
04/10/1996;1,0212
02/10/1996;1,0207
01/10/1996;1,0207
30/09/1996;1,0207
27/09/1996;1,0202
26/09/1996;1,0197
25/09/1996;1,0197
24/09/1996;1,0194
23/09/1996;1,0194
20/09/1996;1,0191
19/09/1996;1,0188
18/09/1996;1,0188
17/09/1996;1,0187
16/09/1996;1,0184
13/09/1996;1,0192
12/09/1996;1,0189
11/09/1996;1,0180
10/09/1996;1,0194
09/09/1996;1,0182
06/09/1996;1,0171
05/09/1996;1,0166
04/09/1996;1,0164
03/09/1996;1,0159
02/09/1996;1,0157
30/08/1996;1,0161
29/08/1996;1,0159
28/08/1996;1,0153
27/08/1996;1,0151
26/08/1996;1,0147
23/08/1996;1,0145
22/08/1996;1,0140
21/08/1996;1,0139
20/08/1996;1,0136
19/08/1996;1,0128
16/08/1996;1,0127
15/08/1996;1,0122
14/08/1996;1,0121
13/08/1996;1,0118
12/08/1996;1,0114
09/08/1996;1,0111
08/08/1996;1,0107
07/08/1996;1,0108
06/08/1996;1,0099
05/08/1996;1,0093
02/08/1996;1,0096
01/08/1996;1,0100
31/07/1996;1,0104
30/07/1996;1,0099
29/07/1996;1,0091
26/07/1996;1,0084
25/07/1996;1,0079
24/07/1996;1,0078
23/07/1996;1,0070
22/07/1996;1,0069
19/07/1996;1,0067
18/07/1996;1,0063
17/07/1996;1,0058
16/07/1996;1,0057
15/07/1996;1,0054
12/07/1996;1,0048
11/07/1996;1,0048
10/07/1996;1,0049
09/07/1996;1,0047
08/07/1996;1,0041
05/07/1996;1,0040
04/07/1996;1,0041
03/07/1996;1,0043
02/07/1996;1,0044
01/07/1996;1,0037
28/06/1996;1,0036
27/06/1996;1,0028
26/06/1996;1,0031
25/06/1996;1,0021
24/06/1996;1,0022
21/06/1996;1,0022
20/06/1996;1,0017
19/06/1996;1,0012
18/06/1996;1,0008
17/06/1996;1,0008
14/06/1996;1,0007
13/06/1996;0,9997
12/06/1996;0,9999
11/06/1996;0,9988
10/06/1996;0,9990
07/06/1996;0,9981
05/06/1996;0,9979
04/06/1996;0,9977
03/06/1996;0,9978
31/05/1996;0,9976
30/05/1996;0,9963
29/05/1996;0,9959
28/05/1996;0,9957
27/05/1996;0,9958
24/05/1996;0,9960
23/05/1996;0,9954
22/05/1996;0,9950
21/05/1996;0,9948
20/05/1996;0,9948
17/05/1996;0,9950
16/05/1996;0,9957
15/05/1996;0,9950
14/05/1996;0,9952
13/05/1996;0,9943
10/05/1996;0,9938
09/05/1996;0,9931
08/05/1996;0,9920
07/05/1996;0,9919
06/05/1996;0,9918
03/05/1996;0,9918
02/05/1996;0,9917
30/04/1996;0,9917
29/04/1996;0,9918
26/04/1996;0,9914
25/04/1996;0,9909
24/04/1996;0,9908
23/04/1996;0,9907
22/04/1996;0,9908
19/04/1996;0,9907
18/04/1996;0,9888
17/04/1996;0,9892
16/04/1996;0,9895
15/04/1996;0,9891
12/04/1996;0,9897
11/04/1996;0,9900
10/04/1996;0,9888
09/04/1996;0,9878
08/04/1996;0,9867
04/04/1996;0,9866
03/04/1996;0,9866
02/04/1996;0,9867
01/04/1996;0,9873
29/03/1996;0,9872
28/03/1996;0,9873
27/03/1996;0,9875
26/03/1996;0,9873
25/03/1996;0,9871
22/03/1996;0,9867
21/03/1996;0,9866
20/03/1996;0,9875
19/03/1996;0,9860
18/03/1996;0,9858
15/03/1996;0,9860
14/03/1996;0,9861
13/03/1996;0,9846
12/03/1996;0,9834
11/03/1996;0,9835
08/03/1996;0,9835
07/03/1996;0,9837
06/03/1996;0,9829
05/03/1996;0,9829
04/03/1996;0,9829
01/03/1996;0,9832
29/02/1996;0,9832
28/02/1996;0,9828
27/02/1996;0,9830
26/02/1996;0,9826
23/02/1996;0,9812
22/02/1996;0,9814
21/02/1996;0,9813
16/02/1996;0,9822
15/02/1996;0,9824
14/02/1996;0,9803
13/02/1996;0,9796
12/02/1996;0,9777
09/02/1996;0,9778
08/02/1996;0,9777
07/02/1996;0,9778
06/02/1996;0,9776
05/02/1996;0,9777
02/02/1996;0,9776
01/02/1996;0,9776
31/01/1996;0,9776
30/01/1996;0,9777
29/01/1996;0,9778
26/01/1996;0,9774
25/01/1996;0,9758
24/01/1996;0,9759
23/01/1996;0,9756
22/01/1996;0,9736
19/01/1996;0,9722
18/01/1996;0,9719
17/01/1996;0,9717
16/01/1996;0,9716
15/01/1996;0,9717
12/01/1996;0,9724
11/01/1996;0,9720
10/01/1996;0,9716
09/01/1996;0,9716
08/01/1996;0,9716
05/01/1996;0,9717
04/01/1996;0,9718
03/01/1996;0,9717
02/01/1996;0,9716
29/12/1995;0,9715
28/12/1995;0,9716
27/12/1995;0,9699
26/12/1995;0,9692
22/12/1995;0,9692
21/12/1995;0,9684
20/12/1995;0,9677
19/12/1995;0,9666
18/12/1995;0,9671
15/12/1995;0,9667
14/12/1995;0,9663
13/12/1995;0,9661
12/12/1995;0,9658
11/12/1995;0,9657
08/12/1995;0,9657
07/12/1995;0,9656
06/12/1995;0,9657
05/12/1995;0,9657
04/12/1995;0,9656
01/12/1995;0,9656
30/11/1995;0,9656
29/11/1995;0,9637
28/11/1995;0,9638
27/11/1995;0,9639
24/11/1995;0,9645
23/11/1995;0,9637
22/11/1995;0,9638
21/11/1995;0,9629
20/11/1995;0,9616
17/11/1995;0,9614
16/11/1995;0,9618
14/11/1995;0,9618
13/11/1995;0,9610
10/11/1995;0,9607
09/11/1995;0,9607
08/11/1995;0,9608
07/11/1995;0,9608
06/11/1995;0,9613
03/11/1995;0,9617
01/11/1995;0,9620
31/10/1995;0,9609
30/10/1995;0,9607
27/10/1995;0,9612
26/10/1995;0,9610
25/10/1995;0,9607
24/10/1995;0,9607
23/10/1995;0,9605
20/10/1995;0,9603
19/10/1995;0,9583
18/10/1995;0,9580
17/10/1995;0,9575
16/10/1995;0,9575
13/10/1995;0,9575
11/10/1995;0,9575
10/10/1995;0,9575
09/10/1995;0,9575
06/10/1995;0,9580
05/10/1995;0,9575
04/10/1995;0,9575
03/10/1995;0,9575
02/10/1995;0,9545
29/09/1995;0,9520
28/09/1995;0,9540
27/09/1995;0,9540
26/09/1995;0,9530
25/09/1995;0,9520
22/09/1995;0,9520
21/09/1995;0,9520
20/09/1995;0,9520
19/09/1995;0,9510
18/09/1995;0,9510
15/09/1995;0,9510
14/09/1995;0,9510
13/09/1995;0,9510
12/09/1995;0,9500
11/09/1995;0,9500
08/09/1995;0,9490
06/09/1995;0,9470
05/09/1995;0,9470
04/09/1995;0,9470
01/09/1995;0,9490
31/08/1995;0,9490
30/08/1995;0,9490
29/08/1995;0,9490
28/08/1995;0,9470
25/08/1995;0,9460
24/08/1995;0,9450
23/08/1995;0,9450
22/08/1995;0,9420
21/08/1995;0,9400
18/08/1995;0,9410
17/08/1995;0,9400
16/08/1995;0,9400
15/08/1995;0,9400
14/08/1995;0,9390
11/08/1995;0,9350
10/08/1995;0,9340
09/08/1995;0,9340
08/08/1995;0,9340
07/08/1995;0,9340
04/08/1995;0,9340
03/08/1995;0,9340
02/08/1995;0,9340
01/08/1995;0,9340
31/07/1995;0,9340
28/07/1995;0,9350
27/07/1995;0,9350
26/07/1995;0,9340
25/07/1995;0,9340
24/07/1995;0,9320
21/07/1995;0,9320
20/07/1995;0,9270
19/07/1995;0,9270
18/07/1995;0,9270
17/07/1995;0,9260
14/07/1995;0,9240
13/07/1995;0,9240
12/07/1995;0,9230
11/07/1995;0,9230
10/07/1995;0,9230
07/07/1995;0,9230
06/07/1995;0,9230
05/07/1995;0,9200
04/07/1995;0,9180
03/07/1995;0,9180
30/06/1995;0,9200
29/06/1995;0,9180
28/06/1995;0,9180
27/06/1995;0,9180
26/06/1995;0,9170
23/06/1995;0,9180
22/06/1995;0,9180
21/06/1995;0,9170
20/06/1995;0,9120
19/06/1995;0,9100
16/06/1995;0,9070
14/06/1995;0,9050
13/06/1995;0,9130
12/06/1995;0,9160
09/06/1995;0,9110
08/06/1995;0,9100
07/06/1995;0,9090
06/06/1995;0,9040
05/06/1995;0,9030
02/06/1995;0,9030
01/06/1995;0,9060
31/05/1995;0,9040
30/05/1995;0,9040
29/05/1995;0,9040
26/05/1995;0,8950
25/05/1995;0,8910
24/05/1995;0,8880
23/05/1995;0,8880
22/05/1995;0,8880
19/05/1995;0,8890
18/05/1995;0,8880
17/05/1995;0,8890
16/05/1995;0,8890
15/05/1995;0,8890
12/05/1995;0,8950
11/05/1995;0,8940
10/05/1995;0,8920
09/05/1995;0,8950
08/05/1995;0,8970
05/05/1995;0,9000
04/05/1995;0,9030
03/05/1995;0,9040
02/05/1995;0,9120
28/04/1995;0,9110
27/04/1995;0,9170
26/04/1995;0,9150
25/04/1995;0,9190
24/04/1995;0,9110
20/04/1995;0,9160
19/04/1995;0,9120
18/04/1995;0,9030
17/04/1995;0,9030
12/04/1995;0,9060
11/04/1995;0,8990
10/04/1995;0,8950
07/04/1995;0,8980
06/04/1995;0,8920
05/04/1995;0,8980
04/04/1995;0,8990
03/04/1995;0,9000
31/03/1995;0,8940
30/03/1995;0,9010
29/03/1995;0,9050
28/03/1995;0,9090
27/03/1995;0,9080
24/03/1995;0,9070
23/03/1995;0,9120
22/03/1995;0,9000
21/03/1995;0,8990
20/03/1995;0,9000
17/03/1995;0,8880
16/03/1995;0,8930
15/03/1995;0,8820
14/03/1995;0,8800
13/03/1995;0,8795
10/03/1995;0,8780
09/03/1995;0,8860
08/03/1995;0,8840
07/03/1995;0,8840
06/03/1995;0,8660
03/03/1995;0,8560
02/03/1995;0,8510
01/03/1995;0,8480
24/02/1995;0,8495
23/02/1995;0,8430
22/02/1995;0,8460
21/02/1995;0,8410
20/02/1995;0,8400
17/02/1995;0,8480
16/02/1995;0,8430
15/02/1995;0,8350
14/02/1995;0,8330
13/02/1995;0,8320
10/02/1995;0,8330
09/02/1995;0,8320
08/02/1995;0,8340
07/02/1995;0,8350
06/02/1995;0,8360
03/02/1995;0,8380
02/02/1995;0,8380
01/02/1995;0,8410
31/01/1995;0,8400
30/01/1995;0,8450
27/01/1995;0,8430
26/01/1995;0,8440
25/01/1995;0,8510
24/01/1995;0,8520
23/01/1995;0,8500
20/01/1995;0,8460
19/01/1995;0,8460
18/01/1995;0,8440
17/01/1995;0,8440
16/01/1995;0,8480
13/01/1995;0,8450
12/01/1995;0,8440
11/01/1995;0,8490
10/01/1995;0,8460
09/01/1995;0,8440
06/01/1995;0,8390
05/01/1995;0,8420
04/01/1995;0,8440
03/01/1995;0,8440
02/01/1995;0,8430
30/12/1994;0,8440
29/12/1994;0,8460
28/12/1994;0,8540
27/12/1994;0,8500
26/12/1994;0,8480
23/12/1994;0,8530
22/12/1994;0,8580
21/12/1994;0,8510
20/12/1994;0,8480
19/12/1994;0,8460
16/12/1994;0,8470
15/12/1994;0,8490
14/12/1994;0,8450
13/12/1994;0,8410
12/12/1994;0,8420
09/12/1994;0,8460
08/12/1994;0,8450
07/12/1994;0,8450
06/12/1994;0,8440
05/12/1994;0,8560
02/12/1994;0,8550
01/12/1994;0,8460
30/11/1994;0,8430
29/11/1994;0,8510
28/11/1994;0,8550
25/11/1994;0,8570
24/11/1994;0,8520
23/11/1994;0,8410
22/11/1994;0,8340
21/11/1994;0,8330
18/11/1994;0,8340
17/11/1994;0,8310
16/11/1994;0,8310
14/11/1994;0,8360
11/11/1994;0,8360
10/11/1994;0,8320
09/11/1994;0,8290
08/11/1994;0,8320
07/11/1994;0,8380
04/11/1994;0,8430
03/11/1994;0,8440
01/11/1994;0,8430
31/10/1994;0,8440
28/10/1994;0,8480
27/10/1994;0,8500
26/10/1994;0,8540
25/10/1994;0,8520
24/10/1994;0,8510
21/10/1994;0,8510
20/10/1994;0,8540
19/10/1994;0,8510
18/10/1994;0,8450
17/10/1994;0,8270
14/10/1994;0,8270
13/10/1994;0,8340
11/10/1994;0,8330
10/10/1994;0,8370
07/10/1994;0,8420
06/10/1994;0,8440
05/10/1994;0,8450
04/10/1994;0,8470
30/09/1994;0,8510
29/09/1994;0,8590
28/09/1994;0,8620
27/09/1994;0,8660
26/09/1994;0,8600
23/09/1994;0,8550
22/09/1994;0,8530
21/09/1994;0,8550
20/09/1994;0,8520
19/09/1994;0,8520
16/09/1994;0,8550
15/09/1994;0,8550
14/09/1994;0,8530
13/09/1994;0,8580
12/09/1994;0,8510
09/09/1994;0,8700
08/09/1994;0,8790
06/09/1994;0,8840
05/09/1994;0,8900
02/09/1994;0,8840
01/09/1994;0,8830
31/08/1994;0,8870
30/08/1994;0,8850
29/08/1994;0,8940
26/08/1994;0,8860
25/08/1994;0,8860
24/08/1994;0,8820
23/08/1994;0,8850
22/08/1994;0,8850
19/08/1994;0,8920
18/08/1994;0,8950
17/08/1994;0,8990
16/08/1994;0,8940
15/08/1994;0,8990
12/08/1994;0,9040
11/08/1994;0,8920
10/08/1994;0,8900
09/08/1994;0,8890
08/08/1994;0,9040
05/08/1994;0,9100
04/08/1994;0,9080
03/08/1994;0,9080
02/08/1994;0,9180
01/08/1994;0,9300
29/07/1994;0,9380
28/07/1994;0,9380
27/07/1994;0,9340
26/07/1994;0,9320
25/07/1994;0,9340
22/07/1994;0,9340
21/07/1994;0,9300
20/07/1994;0,9280
19/07/1994;0,9300
18/07/1994;0,9300
15/07/1994;0,9300
14/07/1994;0,9200
13/07/1994;0,9150
12/07/1994;0,9150
11/07/1994;0,9200
08/07/1994;0,9150
07/07/1994;0,9050
06/07/1994;0,9100
05/07/1994;0,9270
04/07/1994;0,9350
01/07/1994;0,9000
30/06/1994;0,9500
29/06/1994;0,9811
28/06/1994;0,9625
27/06/1994;0,9441
24/06/1994;0,9261
23/06/1994;0,9086
22/06/1994;0,8916
21/06/1994;0,8748
20/06/1994;0,8586
17/06/1994;0,8429
16/06/1994;0,8278
15/06/1994;0,8129
14/06/1994;0,7985
13/06/1994;0,7844
10/06/1994;0,7706
09/06/1994;0,7571
08/06/1994;0,7439
07/06/1994;0,7309
06/06/1994;0,7184
03/06/1994;0,7060
01/06/1994;0,6939
31/05/1994;0,6819
30/05/1994;0,6705
27/05/1994;0,6706
26/05/1994;0,6595
25/05/1994;0,6378
24/05/1994;0,6272
23/05/1994;0,6168
20/05/1994;0,6066
19/05/1994;0,5965
18/05/1994;0,5866
17/05/1994;0,5769
16/05/1994;0,5673
13/05/1994;0,5579
12/05/1994;0,5487
11/05/1994;0,5396
10/05/1994;0,5307
09/05/1994;0,5220
06/05/1994;0,5136
05/05/1994;0,5053
04/05/1994;0,4971
03/05/1994;0,4891
02/05/1994;0,4813
29/04/1994;0,4735
28/04/1994;0,4653
27/04/1994;0,4575
26/04/1994;0,4494
25/04/1994;0,4414
22/04/1994;0,4334
20/04/1994;0,4253
19/04/1994;0,4173
18/04/1994;0,4095
15/04/1994;0,4018
14/04/1994;0,3942
13/04/1994;0,3868
12/04/1994;0,3795
11/04/1994;0,3723
08/04/1994;0,3653
07/04/1994;0,3584
06/04/1994;0,3517
05/04/1994;0,3450
04/04/1994;0,3385
30/03/1994;0,3321
29/03/1994;0,3254
28/03/1994;0,3198
25/03/1994;0,3142
24/03/1994;0,3087
23/03/1994;0,3034
22/03/1994;0,2981
21/03/1994;0,2929
18/03/1994;0,2880
17/03/1994;0,2835
16/03/1994;0,2791
15/03/1994;0,2747
14/03/1994;0,2704
11/03/1994;0,2662
10/03/1994;0,2621
09/03/1994;0,2581
08/03/1994;0,2542
07/03/1994;0,2503
04/03/1994;0,2465
03/03/1994;0,2427
02/03/1994;0,2390
01/03/1994;0,2354
28/02/1994;0,2317
25/02/1994;0,2282
24/02/1994;0,2241
23/02/1994;0,2201
22/02/1994;0,2162
21/02/1994;0,2124
18/02/1994;0,2124
17/02/1994;0,2085
16/02/1994;0,2010
11/02/1994;0,1973
10/02/1994;0,1937
09/02/1994;0,1902
08/02/1994;0,1866
07/02/1994;0,1832
04/02/1994;0,1798
03/02/1994;0,1765
02/02/1994;0,1732
01/02/1994;0,1700
31/01/1994;0,1668
28/01/1994;0,1637
27/01/1994;0,1609
26/01/1994;0,1582
25/01/1994;0,1555
24/01/1994;0,1529
21/01/1994;0,1504
20/01/1994;0,1480
19/01/1994;0,1456
18/01/1994;0,1432
17/01/1994;0,1409
14/01/1994;0,1409
13/01/1994;0,1387
12/01/1994;0,1344
11/01/1994;0,1324
10/01/1994;0,1303
07/01/1994;0,1283
06/01/1994;0,1263
05/01/1994;0,1243
04/01/1994;0,1224
03/01/1994;0,1204
31/12/1993;0,1186
30/12/1993;0,1167
29/12/1993;0,1149
28/12/1993;0,1132
27/12/1993;0,1115
24/12/1993;0,1099
23/12/1993;0,1084
22/12/1993;0,1069
21/12/1993;0,1053
20/12/1993;0,1039
17/12/1993;0,1024
16/12/1993;0,1010
15/12/1993;0,0996
14/12/1993;0,0982
13/12/1993;0,0968
10/12/1993;0,0955
09/12/1993;0,0942
08/12/1993;0,0930
07/12/1993;0,0917
06/12/1993;0,0905
03/12/1993;0,0893
02/12/1993;0,0881
01/12/1993;0,0870
30/11/1993;0,0858
29/11/1993;0,0847
26/11/1993;0,0834
25/11/1993;0,0821
24/11/1993;0,0821
23/11/1993;0,0808
22/11/1993;0,0784
19/11/1993;0,0772
18/11/1993;0,0760
17/11/1993;0,0749
16/11/1993;0,0737
12/11/1993;0,0726
11/11/1993;0,0715
10/11/1993;0,0715
09/11/1993;0,0704
08/11/1993;0,0683
05/11/1993;0,0673
04/11/1993;0,0663
03/11/1993;0,0652
01/11/1993;0,0642
29/10/1993;0,0633
28/10/1993;0,0623
27/10/1993;0,0614
26/10/1993;0,0604
25/10/1993;0,0595
22/10/1993;0,0586
21/10/1993;0,0577
20/10/1993;0,0568
19/10/1993;0,0560
18/10/1993;0,0551
15/10/1993;0,0543
14/10/1993;0,0535
13/10/1993;0,0526
11/10/1993;0,0518
08/10/1993;0,0518
07/10/1993;0,0510
06/10/1993;0,0495
05/10/1993;0,0488
04/10/1993;0,0480
01/10/1993;0,0473
30/09/1993;0,0466
29/09/1993;0,0459
28/09/1993;0,0452
27/09/1993;0,0445
24/09/1993;0,0438
23/09/1993;0,0432
22/09/1993;0,0426
21/09/1993;0,0419
20/09/1993;0,0414
17/09/1993;0,0408
16/09/1993;0,0402
15/09/1993;0,0396
14/09/1993;0,0391
13/09/1993;0,0385
10/09/1993;0,0380
09/09/1993;0,0374
08/09/1993;0,0369
06/09/1993;0,0364
03/09/1993;0,0364
02/09/1993;0,0359
01/09/1993;0,0349
31/08/1993;0,0344
30/08/1993;0,0339
27/08/1993;0,0335
26/08/1993;0,0330
25/08/1993;0,0326
24/08/1993;0,0322
23/08/1993;0,0317
20/08/1993;0,0313
19/08/1993;0,0309
18/08/1993;0,0305
17/08/1993;0,0302
16/08/1993;0,0298
13/08/1993;0,0294
12/08/1993;0,0290
11/08/1993;0,0287
10/08/1993;0,0283
09/08/1993;0,0279
06/08/1993;0,0276
05/08/1993;0,0272
04/08/1993;0,0269
03/08/1993;0,0265
02/08/1993;0,0262
30/07/1993;0,0259
29/07/1993;0,0255
28/07/1993;0,0252
27/07/1993;0,0249
26/07/1993;0,0246
23/07/1993;0,0243
22/07/1993;0,0240
21/07/1993;0,0237
20/07/1993;0,0234
19/07/1993;0,0232
16/07/1993;0,0229
15/07/1993;0,0226
14/07/1993;0,0223
13/07/1993;0,0221
12/07/1993;0,0218
09/07/1993;0,0215
08/07/1993;0,0213
07/07/1993;0,0210
06/07/1993;0,0207
05/07/1993;0,0205
02/07/1993;0,0205
01/07/1993;0,0202
30/06/1993;0,0198
29/06/1993;0,0195
28/06/1993;0,0193
25/06/1993;0,0190
24/06/1993;0,0188
23/06/1993;0,0186
22/06/1993;0,0183
21/06/1993;0,0181
18/06/1993;0,0179
17/06/1993;0,0177
16/06/1993;0,0175
15/06/1993;0,0172
14/06/1993;0,0170
11/06/1993;0,0168
09/06/1993;0,0166
08/06/1993;0,0164
07/06/1993;0,0162
04/06/1993;0,0160
03/06/1993;0,0158
02/06/1993;0,0156
01/06/1993;0,0154
31/05/1993;0,0152
28/05/1993;0,0152
27/05/1993;0,0150
26/05/1993;0,0146
25/05/1993;0,0144
24/05/1993;0,0142
21/05/1993;0,0141
20/05/1993;0,0139
19/05/1993;0,0137
18/05/1993;0,0136
17/05/1993;0,0134
14/05/1993;0,0133
13/05/1993;0,0131
12/05/1993;0,0129
11/05/1993;0,0128
10/05/1993;0,0126
07/05/1993;0,0125
06/05/1993;0,0123
05/05/1993;0,0122
04/05/1993;0,0120
03/05/1993;0,0119
30/04/1993;0,0117
29/04/1993;0,0116
28/04/1993;0,0114
27/04/1993;0,0113
26/04/1993;0,0111
23/04/1993;0,0110
22/04/1993;0,0108
20/04/1993;0,0107
19/04/1993;0,0106
16/04/1993;0,0104
15/04/1993;0,0103
14/04/1993;0,0101
13/04/1993;0,0100
12/04/1993;0,0099
07/04/1993;0,0097
06/04/1993;0,0096
05/04/1993;0,0095
02/04/1993;0,0094
01/04/1993;0,0093
31/03/1993;0,0091
30/03/1993;0,0090
29/03/1993;0,0089
26/03/1993;0,0088
25/03/1993;0,0087
24/03/1993;0,0087
23/03/1993;0,0086
22/03/1993;0,0085
19/03/1993;0,0084
18/03/1993;0,0083
17/03/1993;0,0082
16/03/1993;0,0081
15/03/1993;0,0081
12/03/1993;0,0080
11/03/1993;0,0079
10/03/1993;0,0078
09/03/1993;0,0078
08/03/1993;0,0077
05/03/1993;0,0076
04/03/1993;0,0075
03/03/1993;0,0074
02/03/1993;0,0074
01/03/1993;0,0073
26/02/1993;0,0072
25/02/1993;0,0071
24/02/1993;0,0070
19/02/1993;0,0070
18/02/1993;0,0069
17/02/1993;0,0068
16/02/1993;0,0067
15/02/1993;0,0066
12/02/1993;0,0066
11/02/1993;0,0065
10/02/1993;0,0064
09/02/1993;0,0063
08/02/1993;0,0062
05/02/1993;0,0061
04/02/1993;0,0060
03/02/1993;0,0059
02/02/1993;0,0059
01/02/1993;0,0058
29/01/1993;0,0057
28/01/1993;0,0056
27/01/1993;0,0056
26/01/1993;0,0055
25/01/1993;0,0054
22/01/1993;0,0054
21/01/1993;0,0053
20/01/1993;0,0052
19/01/1993;0,0052
18/01/1993;0,0051
15/01/1993;0,0051
14/01/1993;0,0051
13/01/1993;0,0049
12/01/1993;0,0049
11/01/1993;0,0048
08/01/1993;0,0048
07/01/1993;0,0047
06/01/1993;0,0047
05/01/1993;0,0046
04/01/1993;0,0046
31/12/1992;0,0045
30/12/1992;0,0045
29/12/1992;0,0044
28/12/1992;0,0044
24/12/1992;0,0043
23/12/1992;0,0043
22/12/1992;0,0042
21/12/1992;0,0042
18/12/1992;0,0041
17/12/1992;0,0041
16/12/1992;0,0041
15/12/1992;0,0040
14/12/1992;0,0040
11/12/1992;0,0039
10/12/1992;0,0039
09/12/1992;0,0039
08/12/1992;0,0038
07/12/1992;0,0038
04/12/1992;0,0038
03/12/1992;0,0037
02/12/1992;0,0037
01/12/1992;0,0037
30/11/1992;0,0036
27/11/1992;0,0036
26/11/1992;0,0035
25/11/1992;0,0035
24/11/1992;0,0035
23/11/1992;0,0034
20/11/1992;0,0034
19/11/1992;0,0034
18/11/1992;0,0033
17/11/1992;0,0033
16/11/1992;0,0033
13/11/1992;0,0032
12/11/1992;0,0032
11/11/1992;0,0032
10/11/1992;0,0032
09/11/1992;0,0031
06/11/1992;0,0031
05/11/1992;0,0030
04/11/1992;0,0030
03/11/1992;0,0030
30/10/1992;0,0029
29/10/1992;0,0029
28/10/1992;0,0029
27/10/1992;0,0028
26/10/1992;0,0028
23/10/1992;0,0028
22/10/1992;0,0027
21/10/1992;0,0027
20/10/1992;0,0027
19/10/1992;0,0026
16/10/1992;0,0026
15/10/1992;0,0026
14/10/1992;0,0026
13/10/1992;0,0025
09/10/1992;0,0025
08/10/1992;0,0025
07/10/1992;0,0025
06/10/1992;0,0024
05/10/1992;0,0024
02/10/1992;0,0024
01/10/1992;0,0024
30/09/1992;0,0023
29/09/1992;0,0023
28/09/1992;0,0023
25/09/1992;0,0023
24/09/1992;0,0022
23/09/1992;0,0022
22/09/1992;0,0022
21/09/1992;0,0022
18/09/1992;0,0021
17/09/1992;0,0021
16/09/1992;0,0021
15/09/1992;0,0021
14/09/1992;0,0020
11/09/1992;0,0020
10/09/1992;0,0020
09/09/1992;0,0020
08/09/1992;0,0020
04/09/1992;0,0019
03/09/1992;0,0019
02/09/1992;0,0019
01/09/1992;0,0019
31/08/1992;0,0019
28/08/1992;0,0018
27/08/1992;0,0018
26/08/1992;0,0018
25/08/1992;0,0018
24/08/1992;0,0018
21/08/1992;0,0018
20/08/1992;0,0017
19/08/1992;0,0017
18/08/1992;0,0017
17/08/1992;0,0017
14/08/1992;0,0017
13/08/1992;0,0017
12/08/1992;0,0016
11/08/1992;0,0016
10/08/1992;0,0016
07/08/1992;0,0016
06/08/1992;0,0016
05/08/1992;0,0016
04/08/1992;0,0016
03/08/1992;0,0015
31/07/1992;0,0015
30/07/1992;0,0015
29/07/1992;0,0015
28/07/1992;0,0015
27/07/1992;0,0015
24/07/1992;0,0015
23/07/1992;0,0015
22/07/1992;0,0014
21/07/1992;0,0014
20/07/1992;0,0014
17/07/1992;0,0014
16/07/1992;0,0014
15/07/1992;0,0014
14/07/1992;0,0014
13/07/1992;0,0014
10/07/1992;0,0013
09/07/1992;0,0013
08/07/1992;0,0013
07/07/1992;0,0013
06/07/1992;0,0013
03/07/1992;0,0013
02/07/1992;0,0013
01/07/1992;0,0013
30/06/1992;0,0013
29/06/1992;0,0012
26/06/1992;0,0012
25/06/1992;0,0012
24/06/1992;0,0012
23/06/1992;0,0012
22/06/1992;0,0012
19/06/1992;0,0012
17/06/1992;0,0012
16/06/1992;0,0012
15/06/1992;0,0011
12/06/1992;0,0011
11/06/1992;0,0011
10/06/1992;0,0011
09/06/1992;0,0011
08/06/1992;0,0011
05/06/1992;0,0011
04/06/1992;0,0011
03/06/1992;0,0011
02/06/1992;0,0011
01/06/1992;0,0010
29/05/1992;0,0010
28/05/1992;0,0010
27/05/1992;0,0010
26/05/1992;0,0010
25/05/1992;0,0010
22/05/1992;0,0010
21/05/1992;0,0010
20/05/1992;0,0010
19/05/1992;0,0010
18/05/1992;0,0010
15/05/1992;0,0010
14/05/1992;0,0009
13/05/1992;0,0009
12/05/1992;0,0009
11/05/1992;0,0009
08/05/1992;0,0009
07/05/1992;0,0009
06/05/1992;0,0009
05/05/1992;0,0009
04/05/1992;0,0009
30/04/1992;0,0009
29/04/1992;0,0009
28/04/1992;0,0009
27/04/1992;0,0008
24/04/1992;0,0008
23/04/1992;0,0008
22/04/1992;0,0008
20/04/1992;0,0008
15/04/1992;0,0008
14/04/1992;0,0008
13/04/1992;0,0008
10/04/1992;0,0008
09/04/1992;0,0008
08/04/1992;0,0008
07/04/1992;0,0008
06/04/1992;0,0008
03/04/1992;0,0007
02/04/1992;0,0007
01/04/1992;0,0007
31/03/1992;0,0007
30/03/1992;0,0007
27/03/1992;0,0007
26/03/1992;0,0007
25/03/1992;0,0007
24/03/1992;0,0007
23/03/1992;0,0007
20/03/1992;0,0007
19/03/1992;0,0007
18/03/1992;0,0007
17/03/1992;0,0007
16/03/1992;0,0006
13/03/1992;0,0006
12/03/1992;0,0006
11/03/1992;0,0006
10/03/1992;0,0006
09/03/1992;0,0006
06/03/1992;0,0006
05/03/1992;0,0006
04/03/1992;0,0006
28/02/1992;0,0006
27/02/1992;0,0006
26/02/1992;0,0006
25/02/1992;0,0006
24/02/1992;0,0006
21/02/1992;0,0006
20/02/1992;0,0006
19/02/1992;0,0006
18/02/1992;0,0005
17/02/1992;0,0005
14/02/1992;0,0005
13/02/1992;0,0005
12/02/1992;0,0005
11/02/1992;0,0005
10/02/1992;0,0005
07/02/1992;0,0005
06/02/1992;0,0005
05/02/1992;0,0005
04/02/1992;0,0005
03/02/1992;0,0005
31/01/1992;0,0005
30/01/1992;0,0005
29/01/1992;0,0005
28/01/1992;0,0005
27/01/1992;0,0005
24/01/1992;0,0005
23/01/1992;0,0005
22/01/1992;0,0004
21/01/1992;0,0004
20/01/1992;0,0004
17/01/1992;0,0004
16/01/1992;0,0004
15/01/1992;0,0004
14/01/1992;0,0004
13/01/1992;0,0004
10/01/1992;0,0004
09/01/1992;0,0004
08/01/1992;0,0004
07/01/1992;0,0004
06/01/1992;0,0004
03/01/1992;0,0004
02/01/1992;0,0004
31/12/1991;0,0004
30/12/1991;0,0004
27/12/1991;0,0004
26/12/1991;0,0004
24/12/1991;0,0004
23/12/1991;0,0004
20/12/1991;0,0004
19/12/1991;0,0004
18/12/1991;0,0004
17/12/1991;0,0004
16/12/1991;0,0003
13/12/1991;0,0003
12/12/1991;0,0003
11/12/1991;0,0003
10/12/1991;0,0003
09/12/1991;0,0003
06/12/1991;0,0003
05/12/1991;0,0003
04/12/1991;0,0003
03/12/1991;0,0003
02/12/1991;0,0003
29/11/1991;0,0003
28/11/1991;0,0003
27/11/1991;0,0003
26/11/1991;0,0003
25/11/1991;0,0003
22/11/1991;0,0003
21/11/1991;0,0003
20/11/1991;0,0003
19/11/1991;0,0003
18/11/1991;0,0003
14/11/1991;0,0003
13/11/1991;0,0003
12/11/1991;0,0003
11/11/1991;0,0003
08/11/1991;0,0003
07/11/1991;0,0002
06/11/1991;0,0002
05/11/1991;0,0002
04/11/1991;0,0002
01/11/1991;0,0002
31/10/1991;0,0002
30/10/1991;0,0002
29/10/1991;0,0002
28/10/1991;0,0002
25/10/1991;0,0002
24/10/1991;0,0002
23/10/1991;0,0002
22/10/1991;0,0002
21/10/1991;0,0002
18/10/1991;0,0002
17/10/1991;0,0002
16/10/1991;0,0002
15/10/1991;0,0002
14/10/1991;0,0002
11/10/1991;0,0002
10/10/1991;0,0002
09/10/1991;0,0002
08/10/1991;0,0002
07/10/1991;0,0002
04/10/1991;0,0002
03/10/1991;0,0002
02/10/1991;0,0002
01/10/1991;0,0002
30/09/1991;0,0002
27/09/1991;0,0002
26/09/1991;0,0002
25/09/1991;0,0002
24/09/1991;0,0002
23/09/1991;0,0002
20/09/1991;0,0002
19/09/1991;0,0002
18/09/1991;0,0002
17/09/1991;0,0002
16/09/1991;0,0002
13/09/1991;0,0002
12/09/1991;0,0002
11/09/1991;0,0002
10/09/1991;0,0002
09/09/1991;0,0001
06/09/1991;0,0001
05/09/1991;0,0001
04/09/1991;0,0001
03/09/1991;0,0001
02/09/1991;0,0001
30/08/1991;0,0001
29/08/1991;0,0001
28/08/1991;0,0001
27/08/1991;0,0001
26/08/1991;0,0001
23/08/1991;0,0001
22/08/1991;0,0001
21/08/1991;0,0001
20/08/1991;0,0001
19/08/1991;0,0001
16/08/1991;0,0001
15/08/1991;0,0001
14/08/1991;0,0001
13/08/1991;0,0001
12/08/1991;0,0001
09/08/1991;0,0001
08/08/1991;0,0001
07/08/1991;0,0001
06/08/1991;0,0001
05/08/1991;0,0001
02/08/1991;0,0001
01/08/1991;0,0001
31/07/1991;0,0001
30/07/1991;0,0001
29/07/1991;0,0001
26/07/1991;0,0001
25/07/1991;0,0001
24/07/1991;0,0001
23/07/1991;0,0001
22/07/1991;0,0001
19/07/1991;0,0001
18/07/1991;0,0001
17/07/1991;0,0001
16/07/1991;0,0001
15/07/1991;0,0001
12/07/1991;0,0001
11/07/1991;0,0001
10/07/1991;0,0001
09/07/1991;0,0001
08/07/1991;0,0001
05/07/1991;0,0001
04/07/1991;0,0001
03/07/1991;0,0001
02/07/1991;0,0001
01/07/1991;0,0001
28/06/1991;0,0001
27/06/1991;0,0001
26/06/1991;0,0001
25/06/1991;0,0001
24/06/1991;0,0001
21/06/1991;0,0001
20/06/1991;0,0001
19/06/1991;0,0001
18/06/1991;0,0001
17/06/1991;0,0001
14/06/1991;0,0001
13/06/1991;0,0001
12/06/1991;0,0001
11/06/1991;0,0001
10/06/1991;0,0001
07/06/1991;0,0001
06/06/1991;0,0001
05/06/1991;0,0001
04/06/1991;0,0001
03/06/1991;0,0001
31/05/1991;0,0001
29/05/1991;0,0001
28/05/1991;0,0001
27/05/1991;0,0001
24/05/1991;0,0001
23/05/1991;0,0001
22/05/1991;0,0001
21/05/1991;0,0001
20/05/1991;0,0001
17/05/1991;0,0001
16/05/1991;0,0001
15/05/1991;0,0001
14/05/1991;0,0001
13/05/1991;0,0001
10/05/1991;0,0001
09/05/1991;0,0001
08/05/1991;0,0001
07/05/1991;0,0001
06/05/1991;0,0001
03/05/1991;0,0001
02/05/1991;0,0001
30/04/1991;0,0001
29/04/1991;0,0001
26/04/1991;0,0001
25/04/1991;0,0001
24/04/1991;0,0001
23/04/1991;0,0001
22/04/1991;0,0001
19/04/1991;0,0001
18/04/1991;0,0001
17/04/1991;0,0001
16/04/1991;0,0001
15/04/1991;0,0001
12/04/1991;0,0001
11/04/1991;0,0001
10/04/1991;0,0001
09/04/1991;0,0001
08/04/1991;0,0001
05/04/1991;0,0001
04/04/1991;0,0001
03/04/1991;0,0001
02/04/1991;0,0001
01/04/1991;0,0001
27/03/1991;0,0001
26/03/1991;0,0001
25/03/1991;0,0001
22/03/1991;0,0001
21/03/1991;0,0001
20/03/1991;0,0001
19/03/1991;0,0001
18/03/1991;0,0001
15/03/1991;0,0001
14/03/1991;0,0001
13/03/1991;0,0001
12/03/1991;0,0001
11/03/1991;0,0001
08/03/1991;0,0001
07/03/1991;0,0001
06/03/1991;0,0001
05/03/1991;0,0001
04/03/1991;0,0001
01/03/1991;0,0001
28/02/1991;0,0001
27/02/1991;0,0001
26/02/1991;0,0001
25/02/1991;0,0001
22/02/1991;0,0001
21/02/1991;0,0001
20/02/1991;0,0001
19/02/1991;0,0001
18/02/1991;0,0001
15/02/1991;0,0001
14/02/1991;0,0001
13/02/1991;0,0001
08/02/1991;0,0001
07/02/1991;0,0001
06/02/1991;0,0001
05/02/1991;0,0001
04/02/1991;0,0001
31/01/1991;0,0001
30/01/1991;0,0001
29/01/1991;0,0001
28/01/1991;0,0001
25/01/1991;0,0001
24/01/1991;0,0001
23/01/1991;0,0001
22/01/1991;0,0001
21/01/1991;0,0001
18/01/1991;0,0001
17/01/1991;0,0001
16/01/1991;0,0001
15/01/1991;0,0001
14/01/1991;0,0001
11/01/1991;0,0001
10/01/1991;0,0001
09/01/1991;0,0001
08/01/1991;0,0001
07/01/1991;0,0001
04/01/1991;0,0001
03/01/1991;0,0001
02/01/1991;0,0001
31/12/1990;0,0001
28/12/1990;0,0001
27/12/1990;0,0001
26/12/1990;0,0001
24/12/1990;0,0001
21/12/1990;0,0001
20/12/1990;0,0001
19/12/1990;0,0001
18/12/1990;0,0001
17/12/1990;0,0001
14/12/1990;0,0001
13/12/1990;0,0001
12/12/1990;0,0001
11/12/1990;0,0001
10/12/1990;0,0001
07/12/1990;0,0001
06/12/1990;0,0001
05/12/1990;0,0001
04/12/1990;0,0001
03/12/1990;0,0001
30/11/1990;0,0001
29/11/1990;0,0001
28/11/1990;0,0000
27/11/1990;0,0000
26/11/1990;0,0000
23/11/1990;0,0000
22/11/1990;0,0000
21/11/1990;0,0000
20/11/1990;0,0000
19/11/1990;0,0000
16/11/1990;0,0000
14/11/1990;0,0000
13/11/1990;0,0000
12/11/1990;0,0000
09/11/1990;0,0000
08/11/1990;0,0000
07/11/1990;0,0000
06/11/1990;0,0000
05/11/1990;0,0000
01/11/1990;0,0000
31/10/1990;0,0000
30/10/1990;0,0000
29/10/1990;0,0000
26/10/1990;0,0000
25/10/1990;0,0000
24/10/1990;0,0000
23/10/1990;0,0000
22/10/1990;0,0000
19/10/1990;0,0000
18/10/1990;0,0000
17/10/1990;0,0000
16/10/1990;0,0000
15/10/1990;0,0000
12/10/1990;0,0000
11/10/1990;0,0000
10/10/1990;0,0000
09/10/1990;0,0000
05/10/1990;0,0000
04/10/1990;0,0000
02/10/1990;0,0000
01/10/1990;0,0000
28/09/1990;0,0000
27/09/1990;0,0000
26/09/1990;0,0000
25/09/1990;0,0000
24/09/1990;0,0000
21/09/1990;0,0000
20/09/1990;0,0000
19/09/1990;0,0000
18/09/1990;0,0000
17/09/1990;0,0000
14/09/1990;0,0000
13/09/1990;0,0000
12/09/1990;0,0000
11/09/1990;0,0000
10/09/1990;0,0000
06/09/1990;0,0000
05/09/1990;0,0000
04/09/1990;0,0000
03/09/1990;0,0000
31/08/1990;0,0000
30/08/1990;0,0000
29/08/1990;0,0000
28/08/1990;0,0000
27/08/1990;0,0000
24/08/1990;0,0000
23/08/1990;0,0000
22/08/1990;0,0000
21/08/1990;0,0000
20/08/1990;0,0000
17/08/1990;0,0000
16/08/1990;0,0000
15/08/1990;0,0000
14/08/1990;0,0000
13/08/1990;0,0000
10/08/1990;0,0000
09/08/1990;0,0000
08/08/1990;0,0000
07/08/1990;0,0000
06/08/1990;0,0000
03/08/1990;0,0000
02/08/1990;0,0000
01/08/1990;0,0000
31/07/1990;0,0000
30/07/1990;0,0000
27/07/1990;0,0000
26/07/1990;0,0000
25/07/1990;0,0000
24/07/1990;0,0000
23/07/1990;0,0000
20/07/1990;0,0000
19/07/1990;0,0000
18/07/1990;0,0000
17/07/1990;0,0000
16/07/1990;0,0000
13/07/1990;0,0000
12/07/1990;0,0000
11/07/1990;0,0000
10/07/1990;0,0000
09/07/1990;0,0000
06/07/1990;0,0000
05/07/1990;0,0000
04/07/1990;0,0000
03/07/1990;0,0000
02/07/1990;0,0000
29/06/1990;0,0000
28/06/1990;0,0000
27/06/1990;0,0000
26/06/1990;0,0000
25/06/1990;0,0000
22/06/1990;0,0000
21/06/1990;0,0000
20/06/1990;0,0000
19/06/1990;0,0000
18/06/1990;0,0000
15/06/1990;0,0000
13/06/1990;0,0000
12/06/1990;0,0000
11/06/1990;0,0000
08/06/1990;0,0000
07/06/1990;0,0000
06/06/1990;0,0000
05/06/1990;0,0000
04/06/1990;0,0000
01/06/1990;0,0000
31/05/1990;0,0000
30/05/1990;0,0000
29/05/1990;0,0000
28/05/1990;0,0000
25/05/1990;0,0000
24/05/1990;0,0000
23/05/1990;0,0000
22/05/1990;0,0000
21/05/1990;0,0000
18/05/1990;0,0000
17/05/1990;0,0000
16/05/1990;0,0000
15/05/1990;0,0000
14/05/1990;0,0000
11/05/1990;0,0000
10/05/1990;0,0000
09/05/1990;0,0000
08/05/1990;0,0000
07/05/1990;0,0000
04/05/1990;0,0000
03/05/1990;0,0000
02/05/1990;0,0000
30/04/1990;0,0000
27/04/1990;0,0000
26/04/1990;0,0000
25/04/1990;0,0000
24/04/1990;0,0000
23/04/1990;0,0000
20/04/1990;0,0000
19/04/1990;0,0000
18/04/1990;0,0000
17/04/1990;0,0000
16/04/1990;0,0000
11/04/1990;0,0000
10/04/1990;0,0000
09/04/1990;0,0000
06/04/1990;0,0000
05/04/1990;0,0000
04/04/1990;0,0000
03/04/1990;0,0000
02/04/1990;0,0000
30/03/1990;0,0000
29/03/1990;0,0000
28/03/1990;0,0000
27/03/1990;0,0000
26/03/1990;0,0000
23/03/1990;0,0000
22/03/1990;0,0000
21/03/1990;0,0000
20/03/1990;0,0000
19/03/1990;0,0000
13/03/1990;0,0000
12/03/1990;0,0000
09/03/1990;0,0000
08/03/1990;0,0000
07/03/1990;0,0000
06/03/1990;0,0000
05/03/1990;0,0000
02/03/1990;0,0000
01/03/1990;0,0000
28/02/1990;0,0000
23/02/1990;0,0000
22/02/1990;0,0000
21/02/1990;0,0000
20/02/1990;0,0000
19/02/1990;0,0000
16/02/1990;0,0000
15/02/1990;0,0000
14/02/1990;0,0000
13/02/1990;0,0000
12/02/1990;0,0000
09/02/1990;0,0000
08/02/1990;0,0000
07/02/1990;0,0000
06/02/1990;0,0000
05/02/1990;0,0000
02/02/1990;0,0000
01/02/1990;0,0000
31/01/1990;0,0000
30/01/1990;0,0000
29/01/1990;0,0000
26/01/1990;0,0000
25/01/1990;0,0000
24/01/1990;0,0000
23/01/1990;0,0000
22/01/1990;0,0000
19/01/1990;0,0000
18/01/1990;0,0000
17/01/1990;0,0000
16/01/1990;0,0000
15/01/1990;0,0000
12/01/1990;0,0000
11/01/1990;0,0000
10/01/1990;0,0000
09/01/1990;0,0000
08/01/1990;0,0000
05/01/1990;0,0000
04/01/1990;0,0000
03/01/1990;0,0000
02/01/1990;0,0000
29/12/1989;0,0000
28/12/1989;0,0000
27/12/1989;0,0000
26/12/1989;0,0000
22/12/1989;0,0000
21/12/1989;0,0000
20/12/1989;0,0000
19/12/1989;0,0000
18/12/1989;0,0000
15/12/1989;0,0000
14/12/1989;0,0000
13/12/1989;0,0000
12/12/1989;0,0000
11/12/1989;0,0000
08/12/1989;0,0000
07/12/1989;0,0000
06/12/1989;0,0000
05/12/1989;0,0000
04/12/1989;0,0000
01/12/1989;0,0000
30/11/1989;0,0000
29/11/1989;0,0000
28/11/1989;0,0000
27/11/1989;0,0000
24/11/1989;0,0000
23/11/1989;0,0000
22/11/1989;0,0000
21/11/1989;0,0000
20/11/1989;0,0000
17/11/1989;0,0000
16/11/1989;0,0000
14/11/1989;0,0000
13/11/1989;0,0000
10/11/1989;0,0000
09/11/1989;0,0000
08/11/1989;0,0000
07/11/1989;0,0000
06/11/1989;0,0000
03/11/1989;0,0000
01/11/1989;0,0000
31/10/1989;0,0000
30/10/1989;0,0000
27/10/1989;0,0000
26/10/1989;0,0000
25/10/1989;0,0000
24/10/1989;0,0000
23/10/1989;0,0000
20/10/1989;0,0000
19/10/1989;0,0000
18/10/1989;0,0000
17/10/1989;0,0000
16/10/1989;0,0000
13/10/1989;0,0000
12/10/1989;0,0000
11/10/1989;0,0000
10/10/1989;0,0000
06/10/1989;0,0000
05/10/1989;0,0000
04/10/1989;0,0000
03/10/1989;0,0000
02/10/1989;0,0000
29/09/1989;0,0000
28/09/1989;0,0000
27/09/1989;0,0000
26/09/1989;0,0000
25/09/1989;0,0000
22/09/1989;0,0000
21/09/1989;0,0000
20/09/1989;0,0000
19/09/1989;0,0000
18/09/1989;0,0000
15/09/1989;0,0000
14/09/1989;0,0000
13/09/1989;0,0000
12/09/1989;0,0000
11/09/1989;0,0000
08/09/1989;0,0000
06/09/1989;0,0000
05/09/1989;0,0000
04/09/1989;0,0000
01/09/1989;0,0000
31/08/1989;0,0000
30/08/1989;0,0000
29/08/1989;0,0000
28/08/1989;0,0000
25/08/1989;0,0000
24/08/1989;0,0000
23/08/1989;0,0000
22/08/1989;0,0000
21/08/1989;0,0000
18/08/1989;0,0000
17/08/1989;0,0000
16/08/1989;0,0000
15/08/1989;0,0000
14/08/1989;0,0000
11/08/1989;0,0000
10/08/1989;0,0000
09/08/1989;0,0000
08/08/1989;0,0000
07/08/1989;0,0000
04/08/1989;0,0000
03/08/1989;0,0000
02/08/1989;0,0000
01/08/1989;0,0000
31/07/1989;0,0000
28/07/1989;0,0000
27/07/1989;0,0000
26/07/1989;0,0000
25/07/1989;0,0000
24/07/1989;0,0000
21/07/1989;0,0000
20/07/1989;0,0000
19/07/1989;0,0000
18/07/1989;0,0000
17/07/1989;0,0000
14/07/1989;0,0000
13/07/1989;0,0000
12/07/1989;0,0000
11/07/1989;0,0000
10/07/1989;0,0000
07/07/1989;0,0000
06/07/1989;0,0000
05/07/1989;0,0000
04/07/1989;0,0000
03/07/1989;0,0000
30/06/1989;0,0000
29/06/1989;0,0000
28/06/1989;0,0000
27/06/1989;0,0000
26/06/1989;0,0000
23/06/1989;0,0000
22/06/1989;0,0000
21/06/1989;0,0000
20/06/1989;0,0000
19/06/1989;0,0000
16/06/1989;0,0000
15/06/1989;0,0000
14/06/1989;0,0000
13/06/1989;0,0000
12/06/1989;0,0000
09/06/1989;0,0000
08/06/1989;0,0000
07/06/1989;0,0000
06/06/1989;0,0000
05/06/1989;0,0000
02/06/1989;0,0000
01/06/1989;0,0000
31/05/1989;0,0000
30/05/1989;0,0000
29/05/1989;0,0000
26/05/1989;0,0000
24/05/1989;0,0000
23/05/1989;0,0000
22/05/1989;0,0000
19/05/1989;0,0000
18/05/1989;0,0000
17/05/1989;0,0000
16/05/1989;0,0000
15/05/1989;0,0000
12/05/1989;0,0000
11/05/1989;0,0000
10/05/1989;0,0000
09/05/1989;0,0000
08/05/1989;0,0000
05/05/1989;0,0000
04/05/1989;0,0000
03/05/1989;0,0000
02/05/1989;0,0000
28/04/1989;0,0000
27/04/1989;0,0000
26/04/1989;0,0000
25/04/1989;0,0000
24/04/1989;0,0000
21/04/1989;0,0000
20/04/1989;0,0000
19/04/1989;0,0000
18/04/1989;0,0000
14/04/1989;0,0000
13/04/1989;0,0000
12/04/1989;0,0000
11/04/1989;0,0000
10/04/1989;0,0000
07/04/1989;0,0000
06/04/1989;0,0000
05/04/1989;0,0000
04/04/1989;0,0000
03/04/1989;0,0000
31/03/1989;0,0000
30/03/1989;0,0000
29/03/1989;0,0000
28/03/1989;0,0000
27/03/1989;0,0000
22/03/1989;0,0000
21/03/1989;0,0000
20/03/1989;0,0000
17/03/1989;0,0000
16/03/1989;0,0000
15/03/1989;0,0000
14/03/1989;0,0000
13/03/1989;0,0000
10/03/1989;0,0000
09/03/1989;0,0000
08/03/1989;0,0000
07/03/1989;0,0000
06/03/1989;0,0000
03/03/1989;0,0000
02/03/1989;0,0000
01/03/1989;0,0000
28/02/1989;0,0000
27/02/1989;0,0000
24/02/1989;0,0000
23/02/1989;0,0000
22/02/1989;0,0000
21/02/1989;0,0000
20/02/1989;0,0000
17/02/1989;0,0000
16/02/1989;0,0000
15/02/1989;0,0000
14/02/1989;0,0000
13/02/1989;0,0000
10/02/1989;0,0000
09/02/1989;0,0000
08/02/1989;0,0000
03/02/1989;0,0000
02/02/1989;0,0000
01/02/1989;0,0000
31/01/1989;0,0000
30/01/1989;0,0000
27/01/1989;0,0000
26/01/1989;0,0000
25/01/1989;0,0000
24/01/1989;0,0000
23/01/1989;0,0000
20/01/1989;0,0000
19/01/1989;0,0000
18/01/1989;0,0000
17/01/1989;0,0000
16/01/1989;0,0000
13/01/1989;0,0000
12/01/1989;0,0000
11/01/1989;0,0000
10/01/1989;0,0000
09/01/1989;0,0000
06/01/1989;0,0000
05/01/1989;0,0000
04/01/1989;0,0000
03/01/1989;0,0000
02/01/1989;0,0000
29/12/1988;0,0000
28/12/1988;0,0000
27/12/1988;0,0000
26/12/1988;0,0000
23/12/1988;0,0000
22/12/1988;0,0000
21/12/1988;0,0000
20/12/1988;0,0000
19/12/1988;0,0000
16/12/1988;0,0000
15/12/1988;0,0000
14/12/1988;0,0000
13/12/1988;0,0000
12/12/1988;0,0000
09/12/1988;0,0000
08/12/1988;0,0000
07/12/1988;0,0000
06/12/1988;0,0000
05/12/1988;0,0000
02/12/1988;0,0000
01/12/1988;0,0000
30/11/1988;0,0000
29/11/1988;0,0000
28/11/1988;0,0000
25/11/1988;0,0000
24/11/1988;0,0000
23/11/1988;0,0000
22/11/1988;0,0000
21/11/1988;0,0000
18/11/1988;0,0000
17/11/1988;0,0000
16/11/1988;0,0000
14/11/1988;0,0000
11/11/1988;0,0000
10/11/1988;0,0000
09/11/1988;0,0000
08/11/1988;0,0000
07/11/1988;0,0000
04/11/1988;0,0000
03/11/1988;0,0000
02/11/1988;0,0000
01/11/1988;0,0000
28/10/1988;0,0000
27/10/1988;0,0000
26/10/1988;0,0000
25/10/1988;0,0000
24/10/1988;0,0000
21/10/1988;0,0000
20/10/1988;0,0000
19/10/1988;0,0000
18/10/1988;0,0000
17/10/1988;0,0000
14/10/1988;0,0000
13/10/1988;0,0000
12/10/1988;0,0000
11/10/1988;0,0000
07/10/1988;0,0000
06/10/1988;0,0000
05/10/1988;0,0000
04/10/1988;0,0000
03/10/1988;0,0000
30/09/1988;0,0000
29/09/1988;0,0000
28/09/1988;0,0000
27/09/1988;0,0000
26/09/1988;0,0000
23/09/1988;0,0000
22/09/1988;0,0000
21/09/1988;0,0000
20/09/1988;0,0000
19/09/1988;0,0000
16/09/1988;0,0000
15/09/1988;0,0000
14/09/1988;0,0000
13/09/1988;0,0000
12/09/1988;0,0000
09/09/1988;0,0000
08/09/1988;0,0000
06/09/1988;0,0000
05/09/1988;0,0000
02/09/1988;0,0000
01/09/1988;0,0000
31/08/1988;0,0000
30/08/1988;0,0000
29/08/1988;0,0000
26/08/1988;0,0000
25/08/1988;0,0000
24/08/1988;0,0000
23/08/1988;0,0000
22/08/1988;0,0000
19/08/1988;0,0000
18/08/1988;0,0000
17/08/1988;0,0000
16/08/1988;0,0000
15/08/1988;0,0000
12/08/1988;0,0000
11/08/1988;0,0000
10/08/1988;0,0000
09/08/1988;0,0000
08/08/1988;0,0000
05/08/1988;0,0000
04/08/1988;0,0000
03/08/1988;0,0000
02/08/1988;0,0000
01/08/1988;0,0000
29/07/1988;0,0000
28/07/1988;0,0000
27/07/1988;0,0000
26/07/1988;0,0000
25/07/1988;0,0000
22/07/1988;0,0000
21/07/1988;0,0000
20/07/1988;0,0000
19/07/1988;0,0000
18/07/1988;0,0000
15/07/1988;0,0000
14/07/1988;0,0000
13/07/1988;0,0000
12/07/1988;0,0000
11/07/1988;0,0000
08/07/1988;0,0000
07/07/1988;0,0000
06/07/1988;0,0000
05/07/1988;0,0000
04/07/1988;0,0000
01/07/1988;0,0000
30/06/1988;0,0000
29/06/1988;0,0000
28/06/1988;0,0000
27/06/1988;0,0000
24/06/1988;0,0000
23/06/1988;0,0000
22/06/1988;0,0000
21/06/1988;0,0000
20/06/1988;0,0000
17/06/1988;0,0000
16/06/1988;0,0000
15/06/1988;0,0000
14/06/1988;0,0000
13/06/1988;0,0000
10/06/1988;0,0000
09/06/1988;0,0000
08/06/1988;0,0000
07/06/1988;0,0000
06/06/1988;0,0000
03/06/1988;0,0000
02/06/1988;0,0000
01/06/1988;0,0000
31/05/1988;0,0000
27/05/1988;0,0000
26/05/1988;0,0000
25/05/1988;0,0000
24/05/1988;0,0000
23/05/1988;0,0000
20/05/1988;0,0000
19/05/1988;0,0000
18/05/1988;0,0000
17/05/1988;0,0000
16/05/1988;0,0000
12/05/1988;0,0000
11/05/1988;0,0000
10/05/1988;0,0000
09/05/1988;0,0000
06/05/1988;0,0000
05/05/1988;0,0000
04/05/1988;0,0000
03/05/1988;0,0000
02/05/1988;0,0000
29/04/1988;0,0000
28/04/1988;0,0000
27/04/1988;0,0000
26/04/1988;0,0000
25/04/1988;0,0000
22/04/1988;0,0000
21/04/1988;0,0000
20/04/1988;0,0000
19/04/1988;0,0000
15/04/1988;0,0000
14/04/1988;0,0000
13/04/1988;0,0000
12/04/1988;0,0000
11/04/1988;0,0000
08/04/1988;0,0000
07/04/1988;0,0000
06/04/1988;0,0000
05/04/1988;0,0000
04/04/1988;0,0000
30/03/1988;0,0000
29/03/1988;0,0000
28/03/1988;0,0000
25/03/1988;0,0000
24/03/1988;0,0000
23/03/1988;0,0000
22/03/1988;0,0000
21/03/1988;0,0000
18/03/1988;0,0000
17/03/1988;0,0000
16/03/1988;0,0000
15/03/1988;0,0000
14/03/1988;0,0000
11/03/1988;0,0000
10/03/1988;0,0000
09/03/1988;0,0000
08/03/1988;0,0000
07/03/1988;0,0000
04/03/1988;0,0000
03/03/1988;0,0000
02/03/1988;0,0000
01/03/1988;0,0000
29/02/1988;0,0000
26/02/1988;0,0000
25/02/1988;0,0000
24/02/1988;0,0000
23/02/1988;0,0000
22/02/1988;0,0000
19/02/1988;0,0000
18/02/1988;0,0000
17/02/1988;0,0000
12/02/1988;0,0000
11/02/1988;0,0000
10/02/1988;0,0000
09/02/1988;0,0000
08/02/1988;0,0000
05/02/1988;0,0000
04/02/1988;0,0000
03/02/1988;0,0000
02/02/1988;0,0000
01/02/1988;0,0000
29/01/1988;0,0000
28/01/1988;0,0000
27/01/1988;0,0000
26/01/1988;0,0000
25/01/1988;0,0000
22/01/1988;0,0000
21/01/1988;0,0000
20/01/1988;0,0000
19/01/1988;0,0000
18/01/1988;0,0000
15/01/1988;0,0000
14/01/1988;0,0000
13/01/1988;0,0000
12/01/1988;0,0000
11/01/1988;0,0000
08/01/1988;0,0000
07/01/1988;0,0000
06/01/1988;0,0000
05/01/1988;0,0000
04/01/1988;0,0000
30/12/1987;0,0000
29/12/1987;0,0000
28/12/1987;0,0000
24/12/1987;0,0000
23/12/1987;0,0000
22/12/1987;0,0000
21/12/1987;0,0000
18/12/1987;0,0000
17/12/1987;0,0000
16/12/1987;0,0000
15/12/1987;0,0000
14/12/1987;0,0000
11/12/1987;0,0000
10/12/1987;0,0000
09/12/1987;0,0000
08/12/1987;0,0000
07/12/1987;0,0000
04/12/1987;0,0000
03/12/1987;0,0000
02/12/1987;0,0000
01/12/1987;0,0000
30/11/1987;0,0000
27/11/1987;0,0000
26/11/1987;0,0000
25/11/1987;0,0000
24/11/1987;0,0000
23/11/1987;0,0000
20/11/1987;0,0000
19/11/1987;0,0000
18/11/1987;0,0000
17/11/1987;0,0000
16/11/1987;0,0000
13/11/1987;0,0000
12/11/1987;0,0000
11/11/1987;0,0000
10/11/1987;0,0000
09/11/1987;0,0000
06/11/1987;0,0000
05/11/1987;0,0000
04/11/1987;0,0000
03/11/1987;0,0000
30/10/1987;0,0000
29/10/1987;0,0000
28/10/1987;0,0000
27/10/1987;0,0000
26/10/1987;0,0000
23/10/1987;0,0000
22/10/1987;0,0000
21/10/1987;0,0000
20/10/1987;0,0000
19/10/1987;0,0000
16/10/1987;0,0000
15/10/1987;0,0000
14/10/1987;0,0000
13/10/1987;0,0000
09/10/1987;0,0000
08/10/1987;0,0000
07/10/1987;0,0000
06/10/1987;0,0000
05/10/1987;0,0000
02/10/1987;0,0000
01/10/1987;0,0000
30/09/1987;0,0000
29/09/1987;0,0000
28/09/1987;0,0000
25/09/1987;0,0000
24/09/1987;0,0000
23/09/1987;0,0000
22/09/1987;0,0000
21/09/1987;0,0000
18/09/1987;0,0000
17/09/1987;0,0000
16/09/1987;0,0000
15/09/1987;0,0000
14/09/1987;0,0000
11/09/1987;0,0000
10/09/1987;0,0000
09/09/1987;0,0000
08/09/1987;0,0000
04/09/1987;0,0000
03/09/1987;0,0000
02/09/1987;0,0000
01/09/1987;0,0000
31/08/1987;0,0000
28/08/1987;0,0000
27/08/1987;0,0000
26/08/1987;0,0000
25/08/1987;0,0000
24/08/1987;0,0000
21/08/1987;0,0000
20/08/1987;0,0000
19/08/1987;0,0000
18/08/1987;0,0000
17/08/1987;0,0000
14/08/1987;0,0000
13/08/1987;0,0000
12/08/1987;0,0000
11/08/1987;0,0000
10/08/1987;0,0000
07/08/1987;0,0000
06/08/1987;0,0000
05/08/1987;0,0000
04/08/1987;0,0000
03/08/1987;0,0000
31/07/1987;0,0000
30/07/1987;0,0000
29/07/1987;0,0000
28/07/1987;0,0000
27/07/1987;0,0000
24/07/1987;0,0000
23/07/1987;0,0000
22/07/1987;0,0000
21/07/1987;0,0000
20/07/1987;0,0000
17/07/1987;0,0000
16/07/1987;0,0000
15/07/1987;0,0000
14/07/1987;0,0000
13/07/1987;0,0000
10/07/1987;0,0000
09/07/1987;0,0000
08/07/1987;0,0000
07/07/1987;0,0000
06/07/1987;0,0000
03/07/1987;0,0000
02/07/1987;0,0000
01/07/1987;0,0000
30/06/1987;0,0000
29/06/1987;0,0000
26/06/1987;0,0000
25/06/1987;0,0000
24/06/1987;0,0000
23/06/1987;0,0000
22/06/1987;0,0000
19/06/1987;0,0000
18/06/1987;0,0000
17/06/1987;0,0000
16/06/1987;0,0000
12/06/1987;0,0000
11/06/1987;0,0000
10/06/1987;0,0000
09/06/1987;0,0000
08/06/1987;0,0000
05/06/1987;0,0000
04/06/1987;0,0000
03/06/1987;0,0000
02/06/1987;0,0000
01/06/1987;0,0000
29/05/1987;0,0000
28/05/1987;0,0000
27/05/1987;0,0000
26/05/1987;0,0000
25/05/1987;0,0000
22/05/1987;0,0000
21/05/1987;0,0000
20/05/1987;0,0000
19/05/1987;0,0000
18/05/1987;0,0000
15/05/1987;0,0000
14/05/1987;0,0000
13/05/1987;0,0000
12/05/1987;0,0000
11/05/1987;0,0000
08/05/1987;0,0000
07/05/1987;0,0000
06/05/1987;0,0000
05/05/1987;0,0000
04/05/1987;0,0000
30/04/1987;0,0000
29/04/1987;0,0000
28/04/1987;0,0000
27/04/1987;0,0000
24/04/1987;0,0000
23/04/1987;0,0000
22/04/1987;0,0000
21/04/1987;0,0000
15/04/1987;0,0000
14/04/1987;0,0000
13/04/1987;0,0000
10/04/1987;0,0000
09/04/1987;0,0000
08/04/1987;0,0000
07/04/1987;0,0000
06/04/1987;0,0000
03/04/1987;0,0000
02/04/1987;0,0000
01/04/1987;0,0000
31/03/1987;0,0000
30/03/1987;0,0000
27/03/1987;0,0000
26/03/1987;0,0000
25/03/1987;0,0000
24/03/1987;0,0000
23/03/1987;0,0000
20/03/1987;0,0000
19/03/1987;0,0000
18/03/1987;0,0000
17/03/1987;0,0000
16/03/1987;0,0000
13/03/1987;0,0000
12/03/1987;0,0000
11/03/1987;0,0000
10/03/1987;0,0000
09/03/1987;0,0000
06/03/1987;0,0000
05/03/1987;0,0000
04/03/1987;0,0000
27/02/1987;0,0000
26/02/1987;0,0000
25/02/1987;0,0000
24/02/1987;0,0000
23/02/1987;0,0000
20/02/1987;0,0000
19/02/1987;0,0000
18/02/1987;0,0000
17/02/1987;0,0000
16/02/1987;0,0000
13/02/1987;0,0000
12/02/1987;0,0000
11/02/1987;0,0000
10/02/1987;0,0000
09/02/1987;0,0000
06/02/1987;0,0000
05/02/1987;0,0000
04/02/1987;0,0000
03/02/1987;0,0000
02/02/1987;0,0000
30/01/1987;0,0000
29/01/1987;0,0000
28/01/1987;0,0000
27/01/1987;0,0000
26/01/1987;0,0000
23/01/1987;0,0000
22/01/1987;0,0000
21/01/1987;0,0000
20/01/1987;0,0000
19/01/1987;0,0000
16/01/1987;0,0000
15/01/1987;0,0000
14/01/1987;0,0000
13/01/1987;0,0000
12/01/1987;0,0000
09/01/1987;0,0000
08/01/1987;0,0000
07/01/1987;0,0000
06/01/1987;0,0000
05/01/1987;0,0000
02/01/1987;0,0000
30/12/1986;0,0000
29/12/1986;0,0000
26/12/1986;0,0000
24/12/1986;0,0000
23/12/1986;0,0000
22/12/1986;0,0000
19/12/1986;0,0000
18/12/1986;0,0000
17/12/1986;0,0000
16/12/1986;0,0000
15/12/1986;0,0000
12/12/1986;0,0000
11/12/1986;0,0000
10/12/1986;0,0000
09/12/1986;0,0000
08/12/1986;0,0000
05/12/1986;0,0000
04/12/1986;0,0000
03/12/1986;0,0000
02/12/1986;0,0000
01/12/1986;0,0000
28/11/1986;0,0000
27/11/1986;0,0000
26/11/1986;0,0000
25/11/1986;0,0000
24/11/1986;0,0000
21/11/1986;0,0000
20/11/1986;0,0000
19/11/1986;0,0000
18/11/1986;0,0000
17/11/1986;0,0000
14/11/1986;0,0000
13/11/1986;0,0000
12/11/1986;0,0000
11/11/1986;0,0000
10/11/1986;0,0000
07/11/1986;0,0000
06/11/1986;0,0000
05/11/1986;0,0000
04/11/1986;0,0000
03/11/1986;0,0000
31/10/1986;0,0000
30/10/1986;0,0000
29/10/1986;0,0000
28/10/1986;0,0000
27/10/1986;0,0000
24/10/1986;0,0000
23/10/1986;0,0000
22/10/1986;0,0000
21/10/1986;0,0000
20/10/1986;0,0000
17/10/1986;0,0000
16/10/1986;0,0000
15/10/1986;0,0000
14/10/1986;0,0000
13/10/1986;0,0000
10/10/1986;0,0000
09/10/1986;0,0000
08/10/1986;0,0000
07/10/1986;0,0000
06/10/1986;0,0000
03/10/1986;0,0000
02/10/1986;0,0000
01/10/1986;0,0000
30/09/1986;0,0000
29/09/1986;0,0000
26/09/1986;0,0000
25/09/1986;0,0000
24/09/1986;0,0000
23/09/1986;0,0000
22/09/1986;0,0000
19/09/1986;0,0000
18/09/1986;0,0000
17/09/1986;0,0000
16/09/1986;0,0000
15/09/1986;0,0000
12/09/1986;0,0000
11/09/1986;0,0000
10/09/1986;0,0000
09/09/1986;0,0000
08/09/1986;0,0000
05/09/1986;0,0000
04/09/1986;0,0000
03/09/1986;0,0000
02/09/1986;0,0000
01/09/1986;0,0000
29/08/1986;0,0000
28/08/1986;0,0000
27/08/1986;0,0000
26/08/1986;0,0000
25/08/1986;0,0000
22/08/1986;0,0000
21/08/1986;0,0000
20/08/1986;0,0000
19/08/1986;0,0000
18/08/1986;0,0000
15/08/1986;0,0000
14/08/1986;0,0000
13/08/1986;0,0000
12/08/1986;0,0000
11/08/1986;0,0000
08/08/1986;0,0000
07/08/1986;0,0000
06/08/1986;0,0000
05/08/1986;0,0000
04/08/1986;0,0000
01/08/1986;0,0000
31/07/1986;0,0000
30/07/1986;0,0000
29/07/1986;0,0000
28/07/1986;0,0000
25/07/1986;0,0000
24/07/1986;0,0000
23/07/1986;0,0000
22/07/1986;0,0000
21/07/1986;0,0000
18/07/1986;0,0000
17/07/1986;0,0000
16/07/1986;0,0000
15/07/1986;0,0000
14/07/1986;0,0000
11/07/1986;0,0000
10/07/1986;0,0000
09/07/1986;0,0000
08/07/1986;0,0000
07/07/1986;0,0000
04/07/1986;0,0000
03/07/1986;0,0000
02/07/1986;0,0000
01/07/1986;0,0000
30/06/1986;0,0000
27/06/1986;0,0000
26/06/1986;0,0000
25/06/1986;0,0000
24/06/1986;0,0000
23/06/1986;0,0000
20/06/1986;0,0000
19/06/1986;0,0000
18/06/1986;0,0000
17/06/1986;0,0000
16/06/1986;0,0000
13/06/1986;0,0000
12/06/1986;0,0000
11/06/1986;0,0000
10/06/1986;0,0000
09/06/1986;0,0000
06/06/1986;0,0000
05/06/1986;0,0000
04/06/1986;0,0000
03/06/1986;0,0000
02/06/1986;0,0000
30/05/1986;0,0000
29/05/1986;0,0000
28/05/1986;0,0000
27/05/1986;0,0000
23/05/1986;0,0000
22/05/1986;0,0000
21/05/1986;0,0000
20/05/1986;0,0000
19/05/1986;0,0000
16/05/1986;0,0000
15/05/1986;0,0000
14/05/1986;0,0000
13/05/1986;0,0000
12/05/1986;0,0000
09/05/1986;0,0000
08/05/1986;0,0000
07/05/1986;0,0000
06/05/1986;0,0000
05/05/1986;0,0000
02/05/1986;0,0000
30/04/1986;0,0000
29/04/1986;0,0000
28/04/1986;0,0000
25/04/1986;0,0000
24/04/1986;0,0000
23/04/1986;0,0000
22/04/1986;0,0000
18/04/1986;0,0000
17/04/1986;0,0000
16/04/1986;0,0000
15/04/1986;0,0000
14/04/1986;0,0000
11/04/1986;0,0000
10/04/1986;0,0000
09/04/1986;0,0000
08/04/1986;0,0000
07/04/1986;0,0000
04/04/1986;0,0000
03/04/1986;0,0000
02/04/1986;0,0000
01/04/1986;0,0000
31/03/1986;0,0000
26/03/1986;0,0000
25/03/1986;0,0000
24/03/1986;0,0000
21/03/1986;0,0000
20/03/1986;0,0000
19/03/1986;0,0000
18/03/1986;0,0000
17/03/1986;0,0000
14/03/1986;0,0000
13/03/1986;0,0000
12/03/1986;0,0000
11/03/1986;0,0000
10/03/1986;0,0000
07/03/1986;0,0000
06/03/1986;0,0000
05/03/1986;0,0000
04/03/1986;0,0000
03/03/1986;0,0000
27/02/1986;0,0000
26/02/1986;0,0000
25/02/1986;0,0000
24/02/1986;0,0000
21/02/1986;0,0000
20/02/1986;0,0000
19/02/1986;0,0000
18/02/1986;0,0000
17/02/1986;0,0000
14/02/1986;0,0000
13/02/1986;0,0000
12/02/1986;0,0000
07/02/1986;0,0000
06/02/1986;0,0000
05/02/1986;0,0000
04/02/1986;0,0000
03/02/1986;0,0000
31/01/1986;0,0000
30/01/1986;0,0000
29/01/1986;0,0000
28/01/1986;0,0000
27/01/1986;0,0000
24/01/1986;0,0000
23/01/1986;0,0000
22/01/1986;0,0000
21/01/1986;0,0000
20/01/1986;0,0000
17/01/1986;0,0000
16/01/1986;0,0000
15/01/1986;0,0000
14/01/1986;0,0000
13/01/1986;0,0000
10/01/1986;0,0000
09/01/1986;0,0000
08/01/1986;0,0000
07/01/1986;0,0000
06/01/1986;0,0000
03/01/1986;0,0000
02/01/1986;0,0000
31/12/1985;0,0000
30/12/1985;0,0000
27/12/1985;0,0000
26/12/1985;0,0000
24/12/1985;0,0000
23/12/1985;0,0000
20/12/1985;0,0000
19/12/1985;0,0000
18/12/1985;0,0000
17/12/1985;0,0000
16/12/1985;0,0000
13/12/1985;0,0000
12/12/1985;0,0000
11/12/1985;0,0000
10/12/1985;0,0000
09/12/1985;0,0000
06/12/1985;0,0000
05/12/1985;0,0000
04/12/1985;0,0000
03/12/1985;0,0000
02/12/1985;0,0000
29/11/1985;0,0000
28/11/1985;0,0000
27/11/1985;0,0000
26/11/1985;0,0000
25/11/1985;0,0000
22/11/1985;0,0000
21/11/1985;0,0000
20/11/1985;0,0000
19/11/1985;0,0000
18/11/1985;0,0000
14/11/1985;0,0000
13/11/1985;0,0000
12/11/1985;0,0000
11/11/1985;0,0000
08/11/1985;0,0000
07/11/1985;0,0000
06/11/1985;0,0000
05/11/1985;0,0000
04/11/1985;0,0000
01/11/1985;0,0000
31/10/1985;0,0000
30/10/1985;0,0000
29/10/1985;0,0000
28/10/1985;0,0000
25/10/1985;0,0000
24/10/1985;0,0000
23/10/1985;0,0000
22/10/1985;0,0000
21/10/1985;0,0000
18/10/1985;0,0000
17/10/1985;0,0000
16/10/1985;0,0000
15/10/1985;0,0000
14/10/1985;0,0000
11/10/1985;0,0000
10/10/1985;0,0000
09/10/1985;0,0000
08/10/1985;0,0000
07/10/1985;0,0000
04/10/1985;0,0000
03/10/1985;0,0000
02/10/1985;0,0000
01/10/1985;0,0000
30/09/1985;0,0000
27/09/1985;0,0000
26/09/1985;0,0000
25/09/1985;0,0000
24/09/1985;0,0000
23/09/1985;0,0000
20/09/1985;0,0000
19/09/1985;0,0000
18/09/1985;0,0000
17/09/1985;0,0000
16/09/1985;0,0000
13/09/1985;0,0000
12/09/1985;0,0000
11/09/1985;0,0000
10/09/1985;0,0000
09/09/1985;0,0000
06/09/1985;0,0000
05/09/1985;0,0000
04/09/1985;0,0000
03/09/1985;0,0000
02/09/1985;0,0000
30/08/1985;0,0000
29/08/1985;0,0000
28/08/1985;0,0000
27/08/1985;0,0000
26/08/1985;0,0000
23/08/1985;0,0000
22/08/1985;0,0000
21/08/1985;0,0000
20/08/1985;0,0000
19/08/1985;0,0000
16/08/1985;0,0000
15/08/1985;0,0000
14/08/1985;0,0000
13/08/1985;0,0000
12/08/1985;0,0000
09/08/1985;0,0000
08/08/1985;0,0000
07/08/1985;0,0000
06/08/1985;0,0000
05/08/1985;0,0000
02/08/1985;0,0000
01/08/1985;0,0000
31/07/1985;0,0000
30/07/1985;0,0000
29/07/1985;0,0000
26/07/1985;0,0000
25/07/1985;0,0000
24/07/1985;0,0000
23/07/1985;0,0000
22/07/1985;0,0000
19/07/1985;0,0000
18/07/1985;0,0000
17/07/1985;0,0000
16/07/1985;0,0000
15/07/1985;0,0000
12/07/1985;0,0000
11/07/1985;0,0000
10/07/1985;0,0000
09/07/1985;0,0000
08/07/1985;0,0000
05/07/1985;0,0000
04/07/1985;0,0000
03/07/1985;0,0000
02/07/1985;0,0000
01/07/1985;0,0000
28/06/1985;0,0000
27/06/1985;0,0000
26/06/1985;0,0000
25/06/1985;0,0000
24/06/1985;0,0000
21/06/1985;0,0000
20/06/1985;0,0000
19/06/1985;0,0000
18/06/1985;0,0000
17/06/1985;0,0000
14/06/1985;0,0000
13/06/1985;0,0000
12/06/1985;0,0000
11/06/1985;0,0000
10/06/1985;0,0000
07/06/1985;0,0000
06/06/1985;0,0000
05/06/1985;0,0000
04/06/1985;0,0000
03/06/1985;0,0000
31/05/1985;0,0000
30/05/1985;0,0000
29/05/1985;0,0000
28/05/1985;0,0000
27/05/1985;0,0000
24/05/1985;0,0000
23/05/1985;0,0000
22/05/1985;0,0000
21/05/1985;0,0000
20/05/1985;0,0000
17/05/1985;0,0000
16/05/1985;0,0000
15/05/1985;0,0000
14/05/1985;0,0000
13/05/1985;0,0000
10/05/1985;0,0000
09/05/1985;0,0000
08/05/1985;0,0000
07/05/1985;0,0000
06/05/1985;0,0000
03/05/1985;0,0000
02/05/1985;0,0000
30/04/1985;0,0000
29/04/1985;0,0000
26/04/1985;0,0000
25/04/1985;0,0000
24/04/1985;0,0000
23/04/1985;0,0000
19/04/1985;0,0000
18/04/1985;0,0000
17/04/1985;0,0000
16/04/1985;0,0000
15/04/1985;0,0000
12/04/1985;0,0000
11/04/1985;0,0000
10/04/1985;0,0000
09/04/1985;0,0000
08/04/1985;0,0000
03/04/1985;0,0000
02/04/1985;0,0000
01/04/1985;0,0000
29/03/1985;0,0000
28/03/1985;0,0000
27/03/1985;0,0000
26/03/1985;0,0000
25/03/1985;0,0000
22/03/1985;0,0000
21/03/1985;0,0000
20/03/1985;0,0000
19/03/1985;0,0000
18/03/1985;0,0000
15/03/1985;0,0000
14/03/1985;0,0000
13/03/1985;0,0000
12/03/1985;0,0000
11/03/1985;0,0000
08/03/1985;0,0000
07/03/1985;0,0000
06/03/1985;0,0000
05/03/1985;0,0000
04/03/1985;0,0000
01/03/1985;0,0000
28/02/1985;0,0000
27/02/1985;0,0000
26/02/1985;0,0000
25/02/1985;0,0000
22/02/1985;0,0000
21/02/1985;0,0000
20/02/1985;0,0000
15/02/1985;0,0000
14/02/1985;0,0000
13/02/1985;0,0000
12/02/1985;0,0000
11/02/1985;0,0000
08/02/1985;0,0000
07/02/1985;0,0000
06/02/1985;0,0000
05/02/1985;0,0000
04/02/1985;0,0000
01/02/1985;0,0000
31/01/1985;0,0000
30/01/1985;0,0000
29/01/1985;0,0000
28/01/1985;0,0000
25/01/1985;0,0000
24/01/1985;0,0000
23/01/1985;0,0000
22/01/1985;0,0000
21/01/1985;0,0000
18/01/1985;0,0000
17/01/1985;0,0000
16/01/1985;0,0000
15/01/1985;0,0000
14/01/1985;0,0000
11/01/1985;0,0000
10/01/1985;0,0000
09/01/1985;0,0000
08/01/1985;0,0000
07/01/1985;0,0000
04/01/1985;0,0000
03/01/1985;0,0000
02/01/1985;0,0000
"""
text = StringIO(text_io)
dados = pd.read_csv(text, encoding='ISO-8859-1', skiprows=0, sep=';', skipfooter=12, thousands='.', decimal=',', engine ="python")
text_io = """
"""
text = """
"""

# dados = pd.read_csv("TAXA_CAMBIO_HISTORICO.csv", encoding='ISO-8859-1', skiprows=0, sep=';', skipfooter=12, thousands='.', decimal=',', engine ="python")

text_io = text_io_exp_vinho
text = StringIO(text_io)
dados_vinho = pd.read_csv(text, sep=";")
text_io = """
"""
text = """
"""

# dados_vinho = pd.read_csv("ExpVinho.csv", sep=";") 

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

# st.subheader("Análise Demográfica - Paraguai")

# consumo_2015_2019 = """
# Foi estimado a quantidade de litros consumido de bebidas alcoólicas da população do Paraguai. A quantidade estimada de consumo alcoólico foi através da multiplicação entre quantidade de pessoas maiores de 20 anos e a quantidade de álcool consumido nos respectivos anos, entre 2015 e 2019.
# O gráfico abaixo mostra o estimado de consumo alcoólico do Paraguai e o valor em litros exportado pelo estado do Rio Grande do Sul, entre 2015 a 2019.
# A diferença entre os valores é muito grande, porém é possível verificar que a quantidade exportada segue a tendência do consumo alcoólico do país.
# """
# st.write(consumo_2015_2019)

# corr_retas = """
# A correlação entre essas duas retas é de: **0,9041**.

# Esse crescente consumo de bebidas álcoolicas benefíciou a exportação de derivados de uva do Brasil. A população do Paraguai demandou mais bebidas álcoolicas e nossas vinícolas supriram em parte essa demanda.
# """
# st.write(corr_retas)

# corr_ConsumoVsExportado = df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'].corr(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'])

# corr_ConsumoVsExportado = round(corr_ConsumoVsExportado,4)

# print(f"CORR: {corr_ConsumoVsExportado}")

# df_consumo_alcool_litros_paraguay_2015_over = df_consumo_alcool_litros_paraguay_eua.query('Sex == "Both sexes" and Country == "Paraguay" and Year >= 2015')

# dados_paraguai_anos_15_20_import_vinhos_br_2015_over = dados_paraguai_anos_15_20_import_vinhos_br.query('País == "Paraguai" and Ano >= 2015')

# correlacao_importacaoUSD_pessoasOver20 = dados_paraguai_anos_15_20_import_vinhos_br['import_br_usd'].corr(df_demografico_pop_20_mais['People'])

# Mesclar os DataFrames com base na coluna 'Year'
# df_consumo_alcool_litros_paraguay_2015_over_with_people = pd.merge(
 #    df_consumo_alcool_litros_paraguay_2015_over,
 #    df_demografico_pop_20_mais[['Year', 'People']],
 #    on='Year',
 #    how='left'  # Use 'left' para preservar todas as linhas do DataFrame de consumo
# )

# df_consumo_alcool_litros_paraguay_2015_over_with_people['Liters_Total'] = df_consumo_alcool_litros_paraguay_2015_over_with_people['Liters'] * df_consumo_alcool_litros_paraguay_2015_over_with_people['People']

# dados_paraguai_anos_15_20_import_vinhos_br_2015_over = dados_paraguai_anos_15_20_import_vinhos_br_2015_over.rename(columns={'Ano': 'Year'})
# dados_paraguai_anos_15_20_import_vinhos_br_2015_over

# df_consumo_alcool_litros_paraguay_2015_over_with_people_2 = pd.merge(
  #   df_consumo_alcool_litros_paraguay_2015_over_with_people,
   #  dados_paraguai_anos_15_20_import_vinhos_br_2015_over[['Year', 'Quantidade']],
  #   on='Year',
#     how='left'  # Use 'left' para preservar todas as linhas do DataFrame de consumo
# )

# Configuração do tamanho da figura
# fig, ax = plt.subplots(figsize=(10, 8))

# Definição de cores
# color1 = (128, 0, 128)
# color2 = (190, 142, 230)

# Normalizar os valores RGB para o intervalo [0, 1]
# color1 = tuple(x / 255.0 for x in color1)
# color2 = tuple(x / 255.0 for x in color2)

# Plotar as linhas e adicionar rótulos nos pontos
# plot1 = sns.lineplot(x='Year', y='Liters_Total', data=df_consumo_alcool_litros_paraguay_2015_over_with_people_2, label='Consumo estimado de bebidas alcoólicas', color=color1)
# plot2 = sns.lineplot(x='Year', y='Quantidade', data=df_consumo_alcool_litros_paraguay_2015_over_with_people_2, label='Exportação do Rio Grande do Sul', color=color2)

# Adicionar rótulos nos pontos para o plot1
# for line in range(0, df_consumo_alcool_litros_paraguay_2015_over_with_people_2.shape[0]):
#     plot1.text(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'][line], 
#                df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'][line], 
#                f"{df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Liters_Total'][line]:,.0f}", 
#                ha='center', va='bottom', rotation=45)


# Adicionar rótulos nos pontos para o plot2
# for line in range(0, df_consumo_alcool_litros_paraguay_2015_over_with_people_2.shape[0]):
#     plot2.text(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'][line], 
#                df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'][line], 
#                f"{df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Quantidade'][line]:,.0f}", 
#                ha='center', va='bottom')

# Configurações adicionais do gráfico
# plt.xticks(df_consumo_alcool_litros_paraguay_2015_over_with_people_2['Year'])

# Formate a escala do eixo y para incluir separador de milhar com ponto
# formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x).replace(',', '.'))
# plt.gca().yaxis.set_major_formatter(formatter)

# Coloque um limite para o valor y. Pegue o maior valor e coloque 20% a mais.
# plt.ylim(0, 40000000)

# Adicione rótulos e título ao gráfico
# plt.xlabel('Ano', fontsize=14, labelpad=15)
# plt.ylabel('Quantidade (litros)', fontsize=14, labelpad=15)
# plt.title('Paraguai - Consumo de bebidas alcoólicas x Quantidade Exportada', fontsize=16, pad=20)

# Ajustando o layout para evitar cortes
# plt.tight_layout()

# Adicionando a legenda
# plt.legend()

# Exibindo o gráfico
# st.pyplot(fig)
# st.markdown(
#     "<div style='text-align: center; font-size: 13px;'>Fontes da análise demográfica: População Maior de 20 anos do Paraguai | Consumo de álcool no Paraguai | Exportação do Rio Grande do Sul</div>",
#     unsafe_allow_html=True
# )

st.markdown("<br>", unsafe_allow_html=True)

# Bibliotecas utilizadas
from matplotlib.dates import DateFormatter, MonthLocator, YearLocator
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
# st.image("indicacoes_geograficas.jpg", caption="Fonte: https://www.embrapa.br/uva-e-vinho/indicacoes-geograficas-de-vinhos-do-brasil", use_column_width=True)

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
text_io = """
Cidade,Data de Referência,Temperatura Mediana (°C)
Alegrete,2007-01-01,24.75
Alegrete,2007-02-01,24.05
Alegrete,2007-03-01,23.25
Alegrete,2007-04-01,21.35
Alegrete,2007-05-01,13.45
Alegrete,2007-06-01,12.75
Alegrete,2007-07-01,9.85
Alegrete,2007-08-01,12.1
Alegrete,2007-09-01,18.575000000000003
Alegrete,2007-10-01,20.025
Alegrete,2007-11-01,20.5
Alegrete,2007-12-01,23.8
Alegrete,2008-01-01,24.55
Alegrete,2008-02-01,23.55
Alegrete,2008-03-01,22.575000000000003
Alegrete,2008-04-01,18.425
Alegrete,2008-05-01,14.3
Alegrete,2008-06-01,12.95
Alegrete,2008-07-01,15.275
Alegrete,2008-08-01,14.375
Alegrete,2008-09-01,15.2
Alegrete,2008-10-01,19.4
Alegrete,2008-11-01,23.1
Alegrete,2008-12-01,24.2
Alegrete,2009-01-01,23.85
Alegrete,2009-02-01,24.175
Alegrete,2009-03-01,22.8
Alegrete,2009-04-01,19.15
Alegrete,2009-05-01,17.275
Alegrete,2009-06-01,11.3
Alegrete,2009-07-01,11.0
Alegrete,2009-08-01,14.8
Alegrete,2009-09-01,16.075000000000003
Alegrete,2009-10-01,18.5
Alegrete,2009-11-01,22.75
Alegrete,2009-12-01,24.3
Alegrete,2010-01-01,24.55
Alegrete,2010-02-01,24.6
Alegrete,2010-03-01,21.55
Alegrete,2010-04-01,15.75
Alegrete,2010-05-01,15.4
Alegrete,2010-06-01,14.55
Alegrete,2010-07-01,12.5
Alegrete,2010-08-01,14.325
Alegrete,2010-09-01,16.975
Alegrete,2010-10-01,18.200000000000003
Alegrete,2010-11-01,21.025
Alegrete,2010-12-01,24.15
Alegrete,2011-01-01,25.675
Alegrete,2011-02-01,23.75
Alegrete,2011-03-01,22.125
Alegrete,2011-04-01,19.55
Alegrete,2011-05-01,15.75
Alegrete,2011-06-01,13.3
Alegrete,2011-07-01,13.3
Alegrete,2011-08-01,13.975
Alegrete,2011-09-01,16.725
Alegrete,2011-10-01,18.65
Alegrete,2011-11-01,22.225
Alegrete,2011-12-01,22.55
Alegrete,2012-01-01,25.5
Alegrete,2012-02-01,25.8
Alegrete,2012-03-01,23.175
Alegrete,2012-04-01,18.7
Alegrete,2012-05-01,17.9
Alegrete,2012-06-01,13.35
Alegrete,2012-07-01,11.15
Alegrete,2012-08-01,18.7
Alegrete,2012-09-01,17.950000000000003
Alegrete,2012-10-01,20.85
Alegrete,2012-11-01,23.625
Alegrete,2012-12-01,23.675
Alegrete,2013-01-01,23.3
Alegrete,2013-02-01,23.45
Alegrete,2013-03-01,20.15
Alegrete,2013-04-01,19.4
Alegrete,2013-05-01,15.425
Alegrete,2013-06-01,13.25
Alegrete,2013-07-01,13.6
Alegrete,2013-08-01,11.2
Alegrete,2013-09-01,16.35
Alegrete,2013-10-01,19.4
Alegrete,2013-11-01,21.200000000000003
Alegrete,2013-12-01,27.200000000000003
Alegrete,2014-01-01,25.4
Alegrete,2014-02-01,24.6
Alegrete,2014-03-01,20.55
Alegrete,2014-04-01,19.775
Alegrete,2014-05-01,15.65
Alegrete,2014-06-01,14.2
Alegrete,2014-07-01,14.9
Alegrete,2014-08-01,15.5
Alegrete,2014-09-01,17.35
Alegrete,2014-10-01,20.5
Alegrete,2014-11-01,22.3
Alegrete,2014-12-01,22.5
Alegrete,2015-01-01,
Alegrete,2015-02-01,23.8
Alegrete,2015-03-01,22.75
Alegrete,2015-04-01,19.85
Alegrete,2015-05-01,17.299999999999997
Alegrete,2015-06-01,15.4
Alegrete,2015-07-01,14.1
Alegrete,2015-08-01,18.45
Alegrete,2015-09-01,16.75
Alegrete,2015-10-01,18.25
Alegrete,2015-11-01,20.55
Alegrete,2015-12-01,22.75
Alegrete,2016-01-01,25.25
Alegrete,2016-02-01,24.8
Alegrete,2016-03-01,20.7
Alegrete,2016-04-01,21.55
Alegrete,2016-05-01,14.175
Alegrete,2016-06-01,11.425
Alegrete,2016-07-01,13.0
Alegrete,2016-08-01,15.425
Alegrete,2016-09-01,14.5
Alegrete,2016-10-01,19.35
Alegrete,2016-11-01,21.1
Alegrete,2016-12-01,23.75
Alegrete,2017-01-01,25.4
Alegrete,2017-02-01,
Alegrete,2017-03-01,22.55
Alegrete,2017-04-01,19.225
Alegrete,2017-05-01,16.775
Alegrete,2017-06-01,14.45
Alegrete,2017-07-01,
Alegrete,2017-08-01,16.65
Alegrete,2017-09-01,18.8
Alegrete,2017-10-01,19.5
Alegrete,2017-11-01,20.275
Alegrete,2017-12-01,24.2
Alegrete,2018-01-01,24.075000000000003
Alegrete,2018-02-01,23.375
Alegrete,2018-03-01,21.8
Alegrete,2018-04-01,22.025
Alegrete,2018-05-01,18.05
Alegrete,2018-06-01,11.55
Alegrete,2018-07-01,12.025
Alegrete,2018-08-01,12.65
Alegrete,2018-09-01,18.55
Alegrete,2018-10-01,19.575000000000003
Alegrete,2018-11-01,22.425
Alegrete,2018-12-01,23.375
Alegrete,2019-01-01,24.5
Alegrete,2019-02-01,23.625
Alegrete,2019-03-01,21.575000000000003
Alegrete,2019-04-01,21.25
Alegrete,2019-05-01,17.85
Alegrete,2019-06-01,18.05
Alegrete,2019-07-01,13.25
Alegrete,2019-08-01,14.3
Alegrete,2019-09-01,15.675
Alegrete,2019-10-01,19.05
Alegrete,2019-11-01,21.95
Alegrete,2019-12-01,23.975
Alegrete,2020-01-01,24.75
Alegrete,2020-02-01,24.2
Alegrete,2020-03-01,23.8
Alegrete,2020-04-01,19.950000000000003
Alegrete,2020-05-01,15.7
Alegrete,2020-06-01,14.55
Alegrete,2020-07-01,11.6
Alegrete,2020-08-01,16.275
Alegrete,2020-09-01,16.1
Alegrete,2020-10-01,19.65
Alegrete,2020-11-01,22.25
Alegrete,2020-12-01,23.25
Alegrete,2021-01-01,23.9
Alegrete,2021-02-01,22.725
Alegrete,2021-03-01,21.7
Alegrete,2021-04-01,20.55
Alegrete,2021-05-01,13.95
Alegrete,2021-06-01,12.625
Alegrete,2021-07-01,12.8
Alegrete,2021-08-01,14.9
Alegrete,2021-09-01,17.049999999999997
Alegrete,2021-10-01,18.875
Alegrete,2021-11-01,21.9
Alegrete,2021-12-01,24.0
Alegrete,2022-01-01,27.15
Alegrete,2022-02-01,25.15
Alegrete,2022-03-01,21.2
Alegrete,2022-04-01,18.8
Alegrete,2022-05-01,14.6
Alegrete,2022-06-01,11.95
Alegrete,2022-07-01,
Alegrete,2022-08-01,14.95
Alegrete,2022-09-01,15.3
Alegrete,2022-10-01,17.95
Alegrete,2022-11-01,21.625
Alegrete,2022-12-01,25.225
Bagé,2007-01-01,22.55
Bagé,2007-02-01,23.15
Bagé,2007-03-01,21.65
Bagé,2007-04-01,19.75
Bagé,2007-05-01,12.0
Bagé,2007-06-01,11.4
Bagé,2007-07-01,8.95
Bagé,2007-08-01,10.0
Bagé,2007-09-01,17.174999999999997
Bagé,2007-10-01,18.2
Bagé,2007-11-01,18.6
Bagé,2007-12-01,21.9
Bagé,2008-01-01,22.375
Bagé,2008-02-01,21.65
Bagé,2008-03-01,20.700000000000003
Bagé,2008-04-01,17.1
Bagé,2008-05-01,14.35
Bagé,2008-06-01,11.5
Bagé,2008-07-01,14.1
Bagé,2008-08-01,12.45
Bagé,2008-09-01,12.775
Bagé,2008-10-01,17.525
Bagé,2008-11-01,20.75
Bagé,2008-12-01,21.1
Bagé,2009-01-01,21.4
Bagé,2009-02-01,22.05
Bagé,2009-03-01,21.15
Bagé,2009-04-01,17.75
Bagé,2009-05-01,16.1
Bagé,2009-06-01,10.6
Bagé,2009-07-01,10.1
Bagé,2009-08-01,13.375
Bagé,2009-09-01,14.275
Bagé,2009-10-01,16.05
Bagé,2009-11-01,20.925
Bagé,2009-12-01,21.625
Bagé,2010-01-01,23.025
Bagé,2010-02-01,23.6
Bagé,2010-03-01,21.4
Bagé,2010-04-01,17.95
Bagé,2010-05-01,15.15
Bagé,2010-06-01,13.1
Bagé,2010-07-01,11.65
Bagé,2010-08-01,12.375
Bagé,2010-09-01,15.55
Bagé,2010-10-01,15.75
Bagé,2010-11-01,18.1
Bagé,2010-12-01,22.775
Bagé,2011-01-01,24.475
Bagé,2011-02-01,22.625
Bagé,2011-03-01,20.6
Bagé,2011-04-01,18.05
Bagé,2011-05-01,14.175
Bagé,2011-06-01,11.9
Bagé,2011-07-01,11.75
Bagé,2011-08-01,13.175
Bagé,2011-09-01,14.4
Bagé,2011-10-01,16.9
Bagé,2011-11-01,20.075000000000003
Bagé,2011-12-01,20.3
Bagé,2012-01-01,23.15
Bagé,2012-02-01,23.85
Bagé,2012-03-01,21.25
Bagé,2012-04-01,16.9
Bagé,2012-05-01,16.6
Bagé,2012-06-01,12.0
Bagé,2012-07-01,9.3
Bagé,2012-08-01,17.75
Bagé,2012-09-01,15.975
Bagé,2012-10-01,18.425
Bagé,2012-11-01,20.75
Bagé,2012-12-01,23.5
Bagé,2013-01-01,21.3
Bagé,2013-02-01,22.1
Bagé,2013-03-01,19.15
Bagé,2013-04-01,18.35
Bagé,2013-05-01,14.25
Bagé,2013-06-01,12.175
Bagé,2013-07-01,12.125
Bagé,2013-08-01,9.875
Bagé,2013-09-01,14.8
Bagé,2013-10-01,16.875
Bagé,2013-11-01,19.775
Bagé,2013-12-01,23.450000000000003
Bagé,2014-01-01,23.275
Bagé,2014-02-01,22.5
Bagé,2014-03-01,19.65
Bagé,2014-04-01,18.625
Bagé,2014-05-01,14.8
Bagé,2014-06-01,12.65
Bagé,2014-07-01,14.1
Bagé,2014-08-01,13.875
Bagé,2014-09-01,15.5
Bagé,2014-10-01,18.725
Bagé,2014-11-01,20.05
Bagé,2014-12-01,21.6
Bagé,2015-01-01,22.7
Bagé,2015-02-01,21.9
Bagé,2015-03-01,21.525
Bagé,2015-04-01,18.55
Bagé,2015-05-01,16.0
Bagé,2015-06-01,14.05
Bagé,2015-07-01,12.8
Bagé,2015-08-01,17.0
Bagé,2015-09-01,14.55
Bagé,2015-10-01,15.95
Bagé,2015-11-01,18.7
Bagé,2015-12-01,21.4
Bagé,2016-01-01,23.175
Bagé,2016-02-01,23.8
Bagé,2016-03-01,19.25
Bagé,2016-04-01,20.125
Bagé,2016-05-01,
Bagé,2016-06-01,
Bagé,2016-07-01,11.675
Bagé,2016-08-01,14.025
Bagé,2016-09-01,12.95
Bagé,2016-10-01,17.424999999999997
Bagé,2016-11-01,19.6
Bagé,2016-12-01,22.875
Bagé,2017-01-01,23.1
Bagé,2017-02-01,22.85
Bagé,2017-03-01,20.950000000000003
Bagé,2017-04-01,18.35
Bagé,2017-05-01,15.55
Bagé,2017-06-01,13.75
Bagé,2017-07-01,15.85
Bagé,2017-08-01,15.2
Bagé,2017-09-01,16.85
Bagé,2017-10-01,17.1
Bagé,2017-11-01,18.3
Bagé,2017-12-01,23.225
Bagé,2018-01-01,23.200000000000003
Bagé,2018-02-01,22.4
Bagé,2018-03-01,20.3
Bagé,2018-04-01,20.9
Bagé,2018-05-01,16.950000000000003
Bagé,2018-06-01,11.0
Bagé,2018-07-01,10.8
Bagé,2018-08-01,11.8
Bagé,2018-09-01,16.799999999999997
Bagé,2018-10-01,17.575000000000003
Bagé,2018-11-01,21.25
Bagé,2018-12-01,21.25
Bagé,2019-01-01,23.1
Bagé,2019-02-01,22.450000000000003
Bagé,2019-03-01,20.475
Bagé,2019-04-01,19.025
Bagé,2019-05-01,16.25
Bagé,2019-06-01,17.275
Bagé,2019-07-01,12.175
Bagé,2019-08-01,13.0
Bagé,2019-09-01,14.25
Bagé,2019-10-01,17.725
Bagé,2019-11-01,20.35
Bagé,2019-12-01,22.3
Bagé,2020-01-01,23.075000000000003
Bagé,2020-02-01,22.75
Bagé,2020-03-01,22.55
Bagé,2020-04-01,18.05
Bagé,2020-05-01,14.375
Bagé,2020-06-01,13.7
Bagé,2020-07-01,10.425
Bagé,2020-08-01,15.475
Bagé,2020-09-01,14.05
Bagé,2020-10-01,17.125
Bagé,2020-11-01,19.55
Bagé,2020-12-01,21.4
Bagé,2021-01-01,23.0
Bagé,2021-02-01,21.15
Bagé,2021-03-01,20.625
Bagé,2021-04-01,18.700000000000003
Bagé,2021-05-01,12.725
Bagé,2021-06-01,11.55
Bagé,2021-07-01,12.65
Bagé,2021-08-01,13.35
Bagé,2021-09-01,15.75
Bagé,2021-10-01,17.200000000000003
Bagé,2021-11-01,19.625
Bagé,2021-12-01,21.4
Bagé,2022-01-01,25.1
Bagé,2022-02-01,22.4
Bagé,2022-03-01,20.1
Bagé,2022-04-01,17.75
Bagé,2022-05-01,13.525
Bagé,2022-06-01,11.05
Bagé,2022-07-01,14.4
Bagé,2022-08-01,12.2
Bagé,2022-09-01,13.55
Bagé,2022-10-01,16.0
Bagé,2022-11-01,19.875
Bagé,2022-12-01,22.6
Rio Grande,2007-01-01,23.950000000000003
Rio Grande,2007-02-01,24.0
Rio Grande,2007-03-01,23.3
Rio Grande,2007-04-01,21.5
Rio Grande,2007-05-01,13.9
Rio Grande,2007-06-01,12.25
Rio Grande,2007-07-01,10.675
Rio Grande,2007-08-01,11.2
Rio Grande,2007-09-01,16.0
Rio Grande,2007-10-01,18.700000000000003
Rio Grande,2007-11-01,18.65
Rio Grande,2007-12-01,22.35
Rio Grande,2008-01-01,25.25
Rio Grande,2008-02-01,
Rio Grande,2008-03-01,22.75
Rio Grande,2008-04-01,19.1
Rio Grande,2008-05-01,16.5
Rio Grande,2008-06-01,13.375
Rio Grande,2008-07-01,15.1
Rio Grande,2008-08-01,13.9
Rio Grande,2008-09-01,15.3
Rio Grande,2008-10-01,18.25
Rio Grande,2008-11-01,20.825000000000003
Rio Grande,2008-12-01,21.85
Rio Grande,2009-01-01,22.55
Rio Grande,2009-02-01,23.6
Rio Grande,2009-03-01,22.8
Rio Grande,2009-04-01,20.1
Rio Grande,2009-05-01,17.25
Rio Grande,2009-06-01,12.35
Rio Grande,2009-07-01,11.6
Rio Grande,2009-08-01,13.75
Rio Grande,2009-09-01,17.25
Rio Grande,2009-10-01,
Rio Grande,2009-11-01,21.1
Rio Grande,2009-12-01,22.05
Rio Grande,2010-01-01,24.05
Rio Grande,2010-02-01,25.3
Rio Grande,2010-03-01,23.25
Rio Grande,2010-04-01,20.05
Rio Grande,2010-05-01,17.799999999999997
Rio Grande,2010-06-01,15.0
Rio Grande,2010-07-01,13.2
Rio Grande,2010-08-01,13.5
Rio Grande,2010-09-01,16.375
Rio Grande,2010-10-01,16.9
Rio Grande,2010-11-01,18.875
Rio Grande,2010-12-01,22.5
Rio Grande,2011-01-01,24.4
Rio Grande,2011-02-01,24.0
Rio Grande,2011-03-01,22.3
Rio Grande,2011-04-01,20.1
Rio Grande,2011-05-01,16.4
Rio Grande,2011-06-01,13.75
Rio Grande,2011-07-01,12.25
Rio Grande,2011-08-01,13.25
Rio Grande,2011-09-01,14.925
Rio Grande,2011-10-01,17.75
Rio Grande,2011-11-01,20.35
Rio Grande,2011-12-01,20.875
Rio Grande,2012-01-01,23.3
Rio Grande,2012-02-01,24.75
Rio Grande,2012-03-01,22.975
Rio Grande,2012-04-01,18.85
Rio Grande,2012-05-01,18.4
Rio Grande,2012-06-01,13.05
Rio Grande,2012-07-01,10.95
Rio Grande,2012-08-01,16.7
Rio Grande,2012-09-01,16.85
Rio Grande,2012-10-01,19.200000000000003
Rio Grande,2012-11-01,21.25
Rio Grande,2012-12-01,23.85
Rio Grande,2013-01-01,22.950000000000003
Rio Grande,2013-02-01,23.700000000000003
Rio Grande,2013-03-01,20.9
Rio Grande,2013-04-01,19.65
Rio Grande,2013-05-01,15.725
Rio Grande,2013-06-01,13.5
Rio Grande,2013-07-01,12.6
Rio Grande,2013-08-01,11.6
Rio Grande,2013-09-01,15.5
Rio Grande,2013-10-01,17.75
Rio Grande,2013-11-01,20.4
Rio Grande,2013-12-01,23.0
Rio Grande,2014-01-01,24.450000000000003
Rio Grande,2014-02-01,24.2
Rio Grande,2014-03-01,22.1
Rio Grande,2014-04-01,20.6
Rio Grande,2014-05-01,16.450000000000003
Rio Grande,2014-06-01,15.0
Rio Grande,2014-07-01,15.45
Rio Grande,2014-08-01,14.6
Rio Grande,2014-09-01,16.65
Rio Grande,2014-10-01,19.25
Rio Grande,2014-11-01,21.125
Rio Grande,2014-12-01,23.075000000000003
Rio Grande,2015-01-01,24.4
Rio Grande,2015-02-01,25.700000000000003
Rio Grande,2015-03-01,25.950000000000003
Rio Grande,2015-04-01,20.8
Rio Grande,2015-05-01,18.25
Rio Grande,2015-06-01,14.9
Rio Grande,2015-07-01,14.55
Rio Grande,2015-08-01,17.799999999999997
Rio Grande,2015-09-01,15.75
Rio Grande,2015-10-01,17.1
Rio Grande,2015-11-01,19.25
Rio Grande,2015-12-01,22.4
Rio Grande,2016-01-01,23.75
Rio Grande,2016-02-01,24.5
Rio Grande,2016-03-01,21.625
Rio Grande,2016-04-01,21.65
Rio Grande,2016-05-01,14.925
Rio Grande,2016-06-01,
Rio Grande,2016-07-01,13.15
Rio Grande,2016-08-01,14.0
Rio Grande,2016-09-01,13.75
Rio Grande,2016-10-01,17.35
Rio Grande,2016-11-01,20.0
Rio Grande,2016-12-01,22.5
Rio Grande,2017-01-01,24.05
Rio Grande,2017-02-01,25.325000000000003
Rio Grande,2017-03-01,22.65
Rio Grande,2017-04-01,20.0
Rio Grande,2017-05-01,17.950000000000003
Rio Grande,2017-06-01,15.2
Rio Grande,2017-07-01,16.25
Rio Grande,2017-08-01,
Rio Grande,2017-09-01,18.075000000000003
Rio Grande,2017-10-01,18.675
Rio Grande,2017-11-01,19.4
Rio Grande,2017-12-01,22.05
Rio Grande,2018-01-01,23.75
Rio Grande,2018-02-01,23.1
Rio Grande,2018-03-01,22.0
Rio Grande,2018-04-01,22.35
Rio Grande,2018-05-01,18.0
Rio Grande,2018-06-01,11.875
Rio Grande,2018-07-01,13.05
Rio Grande,2018-08-01,13.2
Rio Grande,2018-09-01,17.0
Rio Grande,2018-10-01,18.0
Rio Grande,2018-11-01,21.3
Rio Grande,2018-12-01,22.025
Rio Grande,2019-01-01,24.3
Rio Grande,2019-02-01,23.75
Rio Grande,2019-03-01,22.1
Rio Grande,2019-04-01,20.35
Rio Grande,2019-05-01,18.700000000000003
Rio Grande,2019-06-01,17.674999999999997
Rio Grande,2019-07-01,12.75
Rio Grande,2019-08-01,13.5
Rio Grande,2019-09-01,14.95
Rio Grande,2019-10-01,18.4
Rio Grande,2019-11-01,21.15
Rio Grande,2019-12-01,22.65
Rio Grande,2020-01-01,23.825000000000003
Rio Grande,2020-02-01,23.700000000000003
Rio Grande,2020-03-01,23.05
Rio Grande,2020-04-01,19.775
Rio Grande,2020-05-01,16.2
Rio Grande,2020-06-01,15.2
Rio Grande,2020-07-01,11.8
Rio Grande,2020-08-01,14.6
Rio Grande,2020-09-01,14.65
Rio Grande,2020-10-01,17.45
Rio Grande,2020-11-01,20.0
Rio Grande,2020-12-01,22.200000000000003
Rio Grande,2021-01-01,24.0
Rio Grande,2021-02-01,23.1
Rio Grande,2021-03-01,22.5
Rio Grande,2021-04-01,20.950000000000003
Rio Grande,2021-05-01,14.4
Rio Grande,2021-06-01,13.95
Rio Grande,2021-07-01,12.325
Rio Grande,2021-08-01,14.15
Rio Grande,2021-09-01,16.6
Rio Grande,2021-10-01,17.75
Rio Grande,2021-11-01,20.450000000000003
Rio Grande,2021-12-01,21.55
Rio Grande,2022-01-01,24.85
Rio Grande,2022-02-01,23.85
Rio Grande,2022-03-01,21.95
Rio Grande,2022-04-01,19.425
Rio Grande,2022-05-01,15.1
Rio Grande,2022-06-01,12.55
Rio Grande,2022-07-01,14.5
Rio Grande,2022-08-01,13.775
Rio Grande,2022-09-01,15.2
Rio Grande,2022-10-01,16.9
Rio Grande,2022-11-01,20.4
Rio Grande,2022-12-01,22.4
Erechim,2007-01-01,21.75
Erechim,2007-02-01,21.0
Erechim,2007-03-01,21.35
Erechim,2007-04-01,18.65
Erechim,2007-05-01,13.15
Erechim,2007-06-01,15.325
Erechim,2007-07-01,11.175
Erechim,2007-08-01,13.575
Erechim,2007-09-01,17.65
Erechim,2007-10-01,18.075000000000003
Erechim,2007-11-01,18.15
Erechim,2007-12-01,21.15
Erechim,2008-01-01,20.700000000000003
Erechim,2008-02-01,20.3
Erechim,2008-03-01,19.15
Erechim,2008-04-01,16.7
Erechim,2008-05-01,14.25
Erechim,2008-06-01,12.15
Erechim,2008-07-01,15.75
Erechim,2008-08-01,15.55
Erechim,2008-09-01,13.825
Erechim,2008-10-01,17.25
Erechim,2008-11-01,18.75
Erechim,2008-12-01,20.475
Erechim,2009-01-01,20.05
Erechim,2009-02-01,20.950000000000003
Erechim,2009-03-01,20.65
Erechim,2009-04-01,18.450000000000003
Erechim,2009-05-01,16.525
Erechim,2009-06-01,11.8
Erechim,2009-07-01,11.05
Erechim,2009-08-01,15.775
Erechim,2009-09-01,15.9
Erechim,2009-10-01,17.2
Erechim,2009-11-01,21.1
Erechim,2009-12-01,21.475
Erechim,2010-01-01,21.45
Erechim,2010-02-01,22.25
Erechim,2010-03-01,19.325000000000003
Erechim,2010-04-01,16.950000000000003
Erechim,2010-05-01,13.525
Erechim,2010-06-01,13.5
Erechim,2010-07-01,13.7
Erechim,2010-08-01,13.95
Erechim,2010-09-01,15.225
Erechim,2010-10-01,15.95
Erechim,2010-11-01,18.55
Erechim,2010-12-01,19.700000000000003
Erechim,2011-01-01,21.450000000000003
Erechim,2011-02-01,20.65
Erechim,2011-03-01,19.05
Erechim,2011-04-01,17.8
Erechim,2011-05-01,14.275
Erechim,2011-06-01,11.975
Erechim,2011-07-01,13.775
Erechim,2011-08-01,14.15
Erechim,2011-09-01,14.4
Erechim,2011-10-01,17.575000000000003
Erechim,2011-11-01,18.675
Erechim,2011-12-01,20.375
Erechim,2012-01-01,20.8
Erechim,2012-02-01,22.5
Erechim,2012-03-01,20.15
Erechim,2012-04-01,17.875
Erechim,2012-05-01,15.025
Erechim,2012-06-01,13.35
Erechim,2012-07-01,12.25
Erechim,2012-08-01,16.65
Erechim,2012-09-01,16.75
Erechim,2012-10-01,17.799999999999997
Erechim,2012-11-01,20.625
Erechim,2012-12-01,21.75
Erechim,2013-01-01,20.05
Erechim,2013-02-01,20.4
Erechim,2013-03-01,17.95
Erechim,2013-04-01,17.200000000000003
Erechim,2013-05-01,15.0
Erechim,2013-06-01,13.475
Erechim,2013-07-01,13.3
Erechim,2013-08-01,12.45
Erechim,2013-09-01,15.15
Erechim,2013-10-01,16.95
Erechim,2013-11-01,19.775
Erechim,2013-12-01,22.025
Erechim,2014-01-01,21.8
Erechim,2014-02-01,21.675
Erechim,2014-03-01,19.15
Erechim,2014-04-01,18.05
Erechim,2014-05-01,18.25
Erechim,2014-06-01,12.75
Erechim,2014-07-01,13.225
Erechim,2014-08-01,15.475
Erechim,2014-09-01,16.35
Erechim,2014-10-01,18.950000000000003
Erechim,2014-11-01,19.8
Erechim,2014-12-01,20.975
Erechim,2015-01-01,20.6
Erechim,2015-02-01,20.65
Erechim,2015-03-01,19.950000000000003
Erechim,2015-04-01,18.15
Erechim,2015-05-01,14.5
Erechim,2015-06-01,14.55
Erechim,2015-07-01,13.475
Erechim,2015-08-01,18.05
Erechim,2015-09-01,16.950000000000003
Erechim,2015-10-01,17.924999999999997
Erechim,2015-11-01,18.9
Erechim,2015-12-01,20.9
Erechim,2016-01-01,22.05
Erechim,2016-02-01,21.5
Erechim,2016-03-01,18.775
Erechim,2016-04-01,21.25
Erechim,2016-05-01,14.45
Erechim,2016-06-01,
Erechim,2016-07-01,12.175
Erechim,2016-08-01,14.35
Erechim,2016-09-01,14.225
Erechim,2016-10-01,17.6
Erechim,2016-11-01,19.5
Erechim,2016-12-01,20.725
Erechim,2017-01-01,21.1
Erechim,2017-02-01,21.4
Erechim,2017-03-01,20.15
Erechim,2017-04-01,17.55
Erechim,2017-05-01,15.575
Erechim,2017-06-01,14.3
Erechim,2017-07-01,14.8
Erechim,2017-08-01,15.325
Erechim,2017-09-01,18.975
Erechim,2017-10-01,17.1
Erechim,2017-11-01,18.175
Erechim,2017-12-01,21.55
Erechim,2018-01-01,20.925
Erechim,2018-02-01,20.05
Erechim,2018-03-01,20.5
Erechim,2018-04-01,21.5
Erechim,2018-05-01,16.2
Erechim,2018-06-01,12.75
Erechim,2018-07-01,14.8
Erechim,2018-08-01,11.7
Erechim,2018-09-01,16.299999999999997
Erechim,2018-10-01,17.225
Erechim,2018-11-01,19.85
Erechim,2018-12-01,21.5
Erechim,2019-01-01,22.575000000000003
Erechim,2019-02-01,20.55
Erechim,2019-03-01,18.825000000000003
Erechim,2019-04-01,18.75
Erechim,2019-05-01,16.450000000000003
Erechim,2019-06-01,16.2
Erechim,2019-07-01,13.75
Erechim,2019-08-01,14.35
Erechim,2019-09-01,16.45
Erechim,2019-10-01,18.775
Erechim,2019-11-01,20.15
Erechim,2019-12-01,21.45
Erechim,2020-01-01,21.35
Erechim,2020-02-01,20.75
Erechim,2020-03-01,21.4
Erechim,2020-04-01,17.3
Erechim,2020-05-01,14.1
Erechim,2020-06-01,14.55
Erechim,2020-07-01,14.25
Erechim,2020-08-01,15.4
Erechim,2020-09-01,17.6
Erechim,2020-10-01,19.35
Erechim,2020-11-01,19.525
Erechim,2020-12-01,21.15
Erechim,2021-01-01,20.65
Erechim,2021-02-01,20.025
Erechim,2021-03-01,19.85
Erechim,2021-04-01,17.45
Erechim,2021-05-01,14.025
Erechim,2021-06-01,12.85
Erechim,2021-07-01,12.45
Erechim,2021-08-01,15.725
Erechim,2021-09-01,20.75
Erechim,2021-10-01,18.675
Erechim,2021-11-01,20.0
Erechim,2021-12-01,22.15
Erechim,2022-01-01,22.5
Erechim,2022-02-01,22.975
Erechim,2022-03-01,
Erechim,2022-04-01,
Erechim,2022-05-01,12.25
Erechim,2022-06-01,12.4
Erechim,2022-07-01,17.0
Erechim,2022-08-01,14.15
Erechim,2022-09-01,16.275
Erechim,2022-10-01,17.35
Erechim,2022-11-01,18.200000000000003
Erechim,2022-12-01,17.45
Bento Gonçalves,2007-01-01,21.975
Bento Gonçalves,2007-02-01,23.05
Bento Gonçalves,2007-03-01,21.4
Bento Gonçalves,2007-04-01,19.450000000000003
Bento Gonçalves,2007-05-01,12.45
Bento Gonçalves,2007-06-01,13.95
Bento Gonçalves,2007-07-01,10.75
Bento Gonçalves,2007-08-01,11.9
Bento Gonçalves,2007-09-01,17.1
Bento Gonçalves,2007-10-01,17.85
Bento Gonçalves,2007-11-01,17.950000000000003
Bento Gonçalves,2007-12-01,20.35
Bento Gonçalves,2008-01-01,20.75
Bento Gonçalves,2008-02-01,20.5
Bento Gonçalves,2008-03-01,20.1
Bento Gonçalves,2008-04-01,17.424999999999997
Bento Gonçalves,2008-05-01,13.55
Bento Gonçalves,2008-06-01,11.85
Bento Gonçalves,2008-07-01,14.5
Bento Gonçalves,2008-08-01,14.05
Bento Gonçalves,2008-09-01,12.95
Bento Gonçalves,2008-10-01,17.0
Bento Gonçalves,2008-11-01,18.75
Bento Gonçalves,2008-12-01,19.7
Bento Gonçalves,2009-01-01,20.3
Bento Gonçalves,2009-02-01,21.1
Bento Gonçalves,2009-03-01,20.700000000000003
Bento Gonçalves,2009-04-01,18.025
Bento Gonçalves,2009-05-01,15.45
Bento Gonçalves,2009-06-01,10.625
Bento Gonçalves,2009-07-01,11.275
Bento Gonçalves,2009-08-01,16.375
Bento Gonçalves,2009-09-01,15.4
Bento Gonçalves,2009-10-01,15.9
Bento Gonçalves,2009-11-01,21.2
Bento Gonçalves,2009-12-01,21.1
Bento Gonçalves,2010-01-01,21.5
Bento Gonçalves,2010-02-01,22.475
Bento Gonçalves,2010-03-01,20.25
Bento Gonçalves,2010-04-01,17.25
Bento Gonçalves,2010-05-01,13.975
Bento Gonçalves,2010-06-01,13.125
Bento Gonçalves,2010-07-01,13.4
Bento Gonçalves,2010-08-01,13.15
Bento Gonçalves,2010-09-01,15.425
Bento Gonçalves,2010-10-01,15.55
Bento Gonçalves,2010-11-01,17.975
Bento Gonçalves,2010-12-01,20.55
Bento Gonçalves,2011-01-01,22.0
Bento Gonçalves,2011-02-01,21.45
Bento Gonçalves,2011-03-01,19.450000000000003
Bento Gonçalves,2011-04-01,17.6
Bento Gonçalves,2011-05-01,14.25
Bento Gonçalves,2011-06-01,11.3
Bento Gonçalves,2011-07-01,12.875
Bento Gonçalves,2011-08-01,13.3
Bento Gonçalves,2011-09-01,14.425
Bento Gonçalves,2011-10-01,17.0
Bento Gonçalves,2011-11-01,19.0
Bento Gonçalves,2011-12-01,19.375
Bento Gonçalves,2012-01-01,21.025
Bento Gonçalves,2012-02-01,22.45
Bento Gonçalves,2012-03-01,20.25
Bento Gonçalves,2012-04-01,17.725
Bento Gonçalves,2012-05-01,16.15
Bento Gonçalves,2012-06-01,13.0
Bento Gonçalves,2012-07-01,10.85
Bento Gonçalves,2012-08-01,17.65
Bento Gonçalves,2012-09-01,15.85
Bento Gonçalves,2012-10-01,18.775
Bento Gonçalves,2012-11-01,20.4
Bento Gonçalves,2012-12-01,22.25
Bento Gonçalves,2013-01-01,20.4
Bento Gonçalves,2013-02-01,21.05
Bento Gonçalves,2013-03-01,17.7
Bento Gonçalves,2013-04-01,17.75
Bento Gonçalves,2013-05-01,15.05
Bento Gonçalves,2013-06-01,13.05
Bento Gonçalves,2013-07-01,12.425
Bento Gonçalves,2013-08-01,10.9
Bento Gonçalves,2013-09-01,14.95
Bento Gonçalves,2013-10-01,16.799999999999997
Bento Gonçalves,2013-11-01,19.85
Bento Gonçalves,2013-12-01,21.55
Bento Gonçalves,2014-01-01,23.0
Bento Gonçalves,2014-02-01,22.2
Bento Gonçalves,2014-03-01,19.85
Bento Gonçalves,2014-04-01,18.375
Bento Gonçalves,2014-05-01,14.6
Bento Gonçalves,2014-06-01,13.75
Bento Gonçalves,2014-07-01,13.95
Bento Gonçalves,2014-08-01,15.075
Bento Gonçalves,2014-09-01,16.525
Bento Gonçalves,2014-10-01,18.1
Bento Gonçalves,2014-11-01,19.825000000000003
Bento Gonçalves,2014-12-01,21.05
Bento Gonçalves,2015-01-01,21.7
Bento Gonçalves,2015-02-01,21.0
Bento Gonçalves,2015-03-01,20.625
Bento Gonçalves,2015-04-01,17.875
Bento Gonçalves,2015-05-01,15.8
Bento Gonçalves,2015-06-01,13.825
Bento Gonçalves,2015-07-01,13.2
Bento Gonçalves,2015-08-01,
Bento Gonçalves,2015-09-01,
Bento Gonçalves,2015-10-01,16.875
Bento Gonçalves,2015-11-01,18.6
Bento Gonçalves,2015-12-01,21.0
Bento Gonçalves,2016-01-01,22.1
Bento Gonçalves,2016-02-01,22.1
Bento Gonçalves,2016-03-01,18.875
Bento Gonçalves,2016-04-01,20.7
Bento Gonçalves,2016-05-01,12.65
Bento Gonçalves,2016-06-01,9.95
Bento Gonçalves,2016-07-01,13.075
Bento Gonçalves,2016-08-01,14.45
Bento Gonçalves,2016-09-01,13.45
Bento Gonçalves,2016-10-01,17.35
Bento Gonçalves,2016-11-01,18.85
Bento Gonçalves,2016-12-01,21.5
Bento Gonçalves,2017-01-01,21.775
Bento Gonçalves,2017-02-01,22.35
Bento Gonçalves,2017-03-01,20.25
Bento Gonçalves,2017-04-01,17.5
Bento Gonçalves,2017-05-01,15.7
Bento Gonçalves,2017-06-01,14.05
Bento Gonçalves,2017-07-01,15.225
Bento Gonçalves,2017-08-01,15.175
Bento Gonçalves,2017-09-01,18.175
Bento Gonçalves,2017-10-01,17.674999999999997
Bento Gonçalves,2017-11-01,17.475
Bento Gonçalves,2017-12-01,21.15
Bento Gonçalves,2018-01-01,20.85
Bento Gonçalves,2018-02-01,20.4
Bento Gonçalves,2018-03-01,20.3
Bento Gonçalves,2018-04-01,19.8
Bento Gonçalves,2018-05-01,16.15
Bento Gonçalves,2018-06-01,11.3
Bento Gonçalves,2018-07-01,12.95
Bento Gonçalves,2018-08-01,11.7
Bento Gonçalves,2018-09-01,16.65
Bento Gonçalves,2018-10-01,17.1
Bento Gonçalves,2018-11-01,19.55
Bento Gonçalves,2018-12-01,21.025
Bento Gonçalves,2019-01-01,23.1
Bento Gonçalves,2019-02-01,20.75
Bento Gonçalves,2019-03-01,19.6
Bento Gonçalves,2019-04-01,18.6
Bento Gonçalves,2019-05-01,14.95
Bento Gonçalves,2019-06-01,16.35
Bento Gonçalves,2019-07-01,12.85
Bento Gonçalves,2019-08-01,13.15
Bento Gonçalves,2019-09-01,14.4
Bento Gonçalves,2019-10-01,17.7
Bento Gonçalves,2019-11-01,19.15
Bento Gonçalves,2019-12-01,22.15
Bento Gonçalves,2020-01-01,21.4
Bento Gonçalves,2020-02-01,21.525
Bento Gonçalves,2020-03-01,21.55
Bento Gonçalves,2020-04-01,17.725
Bento Gonçalves,2020-05-01,14.95
Bento Gonçalves,2020-06-01,15.075
Bento Gonçalves,2020-07-01,11.1
Bento Gonçalves,2020-08-01,14.55
Bento Gonçalves,2020-09-01,16.049999999999997
Bento Gonçalves,2020-10-01,17.825000000000003
Bento Gonçalves,2020-11-01,18.35
Bento Gonçalves,2020-12-01,
Bento Gonçalves,2021-01-01,21.35
Bento Gonçalves,2021-02-01,20.425
Bento Gonçalves,2021-03-01,20.0
Bento Gonçalves,2021-04-01,18.025
Bento Gonçalves,2021-05-01,12.725
Bento Gonçalves,2021-06-01,12.4
Bento Gonçalves,2021-07-01,12.2
Bento Gonçalves,2021-08-01,15.225
Bento Gonçalves,2021-09-01,16.0
Bento Gonçalves,2021-10-01,17.0
Bento Gonçalves,2021-11-01,19.35
Bento Gonçalves,2021-12-01,21.1
Bento Gonçalves,2022-01-01,23.35
Bento Gonçalves,2022-02-01,21.8
Bento Gonçalves,2022-03-01,19.425
Bento Gonçalves,2022-04-01,17.5
Bento Gonçalves,2022-05-01,13.55
Bento Gonçalves,2022-06-01,12.25
Bento Gonçalves,2022-07-01,16.525
Bento Gonçalves,2022-08-01,12.9
Bento Gonçalves,2022-09-01,13.6
Bento Gonçalves,2022-10-01,16.15
Bento Gonçalves,2022-11-01,18.25
Bento Gonçalves,2022-12-01,20.950000000000003
"""
text = StringIO(text_io)
analise_mediana_mensal = pd.read_csv(text, sep=",", parse_dates=["Data de Referência"])
text_io = """
"""
text = """
"""
# analise_mediana_mensal = pd.read_csv("analise_mediana_mensal.csv", parse_dates=["Data de Referência"])

text_io = """
Cidade,Data de Referência,Precipitação (mm)
Alegrete,2007-01-01,86.4
Alegrete,2007-02-01,208.6
Alegrete,2007-03-01,196.2
Alegrete,2007-04-01,112.8
Alegrete,2007-05-01,46.2
Alegrete,2007-06-01,99.4
Alegrete,2007-07-01,50.2
Alegrete,2007-08-01,99.6
Alegrete,2007-09-01,159.4
Alegrete,2007-10-01,162.4
Alegrete,2007-11-01,88.0
Alegrete,2007-12-01,44.0
Alegrete,2008-01-01,162.79999999999998
Alegrete,2008-02-01,147.0
Alegrete,2008-03-01,87.4
Alegrete,2008-04-01,86.2
Alegrete,2008-05-01,137.79999999999998
Alegrete,2008-06-01,138.2
Alegrete,2008-07-01,181.8
Alegrete,2008-08-01,109.2
Alegrete,2008-09-01,93.2
Alegrete,2008-10-01,280.4
Alegrete,2008-11-01,28.2
Alegrete,2008-12-01,39.6
Alegrete,2009-01-01,29.599999999999998
Alegrete,2009-02-01,106.0
Alegrete,2009-03-01,143.2
Alegrete,2009-04-01,23.2
Alegrete,2009-05-01,84.8
Alegrete,2009-06-01,37.8
Alegrete,2009-07-01,61.2
Alegrete,2009-08-01,86.4
Alegrete,2009-09-01,205.4
Alegrete,2009-10-01,120.2
Alegrete,2009-11-01,382.0
Alegrete,2009-12-01,61.599999999999994
Alegrete,2010-01-01,395.6
Alegrete,2010-02-01,149.2
Alegrete,2010-03-01,38.0
Alegrete,2010-04-01,6.799999999999999
Alegrete,2010-05-01,100.2
Alegrete,2010-06-01,50.800000000000004
Alegrete,2010-07-01,247.2
Alegrete,2010-08-01,19.0
Alegrete,2010-09-01,320.0
Alegrete,2010-10-01,56.6
Alegrete,2010-11-01,23.6
Alegrete,2010-12-01,95.8
Alegrete,2011-01-01,90.60000000000001
Alegrete,2011-02-01,234.8
Alegrete,2011-03-01,141.2
Alegrete,2011-04-01,139.2
Alegrete,2011-05-01,63.8
Alegrete,2011-06-01,90.2
Alegrete,2011-07-01,112.60000000000001
Alegrete,2011-08-01,136.0
Alegrete,2011-09-01,78.0
Alegrete,2011-10-01,177.2
Alegrete,2011-11-01,76.0
Alegrete,2011-12-01,117.0
Alegrete,2012-01-01,6.2
Alegrete,2012-02-01,83.60000000000001
Alegrete,2012-03-01,26.4
Alegrete,2012-04-01,120.0
Alegrete,2012-05-01,42.4
Alegrete,2012-06-01,60.2
Alegrete,2012-07-01,86.0
Alegrete,2012-08-01,60.2
Alegrete,2012-09-01,85.6
Alegrete,2012-10-01,124.6
Alegrete,2012-11-01,42.4
Alegrete,2012-12-01,373.4
Alegrete,2013-01-01,124.0
Alegrete,2013-02-01,213.8
Alegrete,2013-03-01,184.6
Alegrete,2013-04-01,133.8
Alegrete,2013-05-01,194.6
Alegrete,2013-06-01,42.0
Alegrete,2013-07-01,147.4
Alegrete,2013-08-01,42.2
Alegrete,2013-09-01,33.4
Alegrete,2013-10-01,100.2
Alegrete,2013-11-01,202.79999999999998
Alegrete,2013-12-01,12.200000000000001
Alegrete,2014-01-01,214.0
Alegrete,2014-02-01,136.8
Alegrete,2014-03-01,233.8
Alegrete,2014-04-01,44.2
Alegrete,2014-05-01,229.4
Alegrete,2014-06-01,114.8
Alegrete,2014-07-01,115.8
Alegrete,2014-08-01,20.8
Alegrete,2014-09-01,0.0
Alegrete,2014-10-01,132.4
Alegrete,2014-11-01,138.4
Alegrete,2014-12-01,179.4
Alegrete,2015-01-01,0.0
Alegrete,2015-02-01,101.2
Alegrete,2015-03-01,74.4
Alegrete,2015-04-01,46.2
Alegrete,2015-05-01,142.0
Alegrete,2015-06-01,106.4
Alegrete,2015-07-01,169.6
Alegrete,2015-08-01,82.0
Alegrete,2015-09-01,85.2
Alegrete,2015-10-01,386.4
Alegrete,2015-11-01,165.6
Alegrete,2015-12-01,422.2
Alegrete,2016-01-01,108.8
Alegrete,2016-02-01,158.6
Alegrete,2016-03-01,135.0
Alegrete,2016-04-01,235.0
Alegrete,2016-05-01,101.8
Alegrete,2016-06-01,77.6
Alegrete,2016-07-01,86.6
Alegrete,2016-08-01,99.6
Alegrete,2016-09-01,29.6
Alegrete,2016-10-01,287.8
Alegrete,2016-11-01,226.0
Alegrete,2016-12-01,191.4
Alegrete,2017-01-01,8.8
Alegrete,2017-02-01,0.0
Alegrete,2017-03-01,0.0
Alegrete,2017-04-01,213.8
Alegrete,2017-05-01,276.6
Alegrete,2017-06-01,82.0
Alegrete,2017-07-01,0.0
Alegrete,2017-08-01,168.2
Alegrete,2017-09-01,107.0
Alegrete,2017-10-01,163.6
Alegrete,2017-11-01,95.2
Alegrete,2017-12-01,117.2
Alegrete,2018-01-01,140.0
Alegrete,2018-02-01,109.2
Alegrete,2018-03-01,197.6
Alegrete,2018-04-01,89.60000000000001
Alegrete,2018-05-01,148.0
Alegrete,2018-06-01,146.4
Alegrete,2018-07-01,50.8
Alegrete,2018-08-01,201.4
Alegrete,2018-09-01,202.2
Alegrete,2018-10-01,200.4
Alegrete,2018-11-01,179.2
Alegrete,2018-12-01,150.4
Alegrete,2019-01-01,523.2
Alegrete,2019-02-01,47.2
Alegrete,2019-03-01,124.0
Alegrete,2019-04-01,61.4
Alegrete,2019-05-01,188.2
Alegrete,2019-06-01,11.8
Alegrete,2019-07-01,152.0
Alegrete,2019-08-01,45.6
Alegrete,2019-09-01,62.199999999999996
Alegrete,2019-10-01,238.0
Alegrete,2019-11-01,157.6
Alegrete,2019-12-01,39.4
Alegrete,2020-01-01,77.6
Alegrete,2020-02-01,83.2
Alegrete,2020-03-01,33.8
Alegrete,2020-04-01,26.6
Alegrete,2020-05-01,187.4
Alegrete,2020-06-01,167.4
Alegrete,2020-07-01,43.4
Alegrete,2020-08-01,34.0
Alegrete,2020-09-01,172.4
Alegrete,2020-10-01,89.8
Alegrete,2020-11-01,112.2
Alegrete,2020-12-01,128.4
Alegrete,2021-01-01,117.2
Alegrete,2021-02-01,84.8
Alegrete,2021-03-01,79.2
Alegrete,2021-04-01,67.2
Alegrete,2021-05-01,203.0
Alegrete,2021-06-01,192.0
Alegrete,2021-07-01,21.2
Alegrete,2021-08-01,26.2
Alegrete,2021-09-01,284.8
Alegrete,2021-10-01,83.39999999999999
Alegrete,2021-11-01,63.2
Alegrete,2021-12-01,71.6
Alegrete,2022-01-01,40.0
Alegrete,2022-02-01,118.0
Alegrete,2022-03-01,174.4
Alegrete,2022-04-01,202.4
Alegrete,2022-05-01,71.8
Alegrete,2022-06-01,49.400000000000006
Alegrete,2022-07-01,0.0
Alegrete,2022-08-01,37.2
Alegrete,2022-09-01,51.199999999999996
Alegrete,2022-10-01,73.0
Alegrete,2022-11-01,77.0
Alegrete,2022-12-01,74.0
Bagé,2007-01-01,52.4
Bagé,2007-02-01,117.8
Bagé,2007-03-01,91.6
Bagé,2007-04-01,62.8
Bagé,2007-05-01,27.4
Bagé,2007-06-01,195.4
Bagé,2007-07-01,74.4
Bagé,2007-08-01,184.0
Bagé,2007-09-01,66.0
Bagé,2007-10-01,161.6
Bagé,2007-11-01,37.8
Bagé,2007-12-01,85.0
Bagé,2008-01-01,75.60000000000001
Bagé,2008-02-01,126.2
Bagé,2008-03-01,56.2
Bagé,2008-04-01,78.0
Bagé,2008-05-01,93.0
Bagé,2008-06-01,181.0
Bagé,2008-07-01,104.0
Bagé,2008-08-01,138.0
Bagé,2008-09-01,82.0
Bagé,2008-10-01,86.8
Bagé,2008-11-01,59.2
Bagé,2008-12-01,85.6
Bagé,2009-01-01,124.2
Bagé,2009-02-01,142.0
Bagé,2009-03-01,56.6
Bagé,2009-04-01,3.2
Bagé,2009-05-01,136.0
Bagé,2009-06-01,42.0
Bagé,2009-07-01,53.6
Bagé,2009-08-01,207.2
Bagé,2009-09-01,221.8
Bagé,2009-10-01,107.4
Bagé,2009-11-01,473.4
Bagé,2009-12-01,120.2
Bagé,2010-01-01,138.4
Bagé,2010-02-01,181.20000000000002
Bagé,2010-03-01,80.60000000000001
Bagé,2010-04-01,85.8
Bagé,2010-05-01,73.2
Bagé,2010-06-01,92.0
Bagé,2010-07-01,259.8
Bagé,2010-08-01,39.4
Bagé,2010-09-01,115.60000000000001
Bagé,2010-10-01,0.2
Bagé,2010-11-01,4.6
Bagé,2010-12-01,57.4
Bagé,2011-01-01,93.6
Bagé,2011-02-01,68.4
Bagé,2011-03-01,135.0
Bagé,2011-04-01,86.2
Bagé,2011-05-01,38.2
Bagé,2011-06-01,111.0
Bagé,2011-07-01,75.0
Bagé,2011-08-01,66.6
Bagé,2011-09-01,63.6
Bagé,2011-10-01,87.4
Bagé,2011-11-01,36.4
Bagé,2011-12-01,52.8
Bagé,2012-01-01,43.6
Bagé,2012-02-01,224.0
Bagé,2012-03-01,20.4
Bagé,2012-04-01,95.8
Bagé,2012-05-01,14.4
Bagé,2012-06-01,109.8
Bagé,2012-07-01,92.0
Bagé,2012-08-01,99.4
Bagé,2012-09-01,123.2
Bagé,2012-10-01,187.20000000000002
Bagé,2012-11-01,75.4
Bagé,2012-12-01,174.0
Bagé,2013-01-01,181.79999999999998
Bagé,2013-02-01,119.8
Bagé,2013-03-01,32.2
Bagé,2013-04-01,78.6
Bagé,2013-05-01,154.4
Bagé,2013-06-01,64.4
Bagé,2013-07-01,47.4
Bagé,2013-08-01,115.6
Bagé,2013-09-01,167.8
Bagé,2013-10-01,196.4
Bagé,2013-11-01,205.6
Bagé,2013-12-01,84.8
Bagé,2014-01-01,285.0
Bagé,2014-02-01,209.6
Bagé,2014-03-01,237.20000000000002
Bagé,2014-04-01,88.0
Bagé,2014-05-01,35.0
Bagé,2014-06-01,40.4
Bagé,2014-07-01,175.0
Bagé,2014-08-01,66.6
Bagé,2014-09-01,179.2
Bagé,2014-10-01,278.0
Bagé,2014-11-01,115.8
Bagé,2014-12-01,188.0
Bagé,2015-01-01,207.4
Bagé,2015-02-01,87.8
Bagé,2015-03-01,32.4
Bagé,2015-04-01,21.2
Bagé,2015-05-01,126.2
Bagé,2015-06-01,207.20000000000002
Bagé,2015-07-01,211.4
Bagé,2015-08-01,106.8
Bagé,2015-09-01,254.4
Bagé,2015-10-01,392.4
Bagé,2015-11-01,93.4
Bagé,2015-12-01,239.79999999999998
Bagé,2016-01-01,81.60000000000001
Bagé,2016-02-01,114.2
Bagé,2016-03-01,192.8
Bagé,2016-04-01,338.0
Bagé,2016-05-01,0.0
Bagé,2016-06-01,0.0
Bagé,2016-07-01,0.0
Bagé,2016-08-01,95.0
Bagé,2016-09-01,55.0
Bagé,2016-10-01,119.2
Bagé,2016-11-01,101.2
Bagé,2016-12-01,78.8
Bagé,2017-01-01,163.4
Bagé,2017-02-01,97.6
Bagé,2017-03-01,5.0
Bagé,2017-04-01,147.8
Bagé,2017-05-01,254.6
Bagé,2017-06-01,118.8
Bagé,2017-07-01,32.6
Bagé,2017-08-01,165.4
Bagé,2017-09-01,225.0
Bagé,2017-10-01,245.20000000000002
Bagé,2017-11-01,26.8
Bagé,2017-12-01,53.4
Bagé,2018-01-01,42.8
Bagé,2018-02-01,57.4
Bagé,2018-03-01,128.8
Bagé,2018-04-01,92.4
Bagé,2018-05-01,111.0
Bagé,2018-06-01,67.8
Bagé,2018-07-01,166.6
Bagé,2018-08-01,206.6
Bagé,2018-09-01,135.4
Bagé,2018-10-01,61.800000000000004
Bagé,2018-11-01,97.4
Bagé,2018-12-01,102.2
Bagé,2019-01-01,478.0
Bagé,2019-02-01,46.8
Bagé,2019-03-01,24.8
Bagé,2019-04-01,86.4
Bagé,2019-05-01,138.0
Bagé,2019-06-01,29.8
Bagé,2019-07-01,159.6
Bagé,2019-08-01,105.2
Bagé,2019-09-01,102.0
Bagé,2019-10-01,397.4
Bagé,2019-11-01,103.2
Bagé,2019-12-01,44.6
Bagé,2020-01-01,105.8
Bagé,2020-02-01,40.2
Bagé,2020-03-01,21.4
Bagé,2020-04-01,83.0
Bagé,2020-05-01,162.6
Bagé,2020-06-01,188.0
Bagé,2020-07-01,54.2
Bagé,2020-08-01,78.0
Bagé,2020-09-01,104.6
Bagé,2020-10-01,77.6
Bagé,2020-11-01,27.0
Bagé,2020-12-01,89.6
Bagé,2021-01-01,145.4
Bagé,2021-02-01,213.6
Bagé,2021-03-01,112.4
Bagé,2021-04-01,24.8
Bagé,2021-05-01,60.2
Bagé,2021-06-01,140.6
Bagé,2021-07-01,31.400000000000002
Bagé,2021-08-01,100.0
Bagé,2021-09-01,205.0
Bagé,2021-10-01,59.2
Bagé,2021-11-01,26.4
Bagé,2021-12-01,49.0
Bagé,2022-01-01,91.2
Bagé,2022-02-01,141.4
Bagé,2022-03-01,90.4
Bagé,2022-04-01,199.8
Bagé,2022-05-01,62.0
Bagé,2022-06-01,86.4
Bagé,2022-07-01,189.2
Bagé,2022-08-01,163.6
Bagé,2022-09-01,69.4
Bagé,2022-10-01,139.0
Bagé,2022-11-01,45.0
Bagé,2022-12-01,59.2
Rio Grande,2007-01-01,28.6
Rio Grande,2007-02-01,84.8
Rio Grande,2007-03-01,130.8
Rio Grande,2007-04-01,135.4
Rio Grande,2007-05-01,103.6
Rio Grande,2007-06-01,261.59999999999997
Rio Grande,2007-07-01,105.4
Rio Grande,2007-08-01,202.2
Rio Grande,2007-09-01,119.4
Rio Grande,2007-10-01,112.0
Rio Grande,2007-11-01,38.4
Rio Grande,2007-12-01,55.2
Rio Grande,2008-01-01,0.2
Rio Grande,2008-02-01,0.0
Rio Grande,2008-03-01,19.2
Rio Grande,2008-04-01,30.0
Rio Grande,2008-05-01,167.2
Rio Grande,2008-06-01,61.4
Rio Grande,2008-07-01,89.6
Rio Grande,2008-08-01,238.8
Rio Grande,2008-09-01,118.2
Rio Grande,2008-10-01,32.2
Rio Grande,2008-11-01,34.8
Rio Grande,2008-12-01,31.8
Rio Grande,2009-01-01,102.0
Rio Grande,2009-02-01,205.4
Rio Grande,2009-03-01,103.2
Rio Grande,2009-04-01,33.4
Rio Grande,2009-05-01,71.2
Rio Grande,2009-06-01,116.6
Rio Grande,2009-07-01,32.4
Rio Grande,2009-08-01,134.6
Rio Grande,2009-09-01,0.6000000000000001
Rio Grande,2009-10-01,0.0
Rio Grande,2009-11-01,158.6
Rio Grande,2009-12-01,91.2
Rio Grande,2010-01-01,3.4000000000000004
Rio Grande,2010-02-01,258.0
Rio Grande,2010-03-01,32.0
Rio Grande,2010-04-01,102.2
Rio Grande,2010-05-01,163.2
Rio Grande,2010-06-01,87.0
Rio Grande,2010-07-01,215.2
Rio Grande,2010-08-01,11.8
Rio Grande,2010-09-01,27.8
Rio Grande,2010-10-01,10.6
Rio Grande,2010-11-01,38.6
Rio Grande,2010-12-01,41.4
Rio Grande,2011-01-01,35.6
Rio Grande,2011-02-01,133.2
Rio Grande,2011-03-01,281.4
Rio Grande,2011-04-01,98.0
Rio Grande,2011-05-01,146.2
Rio Grande,2011-06-01,126.6
Rio Grande,2011-07-01,41.8
Rio Grande,2011-08-01,147.2
Rio Grande,2011-09-01,62.6
Rio Grande,2011-10-01,63.4
Rio Grande,2011-11-01,52.0
Rio Grande,2011-12-01,53.0
Rio Grande,2012-01-01,28.0
Rio Grande,2012-02-01,124.8
Rio Grande,2012-03-01,85.80000000000001
Rio Grande,2012-04-01,84.6
Rio Grande,2012-05-01,11.6
Rio Grande,2012-06-01,81.2
Rio Grande,2012-07-01,117.6
Rio Grande,2012-08-01,110.8
Rio Grande,2012-09-01,132.2
Rio Grande,2012-10-01,36.8
Rio Grande,2012-11-01,36.0
Rio Grande,2012-12-01,138.2
Rio Grande,2013-01-01,78.8
Rio Grande,2013-02-01,194.8
Rio Grande,2013-03-01,31.2
Rio Grande,2013-04-01,149.4
Rio Grande,2013-05-01,89.39999999999999
Rio Grande,2013-06-01,128.4
Rio Grande,2013-07-01,73.4
Rio Grande,2013-08-01,112.4
Rio Grande,2013-09-01,120.8
Rio Grande,2013-10-01,119.2
Rio Grande,2013-11-01,148.2
Rio Grande,2013-12-01,70.4
Rio Grande,2014-01-01,201.4
Rio Grande,2014-02-01,170.4
Rio Grande,2014-03-01,168.4
Rio Grande,2014-04-01,55.4
Rio Grande,2014-05-01,36.4
Rio Grande,2014-06-01,149.0
Rio Grande,2014-07-01,200.2
Rio Grande,2014-08-01,58.8
Rio Grande,2014-09-01,109.4
Rio Grande,2014-10-01,254.4
Rio Grande,2014-11-01,71.4
Rio Grande,2014-12-01,145.0
Rio Grande,2015-01-01,186.4
Rio Grande,2015-02-01,0.7999999999999999
Rio Grande,2015-03-01,1.8
Rio Grande,2015-04-01,4.8
Rio Grande,2015-05-01,126.8
Rio Grande,2015-06-01,122.8
Rio Grande,2015-07-01,148.0
Rio Grande,2015-08-01,62.2
Rio Grande,2015-09-01,278.8
Rio Grande,2015-10-01,203.8
Rio Grande,2015-11-01,124.2
Rio Grande,2015-12-01,136.6
Rio Grande,2016-01-01,66.0
Rio Grande,2016-02-01,151.0
Rio Grande,2016-03-01,189.8
Rio Grande,2016-04-01,188.6
Rio Grande,2016-05-01,0.6000000000000001
Rio Grande,2016-06-01,0.0
Rio Grande,2016-07-01,30.6
Rio Grande,2016-08-01,121.6
Rio Grande,2016-09-01,87.6
Rio Grande,2016-10-01,76.8
Rio Grande,2016-11-01,105.39999999999999
Rio Grande,2016-12-01,82.0
Rio Grande,2017-01-01,61.8
Rio Grande,2017-02-01,74.8
Rio Grande,2017-03-01,169.2
Rio Grande,2017-04-01,93.4
Rio Grande,2017-05-01,175.79999999999998
Rio Grande,2017-06-01,35.6
Rio Grande,2017-07-01,31.200000000000003
Rio Grande,2017-08-01,0.0
Rio Grande,2017-09-01,27.4
Rio Grande,2017-10-01,232.4
Rio Grande,2017-11-01,30.8
Rio Grande,2017-12-01,30.2
Rio Grande,2018-01-01,97.2
Rio Grande,2018-02-01,65.4
Rio Grande,2018-03-01,76.0
Rio Grande,2018-04-01,82.0
Rio Grande,2018-05-01,54.800000000000004
Rio Grande,2018-06-01,0.0
Rio Grande,2018-07-01,225.8
Rio Grande,2018-08-01,75.4
Rio Grande,2018-09-01,147.6
Rio Grande,2018-10-01,19.8
Rio Grande,2018-11-01,0.0
Rio Grande,2018-12-01,46.2
Rio Grande,2019-01-01,222.20000000000002
Rio Grande,2019-02-01,31.799999999999997
Rio Grande,2019-03-01,23.599999999999998
Rio Grande,2019-04-01,63.8
Rio Grande,2019-05-01,44.2
Rio Grande,2019-06-01,38.4
Rio Grande,2019-07-01,120.60000000000001
Rio Grande,2019-08-01,97.4
Rio Grande,2019-09-01,163.6
Rio Grande,2019-10-01,196.6
Rio Grande,2019-11-01,45.8
Rio Grande,2019-12-01,38.800000000000004
Rio Grande,2020-01-01,38.4
Rio Grande,2020-02-01,25.4
Rio Grande,2020-03-01,30.6
Rio Grande,2020-04-01,50.6
Rio Grande,2020-05-01,100.8
Rio Grande,2020-06-01,226.4
Rio Grande,2020-07-01,82.0
Rio Grande,2020-08-01,44.2
Rio Grande,2020-09-01,158.2
Rio Grande,2020-10-01,122.8
Rio Grande,2020-11-01,29.8
Rio Grande,2020-12-01,119.0
Rio Grande,2021-01-01,192.4
Rio Grande,2021-02-01,156.4
Rio Grande,2021-03-01,140.4
Rio Grande,2021-04-01,41.8
Rio Grande,2021-05-01,25.6
Rio Grande,2021-06-01,83.0
Rio Grande,2021-07-01,64.2
Rio Grande,2021-08-01,112.0
Rio Grande,2021-09-01,172.8
Rio Grande,2021-10-01,63.0
Rio Grande,2021-11-01,49.6
Rio Grande,2021-12-01,18.2
Rio Grande,2022-01-01,70.4
Rio Grande,2022-02-01,50.8
Rio Grande,2022-03-01,65.4
Rio Grande,2022-04-01,123.8
Rio Grande,2022-05-01,57.199999999999996
Rio Grande,2022-06-01,84.6
Rio Grande,2022-07-01,173.8
Rio Grande,2022-08-01,118.0
Rio Grande,2022-09-01,56.6
Rio Grande,2022-10-01,93.2
Rio Grande,2022-11-01,49.8
Rio Grande,2022-12-01,17.4
Erechim,2007-01-01,162.8
Erechim,2007-02-01,134.4
Erechim,2007-03-01,119.0
Erechim,2007-04-01,5.6000000000000005
Erechim,2007-05-01,212.4
Erechim,2007-06-01,42.2
Erechim,2007-07-01,197.4
Erechim,2007-08-01,120.2
Erechim,2007-09-01,87.4
Erechim,2007-10-01,166.20000000000002
Erechim,2007-11-01,158.8
Erechim,2007-12-01,118.2
Erechim,2008-01-01,86.39999999999999
Erechim,2008-02-01,97.6
Erechim,2008-03-01,139.4
Erechim,2008-04-01,218.8
Erechim,2008-05-01,71.0
Erechim,2008-06-01,115.4
Erechim,2008-07-01,32.4
Erechim,2008-08-01,115.8
Erechim,2008-09-01,97.2
Erechim,2008-10-01,354.6
Erechim,2008-11-01,163.0
Erechim,2008-12-01,44.2
Erechim,2009-01-01,144.4
Erechim,2009-02-01,169.0
Erechim,2009-03-01,36.0
Erechim,2009-04-01,18.6
Erechim,2009-05-01,122.4
Erechim,2009-06-01,76.2
Erechim,2009-07-01,121.60000000000001
Erechim,2009-08-01,125.6
Erechim,2009-09-01,261.8
Erechim,2009-10-01,202.8
Erechim,2009-11-01,276.8
Erechim,2009-12-01,171.4
Erechim,2010-01-01,157.6
Erechim,2010-02-01,140.2
Erechim,2010-03-01,115.39999999999999
Erechim,2010-04-01,242.0
Erechim,2010-05-01,187.8
Erechim,2010-06-01,85.2
Erechim,2010-07-01,215.2
Erechim,2010-08-01,44.4
Erechim,2010-09-01,195.4
Erechim,2010-10-01,107.8
Erechim,2010-11-01,114.8
Erechim,2010-12-01,262.6
Erechim,2011-01-01,133.2
Erechim,2011-02-01,202.0
Erechim,2011-03-01,255.4
Erechim,2011-04-01,103.0
Erechim,2011-05-01,82.2
Erechim,2011-06-01,267.4
Erechim,2011-07-01,282.6
Erechim,2011-08-01,227.2
Erechim,2011-09-01,100.6
Erechim,2011-10-01,186.0
Erechim,2011-11-01,82.4
Erechim,2011-12-01,14.6
Erechim,2012-01-01,70.6
Erechim,2012-02-01,21.2
Erechim,2012-03-01,3.0
Erechim,2012-04-01,25.0
Erechim,2012-05-01,20.4
Erechim,2012-06-01,172.6
Erechim,2012-07-01,248.0
Erechim,2012-08-01,6.2
Erechim,2012-09-01,117.2
Erechim,2012-10-01,105.0
Erechim,2012-11-01,40.2
Erechim,2012-12-01,177.2
Erechim,2013-01-01,152.0
Erechim,2013-02-01,188.20000000000002
Erechim,2013-03-01,183.8
Erechim,2013-04-01,128.0
Erechim,2013-05-01,113.0
Erechim,2013-06-01,154.0
Erechim,2013-07-01,90.2
Erechim,2013-08-01,318.0
Erechim,2013-09-01,188.6
Erechim,2013-10-01,178.6
Erechim,2013-11-01,163.6
Erechim,2013-12-01,152.6
Erechim,2014-01-01,185.8
Erechim,2014-02-01,231.6
Erechim,2014-03-01,232.4
Erechim,2014-04-01,97.4
Erechim,2014-05-01,0.0
Erechim,2014-06-01,18.2
Erechim,2014-07-01,0.0
Erechim,2014-08-01,87.8
Erechim,2014-09-01,291.0
Erechim,2014-10-01,104.4
Erechim,2014-11-01,159.4
Erechim,2014-12-01,213.4
Erechim,2015-01-01,300.4
Erechim,2015-02-01,202.0
Erechim,2015-03-01,26.200000000000003
Erechim,2015-04-01,28.8
Erechim,2015-05-01,0.0
Erechim,2015-06-01,0.0
Erechim,2015-07-01,0.0
Erechim,2015-08-01,51.2
Erechim,2015-09-01,288.8
Erechim,2015-10-01,248.79999999999998
Erechim,2015-11-01,236.0
Erechim,2015-12-01,436.0
Erechim,2016-01-01,0.0
Erechim,2016-02-01,0.0
Erechim,2016-03-01,0.0
Erechim,2016-04-01,64.0
Erechim,2016-05-01,0.0
Erechim,2016-06-01,0.0
Erechim,2016-07-01,127.4
Erechim,2016-08-01,179.8
Erechim,2016-09-01,55.0
Erechim,2016-10-01,227.6
Erechim,2016-11-01,61.0
Erechim,2016-12-01,191.4
Erechim,2017-01-01,211.6
Erechim,2017-02-01,156.0
Erechim,2017-03-01,151.79999999999998
Erechim,2017-04-01,191.4
Erechim,2017-05-01,463.2
Erechim,2017-06-01,204.6
Erechim,2017-07-01,11.0
Erechim,2017-08-01,75.2
Erechim,2017-09-01,63.199999999999996
Erechim,2017-10-01,113.60000000000001
Erechim,2017-11-01,52.8
Erechim,2017-12-01,22.8
Erechim,2018-01-01,120.8
Erechim,2018-02-01,59.2
Erechim,2018-03-01,59.0
Erechim,2018-04-01,4.0
Erechim,2018-05-01,76.4
Erechim,2018-06-01,113.0
Erechim,2018-07-01,89.0
Erechim,2018-08-01,104.60000000000001
Erechim,2018-09-01,160.8
Erechim,2018-10-01,236.8
Erechim,2018-11-01,199.2
Erechim,2018-12-01,97.0
Erechim,2019-01-01,232.4
Erechim,2019-02-01,193.8
Erechim,2019-03-01,214.0
Erechim,2019-04-01,147.8
Erechim,2019-05-01,270.6
Erechim,2019-06-01,40.0
Erechim,2019-07-01,135.6
Erechim,2019-08-01,53.4
Erechim,2019-09-01,45.4
Erechim,2019-10-01,204.6
Erechim,2019-11-01,118.60000000000001
Erechim,2019-12-01,114.19999999999999
Erechim,2020-01-01,131.4
Erechim,2020-02-01,91.2
Erechim,2020-03-01,27.8
Erechim,2020-04-01,67.6
Erechim,2020-05-01,149.4
Erechim,2020-06-01,238.6
Erechim,2020-07-01,182.4
Erechim,2020-08-01,95.8
Erechim,2020-09-01,67.0
Erechim,2020-10-01,23.4
Erechim,2020-11-01,128.6
Erechim,2020-12-01,144.4
Erechim,2021-01-01,319.0
Erechim,2021-02-01,24.0
Erechim,2021-03-01,95.60000000000001
Erechim,2021-04-01,5.4
Erechim,2021-05-01,115.6
Erechim,2021-06-01,183.4
Erechim,2021-07-01,46.8
Erechim,2021-08-01,32.2
Erechim,2021-09-01,0.4
Erechim,2021-10-01,40.2
Erechim,2021-11-01,63.8
Erechim,2021-12-01,26.2
Erechim,2022-01-01,202.0
Erechim,2022-02-01,0.0
Erechim,2022-03-01,0.0
Erechim,2022-04-01,0.0
Erechim,2022-05-01,44.0
Erechim,2022-06-01,183.4
Erechim,2022-07-01,83.4
Erechim,2022-08-01,61.8
Erechim,2022-09-01,3.6
Erechim,2022-10-01,77.4
Erechim,2022-11-01,94.4
Erechim,2022-12-01,0.0
Bento Gonçalves,2007-01-01,132.2
Bento Gonçalves,2007-02-01,57.2
Bento Gonçalves,2007-03-01,204.4
Bento Gonçalves,2007-04-01,51.4
Bento Gonçalves,2007-05-01,175.8
Bento Gonçalves,2007-06-01,59.0
Bento Gonçalves,2007-07-01,250.0
Bento Gonçalves,2007-08-01,123.6
Bento Gonçalves,2007-09-01,266.4
Bento Gonçalves,2007-10-01,122.2
Bento Gonçalves,2007-11-01,118.0
Bento Gonçalves,2007-12-01,198.6
Bento Gonçalves,2008-01-01,55.0
Bento Gonçalves,2008-02-01,86.2
Bento Gonçalves,2008-03-01,71.4
Bento Gonçalves,2008-04-01,86.4
Bento Gonçalves,2008-05-01,163.0
Bento Gonçalves,2008-06-01,157.6
Bento Gonçalves,2008-07-01,84.4
Bento Gonçalves,2008-08-01,181.2
Bento Gonçalves,2008-09-01,144.0
Bento Gonçalves,2008-10-01,300.2
Bento Gonçalves,2008-11-01,81.8
Bento Gonçalves,2008-12-01,71.6
Bento Gonçalves,2009-01-01,256.4
Bento Gonçalves,2009-02-01,139.0
Bento Gonçalves,2009-03-01,85.2
Bento Gonçalves,2009-04-01,24.4
Bento Gonçalves,2009-05-01,127.8
Bento Gonçalves,2009-06-01,81.0
Bento Gonçalves,2009-07-01,47.0
Bento Gonçalves,2009-08-01,42.8
Bento Gonçalves,2009-09-01,329.6
Bento Gonçalves,2009-10-01,137.0
Bento Gonçalves,2009-11-01,347.2
Bento Gonçalves,2009-12-01,206.6
Bento Gonçalves,2010-01-01,278.4
Bento Gonçalves,2010-02-01,161.4
Bento Gonçalves,2010-03-01,58.4
Bento Gonçalves,2010-04-01,136.4
Bento Gonçalves,2010-05-01,158.8
Bento Gonçalves,2010-06-01,128.0
Bento Gonçalves,2010-07-01,221.4
Bento Gonçalves,2010-08-01,34.8
Bento Gonçalves,2010-09-01,225.4
Bento Gonçalves,2010-10-01,51.0
Bento Gonçalves,2010-11-01,88.4
Bento Gonçalves,2010-12-01,89.6
Bento Gonçalves,2011-01-01,172.4
Bento Gonçalves,2011-02-01,214.0
Bento Gonçalves,2011-03-01,264.6
Bento Gonçalves,2011-04-01,147.8
Bento Gonçalves,2011-05-01,70.0
Bento Gonçalves,2011-06-01,178.6
Bento Gonçalves,2011-07-01,324.4
Bento Gonçalves,2011-08-01,243.0
Bento Gonçalves,2011-09-01,57.800000000000004
Bento Gonçalves,2011-10-01,100.2
Bento Gonçalves,2011-11-01,23.0
Bento Gonçalves,2011-12-01,69.2
Bento Gonçalves,2012-01-01,58.6
Bento Gonçalves,2012-02-01,207.4
Bento Gonçalves,2012-03-01,51.4
Bento Gonçalves,2012-04-01,74.2
Bento Gonçalves,2012-05-01,25.2
Bento Gonçalves,2012-06-01,53.6
Bento Gonçalves,2012-07-01,192.4
Bento Gonçalves,2012-08-01,55.800000000000004
Bento Gonçalves,2012-09-01,221.2
Bento Gonçalves,2012-10-01,154.20000000000002
Bento Gonçalves,2012-11-01,26.0
Bento Gonçalves,2012-12-01,217.2
Bento Gonçalves,2013-01-01,104.4
Bento Gonçalves,2013-02-01,105.8
Bento Gonçalves,2013-03-01,186.4
Bento Gonçalves,2013-04-01,106.8
Bento Gonçalves,2013-05-01,127.60000000000001
Bento Gonçalves,2013-06-01,141.6
Bento Gonçalves,2013-07-01,96.4
Bento Gonçalves,2013-08-01,303.8
Bento Gonçalves,2013-09-01,182.79999999999998
Bento Gonçalves,2013-10-01,121.6
Bento Gonçalves,2013-11-01,242.8
Bento Gonçalves,2013-12-01,137.0
Bento Gonçalves,2014-01-01,88.4
Bento Gonçalves,2014-02-01,192.6
Bento Gonçalves,2014-03-01,194.4
Bento Gonçalves,2014-04-01,124.2
Bento Gonçalves,2014-05-01,158.0
Bento Gonçalves,2014-06-01,246.4
Bento Gonçalves,2014-07-01,136.4
Bento Gonçalves,2014-08-01,113.60000000000001
Bento Gonçalves,2014-09-01,217.6
Bento Gonçalves,2014-10-01,162.6
Bento Gonçalves,2014-11-01,114.2
Bento Gonçalves,2014-12-01,294.2
Bento Gonçalves,2015-01-01,135.2
Bento Gonçalves,2015-02-01,130.4
Bento Gonçalves,2015-03-01,55.6
Bento Gonçalves,2015-04-01,136.6
Bento Gonçalves,2015-05-01,115.0
Bento Gonçalves,2015-06-01,213.0
Bento Gonçalves,2015-07-01,163.6
Bento Gonçalves,2015-08-01,0.0
Bento Gonçalves,2015-09-01,0.0
Bento Gonçalves,2015-10-01,256.0
Bento Gonçalves,2015-11-01,144.8
Bento Gonçalves,2015-12-01,197.8
Bento Gonçalves,2016-01-01,114.8
Bento Gonçalves,2016-02-01,146.4
Bento Gonçalves,2016-03-01,243.4
Bento Gonçalves,2016-04-01,259.6
Bento Gonçalves,2016-05-01,60.0
Bento Gonçalves,2016-06-01,6.800000000000001
Bento Gonçalves,2016-07-01,192.4
Bento Gonçalves,2016-08-01,111.0
Bento Gonçalves,2016-09-01,84.2
Bento Gonçalves,2016-10-01,367.0
Bento Gonçalves,2016-11-01,104.4
Bento Gonçalves,2016-12-01,81.4
Bento Gonçalves,2017-01-01,146.8
Bento Gonçalves,2017-02-01,135.0
Bento Gonçalves,2017-03-01,250.0
Bento Gonçalves,2017-04-01,157.2
Bento Gonçalves,2017-05-01,312.4
Bento Gonçalves,2017-06-01,161.0
Bento Gonçalves,2017-07-01,28.8
Bento Gonçalves,2017-08-01,114.0
Bento Gonçalves,2017-09-01,106.6
Bento Gonçalves,2017-10-01,184.2
Bento Gonçalves,2017-11-01,162.4
Bento Gonçalves,2017-12-01,102.4
Bento Gonçalves,2018-01-01,146.6
Bento Gonçalves,2018-02-01,85.39999999999999
Bento Gonçalves,2018-03-01,124.2
Bento Gonçalves,2018-04-01,40.0
Bento Gonçalves,2018-05-01,118.6
Bento Gonçalves,2018-06-01,182.6
Bento Gonçalves,2018-07-01,163.0
Bento Gonçalves,2018-08-01,215.8
Bento Gonçalves,2018-09-01,183.0
Bento Gonçalves,2018-10-01,221.0
Bento Gonçalves,2018-11-01,191.0
Bento Gonçalves,2018-12-01,134.4
Bento Gonçalves,2019-01-01,138.0
Bento Gonçalves,2019-02-01,66.2
Bento Gonçalves,2019-03-01,82.6
Bento Gonçalves,2019-04-01,161.0
Bento Gonçalves,2019-05-01,70.4
Bento Gonçalves,2019-06-01,69.2
Bento Gonçalves,2019-07-01,44.0
Bento Gonçalves,2019-08-01,97.2
Bento Gonçalves,2019-09-01,72.8
Bento Gonçalves,2019-10-01,258.6
Bento Gonçalves,2019-11-01,158.6
Bento Gonçalves,2019-12-01,37.4
Bento Gonçalves,2020-01-01,144.6
Bento Gonçalves,2020-02-01,67.4
Bento Gonçalves,2020-03-01,33.0
Bento Gonçalves,2020-04-01,8.8
Bento Gonçalves,2020-05-01,136.4
Bento Gonçalves,2020-06-01,247.8
Bento Gonçalves,2020-07-01,309.2
Bento Gonçalves,2020-08-01,112.0
Bento Gonçalves,2020-09-01,137.8
Bento Gonçalves,2020-10-01,46.4
Bento Gonçalves,2020-11-01,5.2
Bento Gonçalves,2020-12-01,0.0
Bento Gonçalves,2021-01-01,226.0
Bento Gonçalves,2021-02-01,64.6
Bento Gonçalves,2021-03-01,148.6
Bento Gonçalves,2021-04-01,6.800000000000001
Bento Gonçalves,2021-05-01,198.0
Bento Gonçalves,2021-06-01,167.2
Bento Gonçalves,2021-07-01,35.4
Bento Gonçalves,2021-08-01,117.2
Bento Gonçalves,2021-09-01,161.4
Bento Gonçalves,2021-10-01,103.8
Bento Gonçalves,2021-11-01,38.2
Bento Gonçalves,2021-12-01,31.2
Bento Gonçalves,2022-01-01,81.6
Bento Gonçalves,2022-02-01,104.0
Bento Gonçalves,2022-03-01,174.0
Bento Gonçalves,2022-04-01,154.0
Bento Gonçalves,2022-05-01,295.0
Bento Gonçalves,2022-06-01,203.0
Bento Gonçalves,2022-07-01,147.8
Bento Gonçalves,2022-08-01,105.4
Bento Gonçalves,2022-09-01,58.800000000000004
Bento Gonçalves,2022-10-01,117.4
Bento Gonçalves,2022-11-01,58.2
Bento Gonçalves,2022-12-01,135.0
"""
text = StringIO(text_io)
analise_precipitacao_mensal = pd.read_csv(text, sep=",", parse_dates=["Data de Referência"])
text_io = """
"""
text = """
"""
# analise_precipitacao_mensal = pd.read_csv("analise_precipitacao_mensal.csv", parse_dates=["Data de Referência"])

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
