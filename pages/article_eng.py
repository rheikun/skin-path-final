import streamlit as st
import os
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_article_eng():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_article = os.path.join(parent_dir, "../static/images/artikel-eng.png")

    # Muat CSS
    load_css(css_path)
    st.image(image_article, use_column_width=True)    
    st.markdown("<div class='title'>Artikel Terkait Perawatan Kulit</div>", unsafe_allow_html=True)  
    # Article 1: Benefits of Sunscreen for All Skin Types
    # Article 1: The Benefits of Sunscreen for All Skin Types
    st.write("""
        ### 1. The Benefits of Sunscreen for All Skin Types
        Sunscreen is an essential skincare product for everyone, regardless of skin type or weather conditions. It helps protect the skin from harmful UV rays that can cause premature aging, hyperpigmentation, and skin cancer.
        
        **Key benefits of sunscreen:**
        - Shields the skin from harmful UVA and UVB rays.
        - Prevents dark spots caused by sun exposure.
        - Reduces the risk of skin cancer.
        - Maintains skin elasticity by protecting collagen fibers.

        Apply sunscreen with at least SPF 30 every day, even indoors, to ensure maximum protection.
    """)

    # Article 2: Daily Skin Care Routine for Oily Skin
    st.write("""
        ### 2. Daily Skin Care Routine for Oily Skin
        Oily skin often struggles with acne, enlarged pores, and excess shine. With the right skincare routine, you can manage oil production and maintain healthy skin.

        **Daily care tips:**
        - Wash your face twice a day with a cleanser containing salicylic acid to control oil production.
        - Use a toner to minimize pores.
        - Choose a lightweight, oil-free moisturizer (non-comedogenic).
        - Avoid heavy products like greasy creams.
        - Use a clay mask once a week to absorb excess oil.

        Avoid over-washing your face, as it can lead to increased oil production as a compensatory mechanism.
    """)

    # Article 3: Tips for Choosing Products for Sensitive Skin
    st.write("""
        ### 3. Tips for Choosing Products for Sensitive Skin
        Sensitive skin requires extra care as it is prone to irritation. Selecting the wrong products can cause redness, itching, or even rashes.

        **Guidelines for choosing products:**
        - Look for labels like "hypoallergenic" or "sensitive skin-friendly."
        - Avoid ingredients like fragrances, alcohol, and parabens.
        - Opt for products with natural ingredients like aloe vera, chamomile, or oat.
        - Always perform a patch test before trying a new product.
        - Choose mineral-based sunscreens (zinc oxide or titanium dioxide) for a gentler option.

        Keep your skin hydrated with fragrance-free moisturizers, especially after cleansing.
    """)

    # Article 4: Foods That Are Good for Your Skin
    st.write("""
        ### 4. Foods That Are Good for Your Skin
        What you eat greatly affects the health and appearance of your skin. A balanced diet can improve skin texture, prevent premature aging, and combat acne.

        **Best foods for healthy skin:**
        - **Fruits and vegetables**: Carrots, oranges, and spinach are rich in vitamins A and C, promoting skin cell regeneration.
        - **Fatty fish**: Salmon and tuna contain omega-3 fatty acids that maintain skin elasticity.
        - **Nuts**: Almonds and walnuts are high in vitamin E, protecting skin from free radical damage.
        - **Water**: Staying hydrated keeps your skin plump and glowing.

        Avoid greasy, sugary, and processed foods to prevent common skin problems like acne.
    """)

    # Article 5: The Importance of Maintaining Facial Cleanliness
    st.write("""
        ### 5. The Importance of Maintaining Facial Cleanliness
        Clean skin is the foundation of any good skincare routine. Proper cleansing removes dirt, oil, and makeup that accumulate throughout the day.

        **Tips for keeping your face clean:**
        - Wash your face twice a day, morning and night.
        - Use lukewarm water (not hot) to avoid irritation.
        - Choose a cleanser suited to your skin type.
        - Avoid scrubbing your face harshly.
        - Always remove makeup before going to bed.

        A consistent cleansing routine can prevent breakouts and keep your skin fresh and healthy.
    """)

    # Article 6: What is Double Cleansing and Its Benefits?
    st.write("""
        ### 6. What is Double Cleansing and Its Benefits?
        Double cleansing is a two-step facial cleansing technique: first using an oil-based cleanser to remove oil-based impurities, then a water-based cleanser to remove water-based impurities.

        **Benefits of double cleansing:**
        - Thoroughly removes makeup and sunscreen.
        - Eliminates pollutants and dirt trapped in pores.
        - Helps prevent acne caused by clogged pores.

        This technique is highly recommended for those who wear makeup frequently or live in polluted areas.
    """)

    # Article 7: Why Moisturizer is Important for All Skin Types
    st.write("""
        ### 7. Why Moisturizer is Important for All Skin Types
        Moisturizers help lock in hydration and repair the skin's natural barrier. Even oily skin requires moisturizers to maintain balance.

        **Benefits of moisturizers:**
        - Keeps the skin hydrated and plump.
        - Prevents flakiness and dryness.
        - Helps smooth fine lines and wrinkles.

        Choose a lightweight moisturizer for oily skin and a richer one for dry skin.
    """)

    # Article 8: Summer Skin Care Tips
    st.write("""
        ### 8. Summer Skin Care Tips
        Summer heat increases the risk of sunburn, dehydration, and acne. Proper skincare during this season is essential.

        **Tips for summer skincare:**
        - Use sunscreen with high SPF daily.
        - Wear protective clothing like hats and sunglasses.
        - Avoid direct sun exposure from 10 AM to 4 PM.
        - Choose lightweight, oil-free skincare products.

        Staying hydrated and avoiding heavy makeup can also help your skin breathe better.
    """)

    # Article 9: Why Getting Enough Sleep is Crucial for Healthy Skin
    st.write("""
        ### 9. Why Getting Enough Sleep is Crucial for Healthy Skin
        Quality sleep allows the skin to repair damaged cells and produce collagen, essential for maintaining skin elasticity.

        **Benefits of adequate sleep:**
        - Promotes skin elasticity and reduces wrinkles.
        - Prevents puffiness and dark circles under the eyes.
        - Enhances skin regeneration and brightness.

        Aim for 7-8 hours of sleep per night for glowing, healthy skin.
    """)