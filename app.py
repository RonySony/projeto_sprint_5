import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles.csv')

st.header('Criando gráficos de análise de dados com Streamlit')

hist_button = st.button("Criar histograma")

disp_button = st.button("Criar gráfico de dispersão")

if hist_button:
    st.write(
        "Criando um histograma para o conjunto de dados de anúncios de vendas de carros")

    fig = px.histogram(car_data, x='odometer',
                       title='Histograma de Preços de Carros')

    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write(
        "Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros")

    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Gráfico de Dispersão de Preços de Carros')

    st.plotly_chart(fig, use_container_width=True)
