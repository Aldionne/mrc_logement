import streamlit as st
import pandas as pd

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("data_mrc_logement.csv")

data = load_data()  

# Diagnostic : afficher les colonnes disponibles
st.write("Colonnes du CSV :", data.columns.tolist())

# Titre
st.title("Évolution du nombre de logements par MRC (2015–2025)")

# Sélection de la MRC
selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))

# Filtrage des données pour la MRC sélectionnée
mrc_data = data[data["MRC"] == selected_mrc].iloc[0]

# Sous-titre
st.subheader(f"Évolution du nombre de logements pour la MRC : {selected_mrc}")

# Création d'une série temporelle à partir des colonnes 2015 à 2025
years = [str(year) for year in range(2015, 2026)]

# Affichage pour diagnostic (facultatif)
st.write("Valeurs pour la MRC sélectionnée :", mrc_data)

# Construction des données pour le graphique
logement_data = pd.DataFrame({
    "Année": years,
    "Nombre de logements": [mrc_data[year] for year in years]
})

# Affichage du graphique
st.bar_chart(logement_data.set_index("Année"))
