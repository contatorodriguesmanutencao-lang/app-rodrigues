import streamlit as st
import pandas as pd

st.title("🏗️ Rodrigues Engenharia - Orçamentos")

# Substitua pelo link CSV da sua planilha (Arquivo > Compartilhar > Publicar na Web > CSV)
URL_PLANILHA = "https://docs.google.com/spreadsheets/d/e/SUA_CHAVE_AQUI/pub?output=csv"

try:
    df = pd.read_csv(URL_PLANILHA)
    servico = st.selectbox("Selecione o Serviço", df['Item / Serviço'].unique())
    dados = df[df['Item / Serviço'] == servico].iloc[0]
    
    st.write(f"**Preço:** R$ {dados['Preço Unitário (R$)']}")
    qtd = st.number_input("Quantidade", min_value=1)
    st.subheader(f"Total: R$ {dados['Preço Unitário (R$)'] * qtd}")
except:
    st.error("Configure o link da sua planilha nas configurações do código.") 
