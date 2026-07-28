import streamlit as st
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Dashboard PERKIN",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background:#EEF4FB;
}

#MainMenu,
footer,
header{
    visibility:hidden;
}

/* HEADER */

.header{
    background:linear-gradient(135deg,#0B4EA2,#42A5F5);
    padding:35px;
    border-radius:25px;
    color:white;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

/* CARD */

.year-card{
    background:white;
    border-radius:18px;
    padding:22px;
    text-align:center;
    border:1px solid #E5ECF5;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    transition:.3s;
    margin-bottom:15px;
}

.year-card:hover{
    transform:translateY(-8px);
    box-shadow:0 18px 35px rgba(0,0,0,.18);
    border:2px solid #1976D2;
}

.year-icon{
    font-size:55px;
}

.year-number{
    font-size:34px;
    font-weight:700;
    color:#0B4EA2;
}

.year-text{
    color:#666;
    margin-top:8px;
}

.year-status{
    display:inline-block;
    margin-top:15px;
    padding:7px 18px;
    border-radius:30px;
    background:#E3F2FD;
    color:#1565C0;
    font-weight:600;
}

/* BUTTON */

div.stButton > button{
    width:100%;
    height:45px;
    border-radius:12px;
    border:none;
    background:linear-gradient(135deg,#0B4EA2,#2F80ED);
    color:white;
    font-weight:600;
    transition:.3s;
}

div.stButton > button:hover{
    transform:translateY(-3px);
}

/* FOOTER */

.footer{
    margin-top:40px;
    background:linear-gradient(90deg,#0B4EA2,#1976D2);
    color:white;
    border-radius:18px;
    padding:25px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([8,4])

with col1:

    st.markdown("""
    <div class="header">

    <div style="font-size:42px;font-weight:700;">
    Selamat Datang di Dashboard PERKIN
    </div>

    <br>

    <div style="font-size:18px;">
    Realisasi Kinerja Program Bangga Kencana
    Provinsi Kepulauan Bangka Belitung
    </div>

    <br>

    <div style="font-size:15px;">
    Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.image(
        BASE_DIR / "assets" / "logo_bkkbnbaru.png",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;
color:#0B4EA2;
font-size:42px;'>

Pilih Tahun Monitoring
</h1>

<p style='text-align:center;
font-size:20px;
color:#555;'>

Pilih dashboard berdasarkan tahun pelaporan.

</p>
""", unsafe_allow_html=True)

# =====================================================
# DATA TAHUN
# =====================================================

tahun = [

    {"tahun":"2022","icon":"🗄️","status":"Data Tidak Tersedia"},
    {"tahun":"2023","icon":"📉","status":"Arsip"},
    {"tahun":"2024","icon":"📉","status":"Arsip"},
    {"tahun":"2025","icon":"📉","status":"Arsip"},
    {"tahun":"2026","icon":"⭐","status":"Aktif"},
    {"tahun":"2027","icon":"📅","status":"Belum Tersedia"},
    {"tahun":"2028","icon":"📅","status":"Belum Tersedia"},
    {"tahun":"2029","icon":"📅","status":"Belum Tersedia"}

]

# =====================================================
# CARD
# =====================================================

for i in range(0, len(tahun), 3):

    cols = st.columns(3)

    for col, item in zip(cols, tahun[i:i+3]):

        with col:

            # ---------- CARD ----------
            st.markdown(f"""
            <div class="year-card">

                <div class="year-icon">
                    {item['icon']}
                </div>

                <div class="year-number">
                    {item['tahun']}
                </div>

                <div class="year-text">
                    Dashboard PERKIN
                </div>

                <div class="year-status">
                    {item['status']}
                </div>

            </div>
            """, unsafe_allow_html=True)

            # ---------- BUTTON ----------

            if item["tahun"] == "2022":

                if st.button(
                    "Buka Dashboard",
                    key="btn2022",
                    use_container_width=True
                ):
                    st.warning(
                        "⚠️ Dashboard PERKIN Tahun 2022 belum tersedia."
                    )

            elif item["tahun"] in ["2027","2028","2029"]:

                if st.button(
                    "Buka Dashboard",
                    key=f"btn{item['tahun']}",
                    use_container_width=True
                ):
                    st.info(
                        "📅 Dashboard tahun ini belum tersedia."
                    )

            elif item["tahun"] == "2023":

                if st.button(
                    "Buka Dashboard",
                    key="btn2023",
                    use_container_width=True
                ):
                    st.switch_page("pages/Dashboard_2023.py")

            elif item["tahun"] == "2024":

                if st.button(
                    "Buka Dashboard",
                    key="btn2024",
                    use_container_width=True
                ):
                    st.switch_page("pages/Dashboard_2024.py")

            elif item["tahun"] == "2025":

                if st.button(
                    "Buka Dashboard",
                    key="btn2025",
                    use_container_width=True
                ):
                    st.switch_page("pages/Dashboard_2025.py")

            elif item["tahun"] == "2026":

                if st.button(
                    "Buka Dashboard",
                    key="btn2026",
                    use_container_width=True
                ):
                    st.switch_page("pages/Dashboard_2026.py")

            st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<h2>
Dashboard PERKIN
</h2>

Monitoring Kinerja Program Bangka Belitung

<br><br>

<b>Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN</b><br>
Perwakilan BKKBN Provinsi Kepulauan Bangka Belitung

<br><br>

© 2026

</div>
""", unsafe_allow_html=True)
