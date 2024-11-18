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
    st.markdown("<div class='section-title'>Related Articles on Skincare</div>", unsafe_allow_html=True)

    # Article 1: Benefits of Sunscreen for All Skin Types
    st.markdown("""
    <div class='section'>
        <h2>1. Benefits of Sunscreen for All Skin Types</h2>
        <p class='section-content'>Sunscreen is a skincare product that should not be skipped by anyone, regardless of skin type or weather. Sunscreen helps protect the skin from UV damage, which can cause skin cancer, premature aging, and hyperpigmentation.</p>
        <p class='section-content'><strong>Main benefits of sunscreen:</strong></p>
        <ul class='section-content'>
            <li>Protects the skin from UVA and UVB rays.</li>
            <li>Prevents dark spots caused by sun exposure.</li>
            <li>Reduces the risk of skin cancer.</li>
            <li>Preserves skin elasticity by preventing collagen damage.</li>
        </ul>
        <p class='section-content'>For best results, use sunscreen with at least SPF 30 daily, even when indoors.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 2: Daily Skincare Routine for Oily Skin
    st.markdown("""
    <div class='section'>
        <h2>2. Daily Skincare Routine for Oily Skin</h2>
        <p class='section-content'>Oily skin often faces issues such as acne, large pores, and excess shine. However, with the right routine, you can control oil production and keep your skin healthy.</p>
        <p class='section-content'><strong>Daily care tips:</strong></p>
        <ul class='section-content'>
            <li>Cleanse your face twice a day with a salicylic acid-based cleanser to reduce excess oil.</li>
            <li>Use a toner to minimize pores.</li>
            <li>Choose a lightweight, oil-free (non-comedogenic) moisturizer.</li>
            <li>Avoid heavy products like overly greasy creams.</li>
            <li>Use a clay mask once a week to reduce oil production.</li>
        </ul>
        <p class='section-content'>Avoid over-washing your face, as this can trigger more oil production as a compensation mechanism.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 3: Tips for Choosing Products for Sensitive Skin
    st.markdown("""
    <div class='section'>
        <h2>3. Tips for Choosing Products for Sensitive Skin</h2>
        <p class='section-content'>Sensitive skin requires extra care as it is prone to irritation. Choosing the wrong products can lead to rashes, redness, or itchiness.</p>
        <p class='section-content'><strong>Guidelines for selecting products:</strong></p>
        <ul class='section-content'>
            <li>Opt for products labeled as "hypoallergenic" or "sensitive skin".</li>
            <li>Avoid ingredients like fragrances, alcohol, and parabens.</li>
            <li>Use products with natural ingredients such as aloe vera, chamomile, or oat.</li>
            <li>Always perform a patch test before trying new products.</li>
            <li>Choose mineral-based sunscreens (like zinc oxide or titanium dioxide) as they are gentler on sensitive skin.</li>
        </ul>
        <p class='section-content'>Additionally, keep your skin hydrated by regularly applying fragrance-free moisturizers, especially after cleansing your face.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 4: Foods That Are Good for Your Skin
    st.markdown("""
    <div class='section'>
        <h2>4. Foods That Are Good for Your Skin</h2>
        <p class='section-content'>What you consume has a significant impact on your skin's health and appearance. The right nutrients can improve skin texture, prevent premature aging, and fight acne.</p>
        <p class='section-content'><strong>Best foods for your skin:</strong></p>
        <ul class='section-content'>
            <li><strong>Bright-colored fruits and vegetables:</strong> Carrots, oranges, and spinach are rich in vitamins C and A, which aid in skin cell regeneration.</li>
            <li><strong>Fatty fish:</strong> Such as salmon and tuna, contain omega-3s that help maintain skin elasticity.</li>
            <li><strong>Nuts:</strong> Rich in vitamin E, which protects the skin from free radical damage.</li>
            <li><strong>Water:</strong> Keeps the skin hydrated from within.</li>
        </ul>
        <p class='section-content'>Avoid greasy foods, excess sugar, and processed foods to prevent skin problems such as acne.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 5: Importance of Keeping Your Face Clean
    st.markdown("""
    <div class='section'>
        <h2>5. Importance of Keeping Your Face Clean</h2>
        <p class='section-content'>Face hygiene is the foundation of a good skincare routine. Properly cleansing your face removes dirt, oil, and makeup buildup throughout the day.</p>
        <p class='section-content'><strong>Tips for maintaining face cleanliness:</strong></p>
        <ul class='section-content'>
            <li>Wash your face twice a day, morning and night.</li>
            <li>Use lukewarm water (not hot) to avoid irritation.</li>
            <li>Choose a cleanser suitable for your skin type.</li>
            <li>Avoid scrubbing your face too hard.</li>
            <li>Always remove makeup before sleeping.</li>
        </ul>
        <p class='section-content'>With consistent habits, you can prevent acne and keep your skin fresh.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 6: What is Double Cleansing and Its Benefits?
    st.markdown("""
    <div class='section'>
        <h2>6. What is Double Cleansing and Its Benefits?</h2>
        <p class='section-content'>Double cleansing is a technique that involves two steps: first removing oil-based impurities with an oil-based cleanser, followed by cleansing with a water-based cleanser.</p>
        <p class='section-content'><strong>Benefits of double cleansing:</strong></p>
        <ul class='section-content'>
            <li>Thoroughly removes makeup and sunscreen residues.</li>
            <li>Cleanses dirt that regular cleansers might miss.</li>
            <li>Helps prevent acne caused by clogged pores.</li>
        </ul>
        <p class='section-content'>This technique is highly recommended for those who wear makeup frequently or live in cities with high pollution levels.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 7: Why is Moisturizer Important for All Skin Types?
    st.markdown("""
    <div class='section'>
        <h2>7. Why is Moisturizer Important for All Skin Types?</h2>
        <p class='section-content'>Moisturizers help maintain skin hydration and restore the skin's natural protective barrier. Even oily skin needs moisturizers.</p>
        <p class='section-content'><strong>Benefits of moisturizers:</strong></p>
        <ul class='section-content'>
            <li>Locks in moisture in the skin.</li>
            <li>Prevents flaking of dry skin.</li>
            <li>Helps minimize the appearance of fine lines and wrinkles.</li>
        </ul>
        <p class='section-content'>Use a lightweight moisturizer for oily skin and a richer one for dry skin.</p>
    </div>
    """, unsafe_allow_html=True)

    # Article 8: Tips for Skincare in the Summer
    st.markdown("""
    <div class='section'>
        <h2>8. Tips for Taking Care of Your Skin in Summer</h2>
        <p class='section-content'>Summer increases the risk of sunburn, dehydration, and acne. Proper skincare is essential during this season.</p>
        <p class='section-content'><strong>Summer skincare tips:</strong></p>
        <ul class='section-content'>
            <li>Always use sunscreen with high SPF every day.</li>
            <li>Wear protective clothing such as hats and sunglasses.</li>
            <li>Avoid direct sun exposure between 10 AM and 4 PM.</li>
            <li>Opt for lightweight and oil-free skincare products.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Article 9: Why is Getting Enough Sleep Important for Skin Health?
    st.markdown("""
    <div class='section'>
        <h2>9. Why is Getting Enough Sleep Important for Skin Health?</h2>
        <p class='section-content'>Adequate sleep helps the skin repair damaged cells and produce collagen.</p>
        <p class='section-content'><strong>Benefits of enough sleep:</strong></p>
        <ul class='section-content'>
            <li>Improves skin elasticity.</li>
            <li>Reduces puffiness and dark circles around the eyes.</li>
            <li>Enhances skin regeneration.</li>
        </ul>
        <p class='section-content'>Make sure to sleep 7–8 hours each night for healthy and glowing skin.</p>
    </div>
    """, unsafe_allow_html=True)





