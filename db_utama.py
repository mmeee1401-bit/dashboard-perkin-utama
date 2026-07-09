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

/* Background */

.stApp{
    background:#EEF4FB;
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

/* Header */

.header{

background:linear-gradient(
135deg,
#0B4EA2,
#42A5F5);

padding:35px;

border-radius:28px;

color:white;

box-shadow:0 12px 30px rgba(0,0,0,.15);

}

/* Tahun */

.tahun-card{

background:white;

padding:25px;

border-radius:22px;

text-align:center;

box-shadow:0 8px 20px rgba(0,0,0,.08);

transition:.3s;

margin-top:15px;

}

.tahun-card:hover{

transform:translateY(-6px);

}

/* Footer */

.footer{

margin-top:45px;

padding:20px;

border-radius:18px;

background:linear-gradient(
90deg,
#0B4EA2,
#1976D2);

color:white;

text-align:center;

}

/* ==========================
CARD DASHBOARD
========================== */

.year-link{
    text-decoration:none !important;
}

.year-card{

    background:white;
    border-radius:18px;

    padding:18px;

    text-align:center;

    border:1px solid #E5ECF5;

    box-shadow:0 8px 18px rgba(0,0,0,.08);

    transition:.3s;

    margin-bottom:18px;
}

.year-card:hover{

    transform:translateY(-10px);

    box-shadow:0 18px 35px rgba(0,0,0,.18);

    border:2px solid #1976D2;

}

.year-icon{
    font-size:55px;
    margin-bottom:8px;
}

.year-number{

    font-size:34px;

    font-weight:700;

    color:#0B4EA2;

}

.year-text{

    margin-top:10px;

    font-size:17px;

    color:#666;

}

.year-section{
    margin-top:-60px;
}

.year-status{

    margin-top:18px;

    display:inline-block;

    padding:7px 18px;

    border-radius:50px;

    background:#E3F2FD;

    color:#1565C0;

    font-weight:600;

    font-size:14px;

}

/* Hilangkan icon link */
a[title="Open link"]{
    display:none !important;
}

[data-testid="stMarkdownContainer"] a svg{
    display:none !important;
}
            
.status-active{
background:#D4EDDA;
color:#0B7A39;
}

.status-archive{
background:#E3F2FD;
color:#1565C0;
}

.status-empty{
background:#FFF3CD;
color:#C27C00;
}

.status-coming{
background:#F3F4F6;
color:#666;
}

            /* Samakan tinggi semua tombol */
div.stButton > button,
div.stLinkButton > a{
    width:100%;
    height:44px;
    border-radius:12px;
    font-weight:600;
}           
            
/* ===========================
FOOTER
=========================== */
.footer{
margin-top:40px;
padding:22px;
background:linear-gradient(
90deg,
#0B4EA2,
#1976D2);
border-radius:18px;
color:white;
text-align:center;
}


.footer h2 a{
    display:none !important;
}
           
.footer h2::after{
    display:none !important;
}


</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

col1,col2=st.columns([8,4.5])

with col1:

    st.markdown("""

<div class="header">

<div style="
font-size:42px;
font-weight:700;
margin-bottom:8px;">

<b> Selamat Datang di Dashboard PERKIN</b>

</div>

<div style="
font-size:18px;">

Realisasi Kinerja Program Bangga Kencana
Provinsi Kepulauan Bangka Belitung

</div>

<div style="
margin-top:18px;
font-size:15px;">

Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown(
        "<div style='margin-top:20px'></div>",
        unsafe_allow_html=True
    )

    st.image(
        "logo_bkkbnbaru.png",
        width=380
    )


# =====================================================
# JUDUL
# =====================================================

st.markdown("""
<div style="
text-align:center;
margin-top:25px;
margin-bottom:8px;
">

<h1 style="
color:#0B4EA2;
font-size:40px;
font-weight:300;
margin-bottom:8px;
line-height:1.1;
">

<b> Pilih tahun monitoring untuk melihat capaian indikator </b>

</h1>

</div>
""", unsafe_allow_html=True)

# =====================================================
# PILIHAN TAHUN
# =====================================================

tahun = [

{
"tahun":"2022",
"icon":"🗄️",
"status":"Data Tidak Tersedia",
"url":""
},

{
"tahun":"2023",
"icon":"📉",
"status":"Arsip",
"url":"https://dashboard-perkin-2023.streamlit.app/"
},

{
"tahun":"2024",
"icon":"📉",
"status":"Arsip",
"url":"https://dashboard-perkin-2024.streamlit.app/"
},

{
"tahun":"2025",
"icon":"📉",
"status":"Arsip",
"url":"https://dashboard-perkin-2025.streamlit.app/"
},

{
"tahun":"2026",
"icon":"⭐",
"status":"Aktif",
"url":"https://dashboard-perkin-2026new.streamlit.app/"
},

{
"tahun":"2027",
"icon":"📅",
"status":"Belum Tersedia",
"url":""
},

{
"tahun":"2028",
"icon":"📅",
"status":"Belum Tersedia",
"url":""
},

{
"tahun":"2029",
"icon":"📅",
"status":"Belum Tersedia",
"url":""
}

]

for i in range(0, len(tahun), 3):

    cols = st.columns(3)

    for col, item in zip(cols, tahun[i:i+3]):

        with col:

            st.markdown(f"""
            <div class="year-card">

            <div class="year-icon">{item['icon']}</div>

            <div class="year-number">{item['tahun']}</div>

            <div class="year-text">
            Dashboard PERKIN
            </div>

            <div class="year-status">
            {item['status']}
            </div>

            </div>
            """, unsafe_allow_html=True)

            

            if item["tahun"] == "2022":

                if st.button("Buka Dashboard", key="2022", use_container_width=True):

                    st.warning("⚠️ Data Dashboard PERKIN Tahun 2022 belum tersedia.")

            elif item["tahun"] in ["2027","2028","2029"]:

                if st.button("Buka Dashboard", key=item["tahun"], use_container_width=True):

                    st.info("📅 Data Dashboard tahun ini belum tersedia.")

            else:

                st.link_button(
                    "Buka Dashboard",
                    item["url"],
                    use_container_width=True
                )


# =====================================================
# FOOTER
# =====================================================


st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""
<div class="footer">
           
<h2 style="margin-bottom:8px;">
Dashboard PERKIN 2026
</h2>
<div style="font-size:16px; opacity:.95;">
Monitoring Kinerja Program Bangka Belitung
</div>
<br>
<hr style="
border:1px solid rgba(255,255,255,.25);
">
<div style="
font-size:15px;
line-height:1.8;
">
<b>Kementerian Kependudukan dan Pembangunan Keluarga / BKKBN</b><br>
<b> Perwakilan BKKBN</b><br>
<b> Provinsi Kepulauan Bangka Belitung</b><br>
<br>  
 ©
<b>BKKBN</b> -
<b>BANGKA BELITUNG</b> -
<b>2026</b>


</div>


</div>
""", unsafe_allow_html=True)
