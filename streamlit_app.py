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
# Criando duas colunas: a primeira para Qtd e a segunda para o Total
col1, col2 = st.columns(2)

with col1:
    qtd = st.number_input("Quantidade", min_value=1, value=1, step=1)

with col2:
    valor_total = dados['Preço Unitário (R$)'] * qtd
    st.metric("Total (R$)", f"{valor_total:,.2f}")
  if st.button("Gerar Orçamento para WhatsApp"):
    # Montando o texto formatado
    resumo = f"""
*RODRIGUES ENGENHARIA - ORÇAMENTO*
----------------------------------
*Serviço:* {servico}
*Quantidade:* {qtd} {dados['Unidade']}
*Valor Unitário:* R$ {dados['Preço Unitário (R$)']:,.2f}
----------------------------------
*VALOR TOTAL: R$ {valor_total:,.2f}*
    """
    
    st.text_area("Copie o texto abaixo:", value=resumo, height=200)
    st.success("Agora é só copiar e colar no WhatsApp do cliente!")
