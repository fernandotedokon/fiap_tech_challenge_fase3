# 📚 Desafio Tech FIAP - Fase 3 - Análise exploratória dos Dados, Modelo Supervisionado e Não Supervisionado de Voos nos Aeroportos Americanos
**Powered by Group 51, 6MLET**

### Este projeto possui **Plataforma analitica para monitoramento e análise de atrasos de voos nos EUA**, realiza Exploração dos Dados (EDA), (atrasos, companhias, meses, aeroportos) Modelos Supervisionado **classificação e regressão** para previsão de atrasos de voos e também Modelos Não Supervisionado com padrões ocultos dos atrasos.




## 📦 Requisitos

- Python 3.8+
- pip

## 🚀 Tecnologias Utilizadas

- **Pandas** — Biblioteca para análise e manipulação de dados estruturados (como planilhas, CSV, tabelas, Parquet).
- **Streamlit** — Framework para criar aplicações web interativas, exibir gráficos, mapas, tabelas e modelos de ML.
- **Plotly** — Biblioteca de visualização interativa, dashboards modernos, graficos linha, barras, pizza, mapas.
- **Folium** — Biblioteca para mapas interativos, visualização dados geográficos, mapas com marcadores, clusters e camadas.
- **Streamlit-folium** — Interação entre Folium e Streamlit, exibir mapas Folium dentro de apps Streamlit, capturar interações dop usuário (cliques no mapa).
- **NumPy** — Biblioteca base para computação numérica em python, operações matemáticas de alta performance.
- **Matplotlib** — Biblioteca de visualização de dados, gráficos estáticos, usado para análises exploratórias (EDA).
- **Seaborn** — Biblioteca de visualização construida sobre o Matplotlib.
- **Scikit-learn** — Principal bibliocate de Machine Learning tradicional em python.



## 🗂️ Estrutura do Projeto

```
FIAP_TECH_CHALLENGE_FASE3/
├── data/
│   ├── airlines.csv              # Dataset dos dados das companhia aéreas
│   ├── airports.csv              # Dataset das informações dos aeroportos americanos
│   └── flights.csv               # Dataset de Atrasos em Voos dos EUA (2015)
│   
├── video/
│   └── presentation.mp4          # Apresentação do projeto desenvolvido com a exploração dos dados
│   
├── flights_dashboard.py          # Painel de voos
├── flights_supervised.ipynb      # Flights Delay Prediction - Exploração de Dados (EDA) - Modelagem Supervisionado
├── flights_unsupervised.ipynb    # Flights Discover Hidden Patterns - Exploração de Dados (EDA) - Modelagem Não Supervisionado
│   
├── requirements.txt              # Dependências das bibliotecas utilizada
└── README.md
```



## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone <https://github.com/fernandotedokon/fiap_tech_challenge_fase3.git>
cd fiap_tech_challenge_fase3
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o Streamlit para exibir o Dashboard

```bash
streamlit run flights_dashboard.py
```


### 5. Dashboard de Atrasos em Voos dos EUA (2015)

- **Ambiente Local**
```bash
http://localshost:8501
```
- **Ambiente Network**
```bash
http://192.168.0.76:8501
```



## 📊 Conclusões e avaliação crítica

```bash
Principais conclusões:
- Identificamos N clusters de rotas com perfis distintos (ex.: rotas curtas com alta frequência e baixo atraso; rotas longas com maior variabilidade de atraso).
- Rotas com maior média de atraso geralmente têm maior distância ou menor frequência — pode indicar dependência logística (rota/turnaround) ou menor prioridade operacional.

Limitações:
- Muitos campos de delay podem estar ausentes ou inconsistentes (NaN) — imputação pode introduzir inconsistencias.
- Dados de um único ano/periodo não capturam sazonalidade longa.
- A clusterização KMeans assume formas convexas e sensíveis à escala e outliers.

Próximos passos e melhorias:
- Normalizar e tratar outliers (winsorizing) antes de treinar modelos.
- Usar modelos de clusterização mais robustos (DBSCAN, HDBSCAN) para capturar topologias não convexas.
- Incluir features adicionais: tempo meteorológico por origem/destino, tráfego horário, tipo de aeronave (TAIL_NUMBER), capacidade da aeronave.
- Construir pipelines de validação temporal (treino/teste por período) para verificar estabilidade dos clusters.
```

## 🎬 Apresentação do projeto

- É apresentado **Dashboards de atrasos de Voos dos EUA** podendo ser visualizado **dados combinados de voos, companhias e aeroportos**,  baseado na Exploração dos Dados (EDA) (atrasos, companhias, meses, aeroportos) Modelos Supervisionado  **classificação e regressão** para previsão de atrasos de voos e também Modelos Não Supervisionados de padrões ocultos (Clusterização: KMeans + PCA).
