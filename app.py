import streamlit as st
import pandas as pd

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("data_mrc_logement.csv")

data = load_data()

# Nettoyage des colonnes
data.columns = data.columns.str.strip()

# Diagnostic : afficher les colonnes disponibles
st.write("Colonnes disponibles :", data.columns.tolist())
st.write("Types de colonnes :", [type(col) for col in data.columns])

# Titre
st.title("Évolution du nombre de logements par MRC (2015–2025)")

# Sélection de la MRC
selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))

# Filtrage des données pour la MRC sélectionnée
mrc_data = data[data["MRC"] == selected_mrc]

# Vérification
if not mrc_data.empty:
    mrc_row = mrc_data.iloc[0]
    st.write("Ligne de données sélectionnée :", mrc_row)

    # Liste des années en tant qu'entiers
    years = list(range(2015, 2026))

    # Création du DataFrame pour le graphique
    logement_data = pd.DataFrame({
        "Année": years,
        "Nombre de logements": [mrc_row[year] for year in years]
    })

    # Affichage du graphique
    st.subheader(f"Évolution du nombre de logements pour la MRC : {selected_mrc}")
    st.bar_chart(logement_data.set_index("Année"))

else:
    st.error("Aucune donnée trouvée pour la MRC sélectionnée.")
