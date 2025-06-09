import streamlit as st
import pandas as pd

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("data_mrc.csv")

data = load_data()

# Titre
st.title("Indicateurs sur le logement et l'habitation")

# Sélection de la MRC
selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))

# Filtrage
mrc_data = data[data["MRC"] == selected_mrc].iloc[0]

# Affichage des données
st.subheader(f"Indicateurs pour la MRC : {selected_mrc}")
st.metric("Population", f"{mrc_data['Population']:,}")
st.metric("Logements", f"{mrc_data['Logements']:,}")
st.metric("Superficie (km²)", f"{mrc_data['Superficie_km2']:,}")
st.metric("Revenu médian", f"{mrc_data['Revenu_median']:,} $")

# Graphique
st.subheader("Comparaison des indicateurs")
chart_data = pd.DataFrame({
    'Indicateur': ['Population', 'Logements', 'Superficie (km²)', 'Revenu médian'],
    'Valeur': [
        mrc_data['Population'],
        mrc_data['Logements'],
        mrc_data['Superficie_km2'],
        mrc_data['Revenu_median']
    ]
})
st.bar_chart(chart_data.set_index("Indicateur"))