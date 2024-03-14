import streamlit as st
import requests
import base64

# Configuration initiale de la page
st.set_page_config(
    page_title="Amazing books",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="auto"
)

# Fonction pour obtenir l'image en base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Fonction pour définir l'image de fond
def set_background(image_path):
    encoded_image = get_image_base64(image_path)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center center;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Appliquer l'image de fond
# Remplacez par le chemin réel de votre image de fond
set_background("/Users/victorconte/Downloads/biblio.jpg")

# Conteneur pour le fond blanc
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400&display=swap');

.garamond {{
    font-family: 'EB Garamond', serif;
}}
</style>
""", unsafe_allow_html=True)

# Utilisation de la classe garamond pour les éléments spécifiques
with st.container():
    st.markdown('<p class="garamond">Comment était votre livre ?</p>', unsafe_allow_html=True)
    model = st.radio("Choisissez un algorithme :", ["Naive Bayes", "LSTM"], key="model")

comment = st.text_input("Entrez un commentaire :", key="comment")

if st.button("Générer une prédiction"):
    params = {
        'modele': model,
        'comment': comment
    }



    ################################# CALL THE API ######################################

    url = 'https://amazing-ympfzdipeq-ew.a.run.app/predict'

    response = requests.get(url, params=params)

    prediction = response.json()

    pred = prediction['prediction']


    st.title("")
    st.title("")

    # Style pour le cadre de réponse avec du texte noir et fond beige
    response_style = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400&display=swap');

.response-container {{
    font-family: 'EB Garamond', serif;
    border-radius: 5px;
    padding: 1rem;
    margin: 1rem 0;
    background-color: #fdefc2;  /* Couleur beige */
    color: #040c19;             /* Couleur du texte */
    font-size: 1.25rem;         /* Taille de la police */
}}
</style>
"""

    # Appliquer le style
    st.markdown(response_style, unsafe_allow_html=True)

    # Déterminez le message de la réponse
    response_message = "👍 It was a good book, wasn't it ?" if pred == 1 else "👎 👎 Looks like you didn't like it..."

    # Encapsuler le message dans un div pour appliquer le style
    st.markdown(f'<div class="response-container">{response_message}</div>', unsafe_allow_html=True)
