import streamlit as st
import os

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_about_eng():
    # Tentukan path file CSS
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_article = os.path.join(parent_dir, "../static/images/about-eng.png")

    # Muat CSS
    load_css(css_path)
    st.image(image_article, use_column_width=True)
    st.title("About the Application")
    st.write("""
        ### What is SkinPath?
        **SkinPath** is an AI-powered application designed to help users understand their skin type through facial image analysis. The application is developed with the goal of providing more personalized and targeted skincare guidance.

        ### Key Features:
        - **Skin Type Detection**: Using deep learning technology with the ResNet50 model, this application can detect three main skin types—dry, oily, and normal—simply by analyzing the user's facial photo.
        - **Product and Skincare Ingredient Recommendations**: After determining the skin type, the app provides product and skincare ingredient recommendations tailored to specific skincare goals.
        - **Ingredient Information**: For each suggested or avoidable ingredient, SkinPath offers explanations about its benefits and potential side effects, helping users make informed decisions.

        ### How the Application Works:
        1. **Select Input Method**: Users can choose to take a picture directly via the camera or upload a photo from their device.
        2. **Skin Type Detection**: The uploaded image is then processed by the ResNet50 model, which has been specifically trained to identify skin types.
        3. **Skincare Recommendations**: Based on the skin type analysis and desired skincare goals, the app provides ingredient recommendations to use or avoid, along with guidance for a suitable skincare routine.
        4. **Ingredient Explanation**: Users can view detailed information about each suggested ingredient, including its benefits, potential side effects, and suitability for various skin types.

        ### Technology Behind SkinPath:
        - **ResNet50 Deep Learning Model**: A custom-trained model to detect skin types based on facial images.
        - **PyTorch Framework**: The application uses PyTorch to load and run the deep learning model.
        - **Streamlit**: SkinPath is built with Streamlit, a Python framework that allows for quick and easy creation of interactive user interfaces.

        ### Disclaimer:
        The information provided by SkinPath is general guidance based on skin type. However, each individual's skin condition may vary, and the app’s analysis may not account for specific factors like sensitivities or allergies. For more accurate results, always consult a dermatologist or healthcare professional before making significant changes to your skincare routine.

        ### Developer:
        SkinPath was developed as a final project for a Web Application Practice course related to the use of AI in skincare. The hope is that this application can be a useful tool in helping users understand and care for their skin better.

        **Developer**: Rheisan Firnandatama Rizky Satria || **Student ID**: 22537141021

        **Thank you for using SkinPath!**
        """)