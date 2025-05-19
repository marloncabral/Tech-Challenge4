
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title('Variação do Preço por Barril do Petróleo Bruto Brent (FOB)')

# Barra lateral fixa com links
st.sidebar.markdown("## Navegação")

# Seção adicional: Cenário Petróleo
st.sidebar.markdown("### Cenário Petróleo")
st.sidebar.markdown("- [Cenário Petróleo](https://app.powerbi.com/view?r=eyJrIjoiNDk4NjRhYTMtMjUyOC00YTBmLWJlZTEtYThmNzFkMDlmMjlkIiwidCI6ImQzNjQ4ZmUxLWRiMjEtNGRhMy1hMTY1LTQ2NjkyMTMyN2E4ZSJ9)")

# Seção adicional: Exploração e Insights
st.sidebar.markdown("### Exploração e Insights")
# Aqui você pode adicionar elementos interativos personalizados:
# Exemplo:
# st.sidebar.text_input("Buscar insight")

pagina = st.sidebar.radio("Ir para:", ["Explicação Tech Challenge 4", "Projeto Final"])

# Conteúdo principal
if pagina == "Explicação Tech Challenge 4":
    st.header("Explicação Tech Challenge 4")
    paragraphs = [
        "Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo Brent, que pode ser encontrado no site do Ipea.",
        "Essa base de dados histórica envolve duas colunas: data e preço (em dólares).",
        "Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para tomada de decisão.",
        "Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo e um modelo de Deploy (nesse caso estarei usando o Streamlit).",
        "Dentro do Streamlit havia duas abas: agora usamos uma barra lateral fixa para navegação.",
    ]
    for paragraph in paragraphs:
        st.write(paragraph)
    
    st.markdown('- [Dados do IPEA](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)')
    st.markdown('- [Vídeo Explicativo](LINK_Video)')
    st.markdown('- [Repositório no GitHub](https://github.com/marloncabral/Tech-Challenge4/tree/main)')

elif pagina == "Projeto Final":
    st.header("Projeto Final")
    st.subheader("Preço do Petróleo")
    paragraphs = [
        "Análise da Flutuação do Preço do Petróleo ao Longo do Tempo.",
        "Este estudo examina a dinâmica do preço do petróleo em diferentes períodos."
    ]
    for paragraph in paragraphs:
        st.write(paragraph)

    df = pd.read_csv("https://raw.githubusercontent.com/marloncabral/Tech-Challenge4/main/ipeadata.csv", sep=';', encoding='utf-8-sig')
    df.columns = df.columns.str.strip()
    df.rename(columns={'Data': 'data', 'Preco': 'preco'}, inplace=True)
    df['preco'] = df['preco'].str.replace(',', '.').astype(float)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce').dt.date

    data_inicial_padrao = pd.to_datetime('2014-01-01').date()
    data_final_padrao = pd.to_datetime('2025-05-02').date()

    data_inicial = st.date_input("Data Inicial", value=data_inicial_padrao, min_value=data_inicial_padrao)
    data_final = st.date_input("Data Final", value=data_final_padrao, max_value=data_final_padrao)

    df_filtrado = df[(df['data'] >= data_inicial) & (df['data'] <= data_final)]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_filtrado['data'], df_filtrado['preco'], marker='o')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.set_title('Preço ao longo dos anos')

    st.pyplot(fig)

    st.subheader('Previsão com Prophet')
    st.image("https://raw.githubusercontent.com/marloncabral/Tech-Challenge4/main/Imagens/newplot.png", use_container_width=True)
    st.caption('Fonte: Código Python disponível no GitHub')
