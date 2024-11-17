import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(page_title="SkinPath",page_icon="👩‍⚕️",initial_sidebar_state="collapsed")

pages = ["Dashboard", "Article", "About", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
styles = {
    "nav": {
        "background-color": "#5dc5d9",
        "justify-content": "right",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "10px",
    },
    "active": {
        "color": "#14525e",
        "font-weight": "reguler",
        "padding": "8px",
        "border-radius": "10px",  # This sets the corner radius to 8px
    }
}

options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    urls=urls,
    styles=styles,
    options=options,
)
functions = {}

if 'bahasa_dipilih' not in st.session_state:
    st.session_state['bahasa_dipilih'] = False

# Tampilkan judul hanya jika bahasa belum dipilih
if not st.session_state['bahasa_dipilih']:
    st.title("Pilih Bahasa / Choose Language")
    bahasa = st.selectbox("Pilih Bahasa:", ["Indonesia", "English"])

    # Set bahasa di session_state setelah dipilih
    if st.button("Lanjut"):
        st.session_state['bahasa'] = bahasa
        st.session_state['bahasa_dipilih'] = True

# Menampilkan halaman dashboard sesuai bahasa yang dipilih setelah tombol lanjut ditekan
if st.session_state.get('bahasa_dipilih', False):
    if st.session_state['bahasa'] == "Indonesia":
        functions = {
            "Dashboard": pg.show_dashboard_id,
            "Article": pg.show_article_id,
            "About": pg.show_about_id,
        }
    elif st.session_state['bahasa'] == "English":
        functions = {
            "Dashboard": pg.show_dashboard_eng,
            "Article": pg.show_article_eng,
            "About": pg.show_about_eng,
        }

# Execute the appropriate function
go_to = functions.get(page)
if go_to:
    go_to()