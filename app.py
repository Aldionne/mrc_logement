import streamlit as st
import pandas as pd
import altair as alt

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("data_mrc_logement.csv", sep=",", engine="python")
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: str(x).strip(";") if isinstance(x, str) else x)
    return df

data = load_data()

# Titre
st.title("Portrait de l'habitation par MRC")

# Sélection de la MRC
selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))

# Filtrage des données pour la MRC sélectionnée
mrc_data = data[data["MRC"] == selected_mrc]

# Vérification qu'on a bien une ligne
if not mrc_data.empty:
    mrc_row = mrc_data.iloc[0]
    years = [str(year) for year in range(2015, 2026)]

    # Création de la DataFrame pour le graphique
    logement_data = pd.DataFrame({
        "Année": years,
        "Nombre de logements": [int(mrc_row[year]) for year in years]
    })

    st.subheader(f"Évolution du nombre de logements (2015-2025) {selected_mrc}")

    # Création du graphique avec Altair
   chart = alt.Chart(logement_data).mark_line(point=alt.OverlayMarkDef(filled=True, size=100), strokeWidth=3).encode(
    x=alt.X("Année:O", title="Année"),
    y=alt.Y("Nombre de logements:Q", title="Nombre de logements"),
    tooltip=["Année", "Nombre de logements"]
).properties(
    width=700,
    height=400,
    title=f"Évolution du nombre de logements - {selected_mrc}"
).interactive()

    st.altair_chart(chart, use_container_width=True)

else:
    st.error("Aucune donnée trouvée pour la MRC sélectionnée.")
