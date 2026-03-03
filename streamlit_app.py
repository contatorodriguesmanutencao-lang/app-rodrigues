import streamlit as st
import pandas as pd

# Link da sua planilha publicada como CSV
URL = "COLE_AQUI_O_LINK_DO_GOOGLE_SHEETS"

df = pd.read_csv(URL)
st.write("### Rodrigues Engenharia - Orçamentos")

# Criando o seletor baseado na sua planilha
servico = st.selectbox("Selecione o Serviço", df['Item / Serviço'].unique())

# Filtrando os dados (Igual ao PROCX)
dados = df[df['Item / Serviço'] == servico].iloc[0]
st.info(f"Unidade: {dados['Unidade']} | Preço: R$ {dados['Preço Unitário (R$)']}")
