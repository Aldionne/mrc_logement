import streamlit as st
import pandas as pd

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("data_mrc_logement.csv")

data = load_data()

# Nettoyage (au cas où il y aurait des espaces dans les noms de colonnes)
data.columns = data.columns.str.strip()

# Diagnostic : afficher les colonnes
st.write("Colonnes disponibles :", data.columns.tolist())

# Titre
st.title("Évolution du nombre de logements par MRC (2015–2025)")

# Sélection de la MRC
selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))

# Filtrage des données pour la MRC sélectionnée
mrc_data = data[data["MRC"] == selected_mrc]

# Vérification qu'on a bien une ligne
if not mrc_data.empty:
    mrc_row = mrc_data.iloc[0]

    st.write("Ligne de données sélectionnée :", mrc_row)

    # Plage d’années
    years = [str(year) for year in range(2015, 2026)]

    # Création de la DataFrame pour le graphique
    logement_data = pd.DataFrame({
        "Année": years,
        "Nombre de logements": [mrc_row[year] for year in years]
    })

    # Affichage du graphique
    st.subheader(f"Évolution du nombre de logements pour la MRC : {selected_mrc}")
    st.bar_chart(logement_data.set_index("Année"))

else:
    st.error("Aucune donnée trouvée pour la MRC sélectionnée.")
