
import streamlit as st
import pandas as pd
import plotly.express as px

# Dados simulados para ETA
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago'],
    'Consumo Água (m³)': [1200, 1350, 1100, 1450, 1600, 1550, 1700, 1620],
    'Uso de Cloro (kg)': [35, 38, 34, 40, 42, 41, 45, 43],
    'pH Médio': [7.2, 7.1, 7.3, 7.0, 6.9, 7.1, 7.2, 7.0],
    'Turbidez (NTU)': [0.8, 1.0, 0.9, 1.2, 1.1, 0.9, 1.0, 1.2]
}

df = pd.DataFrame(dados)

# Título
st.title("Dashboard de Monitoramento Operacional - ETA")

# Filtros interativos
meses = st.multiselect("Selecione os meses:", df["Mês"].unique(), default=df["Mês"].tolist())

df_filtrado = df[df["Mês"].isin(meses)]

# Gráfico de Consumo de Água
fig1 = px.bar(df_filtrado, x='Mês', y='Consumo Água (m³)', text='Consumo Água (m³)', title='Consumo de Água por Mês')
fig1.update_traces(textposition='outside')

# Gráfico de Uso de Cloro
fig2 = px.line(df_filtrado, x='Mês', y='Uso de Cloro (kg)', markers=True, title='Uso de Cloro ao Longo dos Meses')

# Gráfico de pH
fig3 = px.scatter(df_filtrado, x='Mês', y='pH Médio', size='pH Médio', color='pH Médio', title='pH Médio da Água')

# Gráfico de Turbidez
fig4 = px.area(df_filtrado, x='Mês', y='Turbidez (NTU)', title='Turbidez Média por Mês')

# Exibição dos gráficos
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)

# Exibição da tabela
st.subheader("Dados Consolidados")
st.dataframe(df_filtrado.set_index('Mês'))
