import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet18
from PIL import Image
import io
import os

# Fungsi utama untuk aplikasi
def show_dashboard_id():
    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_landing = os.path.join(parent_dir, "../static/images/logo.png")
    image_dashboard = os.path.join(parent_dir, "../static/images/dashboard-id.png")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)

    def load_model():
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = resnet18(pretrained=False)
        model.fc = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(model.fc.in_features, 3)  
        )
        model.load_state_dict(torch.load("./models/model2.pth", map_location=device))
        model = model.to(device)
        model.eval()
        return model, device

    model, device = load_model()
    
    # Fungsi untuk preprocessing gambar
    def preprocess_image(image):
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        image = Image.open(io.BytesIO(image)).convert("RGB")
        return transform(image).unsqueeze(0)

    # Fungsi untuk memprediksi tipe kulit
    def predict_skin_type(image):
        try:
            inputs = preprocess_image(image).to(device)
            with torch.no_grad():
                outputs = model(inputs)
                _, predicted = torch.max(outputs, 1)
            return predicted.item()
        except Exception as e:
            st.error(f"Error dalam prediksi tipe kulit: {e}")
            return None
        
    # Penjelasan untuk setiap bahan
    def ingredient_explanation(ingredient):
        explanations = {
            "Alcohol": "Dapat mengeringkan kulit dan menghilangkan minyak alami kulit, yang dapat memperburuk kondisi kulit kering.",
            "Fragrance": "Dapat menyebabkan iritasi, terutama bagi kulit sensitif atau kering.",
            "Benzoyl Peroxide": "Efektif untuk mengobati jerawat tetapi bisa mengeringkan kulit, terutama bagi mereka dengan kulit kering atau sensitif.",
            "Mineral Oil": "Dapat menyumbat pori-pori, sehingga tidak cocok untuk kulit berminyak atau yang rentan berjerawat.",
            "Lanolin": "Merupakan emolien yang dapat menjebak minyak, sehingga kurang cocok untuk kulit berminyak.",
            "Petrolatum": "Meskipun mengunci kelembapan, dapat terlalu berat untuk kulit berminyak dan mungkin menyumbat pori-pori.",
            "Hyaluronic Acid": "Humektan yang membantu kulit mempertahankan kelembapan, ideal untuk kulit kering.",
            "Ceramides": "Membantu memperbaiki penghalang kulit, mempertahankan kelembapan, dan mencegah kekeringan.",
            "Squalane": "Minyak ringan yang melembabkan kulit tanpa membuatnya berminyak, cocok untuk kulit kering dan normal.",
            "Salicylic Acid": "Asam beta-hidroksi (BHA) yang mengelupas dan membersihkan pori-pori, ideal untuk kulit berminyak atau rentan jerawat.",
            "Niacinamide": "Bahan anti-inflamasi yang mengatur produksi minyak dan memperbaiki fungsi penghalang kulit.",
            "Clay": "Menyerap minyak berlebih dari kulit, sangat cocok untuk kulit berminyak.",
            "Glycerin": "Bahan pelembab yang menarik kelembapan ke dalam kulit, cocok untuk semua jenis kulit.",
            "Centella Asiatica": "Menenangkan iritasi dan membantu memperbaiki penghalang kulit, bermanfaat untuk kulit sensitif atau kering.",
            "Aloe Vera": "Memiliki sifat menenangkan dan melembabkan, cocok untuk kulit normal dan sensitif.",
            "Retinol": "Turunan vitamin A yang mendorong pergantian sel dan membantu mengurangi tanda-tanda penuaan serta jerawat.",
            "Vitamin C": "Antioksidan yang mencerahkan kulit dan membantu mengurangi hiperpigmentasi.",
            "Tea Tree Oil": "Antiseptik alami yang membantu mengobati jerawat dan menenangkan peradangan.",
            "Peptides": "Asam amino yang membantu membentuk protein di kulit, mendorong kekencangan, dan mengurangi kerutan.",
            "Zinc": "Mineral yang membantu mengatur produksi minyak dan dapat menenangkan kulit berjerawat.",
            "Lactic Acid": "Asam alfa hidroksi (AHA) yang secara lembut mengelupas dan melembabkan kulit, ideal untuk kulit kering.",
            "Argan Oil": "Minyak kaya asam lemak dan vitamin E, sangat baik untuk melembabkan kulit kering.",
            "Witch Hazel": "Astringent alami yang dapat membantu mengurangi peradangan dan mengencangkan pori-pori, cocok untuk kulit berminyak.",
            "Cucumber Extract": "Dikenal karena sifat menenangkan dan melembabkan, sempurna untuk kulit sensitif.",
            "Willow Bark": "Sumber alami asam salisilat yang membantu mengatasi jerawat dan mengelupas kulit.",
            "Harsh Sulfates": "Bahan pembersih yang bisa terlalu kuat, terutama bagi kulit sensitif atau kering, dan dapat menyebabkan iritasi atau kekeringan.",
            "Panthenol": "Dikenal juga sebagai provitamin B5, bahan ini membantu menenangkan, melembabkan, dan memperbaiki penghalang kulit.",
            "Cholesterol": "Bahan pelembab yang membantu memperbaiki penghalang kulit, menjaga kelembapan dan elastisitas kulit.",
            "Azelaic Acid": "Membantu mengurangi kemerahan dan mengobati jerawat, serta dapat mencerahkan hiperpigmentasi.",
            "Licorice Root": "Ekstrak akar manis yang memiliki sifat pencerah alami dan membantu mengurangi bintik hitam.",
            "Alpha Arbutin": "Bahan yang membantu mengurangi produksi melanin dan cocok untuk tujuan pencerahan kulit.",
            "Kojic Acid": "Bahan alami yang membantu mencerahkan kulit dan mengurangi hiperpigmentasi.",
        }
        return explanations.get(ingredient, "Tidak ada penjelasan yang tersedia.")

    # Fungsi untuk menyarankan bahan kimia
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
            "Perbaikan Penghalang Kulit": {0: ["Ceramides"], 1: ["Niacinamide"], 2: ["Panthenol"]},
            "Perawatan Jerawat": {0: ["Azelaic Acid"], 1: ["Benzoyl Peroxide"], 2: ["Tea Tree Oil"]},
            "Pemutihan Kulit": {0: ["Vitamin C"], 1: ["Alpha Arbutin"], 2: ["Kojic Acid"]}
        }
        return chemicals_to_avoid[skin_type], chemicals_to_use[skin_type], goal_suggestions[goal][skin_type]

    # Rutinitas perawatan kulit
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

    # Fungsi untuk memberikan deskripsi tipe kulit
    def get_skin_type_description(skin_type):
        descriptions = {
            0: "Kulit kering cenderung terasa kencang, kasar, dan mungkin terlihat kusam. Perawatan yang tepat dapat membantu menjaga kelembapan dan elastisitas kulit.",
            1: "Kulit berminyak sering kali tampak mengkilap dan rentan terhadap jerawat. Perawatan yang tepat dapat membantu mengontrol produksi minyak dan menjaga kebersihan pori-pori.",
            2: "Kulit normal memiliki keseimbangan antara kelembapan dan minyak. Perawatan yang tepat dapat membantu mempertahankan kondisi kulit yang sehat dan seimbang."
        }
        return descriptions.get(skin_type, "Deskripsi tidak tersedia.")

    # Initialize
    if 'landing_done' not in st.session_state:
        st.session_state['landing_done'] = False
    if 'image_confirmed' not in st.session_state:
        st.session_state['image_confirmed'] = False
    if 'show_about' not in st.session_state:
        st.session_state['show_about'] = False

    # Landing Page
    if not st.session_state['landing_done']:
        st.markdown("<div class='section-title'>Selamat Datang di SkinPath 👩‍⚕️</div>", unsafe_allow_html=True)
        st.image(image_landing, use_column_width=True)
        st.markdown("""
            ### Fitur Utama:
            - 🧴 **Deteksi Tipe Kulit**: Unggah foto atau ambil gambar langsung untuk menganalisis tipe kulit Anda. Aplikasi akan mengidentifikasi apakah kulit Anda kering, berminyak, atau normal.
            - 🔍 **Saran Produk Perawatan Kulit**: Setelah tipe kulit terdeteksi, aplikasi memberikan saran produk yang sesuai dan informasi tentang bahan-bahan yang sebaiknya dihindari atau digunakan, berdasarkan tujuan perawatan kulit yang dipilih pengguna.
            - 🧪 **Penjelasan Bahan**: Untuk setiap bahan yang disebutkan dalam rekomendasi, aplikasi menyediakan penjelasan rinci mengenai manfaat dan potensi efek sampingnya.

            ### Cara Penggunaan:
            1. **Pilih Metode Input**: Di panel samping, pilih apakah Anda ingin mengambil gambar langsung dengan kamera atau mengunggah foto dari perangkat.
            2. **Unggah atau Ambil Foto**: Pastikan wajah terlihat jelas tanpa bayangan atau gangguan pencahayaan.
            3. **Konfirmasi Foto**: Setelah mengunggah atau mengambil foto, klik **Confirm Image** untuk melanjutkan ke analisis tipe kulit.
            4. **Lihat Rekomendasi**: Setelah analisis, aplikasi akan menampilkan tipe kulit dan memberikan rekomendasi produk sesuai tujuan perawatan yang Anda pilih.
            5. **Mulai Ulang**: Jika ingin mengulangi analisis, tekan tombol **Restart Analysis** di bagian bawah halaman.
            
            ### Disclaimer
            Informasi yang diberikan di sini hanya sebagai referensi. Harap dicatat bahwa terdapat variabel penentu lain, seperti sensitivitas kulit, yang mungkin tidak didukung oleh aplikasi ini. Pastikan untuk berkonsultasi dengan profesional kesehatan atau dermatologis sebelum mengambil keputusan terkait perawatan kulit.
            
            > **Tip**: Untuk hasil terbaik, gunakan foto dengan pencahayaan alami dan wajah bersih tanpa riasan berlebih.
            """)
        
        if st.button("Lanjutkan ke Analisis"):
            st.session_state['landing_done'] = True
            st.rerun()

    elif st.session_state['landing_done']:
            st.image(image_dashboard, use_column_width=True)
            st.markdown("<div class='title'>Aplikasi SkinPath 👩‍⚕️</div>", unsafe_allow_html=True)
            st.markdown("<div class='sub-header'>Metode Input</div>", unsafe_allow_html=True)
            input_option = st.selectbox("Pilih Masukan Gambar:", ("📸Ambil Gambar", "📄Unggah Gambar"))
            # Menampilkan instruksi kamera untuk panduan pengguna
            if input_option == "📸Ambil Gambar":
                st.info("Pastikan wajah Anda terlihat jelas tanpa bayangan yang menghalangi, dan pencahayaan yang cukup agar hasil lebih maksimal.")

            image = st.camera_input("Mengambil foto") if input_option == "📸Ambil Gambar" else st.file_uploader("Unggah Gambar", type=["jpg", "jpeg"])

            if image and not st.session_state['image_confirmed']:
                st.markdown("### Pratinjau Gambar:")
                st.image(image, caption="Gambar Anda", use_column_width=True)
                if st.button("Konfirmasi Gambar"):
                    st.session_state['image_confirmed'] = True
                    img_bytes = image.read() if hasattr(image, 'read') else image.getvalue()
                    skin_type = predict_skin_type(img_bytes)
                    st.session_state['skin_type'] = skin_type
                    st.rerun()

            elif st.session_state['image_confirmed']:
                skin_types = ["Kering", "Berminyak", "Normal"]
                st.markdown(f"""
                    <div class="result-box">
                        <strong>Tipe Kulit Terdeteksi:</strong> {skin_types[st.session_state['skin_type']]}
                    </div>
                """, unsafe_allow_html=True)
                
                skin_type_description = get_skin_type_description(st.session_state['skin_type'])
                st.markdown(f"""
                    <div class="section skin-type-description">
                        <p>{skin_type_description}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                routine = skincare_routine(st.session_state['skin_type'])

                st.write("")
                st.markdown("<div class='sub-header'>Saran Rutinitas Perawatan Kulit</div>", unsafe_allow_html=True)
                morning, evening = st.columns(2)
                
                with morning:
                    steps_html = """
                    <div class='section'>
                        <h3>🌞 Rutinitas Pagi</h3>
                    """
                    
                    for step in routine["Morning"]:
                        steps_html += f"""
                        🔹 {step}
                        """

                    steps_html += """
                    </div>
                    """
                    
                    st.markdown(steps_html, unsafe_allow_html=True)

                with evening:
                    steps_html = """
                    <div class='section'>
                        <h3>🌜 Rutinitas Malam</h3>
                    """
                    
                    for step in routine["Evening"]:
                        steps_html += f"""
                        🔹 {step}
                        """

                    steps_html += """
                    </div>
                    """
                    
                    st.markdown(steps_html, unsafe_allow_html=True)

                st.write("")

                st.markdown("<div class='sub-header'>Tentukan Tujuan Perawatan Kulit</div>", unsafe_allow_html=True)
                
                goal = st.selectbox(
                    "Pilih tujuan perawatan kulit Anda:",
                    ["Perbaikan Penghalang Kulit", "Perawatan Jerawat", "Pemutihan Kulit"],
                    help="Pilih tujuan perawatan kulit untuk mendapatkan rekomendasi yang sesuai."
                )

                avoid, recommend, additional = suggest_chemicals(st.session_state['skin_type'], goal)

                recommendation, avoidance, addition = st.columns(3)
                with recommendation:
                    st.markdown(f"""
                        <div class='column-header-chemicals-recommend'>
                            <h3>Bahan yang Disarankan</h3>
                            <p>
                                {", ".join(recommend)}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                with avoidance:
                    st.markdown(f"""
                        <div class='column-header-chemicals-avoid'>
                            <h3>Bahan yang Dihindari</h3>
                            <p>
                                {", ".join(avoid)}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

                with addition: 
                    st.markdown(f"""
                        <div class='column-header-chemicals-addition'>
                            <h3>Bahan untuk Tujuan</h3>
                            <p>
                                {", ".join(additional)}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

                unique_ingredients = list(set(avoid + recommend + additional))
                
                st.write("")

                st.markdown("<div class='sub-header'>Penjelasan Bahan 📖</div>", unsafe_allow_html=True)
                for ingredient in unique_ingredients:
                    with st.expander(f"{ingredient} 📜"):
                        st.write(ingredient_explanation(ingredient))

                if st.button("Mulai Ulang Analisis"):
                    st.session_state['image_confirmed'] = False
                    st.session_state['skin_type'] = None
                    st.session_state['image'] = None
                    st.rerun()