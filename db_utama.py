import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard PERKIN",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* ===============================
BACKGROUND
================================ */

.stApp{

background:
linear-gradient(
180deg,
#F7FBFF 0%,
#EEF5FD 100%);

}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* ===============================
HERO
================================ */

.hero{

background:
linear-gradient(
135deg,
#0B4EA2,
#2F80ED);

border-radius:32px;

padding:45px;

overflow:hidden;

position:relative;

box-shadow:
0 18px 45px rgba(0,0,0,.18);

margin-bottom:35px;

}

.hero:before{

content:"";

position:absolute;

width:420px;

height:420px;

background:rgba(255,255,255,.08);

border-radius:50%;

right:-130px;

top:-130px;

}

.hero:after{

content:"";

position:absolute;

width:250px;

height:250px;

background:rgba(255,255,255,.06);

border-radius:50%;

left:-80px;

bottom:-80px;

}

.hero-title{

font-size:48px;

font-weight:700;

color:white;

margin-bottom:8px;

}

.hero-sub{

font-size:20px;

color:white;

opacity:.95;

line-height:1.6;

}

.hero-info{

display:flex;

gap:15px;

margin-top:30px;

flex-wrap:wrap;

}

.hero-badge{

background:rgba(255,255,255,.15);

padding:10px 18px;

border-radius:40px;

color:white;

font-size:15px;

font-weight:600;

backdrop-filter:blur(10px);

}

/* ===============================
BUTTON
================================ */

div.stLinkButton>a{

background:
linear-gradient(
135deg,
#1565C0,
#42A5F5);

color:white !important;

border-radius:15px;

height:48px;

font-weight:700;

display:flex;

align-items:center;

justify-content:center;

border:none;

transition:.35s;

box-shadow:
0 8px 20px rgba(21,101,192,.25);

}

div.stLinkButton>a:hover{

transform:translateY(-3px);

box-shadow:
0 14px 28px rgba(21,101,192,.35);

color:white !important;

}

/* ===============================
SECTION TITLE
================================ */

.section-title{

font-size:36px;

font-weight:700;

text-align:center;

color:#0B4EA2;

margin-top:20px;

margin-bottom:30px;

}

/* ===============================
STAT CARD
================================ */

.stat-card{

background:white;

border-radius:22px;

padding:28px;

text-align:center;

box-shadow:
0 12px 28px rgba(0,0,0,.08);

transition:.35s;

border:1px solid #EAF1FB;

}

.stat-card:hover{

transform:translateY(-8px);

box-shadow:
0 22px 45px rgba(0,0,0,.15);

}

.stat-icon{

font-size:48px;

margin-bottom:8px;

}

.stat-number{

font-size:38px;

font-weight:700;

color:#0B4EA2;

}

.stat-label{

font-size:16px;

margin-top:8px;

color:#666;

}

/* ===============================
CARD TAHUN
================================ */

.year-card{

background:white;

border-radius:25px;

padding:28px;

box-shadow:
0 15px 35px rgba(0,0,0,.08);

transition:.35s;

text-align:center;

border:2px solid transparent;

margin-bottom:20px;

}

.year-card:hover{

transform:translateY(-10px);

box-shadow:
0 25px 50px rgba(0,0,0,.18);

border:2px solid #1976D2;

}

.year-icon{

font-size:65px;

}

.year-title{

font-size:40px;

font-weight:700;

margin-top:10px;

color:#0B4EA2;

}

.year-desc{

margin-top:12px;

font-size:15px;

color:#666;

min-height:45px;

}

.badge{

display:inline-block;

margin-top:20px;

padding:8px 18px;

border-radius:50px;

font-weight:700;

font-size:14px;

}

.badge-active{

background:#D9F7E5;

color:#0E8A47;

}

.badge-archive{

background:#E7F0FF;

color:#1565C0;

}

.badge-coming{

background:#FFF6D8;

color:#C78A00;

}

.badge-empty{

background:#FFE4E4;

color:#D93D3D;

}

/* ===============================
FOOTER
================================ */

.footer{

margin-top:50px;

padding:28px;

border-radius:25px;

background:
linear-gradient(
135deg,
#0B4EA2,
#1976D2);

color:white;

text-align:center;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

hero1,hero2=st.columns([2.3,1])

with hero1:

    st.markdown("""

<div class="hero">

<div class="hero-title">

📊 Dashboard PERKIN

</div>

<div class="hero-sub">

Monitoring Realisasi Kinerja Program Bangga Kencana
Provinsi Kepulauan Bangka Belitung

</div>

<div class="hero-info">

<div class="hero-badge">

⭐ Dashboard Aktif : <b>2026</b>

</div>

<div class="hero-badge">

📅 Last Update : Juli 2026

</div>

<div class="hero-badge">

📍 BKKBN Bangka Belitung

</div>

</div>

</div>

""", unsafe_allow_html=True)

with hero2:

    st.image(
        "logo_bkkbnbaru.png",
        use_container_width=True
    )

    st.link_button(
        "🏠 Kembali ke SIPELIKES",
        "https://ppid-kemendukbanggababel.my.canva.site/sipelikes/",
        use_container_width=True
    )

# =====================================================
# KPI
# =====================================================

k1,k2,k3,k4=st.columns(4)

with k1:

    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">📊</div>
        <div class="stat-number">4</div>
        <div class="stat-label">
            Dashboard Tersedia
        </div>
    </div>
    """, unsafe_allow_html=True)

with k2:

    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">⭐</div>
        <div class="stat-number">1</div>
        <div class="stat-label">
            Dashboard Aktif
        </div>
    </div>
    """, unsafe_allow_html=True)

with k3:

    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">🗂️</div>
        <div class="stat-number">3</div>
        <div class="stat-label">
            Dashboard Arsip
        </div>
    </div>
    """, unsafe_allow_html=True)

with k4:

    st.markdown("""
    <div class="stat-card">
        <div class="stat-icon">📅</div>
        <div class="stat-number">4</div>
        <div class="stat-label">
            Belum Tersedia
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# JUDUL
# =====================================================

st.markdown("""
<div class="section-title">
Pilih Tahun Monitoring
</div>
""", unsafe_allow_html=True)

# =====================================================
# DATA TAHUN
# =====================================================

tahun = [

{
    "tahun":"2022",
    "icon":"🗄️",
    "status":"Data Tidak Tersedia",
    "badge":"badge-empty",
    "deskripsi":"Belum tersedia data monitoring",
    "url":""
},

{
    "tahun":"2023",
    "icon":"📉",
    "status":"Arsip",
    "badge":"badge-archive",
    "deskripsi":"Lihat capaian tahun 2023",
    "url":"https://dashboard-perkin-2023.streamlit.app/"
},

{
    "tahun":"2024",
    "icon":"📉",
    "status":"Arsip",
    "badge":"badge-archive",
    "deskripsi":"Lihat capaian tahun 2024",
    "url":"https://dashboard-perkin-2024.streamlit.app/"
},

{
    "tahun":"2025",
    "icon":"📉",
    "status":"Arsip",
    "badge":"badge-archive",
    "deskripsi":"Lihat capaian tahun 2025",
    "url":"https://dashboard-perkin-2025.streamlit.app/"
},

{
    "tahun":"2026",
    "icon":"⭐",
    "status":"Aktif",
    "badge":"badge-active",
    "deskripsi":"Dashboard Monitoring Terbaru",
    "url":"https://dashboard-perkin-2026new.streamlit.app/"
},

{
    "tahun":"2027",
    "icon":"📅",
    "status":"Belum Tersedia",
    "badge":"badge-coming",
    "deskripsi":"Segera Hadir",
    "url":""
},

{
    "tahun":"2028",
    "icon":"📅",
    "status":"Belum Tersedia",
    "badge":"badge-coming",
    "deskripsi":"Segera Hadir",
    "url":""
},

{
    "tahun":"2029",
    "icon":"📅",
    "status":"Belum Tersedia",
    "badge":"badge-coming",
    "deskripsi":"Segera Hadir",
    "url":""
}

]

# =====================================================
# CARD DASHBOARD
# =====================================================

for i in range(0, len(tahun), 4):

    cols = st.columns(4)

    for col, item in zip(cols, tahun[i:i+4]):

        with col:

            st.markdown(f"""
            <div class="year-card">

                <div class="year-icon">
                    {item['icon']}
                </div>

                <div class="year-title">
                    {item['tahun']}
                </div>

                <div class="year-desc">
                    {item['deskripsi']}
                </div>

                <div class="badge {item['badge']}">
                    {item['status']}
                </div>

            </div>
            """, unsafe_allow_html=True)

            # ==========================
            # BUTTON
            # ==========================

            if item["tahun"] == "2022":

                if st.button(
                    "📂 Buka Dashboard",
                    key="2022",
                    use_container_width=True
                ):

                    st.warning(
                        "⚠️ Data Dashboard PERKIN Tahun 2022 belum tersedia."
                    )

            elif item["tahun"] in ["2027","2028","2029"]:

                if st.button(
                    "📂 Buka Dashboard",
                    key=item["tahun"],
                    use_container_width=True
                ):

                    st.info(
                        "📅 Dashboard tahun ini belum tersedia."
                    )

            else:

                st.link_button(
                    "🚀 Buka Dashboard",
                    item["url"],
                    use_container_width=True
                )

# =====================================================
# INFORMASI DASHBOARD
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:linear-gradient(135deg,#FFFFFF,#F8FBFF);
padding:35px;
border-radius:28px;
box-shadow:0 15px 35px rgba(0,0,0,.08);
margin-top:20px;
">

<h2 style="
color:#0B4EA2;
margin-bottom:18px;
text-align:center;
">

📢 Informasi Dashboard

</h2>

<div style="
display:grid;
grid-template-columns:repeat(2,1fr);
gap:20px;
">

<div style="
background:#EEF5FF;
padding:20px;
border-radius:18px;
">

<h4>📊 Dashboard Aktif</h4>

<p style="margin:0;">
Dashboard PERKIN 2026 merupakan dashboard utama yang digunakan untuk monitoring capaian indikator Program Bangga Kencana Provinsi Kepulauan Bangka Belitung.
</p>

</div>

<div style="
background:#F4FFF5;
padding:20px;
border-radius:18px;
">

<h4>⭐ Update Berkala</h4>

<p style="margin:0;">
Data akan diperbarui secara berkala sesuai pelaporan dari Kabupaten/Kota.
</p>

</div>

<div style="
background:#FFF8E8;
padding:20px;
border-radius:18px;
">

<h4>🗂 Dashboard Arsip</h4>

<p style="margin:0;">
Dashboard tahun sebelumnya tetap dapat diakses sebagai arsip monitoring.
</p>

</div>

<div style="
background:#F5F5F5;
padding:20px;
border-radius:18px;
">

<h4>📅 Dashboard Mendatang</h4>

<p style="margin:0;">
Dashboard tahun berikutnya akan tersedia setelah periode pelaporan dimulai.
</p>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<div style="font-size:30px;font-weight:700;">

📊 Dashboard PERKIN

</div>

<div style="
margin-top:10px;
font-size:18px;
opacity:.95;
">

Monitoring Kinerja Program Bangga Kencana
Provinsi Kepulauan Bangka Belitung

</div>

<hr style="
margin-top:25px;
margin-bottom:25px;
border:1px solid rgba(255,255,255,.2);
">

<div style="
font-size:16px;
line-height:2;
">

<b>Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN</b><br>

Perwakilan BKKBN Provinsi Kepulauan Bangka Belitung

<br><br>

© 2026 • Dashboard PERKIN

</div>

</div>
""", unsafe_allow_html=True)
