import streamlit as st
import base64
import os

# =====================================================
# 1. SETUP NAMA FILE GAMBAR LOKAL
# (File logo & gambar.jpg di folder dashboard Anda)
# =====================================================

FILE_LOGO_BKKBN = "logo_bkkbnbaru.png"
FILE_GAMBAR_BABEL = "gambar1.jpg"

# =====================================================
# PAGE CONFIG & HELPER FUNGSI GAMBAR
# =====================================================

st.set_page_config(
    page_title="Dashboard PERKIN",
    page_icon="📊",
    layout="wide"
)

def load_local_image_b64(image_path):
    """Membaca file gambar lokal dan mengubahnya menjadi Base64"""
    if os.path.exists(image_path):
        ext = image_path.split('.')[-1].lower()
        mime_type = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png" if ext == "png" else "image/svg+xml"
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            return f"data:{mime_type};base64,{encoded}"
    return None

logo_b64 = load_local_image_b64(FILE_LOGO_BKKBN)
babel_img_b64 = load_local_image_b64(FILE_GAMBAR_BABEL)

# HTML untuk Logo Top Navbar
if logo_b64:
    logo_html = f'<img src="{logo_b64}" class="brand-logo-img" alt="Logo BKKBN" />'
else:
    logo_html = f'<div style="font-size:38px;">🏛️</div>'

# URL Fallback jika gambar.jpg belum tersimpan
FALLBACK_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Mercusuar_Pulau_Lengkuas.jpg/800px-Mercusuar_Pulau_Lengkuas.jpg"
bg_image_src = babel_img_b64 if babel_img_b64 else FALLBACK_URL

# =====================================================
# STYLING (CSS DESAIN 100% PERSIS SEPERTI GAMBAR ANDA)
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Background Soft Ambient Light Blue */
.stApp {
    background-color: #EEF4FB;
    background-image: 
        radial-gradient(circle at 5% 5%, rgba(147, 197, 253, 0.35) 0%, transparent 35%),
        radial-gradient(circle at 95% 15%, rgba(59, 130, 246, 0.2) 0%, transparent 40%),
        radial-gradient(circle at 10% 60%, rgba(224, 242, 254, 0.5) 0%, transparent 40%),
        radial-gradient(circle at 90% 85%, rgba(191, 219, 254, 0.4) 0%, transparent 45%);
    background-attachment: fixed;
}

/* Hide default Streamlit components */
#MainMenu, footer, header {
    visibility: hidden;
    height: 0;
}

[data-testid="stHeader"] {
    display: none;
}

.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1240px;
}

/* Navbar Logo & Text */
.brand-container {
    display: flex;
    align-items: center;
    gap: 14px;
}

.brand-logo-img {
    height: 52px;
    width: auto;
    object-fit: contain;
}

.brand-text-title {
    font-weight: 800;
    font-size: 15px;
    color: #0F172A;
    line-height: 1.25;
}

.brand-text-sub {
    font-weight: 600;
    font-size: 13px;
    color: #475569;
    margin-top: 2px;
}

/* Tombol Kembali ke SIPELIKES (Kanan Atas) */
div.stLinkButton > a[href*="sipelikes"] {
    background: linear-gradient(135deg, #1565C0, #0D47A1) !important;
    color: white !important;
    border-radius: 50px !important;
    padding: 11px 26px !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    box-shadow: 0 4px 14px rgba(21, 101, 192, 0.3) !important;
    border: none !important;
    transition: all 0.3s ease !important;
}

div.stLinkButton > a[href*="sipelikes"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(21, 101, 192, 0.45) !important;
}

/* Hero Banner Royal Blue */
.hero-banner {
    position: relative;
    background: linear-gradient(135deg, #0B4EA2 0%, #1565C0 55%, #1D60DB 100%);
    border-radius: 28px;
    padding: 44px 50px;
    color: white;
    box-shadow: 0 20px 45px rgba(11, 78, 162, 0.25);
    overflow: hidden;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 240px;
}

/* Gambar Blend Menyatu di Sisi Kanan Banner (Seamless Blend) */
.hero-bg-blend-image {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 48%;
    height: 100%;
    object-fit: cover;
    object-position: right center;
    opacity: 0.65;
    mix-blend-mode: luminosity;
    -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1) 0%, rgba(0,0,0,0.7) 50%, rgba(0,0,0,0) 100%);
    mask-image: linear-gradient(to left, rgba(0,0,0,1) 0%, rgba(0,0,0,0.7) 50%, rgba(0,0,0,0) 100%);
    pointer-events: none;
    z-index: 1;
}

