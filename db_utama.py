import streamlit as st

st.set_page_config(
    page_title="Dashboard PERKIN",
    page_icon="📊",
    layout="wide"
)

# ====================================================
# CSS
# ====================================================

st.markdown("""
<style>

/* =========================
BACKGROUND
========================= */

.stApp{

background:#EEF4FB;

background-image:
radial-gradient(circle at 15% 20%,rgba(46,134,255,.08) 0%,transparent 28%),
radial-gradient(circle at 80% 10%,rgba(46,134,255,.08) 0%,transparent 25%),
radial-gradient(circle at 70% 85%,rgba(46,134,255,.05) 0%,transparent 22%);

}

/* Hide */

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

/* =========================
HERO
========================= */

.hero{

background:linear-gradient(135deg,#0B4EA2,#4A90E2);

padding:42px;

border-radius:30px;

color:white;

position:relative;

overflow:hidden;

box-shadow:0 18px 45px rgba(0,0,0,.18);

}

/* lingkaran dekorasi */

.hero:before{

content:"";

position:absolute;

width:280px;

height:280px;

background:rgba(255,255,255,.06);

border-radius:50%;

top:-90px;

right:-70px;

}

.hero:after{

content:"";

position:absolute;

width:170px;

height:170px;

background:rgba(255,255,255,.05);

border-radius:50%;

bottom:-80px;

left:-60px;

}

.hero-title{

font-size:48px;

font-weight:700;

margin-bottom:12px;

}

.hero-desc{

font-size:19px;

line-height:1.8;

opacity:.95;

margin-bottom:25px;

}

/* =========================
BADGE
========================= */

.badge{

display:inline-block;

padding:10px 18px;

margin-right:10px;

margin-top:10px;

background:rgba(255,255,255,.14);

backdrop-filter:blur(8px);

border-radius:50px;

font-size:14px;

font-weight:600;

}

/* =========================
BUTTON
========================= */

div.stLinkButton>a{

width:100%;

height:52px;

display:flex;

align-items:center;

justify-content:center;

border-radius:14px;

font-weight:700;

font-size:15px;

background:linear-gradient(135deg,#0B4EA2,#2F80ED);

color:white!important;

border:none;

transition:.3s;

box-shadow:0 10px 20px rgba(0,0,0,.18);

}

div.stLinkButton>a:hover{

transform:translateY(-3px);

box-shadow:0 15px 30px rgba(0,0,0,.25);

color:white!important;

}

/* =========================
LOGO
========================= */

.logo-card{

background:white;

border-radius:24px;

padding:22px;

box-shadow:0 12px 25px rgba(0,0,0,.08);

text-align:center;

}

/* =========================
SECTION TITLE
========================= */

.section-title{

margin-top:50px;

margin-bottom:30px;

text-align:center;

font-size:42px;

font-weight:700;

color:#0B4EA2;

}

/* =========================
KPI CARD
========================= */

.stat-card{

background:white;

border-radius:24px;

padding:35px;

text-align:center;

box-shadow:0 12px 30px rgba(0,0,0,.08);

transition:.35s;

}

.stat-card:hover{

transform:translateY(-8px);

box-shadow:0 22px 40px rgba(0,0,0,.15);

}

.stat-icon{

font-size:55px;

margin-bottom:10px;

}

.stat-number{

font-size:45px;

font-weight:700;

color:#0B4EA2;

}

.stat-label{

font-size:17px;

color:#666;

margin-top:8px;

}

/* =========================
YEAR CARD
========================= */

.year-card{

background:white;

border-radius:25px;

padding:30px;

text-align:center;

box-shadow:0 12px 30px rgba(0,0,0,.08);

transition:.35s;

height:290px;

display:flex;

flex-direction:column;

justify-content:center;

}

.year-card:hover{

transform:translateY(-10px);

box-shadow:0 20px 40px rgba(0,0,0,.15);

}

.year-icon{

font-size:60px;

margin-bottom:18px;

}

.year-title{

font-size:36px;

font-weight:700;

color:#0B4EA2;

}

.year-desc{

margin-top:10px;

font-size:16px;

color:#666;

min-height:45px;

}

.badge-status{

margin-top:18px;

display:inline-block;

padding:8px 18px;

border-radius:50px;

font-size:14px;

font-weight:600;

}

.badge-active{

background:#D8F5DD;

color:#198754;

}

.badge-archive{

background:#DCEEFF;

color:#0B4EA2;

}

.badge-coming{

background:#F3F4F6;

color:#666;

}

.badge-empty{

background:#FFF3CD;

color:#B8860B;

}

</style>
""", unsafe_allow_html=True)

