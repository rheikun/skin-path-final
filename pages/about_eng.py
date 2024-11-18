import streamlit as st
import os

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_about_eng():
    # Tentukan path file CSS
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_about = os.path.join(parent_dir, "../static/images/about-eng.png")

    # Muat CSS
    load_css(css_path)
    # Page content
    st.image(image_about, use_column_width=True)
    st.markdown("<div class='section-title'>About the Application</div>", unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>What is SkinPath?</h2>
                    <p class = 'section-content'><strong>SkinPath</strong> is an AI-based application designed to help users understand their skin type through facial image analysis. The application aims to provide more personalized and precise skincare guidance.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Main Features of the Application</h2>
                    <p class = 'section-content'><strong>- Skin Type Detection</strong>: Utilizing deep learning technology with the ResNet50 model, this app can identify three main skin types—dry, oily, and normal—simply by analyzing the user's facial photo.</p>
                    <p class = 'section-content'><strong>- Product and Skincare Ingredient Recommendations</strong>: After detecting the skin type, the application provides product recommendations and suitable skincare ingredients based on specific skincare goals.</p>
                    <p class = 'section-content'><strong>- Active Ingredient Information</strong>: For every recommended or avoidable ingredient, SkinPath provides explanations about the benefits and potential side effects, helping users make informed decisions.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>How the Application Works</h2>
                    <p class = 'section-content'><strong>1. Choose Input Method</strong>: Users can choose to take a live photo through the camera or upload an image from their device.</p>
                    <p class = 'section-content'><strong>2. Detect Skin Type</strong>: The uploaded image is processed through the ResNet50 model, specifically trained to identify skin types.</p>
                    <p class = 'section-content'><strong>3. Skincare Recommendations</strong>: Based on the skin type analysis and desired skincare goals, the application provides ingredient recommendations to use or avoid, along with suitable skincare routine guidance.</p>
                    <p class = 'section-content'><strong>4. Ingredient Information</strong>: Users can view detailed information about each suggested ingredient, including its benefits, potential side effects, and suitability for various skin types.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Technology Behind SkinPath</h2>
                    <p class = 'section-content'><strong>- ResNet50 Deep Learning Model</strong>: A model tailored for detecting skin types based on facial images.</p>
                    <p class = 'section-content'><strong>- PyTorch Framework</strong>: The application uses PyTorch to load and run the deep learning model.</p>
                    <p class = 'section-content'><strong>- Streamlit</strong>: SkinPath is built using Streamlit, a Python framework that allows for the quick and easy creation of interactive user interfaces.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Disclaimer</h2>
                    <p class = 'section-content'>The information provided by SkinPath is general guidance based on skin type. However, every individual's skin condition is unique, and the application's analysis results may not consider specific factors such as sensitivities or allergies. For more accurate results, always consult with a dermatologist or healthcare professional before making significant changes to your skincare routine.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Note</h2>
                    <p class = 'section-content'>The SkinPath application was developed as a final project for the Web Application Practice course, focusing on the use of AI for skincare. The hope is that this application can serve as a useful tool in helping users understand and care for their skin better.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Developer</div>", unsafe_allow_html=True)
    st.markdown(f"""
                <div class='section'>
                        <div class='circular-position'>
                            <img src="https://media.tenor.com/JuV-wJ4v58EAAAAe/appa-the-goat.png" class="circular-image">
                            <p class = 'section-content-pengembang'>Rheisan Firnandatama Rizky Satria</p>
                            <p class = 'section-content-pengembang'>22537141021</p>
                        </div>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-section">
        <h2>Contact Developer</h2>
        <div class="icon-container">
            <a href="https://www.linkedin.com/in/rheisanfrs/" target="_blank" class="social-icon linkedin"></a>
            <a href="https://www.instagram.com/rheisanfrs/" target="_blank" class="social-icon instagram"></a>
            <a href="mailto:rheisanfirnandatama.2022@student.uny.ac.id" class="social-icon email"></a>
        </div>
    </div>
    """, unsafe_allow_html=True)
