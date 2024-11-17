import streamlit as st
import os
from pages.dashboard_eng import show_dashboard_eng
from pages.dashboard_id import show_dashboard_id

def show_home():
# Set Streamlit page configuration
    st.set_page_config(
        page_title="SkinPath",
        page_icon="👩‍⚕️",
    )
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../static/style/style.css")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)

    # Memilih bahasa dengan dropdown
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
    if st.session_state.get('bahasa_dipilih'):
        if st.session_state['bahasa'] == "Indonesia":
            show_dashboard_id()  # Memanggil fungsi dari dashboard_id.py
        elif st.session_state['bahasa'] == "English":
            show_dashboard_eng()  # Memanggil fungsi dari dashboard_eng.py
            


