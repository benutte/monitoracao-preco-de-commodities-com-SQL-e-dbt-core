# Monitoramento de Preço de Commodities

Este projeto tem como objetivo monitorar o preço de commodities específicas, transformar os dados utilizando DBT, armazená-los em um banco de dados PostgreSQL e visualizar as informações de maneira interativa com Streamlit.

📋 **Funcionalidades**

  - Coleta as cotações diárias de commodities utilizando a API do Yahoo Finance.
  - Realiza transformações nos dados, incluindo conversões de data e cálculos de ganho/perda.
  - Armazena os dados no banco de dados PostgreSQL.
  - Gera documentação da estrutura e modelos no DBT.
  - Visualiza os dados coletados e transformados em uma interface interativa utilizando Streamlit.

🛠️ **Tecnologias Utilizadas**
  
  - **Python**: Linguagem principal do projeto.
  - **yfinance**: Para buscar os preços das commodities.
  - **SQLAlchemy**: Para integração com o banco de dados PostgreSQL.
  - **DBT**: Para transformação e documentação dos dados.
  - **PostgreSQL**: Banco de dados para armazenamento dos dados.
  - **Streamlit**: Para criação da interface interativa.
  
📂 **Estrutura do Projeto**

    monitoramento_commodities/
      ├── app.py              # Código principal para coleta e armazenamento de dados
      ├── models/             # Modelos DBT para transformação de dados
      ├── app.py         # Código para a interface interativa com Streamlit
      ├── dbt_project.yml     # Configurações do projeto DBT
      ├── requirements.txt    # Dependências do projeto
      ├── .env                # Variáveis de ambiente (não deve ser commitado)
      ├── README.md           # Documentação do projeto

🛡️ **Aviso Legal**

  Este projeto foi desenvolvido para fins educacionais e de aprendizado. Certifique-se de seguir as diretrizes de uso da API do Yahoo Finance.

📧 **Contato**

  Se tiver dúvidas ou sugestões, entre em contato:
  
  Email: benutte@gmail.com.com
