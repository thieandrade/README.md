import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de anúncios de venda de veículos nos EUA')

st.write(
    'Este aplicativo permite explorar o conjunto de dados de anúncios de venda '
    'de veículos usados. Use os botões abaixo para gerar os gráficos.'
)

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a quilometragem (odometer) dos veículos anunciados')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre quilometragem (odometer) e preço (price)')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
