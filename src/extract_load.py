# Importação das bibliotecas necessárias
import yfinance as yf
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

def buscar_cotacao(simbolo, periodo='5d', intervalo='1d'):
    """
    Busca a cotação de uma commodity específica usando a API do Yahoo Finance.

    Args:
        simbolo (str): O símbolo da commodity.
        periodo (str): O período de tempo para buscar os dados (padrão é '5d').
        intervalo (str): O intervalo de tempo entre os dados (padrão é '1d').

    Returns:
        pd.DataFrame: DataFrame contendo as cotações da commodity.
    """
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados(commodities):
    """
    Busca as cotações de todas as commodities na lista fornecida.

    Args:
        commodities (list): Lista de símbolos das commodities.

    Returns:
        pd.DataFrame: DataFrame contendo as cotações de todas as commodities.
    """
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_cotacao(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

# Função para salvar os dados no banco de dados
def salvar_dados_no_banco(dados, tabela):
    """
    Salva os dados fornecidos em uma tabela do banco de dados.

    Args:
        dados (pd.DataFrame): DataFrame contendo os dados a serem salvos.
        tabela (str): Nome da tabela no banco de dados onde os dados serão salvos.
    """
    dados.to_sql(tabela, engine, schema=DB_SCHEMA, if_exists='replace', index=True, index_label='Date')

# Buscar dados de todas as commodities e salvar no banco de dados
dados_commodities = buscar_todos_dados(commodities)
salvar_dados_no_banco(dados_commodities, 'commodities')