/* Siluet Peta Bangka Belitung di Tengah */
.hero-map-svg {
    position: absolute;
    right: 210px;
    top: 50%;
    transform: translateY(-50%);
    width: 320px;
    height: auto;
    opacity: 0.38;
    pointer-events: none;
    z-index: 2;
}

.hero-content {
    position: relative;
    z-index: 3;
    max-width: 580px;
}

.hero-subtitle-top {
    font-size: 22px;
    font-weight: 300;
    color: #E0E7FF;
    margin-bottom: 4px;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #FFFFFF;
    line-height: 1.1;
    display: inline-block;
}

/* Garis Kuning di Bawah Judul Dashboard PERKIN */
.hero-title-underline {
    width: 130px;
    height: 4px;
    background: #FFD700;
    border-radius: 4px;
    margin-top: 6px;
    margin-bottom: 16px;
}

.hero-desc {
    font-size: 17px;
    color: #DBEAFE;
    margin-bottom: 24px;
    line-height: 1.5;
    font-weight: 400;
}

/* Glass Badge Kependudukan BKKBN */
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.32);
    padding: 10px 22px;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    color: #FFFFFF;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
}

/* Kutipan Slogan Kanan Banner */
.hero-quote-box {
    position: absolute;
    right: 280px;
    top: 40px;
    z-index: 3;
    text-align: right;
    font-style: italic;
    font-size: 16px;
    color: rgba(255, 255, 255, 0.95);
    max-width: 240px;
    line-height: 1.45;
    font-weight: 500;
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

@media (max-width: 992px) {
    .hero-bg-blend-image { width: 100%; opacity: 0.3; }
    .hero-quote-box { position: relative; right: auto; top: auto; text-align: left; margin-top: 15px; }
}

/* Stat Cards */
.stat-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.03);
    transition: transform 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-3px);
}

.stat-icon-wrapper {
    width: 52px;
    height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    flex-shrink: 0;
}

