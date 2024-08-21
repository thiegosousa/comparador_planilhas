import pandas as pd
import streamlit as st
from io import BytesIO

# Configuração inicial
st.set_page_config(page_title="Comparador de Planilhas por CPF", layout="centered")
st.title("🧮 Comparador de Planilhas por CPF")

# Carregar as planilhas
st.header("🔄 Carregue as planilhas para comparação")
col1, col2 = st.columns(2)

with col1:
    planilha1 = st.file_uploader("📄 Planilha 1 - Mensal", type=["xlsx", "csv"], help="Carregue a primeira planilha (Mensal) para comparação")
with col2:
    planilha2 = st.file_uploader("📄 Planilha 2 - Suplementar", type=["xlsx", "csv"], help="Carregue a segunda planilha (Suplementar) para comparação")

# Verificação e processamento
if planilha1 and planilha2:
    # Ler as planilhas
    def load_data(uploaded_file):
        if uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
    
    df1 = load_data(planilha1)
    df2 = load_data(planilha2)
    
    # Exibir uma prévia das planilhas
    st.subheader("🔍 Prévia das Planilhas Carregadas")
    col3, col4 = st.columns(2)
    with col3:
        st.write("**Planilha 1 - Mensal:**")
        st.dataframe(df1.head(), use_container_width=True)
    with col4:
        st.write("**Planilha 2 - Suplementar:**")
        st.dataframe(df2.head(), use_container_width=True)
    
    # Garantir que a coluna CPF exista em ambas as planilhas
    if "CPF" in df1.columns and "CPF" in df2.columns:
        # Adicionar coluna 'Mensal' na Planilha 2
        df2['Mensal'] = df2['CPF'].isin(df1['CPF']).replace({True: 'SIM', False: 'NÃO'})
        
        # Contagem de SIM e NÃO
        sim_count = df2['Mensal'].value_counts().get('SIM', 0)
        nao_count = df2['Mensal'].value_counts().get('NÃO', 0)
        
        # Exibir as contagens
        st.subheader("📊 Contagem de Resultados")
        st.write(f"**SIM:** {sim_count} registros")
        st.write(f"**NÃO:** {nao_count} registros")
        
        # Exibir a Planilha 2 atualizada
        st.subheader("📊 Resultado da Comparação")
        st.dataframe(df2, use_container_width=True)
        
        # Função para gerar o arquivo de download
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Resultado')
            processed_data = output.getvalue()
            return processed_data

        # Botão para download da planilha atualizada
        st.download_button(
            label="📥 Baixar Planilha 2 - Suplementar Atualizada",
            data=to_excel(df2),
            file_name="planilha2_atualizada.xlsx",
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    else:
        st.error("❗ A coluna 'CPF' não foi encontrada em uma das planilhas.")
else:
    st.info("💡 Por favor, carregue ambas as planilhas para iniciar a comparação.")
