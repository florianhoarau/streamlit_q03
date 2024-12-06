import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
# Nos données utilisateurs doivent respecter ce format

authdata = {'usernames': {'guest': {'name': 'guest',
   'password': 'guestPWD',
   'email': 'guest@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'guest'},
  'root': {'name': 'admin',
   'password': 'adminPWD',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'admin'}}}

authenticator = Authenticate(
    authdata, # Les données des comptes
    "cookie_name_0", # Le nom du cookie, un str quelconque
    "cookie_key_0", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():


# Using "with" notation
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options = ["Home", "Pictures"]
        )

    if selection == "Home":
        st.header("Enjoy this streamlit app :minidisc:")
        st.image("dogg.jpg")
    elif selection == "Pictures":
        st.header("Pictures :chicken:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Bip-Bip")
            st.image("01.jpg")
            st.text(f"*Poule de Laure*")

        with col2:
            st.header("Roussette")
            st.image("02.jpg")
            st.text(f"*Poule de Clément*")

        with col3:
            st.header("Pépite")
            st.image("03.jpg")
            st.text(f"*Poule d'Anaïs*")

if st.session_state["authentication_status"]:
    st.header(f'Welcome *{st.session_state["name"]}*')
    accueil()
    # Le bouton de déconnexion
    authenticator.logout("Disconnect")

elif st.session_state["authentication_status"] is False:
    st.error("Username and password combination is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Please login')