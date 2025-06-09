import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("data_mrc_logement.csv")

data = load_data()
data.columns = data.columns.str.strip()

# Debug utile
st.write("Colonnes disponibles (debug) :", [repr(c) for c in data.columns])

st.title("Évolution du nombre de logements par MRC (2015–2025)")

selected_mrc = st.selectbox("Choisissez une MRC", sorted(data["MRC"].unique()))
mrc_data = data[data["MRC"] == selected_mrc]

if not mrc_data.empty:
    mrc_row = mrc_data.iloc[0]

    # Cette ligne récupère toutes les années automatiquement et évite les KeyError
    years = [col for col in data.columns if col != "MRC"]

    logement_data = pd.DataFrame({
        "Année": years,
        "Nombre de logements": [mrc_row[year] for year in years]
    })

    st.subheader(f"Évolution du nombre de logements pour la MRC : {selected_mrc}")
    st.bar_chart(logement_data.set_index("Année"))
else:
    st.error("Aucune donnée trouvée pour la MRC sélectionnée.")