.stat-icon-blue { background: #EFF6FF; color: #2563EB; }
.stat-icon-gold { background: #FEF9C3; color: #CA8A04; }
.stat-icon-purple { background: #F3E8FF; color: #9333EA; }
.stat-icon-teal { background: #CCFBF1; color: #0D9488; }

.stat-label { font-size: 13px; color: #64748B; font-weight: 500; margin-bottom: 2px; }
.stat-value { font-size: 22px; font-weight: 700; color: #0F172A; }

/* Section Header */
.section-header-box { text-align: center; margin-top: 38px; margin-bottom: 28px; }
.section-title { font-size: 32px; font-weight: 800; color: #0B4EA2; margin-bottom: 8px; }
.section-subtitle { font-size: 15px; color: #64748B; margin-bottom: 14px; }
.section-divider { width: 50px; height: 4px; background: #1976D2; border-radius: 10px; margin: 0 auto; }

/* Year Cards */
.year-card-box {
    border-radius: 20px;
    padding: 24px 20px 20px 20px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: all 0.3s ease;
    min-height: 260px;
    margin-bottom: -50px;
    z-index: 1;
}

.card-archive { background: #FFFFFF; border: 1px solid #E2E8F0; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05); }
.card-archive:hover { transform: translateY(-6px); border-color: #93C5FD; }

.card-unavailable { background: #FFF5F5; border: 1px solid #FEE2E2; }
.card-unavailable:hover { transform: translateY(-4px); }

.card-active-2026 {
    background: linear-gradient(145deg, #1D60DB 0%, #1557C0 100%);
    border: 1px solid #2563EB;
    box-shadow: 0 16px 35px rgba(29, 96, 219, 0.35);
    color: white;
}
.card-active-2026:hover { transform: translateY(-8px); }

.card-future { background: #FFFDF0; border: 1px solid #FEF08A; }
.card-future:hover { transform: translateY(-4px); }

.card-info {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.05);
    border-radius: 20px;
    padding: 24px 22px;
    height: 100%;
    min-height: 310px;
    text-align: left;
}

/* Badges */
.card-badge {
    position: absolute;
    top: 16px; right: 16px;
    padding: 5px 14px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: 700;
}

.badge-archive { background: #E0F2FE; color: #0284C7; }
.badge-unavailable { background: #FEE2E2; color: #DC2626; }
.badge-active { background: #FFFFFF; color: #1D60DB; }
.badge-future { background: #FEF08A; color: #B45309; }

.card-icon-circle {
    width: 64px; height: 64px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 28px; margin: 12px 0;
}

.icon-bg-blue { background: #EFF6FF; }
.icon-bg-red { background: #FEE2E2; }
.icon-bg-gold { background: rgba(255, 255, 255, 0.25); color: #FFD700; }
.icon-bg-yellow { background: #FEF9C3; }

.card-year-num { font-size: 32px; font-weight: 800; line-height: 1; margin-bottom: 4px; }
.card-year-num.text-dark { color: #0F172A; }
.card-year-num.text-white { color: #FFFFFF; }

.card-year-sub { font-size: 14px; font-weight: 600; margin-bottom: 8px; }
.card-year-sub.sub-dark { color: #475569; }
.card-year-sub.sub-white { color: rgba(255, 255, 255, 0.85); }

.card-year-desc { font-size: 13px; line-height: 1.4; max-width: 220px; }
.card-year-desc.desc-dark { color: #64748B; }
.card-year-desc.desc-white { color: rgba(255, 255, 255, 0.95); }

/* Buttons Overrides */
div.stButton > button,
div.stLinkButton > a {
    width: 100% !important;
    height: 46px !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    position: relative !important;
    z-index: 5 !important;
    margin-top: 18px !important;
    transition: all 0.25s ease !important;
}

div.stLinkButton > a {
    background: #1D60DB !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(29, 96, 219, 0.25) !important;
}

div.stLinkButton > a:hover {
    background: #1557C0 !important;
    transform: translateY(-2px) !important;
    color: white !important;
}

div.stButton > button {
    background: #FFFFFF !important;
    color: #475569 !important;
    border: 1.5px solid #CBD5E1 !important;
}

div.stButton > button:hover {
    background: #F8FAFC !important;
    color: #0F172A !important;
    transform: translateY(-2px) !important;
}

/* Target 2026 Button */
[data-testid="stHorizontalBlock"]:nth-of-type(3) [data-testid="stColumn"]:nth-of-type(2) div.stLinkButton > a {
    background: #FFFFFF !important;
    color: #1D60DB !important;
}

/* Target 2022 Button */
[data-testid="stHorizontalBlock"]:nth-of-type(2) [data-testid="stColumn"]:nth-of-type(1) div.stButton > button {
    background: #FFF5F5 !important;
    color: #DC2626 !important;
    border: 1px solid #FECACA !important;
}

/* Target 2027-2029 Buttons */
[data-testid="stHorizontalBlock"]:nth-of-type(3) [data-testid="stColumn"]:nth-of-type(3) div.stButton > button,
[data-testid="stHorizontalBlock"]:nth-of-type(4) [data-testid="stColumn"]:nth-of-type(1) div.stButton > button,
[data-testid="stHorizontalBlock"]:nth-of-type(4) [data-testid="stColumn"]:nth-of-type(2) div.stButton > button {
    background: #FFFDF0 !important;
    color: #B45309 !important;
    border: 1px solid #FDE68A !important;
}

/* Info Card List */
.info-card-header { font-size: 18px; font-weight: 800; color: #1E40AF; display: flex; align-items: center; gap: 8px; margin-bottom: 16px; }
.info-list { list-style: none; padding: 0; margin: 0; }
.info-item { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; color: #1E3A8A; margin-bottom: 12px; line-height: 1.4; font-weight: 500; }
.info-check { width: 20px; height: 20px; border-radius: 50%; background: #10B981; color: white; display: flex; align-items: center; justify-content: center; font-size: 11px; flex-shrink: 0; margin-top: 1px; }

/* Footer */
.footer-wrapper { position: relative; margin-top: 50px; }
.footer-container { position: relative; z-index: 2; padding: 24px 20px; background: linear-gradient(135deg, #0B4EA2, #1565C0); border-radius: 20px; color: white; text-align: center; }
.footer-title { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
.footer-subtitle { font-size: 13px; color: #DBEAFE; margin-bottom: 12px; }
.footer-copy { font-size: 13px; color: rgba(255, 255, 255, 0.75); border-top: 1px solid rgba(255, 255, 255, 0.18); padding-top: 12px; margin-top: 12px; }

.dots-pattern {
    position: absolute; bottom: -10px; right: -10px;
    width: 100px; height: 60px;
    background-image: radial-gradient(#2563EB 2px, transparent 2px);
    background-size: 12px 12px; opacity: 0.35; z-index: 1;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TOP NAVBAR
# =====================================================

c_nav1, c_nav2 = st.columns([8, 3])

with c_nav1:
    st.markdown(f"""<div class="brand-container">{logo_html}<div><div class="brand-text-title">Kementerian Kependudukan dan Pembangunan Keluarga/BKKBN</div><div class="brand-text-sub">Perwakilan BKKBN Provinsi Kep. Bangka Belitung</div></div></div>""", unsafe_allow_html=True)

with c_nav2:
    st.link_button(
        "🏠 Kembali ke SIPELIKES ➔",
        "https://ppid-kemendukbanggababel.my.canva.site/sipelikes/",
        use_container_width=True
    )

# =====================================================
# HERO BANNER (GAMBAR NYATU SEAMLESS DENGAN BACKGROUND)
# =====================================================

hero_html = f"""<div class="hero-banner">
<img src="{bg_image_src}" class="hero-bg-blend-image" alt="Background Babel Landmark" />

<svg class="hero-map-svg" viewBox="0 0 500 320" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M120 40 C160 20, 220 30, 260 70 C290 100, 310 160, 280 220 C250 270, 190 280, 140 240 C100 200, 90 130, 110 80 Z" fill="white" opacity="0.8"/>
<path d="M360 170 C410 150, 460 180, 470 220 C460 270, 410 280, 370 250 C340 220, 340 190, 360 170 Z" fill="white" opacity="0.75"/>
</svg>

<div class="hero-quote-box">
“Bersama Mewujudkan<br>Keluarga Berkualitas<br>untuk Indonesia Emas”
</div>

<div class="hero-content">
<div class="hero-subtitle-top">Selamat Datang di</div>
<div class="hero-title">Dashboard PERKIN</div>
<div class="hero-title-underline"></div>
<div class="hero-desc">
Realisasi Kinerja Program Bangga Kencana<br>
Provinsi Kepulauan Bangka Belitung
</div>
<div class="hero-badge">
🏛️ Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN
</div>
</div>
</div>"""

st.markdown(hero_html, unsafe_allow_html=True)

# =====================================================
# STAT SUMMARY CARDS
# =====================================================

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""<div class="stat-card"><div class="stat-icon-wrapper stat-icon-blue">📊</div><div><div class="stat-label">Dashboard Tersedia</div><div class="stat-value">4 Tahun</div></div></div>""", unsafe_allow_html=True)

with s2:
    st.markdown("""<div class="stat-card"><div class="stat-icon-wrapper stat-icon-gold">⭐</div><div><div class="stat-label">Tahun Aktif</div><div class="stat-value">2026</div></div></div>""", unsafe_allow_html=True)

with s3:
    st.markdown("""<div class="stat-card"><div class="stat-icon-wrapper stat-icon-purple">🗃️</div><div><div class="stat-label">Tahun Arsip</div><div class="stat-value">3 Tahun</div></div></div>""", unsafe_allow_html=True)

with s4:
    st.markdown("""<div class="stat-card"><div class="stat-icon-wrapper stat-icon-teal">📅</div><div><div class="stat-label">Tahun Mendatang</div><div class="stat-value">3 Tahun</div></div></div>""", unsafe_allow_html=True)

# =====================================================
# SECTION HEADER
# =====================================================

st.markdown("""<div class="section-header-box"><div class="section-title">Pilih Tahun Monitoring</div><div class="section-subtitle">Akses dashboard berdasarkan tahun pelaporan untuk melihat capaian indikator PERKIN</div><div class="section-divider"></div></div>""", unsafe_allow_html=True)

# =====================================================
# YEAR CARDS & INFO GRID DATA
# =====================================================

tahun_data = [
    {
        "tahun": "2022",
        "icon": "📁",
        "status": "Data Tidak Tersedia",
        "badge_class": "badge-unavailable",
        "card_class": "card-unavailable",
        "icon_bg": "icon-bg-red",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Data tahun 2022 belum tersedia pada sistem.",
        "url": "",
        "button_text": "🔒 Buka Dashboard ➔"
    },
    {
        "tahun": "2023",
        "icon": "📊",
        "status": "Arsip",
        "badge_class": "badge-archive",
        "card_class": "card-archive",
        "icon_bg": "icon-bg-blue",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Akses data arsip PERKIN tahun 2023.",
        "url": "https://dashboard-perkin-2023.streamlit.app/",
        "button_text": "👁 Buka Dashboard ➔"
    },
    {
        "tahun": "2024",
        "icon": "📈",
        "status": "Arsip",
        "badge_class": "badge-archive",
        "card_class": "card-archive",
        "icon_bg": "icon-bg-blue",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Akses data arsip PERKIN tahun 2024.",
        "url": "https://dashboard-perkin-2024.streamlit.app/",
        "button_text": "👁 Buka Dashboard ➔"
    },
    {
        "tahun": "2025",
        "icon": "📊",
        "status": "Arsip",
        "badge_class": "badge-archive",
        "card_class": "card-archive",
        "icon_bg": "icon-bg-blue",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Akses data arsip PERKIN tahun 2025.",
        "url": "https://dashboard-perkin-2025.streamlit.app/",
        "button_text": "👁 Buka Dashboard ➔"
    },
    {
        "tahun": "2026",
        "icon": "⭐",
        "status": "Aktif",
        "badge_class": "badge-active",
        "card_class": "card-active-2026",
        "icon_bg": "icon-bg-gold",
        "num_class": "text-white",
        "sub_class": "sub-white",
        "desc_class": "desc-white",
        "desc": "Dashboard tahun aktif untuk monitoring capaian indikator.",
        "url": "https://dashboard-perkin-2026new.streamlit.app/",
        "button_text": "👁 Buka Dashboard ➔"
    },
    {
        "tahun": "2027",
        "icon": "📅",
        "status": "Belum Tersedia",
        "badge_class": "badge-future",
        "card_class": "card-future",
        "icon_bg": "icon-bg-yellow",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Dashboard tahun 2027 belum tersedia.",
        "url": "",
        "button_text": "🔒 Buka Dashboard ➔"
    },
    {
        "tahun": "2028",
        "icon": "📅",
        "status": "Belum Tersedia",
        "badge_class": "badge-future",
        "card_class": "card-future",
        "icon_bg": "icon-bg-yellow",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Dashboard tahun 2028 belum tersedia.",
        "url": "",
        "button_text": "🔒 Buka Dashboard ➔"
    },
    {
        "tahun": "2029",
        "icon": "📅",
        "status": "Belum Tersedia",
        "badge_class": "badge-future",
        "card_class": "card-future",
        "icon_bg": "icon-bg-yellow",
        "num_class": "text-dark",
        "sub_class": "sub-dark",
        "desc_class": "desc-dark",
        "desc": "Dashboard tahun 2029 belum tersedia.",
        "url": "",
        "button_text": "🔒 Buka Dashboard ➔"
    }
]

# Render Grid Row 1 (2022, 2023, 2024)
r1_cols = st.columns(3)

for col, item in zip(r1_cols, tahun_data[0:3]):
    with col:
        st.markdown(f"""<div class="year-card-box {item['card_class']}"><div class="card-badge {item['badge_class']}">{item['status']}</div><div class="card-icon-circle {item['icon_bg']}">{item['icon']}</div><div class="card-year-num {item['num_class']}">{item['tahun']}</div><div class="card-year-sub {item['sub_class']}">Dashboard PERKIN</div><div class="card-year-desc {item['desc_class']}">{item['desc']}</div></div>""", unsafe_allow_html=True)
        
        if item["tahun"] == "2022":
            if st.button(item["button_text"], key="2022", use_container_width=True):
                st.warning("⚠️ Data Dashboard PERKIN Tahun 2022 belum tersedia.")
        else:
            st.link_button(
                item["button_text"],
                item["url"],
                use_container_width=True
            )

# Render Grid Row 2 (2025, 2026, 2027)
r2_cols = st.columns(3)

for col, item in zip(r2_cols, tahun_data[3:6]):
    with col:
        st.markdown(f"""<div class="year-card-box {item['card_class']}"><div class="card-badge {item['badge_class']}">{item['status']}</div><div class="card-icon-circle {item['icon_bg']}">{item['icon']}</div><div class="card-year-num {item['num_class']}">{item['tahun']}</div><div class="card-year-sub {item['sub_class']}">Dashboard PERKIN</div><div class="card-year-desc {item['desc_class']}">{item['desc']}</div></div>""", unsafe_allow_html=True)
        
        if item["tahun"] in ["2027", "2028", "2029"]:
            if st.button(item["button_text"], key=item["tahun"], use_container_width=True):
                st.info("📅 Data Dashboard tahun ini belum tersedia.")
        else:
            st.link_button(
                item["button_text"],
                item["url"],
                use_container_width=True
            )

# Render Grid Row 3 (2028, 2029, Info Box)
r3_cols = st.columns(3)

# 2028
with r3_cols[0]:
    item = tahun_data[6]
    st.markdown(f"""<div class="year-card-box {item['card_class']}"><div class="card-badge {item['badge_class']}">{item['status']}</div><div class="card-icon-circle {item['icon_bg']}">{item['icon']}</div><div class="card-year-num {item['num_class']}">{item['tahun']}</div><div class="card-year-sub {item['sub_class']}">Dashboard PERKIN</div><div class="card-year-desc {item['desc_class']}">{item['desc']}</div></div>""", unsafe_allow_html=True)
    if st.button(item["button_text"], key=item["tahun"], use_container_width=True):
        st.info("📅 Data Dashboard tahun ini belum tersedia.")

# 2029
with r3_cols[1]:
    item = tahun_data[7]
    st.markdown(f"""<div class="year-card-box {item['card_class']}"><div class="card-badge {item['badge_class']}">{item['status']}</div><div class="card-icon-circle {item['icon_bg']}">{item['icon']}</div><div class="card-year-num {item['num_class']}">{item['tahun']}</div><div class="card-year-sub {item['sub_class']}">Dashboard PERKIN</div><div class="card-year-desc {item['desc_class']}">{item['desc']}</div></div>""", unsafe_allow_html=True)
    if st.button(item["button_text"], key=item["tahun"], use_container_width=True):
        st.info("📅 Data Dashboard tahun ini belum tersedia.")

# Card 9: Informasi Box
with r3_cols[2]:
    st.markdown("""<div class="card-info"><div class="info-card-header">💡 Informasi</div><ul class="info-list"><li class="info-item"><div class="info-check">✓</div><div>Data realisasi berdasarkan laporan kabupaten/kota se-Provinsi Babel</div></li><li class="info-item"><div class="info-check">✓</div><div>Monitoring capaian indikator setiap bulan</div></li><li class="info-item"><div class="info-check">✓</div><div>Terintegrasi dengan sistem SIPELIKES</div></li><li class="info-item"><div class="info-check">✓</div><div>Mendukung pengambilan keputusan berbasis data</div></li></ul></div>""", unsafe_allow_html=True)

# =====================================================
# FOOTER WITH DOT MATRIX PATTERN
# =====================================================

st.markdown("""<div class="footer-wrapper"><div class="dots-pattern"></div><div class="footer-container"><div class="footer-title">Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN</div><div class="footer-subtitle">Perwakilan BKKBN Provinsi Kepulauan Bangka Belitung</div><div class="footer-copy">Dashboard PERKIN | © 2026</div></div></div>""", unsafe_allow_html=True)
