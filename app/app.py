# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Lista de commodities a serem monitoradas
commodities = ['CL=F', 'GC=F', 'SI=F']

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter credenciais do banco de dados a partir das variáveis de ambiente
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Construir a URL de conexão com o banco de dados
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Criar o motor de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT
        data,
        simbolo,
        valor_fechamento,
        acao,
        quantidade,
        valor,
        ganho
    FROM
    public.dm_commodities;
    """

    df = pd.read_sql(query, engine)
    
    return df

# Configura a página do Stramlit
st.set_page_config(page_title='Commodities Dashboard', page_icon=':bar_chart:', layout='wide')

# Título do Dashboard
st.title('Commodities Dashboard')

# Descrição do Dashboard
st.write('Este dashboard exibe as cotações de commodities em tempo real.')

# Obter os dados
df = get_data()

st.dataframe(df)
