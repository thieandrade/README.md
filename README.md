# Dashboard de Anúncios de Venda de Veículos (EUA)

## Descrição do projeto

Este é um aplicativo web interativo criado com Streamlit, que permite explorar um conjunto de dados de anúncios de venda de carros usados nos EUA (vehicles_us.csv).

O objetivo do projeto é praticar tarefas comuns de engenharia de software: criação e gestão de ambientes virtuais Python, desenvolvimento de um aplicativo web e implantação em um serviço de nuvem (Render).

## Funcionalidades do aplicativo

- Cabeçalho com a descrição do dashboard
- Botão que gera um histograma da distribuição da quilometragem (odometer) dos veículos
- Botão que gera um gráfico de dispersão relacionando quilometragem (odometer) e preço (price)

## Como executar localmente

1. python -m venv vehicles_env
2. source vehicles_env/bin/activate
3. pip install -r requirements.txt
4. streamlit run app.py

## Aplicativo publicado

URL no Render: https://car-sales-dashboard-crfg.onrender.com

## Estrutura do projeto

- README.md
- app.py
- vehicles_us.csv
- requirements.txt
- notebooks/EDA.ipynb
- .streamlit/config.toml
