import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io
import os
import importlib

# Fungsi utama untuk aplikasi
def show_dashboard_eng():
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    image_landing = os.path.join(parent_dir, "../static/images/logo.png")
    image_dashboard = os.path.join(parent_dir, "../static/images/dashboard-eng.png")
    # Memuat CSS
    css_path = os.path.join(parent_dir, "../static/style/style.css")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)

    # Load model architecture (ResNet50)
    model = models.resnet50(pretrained=False)
    model.fc = nn.Linear(in_features=2048, out_features=3)  # Adjust for skin types

    # Load model weights
    state_dict = torch.load("./models/model.pth", map_location=torch.device('cpu'))
    del state_dict['fc.weight']
    del state_dict['fc.bias']
    model.load_state_dict(state_dict, strict=False)
    model.eval()

    # Function for image preprocessing
    def preprocess_image(image):
        transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Resize image
            transforms.ToTensor(),  # Convert image to tensor
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
        ])
        image = Image.open(io.BytesIO(image))  # Read image from bytes
        return transform(image).unsqueeze(0)  # Return image in expected model format

    # Function to predict skin type
    def predict_skin_type(image):
        with torch.no_grad():  # Disable gradient calculation
            inputs = preprocess_image(image)  # Preprocess the image
            outputs = model(inputs)  # Get model output
            _, predicted = torch.max(outputs, 1)  # Take prediction with highest value
            return predicted.item()  # Return prediction
        
    # Explanation for each ingredient
    def ingredient_explanation(ingredient):
        explanations = {
            "Alcohol": "Can dry out the skin and strip its natural oils, potentially worsening dry skin.",
            "Fragrance": "Can cause irritation, especially for sensitive or dry skin.",
            "Benzoyl Peroxide": "Effective for acne treatment but can be drying, especially for dry or sensitive skin.",
            "Mineral Oil": "May clog pores, so it’s not suitable for oily or acne-prone skin.",
            "Lanolin": "An emollient that traps oils, thus less suitable for oily skin.",
            "Petrolatum": "Although it locks in moisture, it can be too heavy for oily skin and might clog pores.",
            "Hyaluronic Acid": "A humectant that helps the skin retain moisture, ideal for dry skin.",
            "Ceramides": "Helps repair the skin barrier, retaining moisture and preventing dryness.",
            "Squalane": "A lightweight oil that moisturizes the skin without making it greasy, suitable for dry and normal skin.",
            "Salicylic Acid": "A beta hydroxy acid (BHA) that exfoliates and cleanses pores, ideal for oily or acne-prone skin.",
            "Niacinamide": "An anti-inflammatory ingredient that regulates oil production and improves skin barrier function.",
            "Clay": "Absorbs excess oil from the skin, very suitable for oily skin.",
            "Glycerin": "A moisturizing ingredient that attracts moisture into the skin, suitable for all skin types.",
            "Centella Asiatica": "Soothes irritation and helps repair the skin barrier, beneficial for sensitive or dry skin.",
            "Aloe Vera": "Has soothing and moisturizing properties, suitable for normal and sensitive skin.",
            "Retinol": "A vitamin A derivative that promotes cell turnover and helps reduce signs of aging and acne.",
            "Vitamin C": "An antioxidant that brightens the skin and helps reduce hyperpigmentation.",
            "Tea Tree Oil": "A natural antiseptic that helps treat acne and soothe inflammation.",
            "Peptides": "Amino acids that help build skin proteins, promoting firmness and reducing wrinkles.",
            "Zinc": "A mineral that helps regulate oil production and can calm acne-prone skin.",
            "Lactic Acid": "An alpha hydroxy acid (AHA) that gently exfoliates and moisturizes, ideal for dry skin.",
            "Argan Oil": "An oil rich in fatty acids and vitamin E, excellent for moisturizing dry skin.",
            "Witch Hazel": "A natural astringent that can help reduce inflammation and tighten pores, suitable for oily skin.",
            "Cucumber Extract": "Known for its soothing and moisturizing properties, perfect for sensitive skin.",
            "Willow Bark": "A natural source of salicylic acid that helps treat acne and exfoliate the skin.",
            "Harsh Sulfates": "Cleansing agents that can be too harsh, especially for sensitive or dry skin, and may cause irritation or dryness.",
            "Panthenol": "Also known as provitamin B5, this ingredient helps soothe, moisturize, and repair the skin barrier.",
            "Cholesterol": "A moisturizing ingredient that helps repair the skin barrier, maintaining moisture and elasticity.",
            "Azelaic Acid": "Helps reduce redness and treat acne, as well as brightening hyperpigmentation.",
            "Licorice Root": "A natural brightening extract that helps reduce dark spots.",
            "Alpha Arbutin": "An ingredient that helps reduce melanin production and is suitable for skin brightening.",
            "Kojic Acid": "A natural ingredient that helps lighten skin and reduce hyperpigmentation.",
        }
        return explanations.get(ingredient, "No explanation available.")

    # Function to suggest chemicals
    def suggest_chemicals(skin_type, goal):
        chemicals_to_avoid = {
            0: ["Alcohol", "Fragrance"],
            1: ["Mineral Oil", "Petrolatum"],
            2: ["Harsh Sulfates", "Fragrance"]
        }
        chemicals_to_use = {
            0: ["Hyaluronic Acid", "Ceramides"],
            1: ["Salicylic Acid", "Niacinamide"],
            2: ["Glycerin", "Centella Asiatica"]
        }
        goal_suggestions = {
            "Skin Barrier Repair": {0: ["Ceramides"], 1: ["Niacinamide"], 2: ["Panthenol"]},
            "Acne Treatment": {0: ["Azelaic Acid"], 1: ["Benzoyl Peroxide"], 2: ["Tea Tree Oil"]},
            "Skin Whitening": {0: ["Vitamin C"], 1: ["Alpha Arbutin"], 2: ["Kojic Acid"]}
        }
        return chemicals_to_avoid[skin_type], chemicals_to_use[skin_type], goal_suggestions[goal][skin_type]

    # Skincare routine
    def skincare_routine(skin_type):
        routines = {
            0: {"Morning": ["Gentle Cleanser", "Hyaluronic Acid", "Moisturizer", "Sunscreen"],
                "Evening": ["Cream Cleanser", "Retinol", "Moisturizer"]},
            1: {"Morning": ["Foaming Cleanser", "Niacinamide", "Moisturizer", "Sunscreen"],
                "Evening": ["Gel Cleanser", "Salicylic Acid Treatment", "Oil-Free Moisturizer"]},
            2: {"Morning": ["Gentle Cleanser", "Vitamin C Serum", "Moisturizer", "Sunscreen"],
                "Evening": ["Gentle Cleanser", "Peptides Serum", "Moisturizer"]}
        }
        return routines[skin_type]

    # Initialize
    if 'landing_done' not in st.session_state:
        st.session_state['landing_done'] = False
    if 'image_confirmed' not in st.session_state:
        st.session_state['image_confirmed'] = False
    if 'show_about' not in st.session_state:
        st.session_state['show_about'] = False

    # Landing Page
    if not st.session_state['landing_done']:
        st.title("Welcome to SkinPath 👩‍⚕️")
        st.image(image_landing, use_column_width=True)
        st.markdown("""
            ### Key Features:
            - 🧴 **Skin Type Detection**: Upload or capture a photo to analyze your skin type. The app will identify if your skin is dry, oily, or normal.
            - 🔍 **Skincare Product Recommendations**: After detecting your skin type, the app provides suitable product suggestions and ingredient information based on your chosen skincare goal.
            - 🧪 **Ingredient Explanations**: For each ingredient mentioned in recommendations, the app provides a detailed explanation of its benefits and potential side effects.

            ### How to Use:
            1. **Choose Input Method**: In the sidebar, select whether you want to capture an image or upload a photo from your device.
            2. **Upload or Capture Photo**: Ensure a clear, well-lit image without shadows.
            3. **Confirm Image**: After uploading or capturing a photo, click **Confirm Image** to proceed with the skin type analysis.
            4. **View Recommendations**: After analysis, the app will display your skin type and provide product recommendations based on your selected skincare goal.
            5. **Restart**: If you want to repeat the analysis, click **Restart Analysis** at the bottom of the page.
            
            ### Disclaimer
            The information provided here is for reference only. Keep in mind there are other determining variables, such as skin sensitivity, that this app may not support. Make sure to consult a healthcare professional or dermatologist before making skincare decisions.
            
            > **Tip**: For best results, use a photo with natural lighting and a clean face without excess makeup.
            """)
        
        if st.button("Proceed to Analysis"):
            st.session_state['landing_done'] = True
            st.rerun()
    
    elif st.session_state['landing_done']:
            st.image(image_dashboard, use_column_width=True)
            st.title("SkinPath App 👩‍⚕️")
            st.subheader("Input Method")
            input_option = st.selectbox("Select Image Input:", ("📸Capture Image", "📄Upload Photo"))

            if input_option == "📸Capture Image":
                st.info("Make sure you have a clear view of your face with no shadows, and enough lighting to maximize the results.")
            
            image = st.camera_input("Take a photo") if input_option == "📸Capture Image" else st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])

            if image and not st.session_state['image_confirmed']:
                st.markdown("### Image Preview:")
                st.image(image, caption="Your Image", use_column_width=True)
                if st.button("Confirm Image"):
                    st.session_state['image_confirmed'] = True
                    img_bytes = image.read() if hasattr(image, 'read') else image.getvalue()
                    skin_type = predict_skin_type(img_bytes)
                    st.session_state['skin_type'] = skin_type
                    st.rerun()
            
            elif st.session_state['image_confirmed']:
                skin_types = ["Dry", "Oily", "Normal"]
                st.success(f"Detected Skin Type: **{skin_types[st.session_state['skin_type']]}**")

                routine = skincare_routine(st.session_state['skin_type'])
                st.markdown("<div class='sub-header'>Skincare Routine Suggestions</div>", unsafe_allow_html=True)
                morning, evening = st.columns(2)
                
                with morning:
                    st.subheader("🌞 Morning Routine")
                    for step in routine["Morning"]:
                        st.write(f"🔹 {step}")

                with evening:
                    st.subheader("🌜 Evening Routine")
                    for step in routine["Evening"]:
                        st.write(f"🔹 {step}")
                
                st.header("Set Your Skincare Goal 🎯")
                goal = st.selectbox(
                    "Choose your skincare goal:", 
                    ["Skin Barrier Repair", "Acne Treatment", "Skin Whitening"],
                    help="Select your primary skincare goal to receive ingredient recommendations."        )

                avoid, recommend, additional = suggest_chemicals(st.session_state['skin_type'], goal)
                st.markdown("### Ingredients to Avoid 🚫")
                st.write(", ".join(avoid))

                st.markdown("### Recommended Ingredients ✅")
                st.write(", ".join(recommend))

                st.markdown("### Additional Ingredients for Goals 💡")
                st.write(", ".join(additional))

                unique_ingredients = list(set(avoid + recommend + additional))

                st.markdown("### Ingredient Explanations 📖")
                for ingredient in unique_ingredients:
                    with st.expander(f"{ingredient} 📜"):
                        st.write(ingredient_explanation(ingredient))

                if st.button("Restart Analysis"):
                    st.session_state['image_confirmed'] = False
                    st.session_state['skin_type'] = None
                    st.session_state['image'] = None
                    st.rerun()