# ====================================================
# HERO
# ====================================================

left,right=st.columns([7,3])

with left:

    st.markdown("""

<div class="hero">

<div class="hero-title">

📊 Dashboard PERKIN

</div>

<div class="hero-desc">

Monitoring Realisasi Kinerja Program Bangga Kencana
Provinsi Kepulauan Bangka Belitung

</div>

<div class="badge">
⭐ Dashboard Aktif : 2026
</div>

<div class="badge">
📅 Last Update : Juli 2026
</div>

<div class="badge">
📍 BKKBN Bangka Belitung
</div>

</div>

""",unsafe_allow_html=True)

with right:

    st.markdown('<div class="logo-card">',unsafe_allow_html=True)

    st.image(
        "logo_bkkbnbaru.png",
        width=260
    )

    st.link_button(
        "🏠 Kembali ke SIPELIKES",
        "https://ppid-kemendukbanggababel.my.canva.site/sipelikes/",
        use_container_width=True
    )

    st.markdown("</div>",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

# ====================================================
# KPI
# ====================================================

k1,k2,k3,k4 = st.columns(4)

with k1:

    st.markdown("""

<div class="stat-card">

<div class="stat-icon">
📊
</div>

<div class="stat-number">
4
</div>

<div class="stat-label">
Dashboard Tersedia
</div>

</div>

""",unsafe_allow_html=True)

with k2:

    st.markdown("""

<div class="stat-card">

<div class="stat-icon">
⭐
</div>

<div class="stat-number">
1
</div>

<div class="stat-label">
Dashboard Aktif
</div>

</div>

""",unsafe_allow_html=True)

with k3:

    st.markdown("""

<div class="stat-card">

<div class="stat-icon">
🗂️
</div>

<div class="stat-number">
3
</div>

<div class="stat-label">
Dashboard Arsip
</div>

</div>

""",unsafe_allow_html=True)

with k4:

    st.markdown("""

<div class="stat-card">

<div class="stat-icon">
📅
</div>

<div class="stat-number">
4
</div>

<div class="stat-label">
Belum Tersedia
</div>

</div>

""",unsafe_allow_html=True)

# ====================================================
# JUDUL
# ====================================================

st.markdown("""

<div class="section-title">

Pilih Tahun Monitoring

</div>

""",unsafe_allow_html=True)

# ====================================================
# DATA DASHBOARD
# ====================================================

dashboard = [

{
"tahun":"2022",
"icon":"🗄️",
"desc":"Belum tersedia data monitoring",
"status":"Data Tidak Tersedia",
"class":"badge-empty",
"url":""
},

{
"tahun":"2023",
"icon":"📉",
"desc":"Lihat capaian tahun 2023",
"status":"Arsip",
"class":"badge-archive",
"url":"https://dashboard-perkin-2023.streamlit.app/"
},

{
"tahun":"2024",
"icon":"📉",
"desc":"Lihat capaian tahun 2024",
"status":"Arsip",
"class":"badge-archive",
"url":"https://dashboard-perkin-2024.streamlit.app/"
},

{
"tahun":"2025",
"icon":"📉",
"desc":"Lihat capaian tahun 2025",
"status":"Arsip",
"class":"badge-archive",
"url":"https://dashboard-perkin-2025.streamlit.app/"
},

{
"tahun":"2026",
"icon":"⭐",
"desc":"Dashboard Monitoring Utama",
"status":"Aktif",
"class":"badge-active",
"url":"https://dashboard-perkin-2026new.streamlit.app/"
},

{
"tahun":"2027",
"icon":"📅",
"desc":"Segera Hadir",
"status":"Belum Tersedia",
"class":"badge-coming",
"url":""
},

{
"tahun":"2028",
"icon":"📅",
"desc":"Segera Hadir",
"status":"Belum Tersedia",
"class":"badge-coming",
"url":""
},

{
"tahun":"2029",
"icon":"📅",
"desc":"Segera Hadir",
"status":"Belum Tersedia",
"class":"badge-coming",
"url":""
}

]

for i in range(0,len(dashboard),4):

    cols=st.columns(4)

    for col,item in zip(cols,dashboard[i:i+4]):

        with col:

            st.markdown(f"""

<div class="year-card">

<div class="year-icon">
{item["icon"]}
</div>

<div class="year-title">
{item["tahun"]}
</div>

<div class="year-desc">
{item["desc"]}
</div>

<div class="badge-status {item["class"]}">
{item["status"]}
</div>

</div>

""",unsafe_allow_html=True)

            # ============================
            # BUTTON
            # ============================

            if item["tahun"]=="2022":

                if st.button(
                    "📁 Buka Dashboard",
                    key="2022",
                    use_container_width=True
                ):

                    st.warning(
                        "Data Dashboard PERKIN Tahun 2022 belum tersedia."
                    )

            elif item["tahun"] in ["2027","2028","2029"]:

                if st.button(
                    "📁 Buka Dashboard",
                    key=item["tahun"],
                    use_container_width=True
                ):

                    st.info(
                        "Dashboard tahun ini belum tersedia."
                    )

            else:

                st.link_button(
                    "🚀 Buka Dashboard",
                    item["url"],
                    use_container_width=True
                )

# ====================================================
# INFORMASI
# ====================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="section-title">

📢 Informasi Dashboard

</div>

""", unsafe_allow_html=True)

c1,c2=st.columns(2)

with c1:

    st.markdown("""

<div class="info-card blue">

<div class="info-icon">

📊

</div>

<h3>Dashboard Aktif</h3>

<p>

Dashboard PERKIN Tahun 2026 merupakan dashboard utama yang digunakan
untuk monitoring capaian indikator Program Bangga Kencana
Provinsi Kepulauan Bangka Belitung.

</p>

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""

<div class="info-card yellow">

<div class="info-icon">

🗂️

</div>

<h3>Dashboard Arsip</h3>

<p>

Dashboard tahun 2023–2025 tetap tersedia sebagai arsip
monitoring dan evaluasi kinerja.

</p>

</div>

""",unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="info-card green">

<div class="info-icon">

⭐

</div>

<h3>Update Berkala</h3>

<p>

Seluruh data akan diperbarui secara berkala
sesuai hasil pelaporan Kabupaten/Kota.

</p>

</div>

""",unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown("""

<div class="info-card gray">

<div class="info-icon">

📅

</div>

<h3>Dashboard Mendatang</h3>

<p>

Dashboard Tahun 2027 dan seterusnya akan
tersedia setelah periode pelaporan dimulai.

</p>

</div>

""",unsafe_allow_html=True)

/* ===========================
INFO CARD
=========================== */

.info-card{

padding:28px;

border-radius:22px;

box-shadow:0 12px 28px rgba(0,0,0,.08);

transition:.35s;

}

.info-card:hover{

transform:translateY(-8px);

box-shadow:0 18px 35px rgba(0,0,0,.15);

}

.info-icon{

font-size:45px;

margin-bottom:15px;

}

.info-card h3{

margin-bottom:12px;

color:#0B4EA2;

}

.info-card p{

line-height:1.8;

font-size:15px;

color:#555;

}

.blue{

background:#EEF6FF;

}

.green{

background:#EDFCEF;

}

.yellow{

background:#FFF8E6;

}

.gray{

background:#F5F5F5;

}

st.markdown("""
<style>

.footer-perkin {
    background: linear-gradient(135deg, #0B4EA2, #2F80ED);
    padding: 20px 30px;
    border-radius: 15px;
    margin-top: 40px;
    color: white;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
}

.footer-perkin h4 {
    margin: 0;
    font-size: 18px;
    font-weight: 700;
}

.footer-perkin p {
    margin: 5px 0;
    font-size: 14px;
    opacity: 0.9;
}

.footer-line {
    height: 1px;
    background: rgba(255,255,255,0.4);
    margin: 15px 0;
}

</style>

<div class="footer-perkin">

<h4>
📊 Dashboard PERKIN 2026
</h4>

<div class="footer-line"></div>

<p>
Sistem Visualisasi Data Kinerja
</p>

<p>
© 2026 Kemendukbangga/BKKBN
</p>

<p>
Dikembangkan untuk mendukung monitoring dan evaluasi program
</p>

</div>

""", unsafe_allow_html=True)
