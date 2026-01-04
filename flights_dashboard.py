import streamlit as st
import pandas as pd
import plotly.express as px
import folium
import os
from streamlit_folium import st_folium

st.set_page_config(page_title="✈️ Análise de Atrasos em Voos", layout="wide")
data_dir = 'data'
csv_path_flights = os.path.join(data_dir, 'flights.csv') 
csv_path_airlines = os.path.join(data_dir, 'airlines.csv') 
csv_path_airports = os.path.join(data_dir, 'airports.csv') 

@st.cache_data
def load_data():
    flights = pd.read_csv(csv_path_flights, low_memory=True)

    # SAMPLE_MODE = True reduz o dataset para ~500 mil linhas (ajuste conforme desejar)
    SAMPLE_MODE = True
    SAMPLE_SIZE = 500_000

    if SAMPLE_MODE:
      flights = flights.sample(SAMPLE_SIZE, random_state=42)

    airlines = pd.read_csv(csv_path_airlines, low_memory=True)
    airports = pd.read_csv(csv_path_airports, low_memory=True)
    df = flights.merge(airlines, left_on='AIRLINE', right_on='IATA_CODE', how='left') \
                .merge(airports[['IATA_CODE', 'CITY', 'STATE', 'LATITUDE', 'LONGITUDE']],
                       left_on='ORIGIN_AIRPORT', right_on='IATA_CODE', how='left',
                       suffixes=('', '_ORIGIN'))
    return df


flights = load_data()

st.title("✈️ Dashboard de Atrasos em Voos dos EUA (2015)")
st.markdown("### Dados combinados de voos, companhias e aeroportos")

# Classificacao de atraso
def classify_delay(delay):
    if pd.isna(delay):
        return 'Sem dado'
    elif delay > 0.3:
        return 'Alto atraso'
    elif delay > 0.15:
        return 'Médio atraso'
    else:
        return 'Baixo atraso'

flights['DELAY_CLASS'] = flights['ARRIVAL_DELAY'].apply(classify_delay)

# Filtros
col1, col2, col3, col4 = st.columns(4)

with col1:
    airline_sel = st.selectbox(
        "Companhia Aérea",
        [None] + sorted(flights['AIRLINE_y'].dropna().unique().tolist())
    )

with col2:
    month_sel = st.selectbox(
        "Mês",
        [None] + sorted(flights['MONTH'].dropna().unique().tolist())
    )

with col3:
    origin_sel = st.selectbox(
        "Aeroporto de Origem (Cidade)",
        [None] + sorted(flights['CITY'].dropna().unique().tolist())
    )

with col4:
    delay_sel = st.selectbox(
        "Nível de Atraso",
        [None, 'Baixo atraso', 'Médio atraso', 'Alto atraso']
    )

# Aplicar o filtro no DataFrame
df_filtered = flights.copy()

if airline_sel:
    df_filtered = df_filtered[df_filtered['AIRLINE_y'] == airline_sel]

if month_sel:
    df_filtered = df_filtered[df_filtered['MONTH'] == month_sel]

if origin_sel:
    df_filtered = df_filtered[df_filtered['CITY'] == origin_sel]

if delay_sel:
    df_filtered = df_filtered[df_filtered['DELAY_CLASS'] == delay_sel]



st.markdown(f"#### Total de voos filtrados: {len(df_filtered):,}")

st.subheader("📊 Atraso Médio por Companhia Aérea")
mean_delay = df_filtered.groupby('AIRLINE_y')['ARRIVAL_DELAY'].mean().reset_index()
fig_delay = px.bar(mean_delay, x='AIRLINE_y', y='ARRIVAL_DELAY',
                   color='ARRIVAL_DELAY', color_continuous_scale='Reds',
                   labels={'AIRLINE_y': 'Companhia', 'ARRIVAL_DELAY': 'Atraso Médio (min)'},
                   title='Atraso Médio por Companhia')
st.plotly_chart(fig_delay, use_container_width=True)

st.subheader("📈 Relação entre Distância e Atraso")
if len(df_filtered) > 0:
    fig_scatter = px.scatter(df_filtered.sample(min(5000, len(df_filtered))),
                             x='DISTANCE', y='ARRIVAL_DELAY',
                             color='MONTH',
                             labels={'DISTANCE': 'Distância (milhas)', 'ARRIVAL_DELAY': 'Atraso (min)'},
                             title='Dispersão Distância × Atraso')
    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.info("Nenhum dado disponível para os filtros selecionados.")


# Legenda com as cores para ser exibido no mapa
legend_html = """
<div style="
    position: fixed; 
    bottom: 50px; left: 50px; width: 220px; 
    background-color: white;
    border: 2px solid grey; 
    z-index:9999; 
    font-size:14px;
    padding: 10px;
">
<b>Legenda - Nível de Atraso</b><br>
<span style="color:green;">●</span> Baixo atraso (≤ 0.15)<br>
<span style="color:orange;">●</span> Médio atraso (0.15 – 0.30)<br>
<span style="color:red;">●</span> Alto atraso (> 0.30)
</div>
"""

st.subheader("🗺️ Mapa de Atrasos Médios por Aeroporto de Origem")
map_data = df_filtered.groupby(['CITY', 'LATITUDE', 'LONGITUDE'])['ARRIVAL_DELAY'].mean().reset_index()
if not map_data.empty:
    m = folium.Map(location=[37, -96], zoom_start=4)

    m.get_root().html.add_child(folium.Element(legend_html)) #ted

    for _, row in map_data.iterrows():
        folium.CircleMarker(
            location=[row['LATITUDE'], row['LONGITUDE']],
            radius=6,
            popup=f"{row['CITY']}: {row['ARRIVAL_DELAY']:.1f} min",
            color='red' if row['ARRIVAL_DELAY'] > 0.3 else 'orange' if row['ARRIVAL_DELAY'] > 0.15 else 'green',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)
    st_folium(m, width=2500, height=1200)
else:
    st.info("Sem dados suficientes para exibir o mapa.")

st.markdown("---")
st.caption("FIAP TECH CHALLENGE | Powered by Group 51, 6MLET | Dados de voos dos EUA (2015)")
