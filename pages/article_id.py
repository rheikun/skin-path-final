import streamlit as st
import os
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_article_id():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../static/style/style.css")
    image_article = os.path.join(parent_dir, "../static/images/artikel-id.png")

    # Muat CSS
    load_css(css_path)
    # Menampilkan artikel terkait perawatan kulit
    st.image(image_article, use_column_width=True)
    st.markdown("<div class='section-title'>Artikel Terkait Perawatan Kulit</div>", unsafe_allow_html=True)
    # Artikel 1: Manfaat Sunscreen untuk Semua Jenis Kulit
    st.markdown("""
    <div class='section'>
        <h2>1. Manfaat Sunscreen untuk Semua Jenis Kulit</h2>
        <p class='section-content'>Sunscreen adalah salah satu produk skincare yang tidak boleh dilewatkan oleh siapa pun, terlepas dari jenis kulit atau cuaca. Sunscreen membantu melindungi kulit dari kerusakan akibat sinar UV, yang dapat menyebabkan kanker kulit, penuaan dini, dan hiperpigmentasi.</p>
        <p class='section-content'><strong>Manfaat utama sunscreen:</strong></p>
        <ul class='section-content'>
            <li>Melindungi kulit dari sinar UV A dan UV B.</li>
            <li>Mencegah pembentukan flek hitam akibat paparan sinar matahari.</li>
            <li>Mengurangi risiko kanker kulit.</li>
            <li>Mempertahankan elastisitas kulit dengan mencegah kerusakan kolagen.</li>
        </ul>
        <p class='section-content'>Untuk hasil terbaik, gunakan sunscreen dengan SPF minimal 30 setiap hari, bahkan ketika berada di dalam ruangan.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 2: Perawatan Kulit Sehari-hari untuk Kulit Berminyak
    st.markdown("""
    <div class='section'>
        <h2>2. Perawatan Kulit Sehari-hari untuk Kulit Berminyak</h2>
        <p class='section-content'>Kulit berminyak sering kali mengalami masalah seperti jerawat, pori-pori besar, dan kilau berlebih. Namun, dengan rutinitas yang tepat, Anda dapat mengontrol produksi minyak dan menjaga kulit tetap sehat.</p>
        <p class='section-content'><strong>Tips perawatan harian:</strong></p>
        <ul class='section-content'>
            <li>Bersihkan wajah dua kali sehari dengan pembersih yang mengandung asam salisilat untuk mengurangi minyak berlebih.</li>
            <li>Gunakan toner yang membantu mengecilkan pori-pori.</li>
            <li>Pilih pelembap ringan yang bebas minyak (non-komedogenik).</li>
            <li>Hindari produk berbahan berat seperti krim yang terlalu berminyak.</li>
            <li>Gunakan masker tanah liat (clay mask) seminggu sekali untuk mengurangi produksi minyak.</li>
        </ul>
        <p class='section-content'>Penting untuk tidak terlalu sering mencuci wajah, karena ini dapat memicu kulit memproduksi lebih banyak minyak sebagai kompensasi.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 3: Tips Memilih Produk untuk Kulit Sensitif
    st.markdown("""
    <div class='section'>
        <h2>3. Tips Memilih Produk untuk Kulit Sensitif</h2>
        <p class='section-content'>Kulit sensitif memerlukan perhatian ekstra karena mudah teriritasi. Salah memilih produk dapat menyebabkan ruam, kemerahan, atau rasa gatal.</p>
        <p class='section-content'><strong>Panduan memilih produk:</strong></p>
        <ul class='section-content'>
            <li>Pilih produk yang diberi label "hypoallergenic" atau "sensitive skin".</li>
            <li>Hindari bahan-bahan seperti pewangi, alkohol, dan paraben.</li>
            <li>Gunakan produk dengan bahan alami seperti lidah buaya, chamomile, atau oat.</li>
            <li>Selalu lakukan patch test sebelum mencoba produk baru.</li>
            <li>Pilih sunscreen dengan mineral-based (seperti zinc oxide atau titanium dioxide) karena lebih lembut untuk kulit sensitif.</li>
        </ul>
        <p class='section-content'>Selain itu, jaga kelembapan kulit dengan menggunakan pelembap bebas pewangi secara rutin, terutama setelah mencuci muka.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 4: Makanan yang Baik untuk Kulit Anda
    st.markdown("""
    <div class='section'>
        <h2>4. Makanan yang Baik untuk Kulit Anda</h2>
        <p class='section-content'>Apa yang Anda konsumsi berdampak besar pada kesehatan dan penampilan kulit Anda. Nutrisi yang tepat dapat memperbaiki tekstur kulit, mencegah penuaan dini, dan melawan jerawat.</p>
        <p class='section-content'><strong>Makanan terbaik untuk kulit:</strong></p>
        <ul class='section-content'>
            <li><strong>Buah-buahan dan sayuran berwarna cerah:</strong> Wortel, jeruk, dan bayam kaya akan vitamin C dan A, yang membantu regenerasi sel kulit.</li>
            <li><strong>Ikan berlemak:</strong> Seperti salmon dan tuna, mengandung omega-3 yang membantu menjaga elastisitas kulit.</li>
            <li><strong>Kacang-kacangan:</strong> Kaya akan vitamin E, yang melindungi kulit dari kerusakan akibat radikal bebas.</li>
            <li><strong>Air putih:</strong> Menjaga kulit tetap terhidrasi dari dalam.</li>
        </ul>
        <p class='section-content'>Hindari makanan berminyak, gula berlebih, dan makanan olahan untuk mencegah masalah kulit seperti jerawat.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 5: Pentingnya Menjaga Kebersihan Kulit Wajah
    st.markdown("""
    <div class='section'>
        <h2>5. Pentingnya Menjaga Kebersihan Kulit Wajah</h2>
        <p class='section-content'>Kebersihan wajah adalah dasar dari rutinitas perawatan kulit yang baik. Membersihkan wajah dengan benar membantu menghilangkan kotoran, minyak, dan makeup yang menumpuk sepanjang hari.</p>
        <p class='section-content'><strong>Tips menjaga kebersihan kulit wajah:</strong></p>
        <ul class='section-content'>
            <li>Cuci muka dua kali sehari, pagi dan malam.</li>
            <li>Gunakan air hangat (bukan air panas) untuk menghindari iritasi.</li>
            <li>Pilih pembersih sesuai jenis kulit.</li>
            <li>Hindari menggosok wajah terlalu keras.</li>
            <li>Selalu bersihkan makeup sebelum tidur.</li>
        </ul>
        <p class='section-content'>Dengan kebiasaan yang konsisten, Anda dapat mencegah jerawat dan menjaga kulit tetap segar.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 6: Apa Itu Double Cleansing dan Manfaatnya?
    st.markdown("""
    <div class='section'>
        <h2>6. Apa Itu Double Cleansing dan Manfaatnya?</h2>
        <p class='section-content'>Double cleansing adalah teknik membersihkan wajah dalam dua tahap: membersihkan kotoran berbasis minyak dengan pembersih berbasis minyak, lalu melanjutkan dengan pembersih berbasis air.</p>
        <p class='section-content'><strong>Manfaat double cleansing:</strong></p>
        <ul class='section-content'>
            <li>Membersihkan sisa makeup dan sunscreen secara menyeluruh.</li>
            <li>Mengangkat kotoran yang tidak terhapus oleh pembersih biasa.</li>
            <li>Membantu mencegah jerawat akibat pori-pori tersumbat.</li>
        </ul>
        <p class='section-content'>Teknik ini sangat dianjurkan bagi mereka yang sering memakai makeup atau tinggal di kota dengan tingkat polusi tinggi.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 7: Mengapa Pelembap Penting untuk Semua Jenis Kulit?
    st.markdown("""
    <div class='section'>
        <h2>7. Mengapa Pelembap Penting untuk Semua Jenis Kulit?</h2>
        <p class='section-content'>Pelembap membantu menjaga hidrasi kulit dan memperbaiki lapisan pelindung alami kulit. Bahkan kulit berminyak membutuhkan pelembap.</p>
        <p class='section-content'><strong>Manfaat pelembap:</strong></p>
        <ul class='section-content'>
            <li>Mengunci kelembapan di kulit.</li>
            <li>Mencegah pengelupasan kulit kering.</li>
            <li>Membantu menyamarkan garis halus dan kerutan.</li>
        </ul>
        <p class='section-content'>Gunakan pelembap berbahan ringan untuk kulit berminyak dan pelembap yang lebih kaya untuk kulit kering.</p>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 8: Tips Merawat Kulit di Musim Panas
    st.markdown("""
    <div class='section'>
        <h2>8. Tips Merawat Kulit di Musim Panas</h2>
        <p class='section-content'>Musim panas meningkatkan risiko kulit terbakar, dehidrasi, dan jerawat. Perawatan kulit yang tepat sangat penting.</p>
        <p class='section-content'><strong>Tips musim panas:</strong></p>
        <ul class='section-content'>
            <li>Gunakan sunscreen SPF tinggi setiap hari.</li>
            <li>Gunakan pakaian pelindung seperti topi dan kacamata.</li>
            <li>Hindari paparan sinar matahari langsung antara pukul 10 pagi hingga 4 sore.</li>
            <li>Pilih skincare yang ringan dan bebas minyak.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Artikel 9: Mengapa Tidur yang Cukup Penting untuk Kesehatan Kulit?
    st.markdown("""
    <div class='section'>
        <h2>9. Mengapa Tidur yang Cukup Penting untuk Kesehatan Kulit?</h2>
        <p class='section-content'>Tidur cukup membantu kulit memperbaiki sel-sel yang rusak dan memproduksi kolagen.</p>
        <p class='section-content'><strong>Manfaat tidur cukup:</strong></p>
        <ul class='section-content'>
            <li>Meningkatkan elastisitas kulit.</li>
            <li>Mengurangi kantung mata dan lingkaran hitam.</li>
            <li>Meningkatkan regenerasi kulit.</li>
        </ul>
        <p class='section-content'>Pastikan tidur 7-8 jam setiap malam untuk mendapatkan kulit yang sehat dan bercahaya.</p>
    </div>
    """, unsafe_allow_html=True)
