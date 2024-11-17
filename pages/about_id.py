import streamlit as st
import os

def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_about_id():
    """Menampilkan halaman 'Tentang Aplikasi'."""
    # Tentukan path file CSS
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_about = os.path.join(parent_dir, "../static/images/about-id.png")
    image_path = os.path.join(parent_dir, "../static/images/logo.png")

    # Muat CSS
    load_css(css_path)

    # Konten halaman
    st.image(image_about, use_column_width=True)
    st.markdown("<div class='section-title'>Tentang Aplikasi</div>", unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Apa itu SkinPath?</h2>
                    <p class = 'section-content'><strong>SkinPath</strong> adalah aplikasi berbasis kecerdasan buatan yang bertujuan untuk membantu pengguna memahami tipe kulit mereka melalui analisis gambar wajah. Aplikasi ini dikembangkan dengan tujuan memberikan panduan perawatan kulit yang lebih personal dan tepat sasaran.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Fitur Utama Aplikasi</h2>
                    <p class = 'section-content'><strong>- Deteksi Tipe Kulit</strong> : Menggunakan teknologi deep learning dengan model ResNet50, aplikasi ini mampu mendeteksi tiga tipe kulit utama - kering, berminyak, dan normal - hanya dengan menganalisis foto wajah pengguna.</p>
                    <p class = 'section-content'><strong>- Saran Produk dan Bahan Perawatan Kulit</strong> : Setelah tipe kulit terdeteksi, aplikasi menyediakan rekomendasi produk serta bahan perawatan kulit yang sesuai berdasarkan tujuan perawatan tertentu.</p>
                    <p class = 'section-content'><strong>- Informasi Bahan Aktif</strong> : Untuk setiap bahan yang disarankan atau perlu dihindari, SkinPath memberikan penjelasan mengenai manfaat dan potensi efek samping bahan tersebut, membantu pengguna membuat keputusan yang lebih terinformasi.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Cara Kerja Aplikasi</h2>
                    <p class = 'section-content'><strong>1. Pilih Metode Input</strong> : Pengguna dapat memilih untuk mengambil gambar langsung melalui kamera atau mengunggah foto dari perangkat mereka.</p>
                    <p class = 'section-content'><strong>2. Deteksi Tipe Kulit</strong> : Gambar yang diunggah kemudian diproses melalui model ResNet50 yang telah dilatih khusus untuk mengidentifikasi tipe kulit.</p>
                    <p class = 'section-content'><strong>3. Rekomendasi Perawatan</strong> : Berdasarkan hasil analisis tipe kulit dan tujuan perawatan kulit yang diinginkan, aplikasi menyediakan rekomendasi bahan yang sebaiknya digunakan atau dihindari, serta panduan rutinitas perawatan kulit yang sesuai.</p>
                    <p class = 'section-content'><strong>4. Penjelasan Bahan</strong> : Pengguna dapat melihat informasi detail mengenai setiap bahan yang disarankan, yang meliputi manfaat, potensi efek samping, dan kecocokannya untuk berbagai tipe kulit.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Teknologi di Balik SkinPath</h2>
                    <p class = 'section-content'><strong>- Model Deep Learning ResNet50</strong> : Model yang telah disesuaikan untuk mendeteksi tipe kulit berdasarkan gambar wajah.</p>
                    <p class = 'section-content'><strong>- PyTorch Framework</strong> : Aplikasi menggunakan PyTorch untuk memuat dan menjalankan model deep learning.</p>
                    <p class = 'section-content'><strong>- Streamlit</strong> : SkinPath dibangun menggunakan Streamlit, framework Python yang memungkinkan pembuatan antarmuka pengguna interaktif dengan cepat dan mudah.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Disclaimer</h2>
                    <p class = 'section-content'>Informasi yang diberikan oleh SkinPath adalah panduan umum berdasarkan tipe kulit. Namun, kondisi kulit setiap individu bisa berbeda-beda, dan hasil analisis aplikasi mungkin tidak memperhitungkan faktor khusus seperti sensitivitas atau alergi tertentu. Untuk hasil yang lebih akurat, selalu konsultasikan dengan dermatologis atau profesional kesehatan sebelum melakukan perubahan signifikan pada rutinitas perawatan kulit Anda.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("""
                <div class='section'>
                    <h2>Catatan</h2>
                    <p class = 'section-content'>Aplikasi SkinPath dikembangkan sebagai proyek akhir Praktik Aplikasi Web yang berkaitan dengan penggunaan AI untuk perawatan kulit. Harapannya adalah bahwa aplikasi ini dapat menjadi alat yang berguna dalam membantu pengguna memahami dan merawat kulit mereka dengan lebih baik.</p>
                </div>
                """, unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Pengembang</div>", unsafe_allow_html=True)
    st.markdown(f"""
                <div class='section'>
                    <img src="{image_path}" class="circular-image">
                    <p class = 'section-content-pengembang'>Rheisan Firnandatama Rizky Satria</p>
                    <p class = 'section-content-pengembang'>22537141021</p>
                </div>
                """, unsafe_allow_html=True)

