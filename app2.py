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
set_background("data/biblio.jpg")

# Conteneur pour le fond blanc

col1,col2,col3= st.columns(3)

with col2:
    st.markdown('<h1 style="color: white;">How was your book?</h1>', unsafe_allow_html=True)

        # Choix du modèle


    # Widget radio avec des éléments colorés
    st.markdown(
    """
    <style>
        .st-eb .st-d7 .st-da {
            font-size: px; /* Changer la taille de la police */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Widget radio avec une taille de police plus grande
    model = st.radio("Choose an algorithm:", ["Naive Bayes", "LSTM"])
# Exemple d'utilisation du modèle sélectionné

    if model == "Naive Bayes":
        model_clean="naive"
    else:
        model_clean="lstm"


    # Entrée de texte
    comment = st.text_input("")

    response_placeholder = st.empty()
    # Affichage de la prédiction
    # Bouton pour déclencher l'action
    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400&display=swap');
    .stButton button {
        color: #040c19; /* Couleur de la typographie */
        background-color: #fdefc2; /* Couleur du bouton */
        font-family: 'EB Garamond', serif; /* Typographie du bouton */
        font-size: 16px; /* Taille de la typographie */
        padding: 8px 16px; /* Espacement du texte à l'intérieur du bouton */
        border-radius: 5px; /* Bordure arrondie du bouton */
        border: none; /* Supprime la bordure du bouton */
    }
    .stButton button:hover {
        background-color: #040c19; /* Couleur du bouton au survol */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Affichage du bouton personnalisé

    if st.button("Générer une prédiction"):
        params = {
            'modele': model_clean,
            'comment': comment
    }



    ################################# CALL THE API ######################################

        col1,col2,col3 =st.columns(3)
        with col2:
            url = 'https://amazing2-ympfzdipeq-ew.a.run.app/predict'


            response = requests.get(url, params=params)

            prediction = response.json()

            pred = prediction['prediction']


            st.title("")
            st.title("")

            # Style pour le cadre de réponse avec du texte noir et fond beige
        if model_clean=="naive":
            response_message = "👍 It was a good book, wasn't it ?" if pred == 1 else "👎 Looks like you didn't like it..."
        elif model_clean=='lstm':
            if pred == 1:
                response_message = "👍 It was a good book, wasn't it ?"
            elif pred==0:
                response_message = "👉 Not so sure about it?"
            elif pred==-1:
                response_message = "👎 Looks like you didn't like it..."


        # Appliquer le style de fond en fonction de la valeur de pred
        if pred == 1:
            background_color = "#C1FFC1"  # Vert pâle
        elif pred==0:
            background_color = "#FFFF99"  # Jaune pâle
        else:
            background_color = "#FFC0CB"  # Rouge pâle

        # Appliquer le style dynamique
        response_style = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400&display=swap');

        .response-container {{
        font-family: 'EB Garamond', serif;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        color: #040c19;             /* Couleur du texte */
        font-size: 1.25rem;         /* Taille de la police */
        background-color: {background_color};  /* Couleur de fond dynamique */
        }}
        </style>
        """

        # Appliquer le style
        st.markdown(response_style, unsafe_allow_html=True)

        # Afficher la réponse
        st.markdown(f'<div class="response-container">{response_message}</div>', unsafe_allow_html=True)
