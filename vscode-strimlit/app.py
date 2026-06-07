import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import random

# ============================================
# IMPORT SOAL DARI STORAGE
# ============================================
from quiz_storage import get_random_questions

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="Analisis Kation Golongan I, III, IV",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# INISIALISASI THEME
# ============================================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ============================================
# CSS DINAMIS BERDASARKAN TEMA
# ============================================
def get_css(dark_mode):
    if dark_mode:
        bg_primary     = "#0f1117"
        bg_secondary   = "#1a1d27"
        bg_card        = "#1e2130"
        bg_reaction    = "#151825"
        text_primary   = "#e8eaf6"
        text_secondary = "#9fa8da"
        border_color   = "#2d3561"
        accent_blue    = "#5c7cfa"
        accent_orange  = "#ff8c42"
        accent_green   = "#56cf86"
        accent_red     = "#ff6b6b"
        accent_yellow  = "#ffd93d"
        accent_teal    = "#4ecdc4"
        header_bg      = "linear-gradient(135deg, #1a1d27 0%, #0f1117 100%)"
        sidebar_bg     = "#13161f"
        table_alt      = "#252840"
        table_header   = "#1f2235"
        info_bg        = "rgba(92,124,250,0.15)"
        info_border    = "#5c7cfa"
        warning_bg     = "rgba(255,140,66,0.15)"
        warning_border = "#ff8c42"
        success_bg     = "rgba(86,207,134,0.15)"
        success_border = "#56cf86"
        correct_bg     = "rgba(86,207,134,0.2)"
        wrong_bg       = "rgba(255,107,107,0.2)"
        quiz_hover     = "rgba(92,124,250,0.15)"
        toggle_bg      = "#2d3561"
        bubble_color   = "rgba(92,124,250,0.08)"
    else:
        bg_primary     = "#f4f6fb"
        bg_secondary   = "#ffffff"
        bg_card        = "#ffffff"
        bg_reaction    = "#f0f4ff"
        text_primary   = "#1a1a2e"
        text_secondary = "#4a5568"
        border_color   = "#d0d9f0"
        accent_blue    = "#3a5bd9"
        accent_orange  = "#e05c00"
        accent_green   = "#1a9e56"
        accent_red     = "#d32f2f"
        accent_yellow  = "#b8860b"
        accent_teal    = "#00796b"
        header_bg      = "linear-gradient(135deg, #dde8ff 0%, #f4f6fb 100%)"
        sidebar_bg     = "#eaefff"
        table_alt      = "#f0f4ff"
        table_header   = "#3a5bd9"
        info_bg        = "rgba(58,91,217,0.08)"
        info_border    = "#3a5bd9"
        warning_bg     = "rgba(224,92,0,0.08)"
        warning_border = "#e05c00"
        success_bg     = "rgba(26,158,86,0.08)"
        success_border = "#1a9e56"
        correct_bg     = "rgba(26,158,86,0.12)"
        wrong_bg       = "rgba(211,47,47,0.12)"
        quiz_hover     = "rgba(58,91,217,0.08)"
        toggle_bg      = "#d0d9f0"
        bubble_color   = "rgba(58,91,217,0.05)"

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:wght@700&display=swap');

/* ========== GLOBAL RESET ========== */
*, *::before, *::after {{ box-sizing: border-box; }}

/* ========== APP BACKGROUND ========== */
.stApp {{
    background: {bg_primary} !important;
    font-family: 'Space Grotesk', sans-serif;
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background: {sidebar_bg} !important;
    border-right: 2px solid {border_color};
}}
[data-testid="stSidebar"] * {{
    color: {text_primary} !important;
}}

/* Main content background */
.main .block-container {{
    background: transparent !important;
    padding-top: 2rem;
}}

/* ========== TYPOGRAPHY ========== */
h1, h2, h3, h4 {{
    font-family: 'Space Grotesk', sans-serif;
    color: {text_primary};
}}

p, li, td, th, label, div {{
    color: {text_primary};
}}

/* ========== HEADER ========== */
.main-header {{
    background: {header_bg};
    border: 2px solid {border_color};
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}}
.main-header::before {{
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 50%, {bubble_color} 0%, transparent 60%),
                radial-gradient(circle at 70% 50%, {bubble_color} 0%, transparent 60%);
    pointer-events: none;
}}
.main-header h1 {{
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: {accent_blue};
    margin: 0 0 0.5rem 0;
    position: relative;
}}
.main-header p {{
    color: {text_secondary};
    font-size: 1rem;
    margin: 0;
    position: relative;
}}

/* ========== CARDS ========== */
.cation-card {{
    background: {bg_card};
    border: 1.5px solid {border_color};
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 2px 16px rgba(0,0,0,{0.25 if dark_mode else 0.06});
    transition: box-shadow 0.3s ease;
}}
.cation-card:hover {{
    box-shadow: 0 6px 28px rgba(0,0,0,{0.35 if dark_mode else 0.10});
}}

/* ========== REACTION BOX ========== */
.reaction-box {{
    background: {bg_reaction};
    border-left: 4px solid {accent_blue};
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin: 0.6rem 0;
    font-size: 0.95rem;
    color: {text_primary};
}}

/* ========== INFO / WARNING / SUCCESS BOXES ========== */
.info-box {{
    background: {info_bg};
    border: 1.5px solid {info_border};
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 0.8rem 0;
    color: {text_primary};
}}
.warning-box {{
    background: {warning_bg};
    border: 1.5px solid {warning_border};
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 0.8rem 0;
    color: {text_primary};
}}
.success-box {{
    background: {success_bg};
    border: 1.5px solid {success_border};
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 0.8rem 0;
    color: {text_primary};
}}

/* ========== QUIZ OPTIONS ========== */
.quiz-option {{
    background: {bg_card};
    border: 1.5px solid {border_color};
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    margin: 0.5rem 0;
    cursor: pointer;
    transition: all 0.25s;
    color: {text_primary};
}}
.quiz-option:hover {{ background: {quiz_hover}; border-color: {accent_blue}; }}
.correct {{ background: {correct_bg} !important; border: 2px solid {accent_green} !important; }}
.wrong   {{ background: {wrong_bg} !important;   border: 2px solid {accent_red} !important;   }}

/* ========== TABLE ========== */
.styled-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    color: {text_primary};
}}
.styled-table th {{
    background: {table_header};
    color: {'#fff' if not dark_mode else text_primary};
    padding: 12px 14px;
    border: 1px solid {border_color};
    text-align: left;
    font-weight: 600;
}}
.styled-table td {{
    padding: 10px 14px;
    border: 1px solid {border_color};
    color: {text_primary};
}}
.styled-table tr:nth-child(even) td {{ background: {table_alt}; }}
.styled-table tr:hover td {{ background: {quiz_hover}; }}

/* ========== PRECIPITATE COLORS ========== */
.p-white  {{ color: {'#aaa' if dark_mode else '#777'}; font-weight: 700; }}
.p-yellow {{ color: {accent_yellow}; font-weight: 700; }}
.p-black  {{ color: {'#ccc' if dark_mode else '#222'}; font-weight: 700; }}
.p-brown  {{ color: #a1887f; font-weight: 700; }}
.p-red    {{ color: {accent_red}; font-weight: 700; }}
.p-green  {{ color: {accent_green}; font-weight: 700; }}
.p-teal   {{ color: {accent_teal}; font-weight: 700; }}

/* ========== GOLONGAN BADGES ========== */
.badge {{
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-right: 6px;
}}
.badge-I   {{ background: rgba(255,107,107,0.2); color: {accent_red}; border: 1px solid {accent_red}; }}
.badge-III {{ background: rgba(78,205,196,0.2); color: {accent_teal}; border: 1px solid {accent_teal}; }}
.badge-IV  {{ background: rgba(255,217,61,0.2); color: {accent_yellow}; border: 1px solid {accent_yellow}; }}

/* ========== STEP INDICATOR ========== */
.step-num {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: {accent_blue};
    color: #fff;
    font-size: 0.8rem;
    font-weight: 700;
    margin-right: 10px;
    flex-shrink: 0;
}}

/* ========== DIGITALISASI - QUESTION BOX ========== */
.q-box {{
    background: {bg_card};
    border: 2px solid {accent_blue};
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
}}
.q-box h3 {{
    color: {accent_blue};
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}}

/* ========== RESULT BOX ========== */
.result-box {{
    background: {success_bg};
    border: 2px solid {success_border};
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    text-align: center;
}}
.result-box h2 {{ color: {accent_green}; font-size: 1.8rem; }}
.result-box .ion {{ font-size: 2.5rem; font-weight: 700; color: {accent_blue}; font-family: 'JetBrains Mono', monospace; }}

/* ========== MONO CODE ========== */
.mono {{
    font-family: 'JetBrains Mono', monospace;
    background: {bg_reaction};
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.9rem;
    color: {accent_orange};
}}

/* ========== THEME TOGGLE ========== */
.theme-status {{
    background: {toggle_bg};
    border-radius: 10px;
    padding: 8px 14px;
    text-align: center;
    font-size: 0.85rem;
    color: {text_secondary};
    margin-bottom: 10px;
}}

/* ========== STREAMLIT OVERRIDES ========== */
.stButton > button {{
    background: {accent_blue} !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    transition: opacity 0.2s !important;
}}
.stButton > button:hover {{ opacity: 0.85 !important; }}

.stSelectbox > div > div {{
    background: {bg_card} !important;
    border-color: {border_color} !important;
    color: {text_primary} !important;
    border-radius: 10px !important;
}}
.stSelectbox label {{ color: {text_primary} !important; }}

.stTabs [data-baseweb="tab-list"] {{
    background: {bg_secondary} !important;
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}}
.stTabs [data-baseweb="tab"] {{
    background: transparent !important;
    color: {text_secondary} !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 500 !important;
}}
.stTabs [aria-selected="true"] {{
    background: {accent_blue} !important;
    color: #fff !important;
}}

.stExpander {{
    background: {bg_card} !important;
    border: 1.5px solid {border_color} !important;
    border-radius: 12px !important;
}}
.stExpander summary {{ color: {text_primary} !important; }}

.stRadio > div {{ gap: 6px; }}
.stRadio label {{ color: {text_primary} !important; }}

.stProgress > div > div > div {{
    background: {accent_blue} !important;
}}

/* Sidebar radio */
[data-testid="stSidebar"] .stRadio label {{
    padding: 8px 12px !important;
    border-radius: 8px !important;
    transition: background 0.2s !important;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: {quiz_hover} !important;
}}

/* Input / text area */
.stTextInput input, .stTextArea textarea {{
    background: {bg_card} !important;
    color: {text_primary} !important;
    border-color: {border_color} !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}}

/* Multiselect */
.stMultiSelect [data-baseweb="select"] {{
    background: {bg_card} !important;
}}

/* Hide default streamlit elements */
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header {{ visibility: hidden; }}

/* Column gap */
[data-testid="column"] {{ padding: 0 0.5rem; }}
</style>
"""

st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

# ============================================
# DATA KATION
# ============================================

cation_data = {
    "Golongan I": {
        "label": "Ag⁺, Pb²⁺, Hg₂²⁺",
        "color": "#FF6B6B",
        "reagen": "HCl encer",
        "precipitate": "AgCl (putih), PbCl₂ (putih), Hg₂Cl₂ (putih)",
        "steps": [
            {
                "action": "Tambahkan HCl encer ke sampel",
                "result": "Terbentuk endapan putih: AgCl, PbCl₂, Hg₂Cl₂",
                "filtrate": "Filtrat → Golongan III (setelah skip Golongan II)",
                "residue": "AgCl, PbCl₂, Hg₂Cl₂"
            },
            {
                "action": "Tambahkan H₂O panas pada endapan",
                "result": "PbCl₂ larut, AgCl dan Hg₂Cl₂ tidak larut",
                "filtrate": "Pb²⁺ (larut)",
                "residue": "AgCl, Hg₂Cl₂"
            },
            {
                "action": "Pada filtrat Pb²⁺: Tambahkan K₂CrO₄",
                "result": "Endapan kuning PbCrO₄",
                "confirm": "Pb²⁺ terkonfirmasi ✅"
            },
            {
                "action": "Pada residu AgCl, Hg₂Cl₂: Tambahkan NH₄OH",
                "result": "AgCl larut → [Ag(NH₃)₂]⁺; Hg₂Cl₂ → Hg (hitam) + Hg(NH₂)Cl (putih)",
                "filtrate": "[Ag(NH₃)₂]⁺",
                "residue": "Hg + Hg(NH₂)Cl"
            },
            {
                "action": "Pada filtrat [Ag(NH₃)₂]⁺: Tambahkan HNO₃",
                "result": "Endapan putih AgCl terbentuk kembali",
                "confirm": "Ag⁺ terkonfirmasi ✅"
            }
        ]
    },
    "Golongan III": {
        "label": "Fe³⁺, Al³⁺, Cr³⁺",
        "color": "#4ECDC4",
        "reagen": "NH₄OH berlebih + NH₄Cl",
        "precipitate": "Fe(OH)₃ (coklat), Al(OH)₃ (putih/gel), Cr(OH)₃ (abu-abu/hijau)",
        "steps": [
            {
                "action": "Tambahkan NH₄OH + NH₄Cl pada filtrat",
                "result": "Fe(OH)₃ (coklat), Al(OH)₃ (putih/gel), Cr(OH)₃ (abu-abu) terendap",
                "filtrate": "Filtrat → Golongan IV",
                "residue": "Fe(OH)₃, Al(OH)₃, Cr(OH)₃"
            },
            {
                "action": "Tambahkan NaOH berlebih + H₂O₂ pada endapan",
                "result": "Al(OH)₃ → [Al(OH)₄]⁻, Cr(OH)₃ → CrO₄²⁻ (keduanya larut), Fe(OH)₃ tidak larut",
                "filtrate": "[Al(OH)₄]⁻, CrO₄²⁻",
                "residue": "Fe(OH)₃"
            },
            {
                "action": "Pada residu Fe(OH)₃: Tambahkan HCl + KSCN",
                "result": "Larutan merah darah [Fe(SCN)]²⁺",
                "confirm": "Fe³⁺ terkonfirmasi ✅"
            },
            {
                "action": "Pada filtrat [Al(OH)₄]⁻: Tambahkan HCl perlahan",
                "result": "Endapan putih/gel Al(OH)₃ kembali terbentuk",
                "confirm": "Al³⁺ terkonfirmasi ✅"
            },
            {
                "action": "Pada filtrat CrO₄²⁻: Tambahkan Pb(NO₃)₂",
                "result": "Endapan kuning PbCrO₄",
                "confirm": "Cr³⁺ terkonfirmasi ✅"
            }
        ]
    },
    "Golongan IV": {
        "label": "Ba²⁺, Sr²⁺, Ca²⁺",
        "color": "#FFD93D",
        "reagen": "(NH₄)₂CO₃ + NH₄OH + NH₄Cl",
        "precipitate": "BaCO₃ (putih), SrCO₃ (putih), CaCO₃ (putih)",
        "steps": [
            {
                "action": "Tambahkan (NH₄)₂CO₃ + NH₄OH + NH₄Cl pada filtrat",
                "result": "BaCO₃, SrCO₃, CaCO₃ terendap putih",
                "filtrate": "Filtrat → Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺)",
                "residue": "BaCO₃, SrCO₃, CaCO₃"
            },
            {
                "action": "Tambahkan CH₃COOH (asam asetat) pada endapan",
                "result": "Semua karbonat larut menjadi asetat",
                "filtrate": "Ba²⁺, Sr²⁺, Ca²⁺ (sebagai asetat)",
                "residue": "-"
            },
            {
                "action": "Pada larutan asetat: Tambahkan K₂CrO₄",
                "result": "Endapan kuning BaCrO₄, Sr²⁺ dan Ca²⁺ tetap larut",
                "filtrate": "Sr²⁺, Ca²⁺",
                "residue": "BaCrO₄ (kuning)"
            },
            {
                "action": "Pada filtrat Sr²⁺, Ca²⁺: Tambahkan (NH₄)₂SO₄",
                "result": "Endapan putih SrSO₄, Ca²⁺ tetap larut",
                "filtrate": "Ca²⁺",
                "residue": "SrSO₄ (putih)"
            },
            {
                "action": "Pada filtrat Ca²⁺: Tambahkan (NH₄)₂C₂O₄",
                "result": "Endapan putih CaC₂O₄",
                "confirm": "Ca²⁺ terkonfirmasi ✅"
            }
        ]
    }
}

# ============================================
# QUIZ QUESTIONS (BUILT-IN)
# ============================================

quiz_questions = {
    "Golongan I": [
        {
            "question": "Reagen apa yang digunakan untuk mengendapkan kation Golongan I?",
            "options": ["H₂SO₄ encer", "HCl encer", "NH₄OH", "NaOH"],
            "correct": 1,
            "explanation": "HCl encer digunakan karena Ag⁺, Pb²⁺, dan Hg₂²⁺ membentuk garam klorida yang tidak larut."
        },
        {
            "question": "Warna endapan PbCl₂ adalah...",
            "options": ["Kuning", "Hitam", "Putih", "Merah"],
            "correct": 2,
            "explanation": "PbCl₂ membentuk endapan berwarna putih saat bereaksi dengan HCl encer."
        },
        {
            "question": "Bagaimana cara memisahkan Pb²⁺ dari AgCl dan Hg₂Cl₂?",
            "options": ["Tambahkan NH₄OH", "Panaskan dengan air panas", "Tambahkan HNO₃", "Tambahkan NaOH"],
            "correct": 1,
            "explanation": "PbCl₂ larut dalam air panas karena kelarutannya meningkat signifikan dengan suhu, sedangkan AgCl dan Hg₂Cl₂ tetap sebagai endapan."
        },
        {
            "question": "Reagen apa yang digunakan untuk mengkonfirmasi keberadaan Pb²⁺?",
            "options": ["KSCN", "K₂CrO₄", "NH₄OH", "HNO₃"],
            "correct": 1,
            "explanation": "K₂CrO₄ menghasilkan endapan kuning PbCrO₄ yang mengkonfirmasi keberadaan Pb²⁺."
        },
        {
            "question": "Apa yang terjadi pada Hg₂Cl₂ saat ditambahkan NH₄OH?",
            "options": [
                "Larut sempurna",
                "Berubah menjadi endapan kuning",
                "Terbentuk Hg (hitam) + Hg(NH₂)Cl (putih)",
                "Tidak bereaksi"
            ],
            "correct": 2,
            "explanation": "Hg₂Cl₂ mengalami disproporsionasi dengan NH₄OH: Hg₂²⁺ → Hg⁰ (hitam) + Hg²⁺ yang membentuk Hg(NH₂)Cl (putih)."
        },
        {
            "question": "Kompleks apa yang terbentuk saat AgCl dilarutkan dalam NH₄OH?",
            "options": ["Ag(OH)₂⁻", "[Ag(NH₃)₂]⁺", "AgNO₃", "AgCl₂⁻"],
            "correct": 1,
            "explanation": "[Ag(NH₃)₂]⁺ adalah kompleks diamminperak(I) yang larut dalam larutan amonia berlebih."
        },
        {
            "question": "Untuk mengkonfirmasi Ag⁺ setelah pembentukan [Ag(NH₃)₂]⁺, reagen apa yang ditambahkan?",
            "options": ["HCl", "HNO₃", "H₂SO₄", "H₃PO₄"],
            "correct": 1,
            "explanation": "Penambahan HNO₃ mengasidifikasi larutan sehingga AgCl mengendap kembali, mengkonfirmasi keberadaan Ag⁺."
        },
        {
            "question": "Warna endapan PbCrO₄ adalah...",
            "options": ["Putih", "Merah", "Kuning", "Hitam"],
            "correct": 2,
            "explanation": "PbCrO₄ adalah endapan berwarna kuning cerah yang merupakan konfirmasi Pb²⁺."
        },
        {
            "question": "Mengapa PbCl₂ dapat dipisahkan dari AgCl menggunakan air panas?",
            "options": [
                "PbCl₂ lebih berat",
                "PbCl₂ memiliki kelarutan yang meningkat dengan suhu",
                "PbCl₂ bersifat asam",
                "AgCl tidak stabil"
            ],
            "correct": 1,
            "explanation": "Kelarutan PbCl₂ meningkat signifikan dengan suhu (kelarutan endotermik), sehingga larut dalam air panas sedangkan AgCl tetap tidak larut."
        },
        {
            "question": "Kation mana yang TIDAK termasuk dalam Golongan I analisis kation?",
            "options": ["Ag⁺", "Pb²⁺", "Ba²⁺", "Hg₂²⁺"],
            "correct": 2,
            "explanation": "Ba²⁺ termasuk Golongan IV, bukan Golongan I. Golongan I terdiri dari Ag⁺, Pb²⁺, dan Hg₂²⁺."
        }
    ],
    "Golongan III": [
        {
            "question": "Reagen pengendap Golongan III adalah...",
            "options": ["HCl encer", "(NH₄)₂CO₃", "NH₄OH + NH₄Cl", "NaOH + H₂O₂"],
            "correct": 2,
            "explanation": "NH₄OH + NH₄Cl digunakan. NH₄Cl berfungsi sebagai penyangga untuk menekan [OH⁻] agar Mg²⁺ tidak ikut terendap."
        },
        {
            "question": "Warna endapan Fe(OH)₃ adalah...",
            "options": ["Putih", "Kuning", "Coklat/Merah", "Hitam"],
            "correct": 2,
            "explanation": "Fe(OH)₃ membentuk endapan berwarna coklat kemerahan yang khas."
        },
        {
            "question": "Reagen apa yang digunakan untuk mengkonfirmasi Fe³⁺?",
            "options": ["K₂CrO₄", "KSCN", "NH₄OH", "Pb(NO₃)₂"],
            "correct": 1,
            "explanation": "KSCN (kalium tiosianat) menghasilkan warna merah darah [Fe(SCN)]²⁺ yang sangat sensitif untuk Fe³⁺."
        },
        {
            "question": "Fungsi NH₄Cl dalam pengendapan Golongan III adalah...",
            "options": [
                "Meningkatkan pH larutan",
                "Menekan [OH⁻] agar Mg²⁺ tidak terendap",
                "Mengoksidasi Fe²⁺ menjadi Fe³⁺",
                "Melarutkan endapan"
            ],
            "correct": 1,
            "explanation": "NH₄Cl berfungsi sebagai buffer/penyangga yang menekan konsentrasi OH⁻ sehingga Mg(OH)₂ tidak terbentuk pada pH tersebut."
        },
        {
            "question": "Bagaimana Al(OH)₃ dapat dibedakan dari Fe(OH)₃?",
            "options": [
                "Al(OH)₃ berwarna merah",
                "Al(OH)₃ larut dalam NaOH berlebih",
                "Al(OH)₃ mengendap dalam HCl",
                "Al(OH)₃ bereaksi dengan KSCN"
            ],
            "correct": 1,
            "explanation": "Al(OH)₃ bersifat amfoter sehingga larut dalam NaOH berlebih membentuk [Al(OH)₄]⁻, sedangkan Fe(OH)₃ tidak larut dalam basa berlebih."
        },
        {
            "question": "Cr³⁺ dioksidasi menjadi CrO₄²⁻ menggunakan...",
            "options": ["HCl", "H₂O₂ + NaOH berlebih", "NH₄OH", "H₂SO₄"],
            "correct": 1,
            "explanation": "H₂O₂ dalam suasana basa (NaOH berlebih) mengoksidasi Cr³⁺ dari Cr(OH)₃ menjadi CrO₄²⁻ (kromat) yang larut."
        },
        {
            "question": "Warna larutan [Fe(SCN)]²⁺ adalah...",
            "options": ["Kuning", "Biru", "Merah Darah", "Hijau"],
            "correct": 2,
            "explanation": "[Fe(SCN)]²⁺ menghasilkan warna merah darah yang intens, sangat sensitif bahkan pada konsentrasi rendah."
        },
        {
            "question": "Untuk mengkonfirmasi Cr³⁺, filtrat CrO₄²⁻ ditambahkan...",
            "options": ["KSCN", "K₂CrO₄", "Pb(NO₃)₂", "NH₄OH"],
            "correct": 2,
            "explanation": "Pb(NO₃)₂ bereaksi dengan CrO₄²⁻ membentuk endapan kuning PbCrO₄ yang mengkonfirmasi Cr³⁺."
        },
        {
            "question": "Al(OH)₃ dikonfirmasi dengan cara...",
            "options": [
                "Menambahkan KSCN",
                "Menambahkan HCl perlahan pada filtrat [Al(OH)₄]⁻",
                "Memanaskan dengan NaOH",
                "Menambahkan K₂CrO₄"
            ],
            "correct": 1,
            "explanation": "Penambahan HCl perlahan pada [Al(OH)₄]⁻ akan mengendapkan kembali Al(OH)₃ (putih/gel) ketika pH turun ke titik isoelektrik."
        },
        {
            "question": "Kation mana yang TIDAK termasuk Golongan III?",
            "options": ["Fe³⁺", "Al³⁺", "Cr³⁺", "Ca²⁺"],
            "correct": 3,
            "explanation": "Ca²⁺ termasuk Golongan IV, bukan Golongan III. Golongan III terdiri dari Fe³⁺, Al³⁺, dan Cr³⁺."
        }
    ],
    "Golongan IV": [
        {
            "question": "Reagen pengendap Golongan IV adalah...",
            "options": ["HCl encer", "NH₄OH + NH₄Cl", "(NH₄)₂CO₃ + NH₄OH + NH₄Cl", "NaOH"],
            "correct": 2,
            "explanation": "(NH₄)₂CO₃ mengendapkan Ba²⁺, Sr²⁺, Ca²⁺ sebagai karbonat. NH₄OH + NH₄Cl mencegah MgCO₃ ikut terendap."
        },
        {
            "question": "Semua karbonat Golongan IV (BaCO₃, SrCO₃, CaCO₃) dilarutkan dengan...",
            "options": ["HCl pekat", "NaOH", "CH₃COOH (asam asetat)", "H₂SO₄"],
            "correct": 2,
            "explanation": "Asam asetat (CH₃COOH) digunakan untuk melarutkan karbonat menjadi asetat yang larut, tanpa memasukkan anion pengganggu seperti Cl⁻ atau SO₄²⁻."
        },
        {
            "question": "Bagaimana Ba²⁺ dipisahkan dari Sr²⁺ dan Ca²⁺?",
            "options": [
                "Dengan menambahkan NH₄OH",
                "Dengan menambahkan K₂CrO₄ pada larutan asetat",
                "Dengan pemanasan",
                "Dengan menambahkan NaOH"
            ],
            "correct": 1,
            "explanation": "K₂CrO₄ mengendapkan Ba²⁺ sebagai BaCrO₄ (kuning) di pH netral, sedangkan SrCrO₄ dan CaCrO₄ lebih larut pada kondisi ini."
        },
        {
            "question": "Warna endapan BaCrO₄ adalah...",
            "options": ["Putih", "Kuning", "Merah", "Hitam"],
            "correct": 1,
            "explanation": "BaCrO₄ adalah endapan berwarna kuning yang mengkonfirmasi keberadaan Ba²⁺."
        },
        {
            "question": "Reagen apa yang digunakan untuk memisahkan Sr²⁺ dari Ca²⁺?",
            "options": ["K₂CrO₄", "(NH₄)₂CO₃", "(NH₄)₂SO₄", "(NH₄)₂C₂O₄"],
            "correct": 2,
            "explanation": "(NH₄)₂SO₄ mengendapkan SrSO₄ (putih) sedangkan CaSO₄ lebih larut, sehingga Ca²⁺ tetap dalam larutan."
        },
        {
            "question": "Cara mengkonfirmasi Ca²⁺ adalah dengan menambahkan...",
            "options": ["K₂CrO₄", "(NH₄)₂SO₄", "(NH₄)₂C₂O₄", "KSCN"],
            "correct": 2,
            "explanation": "(NH₄)₂C₂O₄ (ammonium oksalat) mengendapkan Ca²⁺ sebagai CaC₂O₄ (putih) yang mengkonfirmasi keberadaan Ca²⁺."
        },
        {
            "question": "Mengapa NH₄Cl ditambahkan dalam pengendapan Golongan IV?",
            "options": [
                "Mengoksidasi kation",
                "Mencegah pengendapan MgCO₃",
                "Melarutkan endapan",
                "Menaikkan pH"
            ],
            "correct": 1,
            "explanation": "NH₄Cl menekan konsentrasi CO₃²⁻ melalui efek ion bersama pada NH₃/NH₄⁺, sehingga MgCO₃ tidak terendap karena Ksp-nya lebih besar dari hasil kali ion."
        },
        {
            "question": "Warna endapan SrSO₄ adalah...",
            "options": ["Kuning", "Merah", "Putih", "Abu-abu"],
            "correct": 2,
            "explanation": "SrSO₄ membentuk endapan berwarna putih saat Sr²⁺ bereaksi dengan SO₄²⁻."
        },
        {
            "question": "Kation mana yang TIDAK termasuk Golongan IV?",
            "options": ["Ba²⁺", "Sr²⁺", "Ca²⁺", "Fe³⁺"],
            "correct": 3,
            "explanation": "Fe³⁺ termasuk Golongan III, bukan Golongan IV. Golongan IV terdiri dari Ba²⁺, Sr²⁺, dan Ca²⁺."
        },
        {
            "question": "Warna endapan CaC₂O₄ adalah...",
            "options": ["Kuning", "Putih", "Merah", "Biru"],
            "correct": 1,
            "explanation": "CaC₂O₄ (kalsium oksalat) membentuk endapan putih yang mengkonfirmasi Ca²⁺."
        }
    ]
}

def get_random_questions(group, n=10):
    questions = quiz_questions.get(group, [])
    if len(questions) <= n:
        return random.sample(questions, len(questions))
    return random.sample(questions, n)

# ============================================
# DIGITALISASI KIMIA - LOGIC
# ============================================

CATION_PROFILES = {
    "Ag⁺": {
        "group": "I",
        "reactions": [
            "Ag⁺ + Cl⁻ → AgCl↓ (Putih)",
            "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻",
            "[Ag(NH₃)₂]⁺ + 2H⁺ + Cl⁻ → AgCl↓ (Putih) + 2NH₄⁺"
        ],
        "confirmasi": "Endapan putih AgCl → larut dalam NH₄OH → endapan putih kembali dengan HNO₃",
        "warna_endapan": "Putih",
        "icon": "🥈"
    },
    "Pb²⁺": {
        "group": "I",
        "reactions": [
            "Pb²⁺ + 2Cl⁻ → PbCl₂↓ (Putih)",
            "PbCl₂ → Pb²⁺ + 2Cl⁻  (larut dalam H₂O panas)",
            "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (Kuning)"
        ],
        "confirmasi": "Endapan kuning PbCrO₄ setelah penambahan K₂CrO₄",
        "warna_endapan": "Kuning",
        "icon": "🟡"
    },
    "Hg₂²⁺": {
        "group": "I",
        "reactions": [
            "Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓ (Putih)",
            "Hg₂Cl₂ + 2NH₃ → Hg↓ (Hitam) + Hg(NH₂)Cl↓ (Putih) + NH₄⁺ + Cl⁻"
        ],
        "confirmasi": "Endapan hitam Hg dan putih Hg(NH₂)Cl saat ditambahkan NH₄OH",
        "warna_endapan": "Hitam + Putih",
        "icon": "⚫"
    },
    "Fe³⁺": {
        "group": "III",
        "reactions": [
            "Fe³⁺ + 3OH⁻ → Fe(OH)₃↓ (Coklat)",
            "Fe(OH)₃ + 3HCl → FeCl₃ + 3H₂O",
            "Fe³⁺ + SCN⁻ → [Fe(SCN)]²⁺ (Merah Darah)"
        ],
        "confirmasi": "Warna merah darah [Fe(SCN)]²⁺ dengan KSCN",
        "warna_endapan": "Coklat/Merah",
        "icon": "🟤"
    },
    "Al³⁺": {
        "group": "III",
        "reactions": [
            "Al³⁺ + 3OH⁻ → Al(OH)₃↓ (Putih/Gel)",
            "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻  (larut dalam NaOH berlebih)",
            "[Al(OH)₄]⁻ + H⁺ → Al(OH)₃↓ (Putih)"
        ],
        "confirmasi": "Endapan putih/gel Al(OH)₃ yang larut dalam NaOH berlebih dan mengendap kembali dengan asam",
        "warna_endapan": "Putih/Gel",
        "icon": "⚪"
    },
    "Cr³⁺": {
        "group": "III",
        "reactions": [
            "Cr³⁺ + 3OH⁻ → Cr(OH)₃↓ (Abu-abu/Hijau)",
            "2Cr(OH)₃ + 3H₂O₂ + 4OH⁻ → 2CrO₄²⁻ + 8H₂O",
            "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (Kuning)"
        ],
        "confirmasi": "Endapan kuning PbCrO₄ setelah oksidasi Cr(OH)₃ dengan H₂O₂/NaOH",
        "warna_endapan": "Abu-abu/Hijau → Kuning (PbCrO₄)",
        "icon": "🟢"
    },
    "Ba²⁺": {
        "group": "IV",
        "reactions": [
            "Ba²⁺ + CO₃²⁻ → BaCO₃↓ (Putih)",
            "BaCO₃ + 2CH₃COOH → Ba²⁺ + 2CH₃COO⁻ + H₂O + CO₂",
            "Ba²⁺ + CrO₄²⁻ → BaCrO₄↓ (Kuning)"
        ],
        "confirmasi": "Endapan kuning BaCrO₄ dengan K₂CrO₄ pada suasana netral/asetat",
        "warna_endapan": "Kuning",
        "icon": "🟨"
    },
    "Sr²⁺": {
        "group": "IV",
        "reactions": [
            "Sr²⁺ + CO₃²⁻ → SrCO₃↓ (Putih)",
            "SrCO₃ + 2CH₃COOH → Sr²⁺ + 2CH₃COO⁻ + H₂O + CO₂",
            "Sr²⁺ + SO₄²⁻ → SrSO₄↓ (Putih)"
        ],
        "confirmasi": "Endapan putih SrSO₄ dengan (NH₄)₂SO₄",
        "warna_endapan": "Putih",
        "icon": "🔲"
    },
    "Ca²⁺": {
        "group": "IV",
        "reactions": [
            "Ca²⁺ + CO₃²⁻ → CaCO₃↓ (Putih)",
            "CaCO₃ + 2CH₃COOH → Ca²⁺ + 2CH₃COO⁻ + H₂O + CO₂",
            "Ca²⁺ + C₂O₄²⁻ → CaC₂O₄↓ (Putih)"
        ],
        "confirmasi": "Endapan putih CaC₂O₄ dengan (NH₄)₂C₂O₄",
        "warna_endapan": "Putih",
        "icon": "⬜"
    }
}

# Decision tree questions
DIG_QUESTIONS = [
    {
        "id": "q1",
        "text": "Apakah terbentuk endapan putih saat sampel ditambahkan HCl encer?",
        "yes": "q2",
        "no": "q_g3_start",
        "hint": "Kation Golongan I (Ag⁺, Pb²⁺, Hg₂²⁺) membentuk garam klorida tidak larut."
    },
    {
        "id": "q2",
        "text": "Apakah sebagian endapan larut saat dipanaskan dengan air panas?",
        "yes": "q3",
        "no": "q4",
        "hint": "PbCl₂ larut dalam air panas karena kelarutannya meningkat dengan suhu."
    },
    {
        "id": "q3",
        "text": "Apakah filtrat (air panas) membentuk endapan kuning saat ditambahkan K₂CrO₄?",
        "yes": "confirm_Pb",
        "no": "q4",
        "hint": "PbCrO₄ berwarna kuning — tanda khas Pb²⁺."
    },
    {
        "id": "q4",
        "text": "Apakah endapan yang tidak larut dalam air panas berubah menjadi hitam saat ditambahkan NH₄OH?",
        "yes": "confirm_Hg",
        "no": "q5",
        "hint": "Hg₂Cl₂ mengalami disproporsionasi dengan NH₄OH: Hg⁰ (hitam) + Hg(NH₂)Cl (putih)."
    },
    {
        "id": "q5",
        "text": "Apakah endapan larut dalam NH₄OH dan terbentuk endapan putih kembali saat ditambahkan HNO₃?",
        "yes": "confirm_Ag",
        "no": "q_g3_start",
        "hint": "AgCl larut dalam NH₄OH membentuk [Ag(NH₃)₂]⁺, lalu mengendap kembali dengan asam."
    },
    {
        "id": "q_g3_start",
        "text": "Apakah terbentuk endapan (coklat/putih/abu-abu) saat sampel ditambahkan NH₄OH + NH₄Cl?",
        "yes": "q_g3_1",
        "no": "q_g4_start",
        "hint": "Fe(OH)₃ (coklat), Al(OH)₃ (putih), Cr(OH)₃ (abu-abu/hijau) menandakan Golongan III."
    },
    {
        "id": "q_g3_1",
        "text": "Apakah terbentuk warna merah darah saat endapan dilarutkan HCl lalu ditambahkan KSCN?",
        "yes": "confirm_Fe",
        "no": "q_g3_2",
        "hint": "[Fe(SCN)]²⁺ berwarna merah darah — sangat sensitif untuk Fe³⁺."
    },
    {
        "id": "q_g3_2",
        "text": "Apakah endapan larut dalam NaOH berlebih + H₂O₂ dan terbentuk endapan putih/gel saat filtrat diasamkan?",
        "yes": "confirm_Al",
        "no": "q_g3_3",
        "hint": "Al(OH)₃ bersifat amfoter — larut dalam basa berlebih → [Al(OH)₄]⁻, mengendap kembali saat diasamkan."
    },
    {
        "id": "q_g3_3",
        "text": "Apakah filtrat berwarna kuning/jingga (CrO₄²⁻) dan membentuk endapan kuning dengan Pb(NO₃)₂?",
        "yes": "confirm_Cr",
        "no": "q_g4_start",
        "hint": "CrO₄²⁻ berwarna kuning dan membentuk PbCrO₄ (kuning) dengan Pb(NO₃)₂."
    },
    {
        "id": "q_g4_start",
        "text": "Apakah terbentuk endapan putih saat sampel ditambahkan (NH₄)₂CO₃ + NH₄OH + NH₄Cl?",
        "yes": "q_g4_1",
        "no": "no_match",
        "hint": "BaCO₃, SrCO₃, CaCO₃ semuanya berwarna putih — khas Golongan IV."
    },
    {
        "id": "q_g4_1",
        "text": "Setelah dilarutkan dengan CH₃COOH, apakah terbentuk endapan kuning dengan K₂CrO₄?",
        "yes": "confirm_Ba",
        "no": "q_g4_2",
        "hint": "BaCrO₄ berwarna kuning — mengkonfirmasi Ba²⁺."
    },
    {
        "id": "q_g4_2",
        "text": "Apakah terbentuk endapan putih dengan (NH₄)₂SO₄?",
        "yes": "confirm_Sr",
        "no": "q_g4_3",
        "hint": "SrSO₄ berwarna putih — mengkonfirmasi Sr²⁺."
    },
    {
        "id": "q_g4_3",
        "text": "Apakah terbentuk endapan putih dengan (NH₄)₂C₂O₄?",
        "yes": "confirm_Ca",
        "no": "no_match",
        "hint": "CaC₂O₄ (putih) mengkonfirmasi Ca²⁺."
    }
]

DIG_Q_MAP = {q["id"]: q for q in DIG_QUESTIONS}

def render_digitalisasi():
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"
    card   = "#1e2130" if dm else "#ffffff"
    border = "#2d3561" if dm else "#d0d9f0"
    green  = "#56cf86" if dm else "#1a9e56"
    yellow = "#ffd93d" if dm else "#b8860b"
    red    = "#ff6b6b" if dm else "#d32f2f"

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,{'#1a1d27' if dm else '#dde8ff'} 0%,{'#0f1117' if dm else '#f4f6fb'} 100%);
        border:2px solid {border}; border-radius:20px; padding:2rem; margin-bottom:1.5rem;">
        <h1 style="color:{accent};font-family:'Playfair Display',serif;font-size:2rem;margin:0 0 0.4rem 0;">
            🔍 Digitalisasi Analisis Kation
        </h1>
        <p style="color:{text};opacity:0.7;margin:0;">
            Jawab serangkaian pertanyaan berdasarkan observasi lab untuk mengidentifikasi kation yang ada dalam sampel Anda.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Init state
    if "dig_current" not in st.session_state:
        st.session_state.dig_current = "q1"
        st.session_state.dig_history = []
        st.session_state.dig_result  = None

    # Reset button
    col_r, col_s = st.columns([8, 2])
    with col_s:
        if st.button("🔄 Reset", use_container_width=True):
            st.session_state.dig_current = "q1"
            st.session_state.dig_history = []
            st.session_state.dig_result  = None
            st.rerun()

    # History path
    if st.session_state.dig_history:
        path_text = " → ".join([
            f"{'✅' if a else '❌'} {DIG_Q_MAP[q]['text'][:40]}..." 
            for q, a in st.session_state.dig_history
        ])
        st.markdown(f"""
        <div style="background:{'rgba(92,124,250,0.1)' if dm else 'rgba(58,91,217,0.06)'};
            border:1px solid {border}; border-radius:12px; padding:0.8rem 1rem;
            margin-bottom:1rem; font-size:0.8rem; color:{text}; opacity:0.8; line-height:1.8;">
            <strong>Jejak Analisis:</strong><br>{path_text}
        </div>
        """, unsafe_allow_html=True)

    # Show result
    if st.session_state.dig_result:
        result_key = st.session_state.dig_result

        if result_key == "no_match":
            st.markdown(f"""
            <div style="background:{'rgba(255,107,107,0.15)' if dm else 'rgba(211,47,47,0.08)'};
                border:2px solid {red}; border-radius:16px; padding:2rem; text-align:center;">
                <h2 style="color:{red};">⚠️ Kation Tidak Teridentifikasi</h2>
                <p style="color:{text};">Berdasarkan jawaban Anda, kation tidak dapat diidentifikasi dalam Golongan I, III, atau IV.<br>
                Kemungkinan sampel mengandung kation Golongan II atau V, atau terdapat kesalahan prosedur.</p>
            </div>
            """, unsafe_allow_html=True)
            return

        ion_key = result_key.replace("confirm_", "")
        # Map key to actual ion symbol
        ion_map = {
            "Pb": "Pb²⁺", "Ag": "Ag⁺", "Hg": "Hg₂²⁺",
            "Fe": "Fe³⁺", "Al": "Al³⁺", "Cr": "Cr³⁺",
            "Ba": "Ba²⁺", "Sr": "Sr²⁺", "Ca": "Ca²⁺"
        }
        ion = ion_map.get(ion_key, ion_key)
        profile = CATION_PROFILES.get(ion, {})
        grp = profile.get("group", "?")
        grp_colors = {"I": red, "III": "#4ecdc4" if dm else "#00796b", "IV": yellow}
        gc = grp_colors.get(grp, accent)

        st.markdown(f"""
        <div style="background:{card}; border:2px solid {gc};
            border-radius:20px; padding:2rem; margin:1rem 0; text-align:center;">
            <div style="font-size:3.5rem;">{profile.get('icon','⚗️')}</div>
            <h2 style="color:{gc}; font-family:'Playfair Display',serif; font-size:2.2rem; margin:0.5rem 0;">
                {ion}
            </h2>
            <div style="display:inline-block; background:{gc}20; border:1px solid {gc};
                border-radius:20px; padding:4px 18px; margin-bottom:1rem;">
                <span style="color:{gc}; font-weight:600; font-size:0.9rem;">Golongan {grp}</span>
            </div>
            <p style="color:{text}; margin:0;">
                <strong>Warna Endapan:</strong> {profile.get('warna_endapan','—')}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### ⚗️ Reaksi Kimia yang Terjadi")
        for rxn in profile.get("reactions", []):
            st.markdown(f"""
            <div style="background:{'rgba(92,124,250,0.08)' if dm else 'rgba(58,91,217,0.05)'};
                border-left:4px solid {accent}; border-radius:8px;
                padding:0.8rem 1.2rem; margin:0.4rem 0;
                font-family:'JetBrains Mono',monospace; font-size:0.92rem; color:{text};">
                {rxn}
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:{'rgba(86,207,134,0.12)' if dm else 'rgba(26,158,86,0.08)'};
            border:1.5px solid {green}; border-radius:12px;
            padding:1rem 1.2rem; margin-top:1rem; color:{text};">
            <strong style="color:{green};">✅ Konfirmasi:</strong> {profile.get('confirmasi','—')}
        </div>
        """, unsafe_allow_html=True)

        # Prosedur lengkap
        grp_full = {"I": "Golongan I", "III": "Golongan III", "IV": "Golongan IV"}.get(grp, "")
        if grp_full in cation_data:
            with st.expander("📋 Lihat Prosedur Analisis Lengkap Golongan " + grp):
                for i, step in enumerate(cation_data[grp_full]["steps"], 1):
                    st.markdown(f"""
                    <div style="display:flex; align-items:flex-start; gap:10px; margin:8px 0;">
                        <div style="background:{accent}; color:#fff; width:26px; height:26px;
                            border-radius:50%; display:flex; align-items:center; justify-content:center;
                            font-size:0.78rem; font-weight:700; flex-shrink:0;">{i}</div>
                        <div style="background:{'rgba(92,124,250,0.08)' if dm else '#f0f4ff'};
                            border-radius:10px; padding:0.7rem 1rem; flex:1; color:{text};">
                            <strong>{step['action']}</strong><br>
                            <span style="opacity:0.85;">{step['result']}</span>
                            {f"<br><span style='color:{green};'>✅ {step['confirm']}</span>" if 'confirm' in step else ''}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        return

    # Current question
    curr_id = st.session_state.dig_current
    if curr_id not in DIG_Q_MAP:
        return

    q = DIG_Q_MAP[curr_id]
    total_q = len(DIG_QUESTIONS)
    answered = len(st.session_state.dig_history)
    progress = answered / total_q

    st.progress(progress)
    st.markdown(f"<p style='color:{text};opacity:0.6;font-size:0.85rem;'>Pertanyaan {answered+1} dari ~{total_q}</p>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{card}; border:2px solid {accent};
        border-radius:16px; padding:1.5rem 2rem; margin:1rem 0;">
        <p style="color:{accent}; font-size:0.82rem; font-weight:600; margin:0 0 0.5rem 0; text-transform:uppercase; letter-spacing:1px;">
            OBSERVASI LAB
        </p>
        <h3 style="color:{text}; font-size:1.2rem; margin:0 0 1rem 0;">{q['text']}</h3>
        <div style="background:{'rgba(255,140,66,0.12)' if dm else 'rgba(224,92,0,0.07)'};
            border-left:3px solid {'#ff8c42' if dm else '#e05c00'};
            border-radius:6px; padding:0.6rem 1rem; font-size:0.85rem; color:{text}; opacity:0.85;">
            💡 <em>{q['hint']}</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("✅  Ya — Teramati", use_container_width=True, key=f"yes_{curr_id}"):
            st.session_state.dig_history.append((curr_id, True))
            nxt = q["yes"]
            if nxt.startswith("confirm_") or nxt == "no_match":
                st.session_state.dig_result = nxt
            else:
                st.session_state.dig_current = nxt
            st.rerun()
    with col_no:
        if st.button("❌  Tidak — Tidak Teramati", use_container_width=True, key=f"no_{curr_id}"):
            st.session_state.dig_history.append((curr_id, False))
            nxt = q["no"]
            if nxt.startswith("confirm_") or nxt == "no_match":
                st.session_state.dig_result = nxt
            else:
                st.session_state.dig_current = nxt
            st.rerun()

# ============================================
# SIDEBAR
# ============================================

st.sidebar.markdown("## ⚗️ Analisis Kation")

# Theme toggle
dm = st.session_state.dark_mode
mode_label = "🌙 Mode Gelap" if dm else "☀️ Mode Terang"
st.sidebar.markdown(f'<div class="theme-status">{mode_label} aktif</div>', unsafe_allow_html=True)
if st.sidebar.button("🔄 Ganti Tema", use_container_width=True):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Menu")

page = st.sidebar.radio(
    "Navigasi:",
    ["🏠 Beranda", "🔍 Digitalisasi Kimia", "📊 Bagan Analisis", "🔬 Detail Reaksi", "📝 Kuis", "📚 Referensi"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="font-size:0.8rem; opacity:0.6; line-height:1.6;">
Mencakup Golongan I, III, dan IV<br>
Versi 3.0 | 2026
</div>
""", unsafe_allow_html=True)

# ============================================
# HALAMAN: BERANDA
# ============================================

if page == "🏠 Beranda":
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"
    card   = "#1e2130" if dm else "#ffffff"
    border = "#2d3561" if dm else "#d0d9f0"

    st.markdown("""
    <div class="main-header">
        <h1>⚗️ Analisis Kation<br>Golongan I, III, IV</h1>
        <p>Sistem pembelajaran kimia analitik berbasis web — interaktif & komprehensif</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown(f"""
        <div class="cation-card">
            <h3 style="color:{accent};">🔬 Kation yang Dianalisis</h3>
            <table class="styled-table">
                <tr>
                    <th>Golongan</th>
                    <th>Kation</th>
                    <th>Reagen Pengendap</th>
                    <th>Endapan</th>
                </tr>
                <tr>
                    <td><span class="badge badge-I">I</span></td>
                    <td><span class="mono">Ag⁺, Pb²⁺, Hg₂²⁺</span></td>
                    <td>HCl encer</td>
                    <td class="p-white">Putih</td>
                </tr>
                <tr>
                    <td><span class="badge badge-III">III</span></td>
                    <td><span class="mono">Fe³⁺, Al³⁺, Cr³⁺</span></td>
                    <td>NH₄OH + NH₄Cl</td>
                    <td class="p-brown">Coklat/Putih/Abu²</td>
                </tr>
                <tr>
                    <td><span class="badge badge-IV">IV</span></td>
                    <td><span class="mono">Ba²⁺, Sr²⁺, Ca²⁺</span></td>
                    <td>(NH₄)₂CO₃ + NH₄OH + NH₄Cl</td>
                    <td class="p-white">Putih</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="warning-box">
            <strong>⚠️ Catatan:</strong> Golongan II dan V <strong>tidak dibahas</strong> dalam aplikasi ini.
            Golongan II (Cu²⁺, Cd²⁺, Bi³⁺, Hg²⁺, Sn²⁺, Sb³⁺, As³⁺) dilewati, 
            dan Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺) tidak tercakup dalam analisis ini.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        features = [
            ("🔍", "Digitalisasi Kimia", "Identifikasi kation secara interaktif melalui tanya-jawab berbasis observasi lab"),
            ("📊", "Bagan Analisis", "Visualisasi alur analisis dari sampel hingga konfirmasi kation"),
            ("🔬", "Detail Reaksi", "Penjelasan step-by-step setiap reaksi kimia"),
            ("📝", "Kuis Interaktif", "Uji pemahaman dengan 10 soal acak per golongan"),
            ("📚", "Referensi", "Tabel warna endapan dan rangkuman reaksi lengkap"),
        ]
        for icon, title, desc in features:
            st.markdown(f"""
            <div class="cation-card" style="padding:1rem 1.2rem; margin:0.5rem 0;">
                <div style="display:flex; align-items:flex-start; gap:12px;">
                    <span style="font-size:1.4rem;">{icon}</span>
                    <div>
                        <strong style="color:{accent};">{title}</strong>
                        <p style="margin:0.2rem 0 0 0; font-size:0.87rem; color:{text}; opacity:0.8;">{desc}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ============================================
# HALAMAN: DIGITALISASI KIMIA
# ============================================

elif page == "🔍 Digitalisasi Kimia":
    render_digitalisasi()

# ============================================
# HALAMAN: BAGAN ANALISIS
# ============================================

elif page == "📊 Bagan Analisis":
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"
    card   = "#1e2130" if dm else "#ffffff"
    border = "#2d3561" if dm else "#d0d9f0"
    bg     = "#151825" if dm else "#f0f4ff"

    st.markdown("""
    <div class="main-header">
        <h1>📊 Bagan Alur Analisis Kation</h1>
        <p>Alur sistematis dari sampel hingga identifikasi kation</p>
    </div>
    """, unsafe_allow_html=True)

    def flow_node(label, color, shape="box", note=""):
        return f"""
        <div style="background:{color}20; border:2px solid {color}; border-radius:12px;
            padding:10px 16px; text-align:center; margin:4px auto; max-width:280px;
            color:{text}; font-size:0.88rem; font-weight:600; line-height:1.4;">
            {label}
            {f'<div style="font-size:0.75rem; opacity:0.7; font-weight:400; margin-top:4px;">{note}</div>' if note else ''}
        </div>
        """

    def arrow(label=""):
        return f"""
        <div style="text-align:center; color:{text}; opacity:0.5; font-size:1.2rem; margin:2px 0;">
            ↓{f' <span style="font-size:0.78rem;">{label}</span>' if label else ''}
        </div>
        """

    def branch_label(txt, color):
        return f'<div style="text-align:center; color:{color}; font-size:0.78rem; font-weight:600; margin:2px 0;">{txt}</div>'

    # === GOLONGAN I ===
    st.markdown(f"### <span class='badge badge-I'>Golongan I</span>", unsafe_allow_html=True)

    st.markdown(flow_node("🧪 SAMPEL<br>Ag⁺, Pb²⁺, Hg₂²⁺, Fe³⁺, Al³⁺, Cr³⁺, Ba²⁺, Sr²⁺, Ca²⁺", accent), unsafe_allow_html=True)
    st.markdown(arrow("+ HCl encer"), unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(flow_node("⬇️ Endapan Putih<br>AgCl, PbCl₂, Hg₂Cl₂", "#FF6B6B", note="GOLONGAN I"), unsafe_allow_html=True)
        st.markdown(arrow("+ H₂O panas"), unsafe_allow_html=True)
        ca, cb = st.columns(2)
        with ca:
            st.markdown(flow_node("Filtrat: Pb²⁺<br>(larut)", "#FFD93D"), unsafe_allow_html=True)
            st.markdown(arrow("+ K₂CrO₄"), unsafe_allow_html=True)
            st.markdown(flow_node("🟡 PbCrO₄↓<br>Kuning → Pb²⁺ ✅", "#FFD93D"), unsafe_allow_html=True)
        with cb:
            st.markdown(flow_node("Residu: AgCl,<br>Hg₂Cl₂", "#9E9E9E"), unsafe_allow_html=True)
            st.markdown(arrow("+ NH₄OH"), unsafe_allow_html=True)
            caa, cab = st.columns(2)
            with caa:
                st.markdown(flow_node("[Ag(NH₃)₂]⁺<br>(larut)", "#4ECDC4"), unsafe_allow_html=True)
                st.markdown(arrow("+ HNO₃"), unsafe_allow_html=True)
                st.markdown(flow_node("⚪ AgCl↓<br>Putih → Ag⁺ ✅", "#9E9E9E"), unsafe_allow_html=True)
            with cab:
                st.markdown(flow_node("⚫ Hg↓ + Hg(NH₂)Cl<br>Hitam+Putih → Hg₂²⁺ ✅", "#616161"), unsafe_allow_html=True)
    with c2:
        st.markdown(flow_node("→ Filtrat<br>ke Golongan III", border, note="(skip Gol. II)"), unsafe_allow_html=True)

    st.markdown("---")

    # === GOLONGAN III ===
    st.markdown(f"### <span class='badge badge-III'>Golongan III</span>", unsafe_allow_html=True)
    st.markdown(flow_node("Filtrat dari Gol. I<br>Fe³⁺, Al³⁺, Cr³⁺, Ba²⁺, Sr²⁺, Ca²⁺", "#4ECDC4"), unsafe_allow_html=True)
    st.markdown(arrow("+ NH₄OH + NH₄Cl"), unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(flow_node("⬇️ Endapan<br>Fe(OH)₃ (Coklat)<br>Al(OH)₃ (Putih/Gel)<br>Cr(OH)₃ (Abu-abu)", "#4ECDC4", note="GOLONGAN III"), unsafe_allow_html=True)
        st.markdown(arrow("+ NaOH berlebih + H₂O₂"), unsafe_allow_html=True)
        ca, cb = st.columns(2)
        with ca:
            st.markdown(flow_node("Residu: Fe(OH)₃<br>(tidak larut)", "#8D6E63"), unsafe_allow_html=True)
            st.markdown(arrow("+ HCl + KSCN"), unsafe_allow_html=True)
            st.markdown(flow_node("🔴 [Fe(SCN)]²⁺<br>Merah Darah → Fe³⁺ ✅", "#F44336"), unsafe_allow_html=True)
        with cb:
            st.markdown(flow_node("Filtrat: [Al(OH)₄]⁻<br>+ CrO₄²⁻", "#C8E6C9"), unsafe_allow_html=True)
            caa, cab = st.columns(2)
            with caa:
                st.markdown(arrow("+ HCl perlahan"), unsafe_allow_html=True)
                st.markdown(flow_node("⚪ Al(OH)₃↓<br>Putih/Gel → Al³⁺ ✅", "#E0E0E0"), unsafe_allow_html=True)
            with cab:
                st.markdown(arrow("+ Pb(NO₃)₂"), unsafe_allow_html=True)
                st.markdown(flow_node("🟡 PbCrO₄↓<br>Kuning → Cr³⁺ ✅", "#FFD93D"), unsafe_allow_html=True)
    with c2:
        st.markdown(flow_node("→ Filtrat<br>ke Golongan IV", border, note="Ba²⁺, Sr²⁺, Ca²⁺"), unsafe_allow_html=True)

    st.markdown("---")

    # === GOLONGAN IV ===
    st.markdown(f"### <span class='badge badge-IV'>Golongan IV</span>", unsafe_allow_html=True)
    st.markdown(flow_node("Filtrat dari Gol. III<br>Ba²⁺, Sr²⁺, Ca²⁺", "#FFD93D"), unsafe_allow_html=True)
    st.markdown(arrow("+ (NH₄)₂CO₃ + NH₄OH + NH₄Cl"), unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(flow_node("⬇️ Endapan Putih<br>BaCO₃, SrCO₃, CaCO₃", "#FFD93D", note="GOLONGAN IV"), unsafe_allow_html=True)
        st.markdown(arrow("+ CH₃COOH (larutkan)"), unsafe_allow_html=True)
        st.markdown(flow_node("Ba²⁺, Sr²⁺, Ca²⁺<br>(larutan asetat)", "#FFF9C4"), unsafe_allow_html=True)
        st.markdown(arrow("+ K₂CrO₄"), unsafe_allow_html=True)
        ca, cb = st.columns(2)
        with ca:
            st.markdown(flow_node("🟡 BaCrO₄↓<br>Kuning → Ba²⁺ ✅", "#FFD93D"), unsafe_allow_html=True)
        with cb:
            st.markdown(flow_node("Filtrat: Sr²⁺, Ca²⁺", "#FFF9C4"), unsafe_allow_html=True)
            st.markdown(arrow("+ (NH₄)₂SO₄"), unsafe_allow_html=True)
            caa, cab = st.columns(2)
            with caa:
                st.markdown(flow_node("⚪ SrSO₄↓<br>Putih → Sr²⁺ ✅", "#E0E0E0"), unsafe_allow_html=True)
            with cab:
                st.markdown(flow_node("Filtrat: Ca²⁺", "#FFF9C4"), unsafe_allow_html=True)
                st.markdown(arrow("+ (NH₄)₂C₂O₄"), unsafe_allow_html=True)
                st.markdown(flow_node("⚪ CaC₂O₄↓<br>Putih → Ca²⁺ ✅", "#E0E0E0"), unsafe_allow_html=True)
    with c2:
        st.markdown(flow_node("→ Filtrat Golongan V<br>(tidak dianalisis)", border), unsafe_allow_html=True)

# ============================================
# HALAMAN: DETAIL REAKSI
# ============================================

elif page == "🔬 Detail Reaksi":
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"

    st.markdown("""
    <div class="main-header">
        <h1>🔬 Detail Reaksi Analisis</h1>
        <p>Penjelasan langkah-demi-langkah setiap reaksi kimia</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        "⬛ Golongan I  (Ag⁺, Pb²⁺, Hg₂²⁺)",
        "🟦 Golongan III  (Fe³⁺, Al³⁺, Cr³⁺)",
        "🟨 Golongan IV  (Ba²⁺, Sr²⁺, Ca²⁺)"
    ])

    def render_steps(group_key, rxns_html):
        st.markdown(rxns_html, unsafe_allow_html=True)
        for i, step in enumerate(cation_data[group_key]["steps"], 1):
            with st.expander(f"Langkah {i}: {step['action']}"):
                confirm_html = f'<div class="success-box" style="margin-top:8px;"><strong>✅ Konfirmasi:</strong> {step["confirm"]}</div>' if 'confirm' in step else ''
                filtrate_html = f'<p style="color:{text};"><strong>Filtrat:</strong> {step["filtrate"]}</p>' if 'filtrate' in step else ''
                residue_html  = f'<p style="color:{text};"><strong>Residu:</strong> {step["residue"]}</p>' if 'residue' in step else ''
                st.markdown(f"""
                <div class="reaction-box">
                    <p style="color:{text};"><strong>Aksi:</strong> {step['action']}</p>
                    <p style="color:{text};"><strong>Hasil:</strong> {step['result']}</p>
                    {filtrate_html}{residue_html}
                </div>
                {confirm_html}
                """, unsafe_allow_html=True)

    with tab1:
        render_steps("Golongan I", f"""
        <div class="cation-card">
            <h3 style="color:{accent};">🧪 Reagen: HCl encer</h3>
            <ul style="color:{st.session_state.dark_mode and '#e8eaf6' or '#1a1a2e'};">
                <li>Ag⁺ + Cl⁻ → <span class="p-white">AgCl↓ (Putih)</span></li>
                <li>Pb²⁺ + 2Cl⁻ → <span class="p-white">PbCl₂↓ (Putih)</span></li>
                <li>Hg₂²⁺ + 2Cl⁻ → <span class="p-white">Hg₂Cl₂↓ (Putih)</span></li>
            </ul>
        </div>
        """)

    with tab2:
        render_steps("Golongan III", f"""
        <div class="cation-card">
            <h3 style="color:{accent};">🧪 Reagen: NH₄OH + NH₄Cl</h3>
            <ul style="color:{st.session_state.dark_mode and '#e8eaf6' or '#1a1a2e'};">
                <li>Fe³⁺ + 3OH⁻ → <span class="p-brown">Fe(OH)₃↓ (Coklat/Merah)</span></li>
                <li>Al³⁺ + 3OH⁻ → <span class="p-white">Al(OH)₃↓ (Putih/Gel)</span></li>
                <li>Cr³⁺ + 3OH⁻ → <span class="p-green">Cr(OH)₃↓ (Abu-abu/Hijau)</span></li>
            </ul>
            <div class="info-box">⚠️ <strong>NH₄Cl</strong> berfungsi sebagai penyangga untuk menekan [OH⁻] agar Mg²⁺ tidak terendap.</div>
        </div>
        """)

    with tab3:
        render_steps("Golongan IV", f"""
        <div class="cation-card">
            <h3 style="color:{accent};">🧪 Reagen: (NH₄)₂CO₃ + NH₄OH + NH₄Cl</h3>
            <ul style="color:{st.session_state.dark_mode and '#e8eaf6' or '#1a1a2e'};">
                <li>Ba²⁺ + CO₃²⁻ → <span class="p-white">BaCO₃↓ (Putih)</span></li>
                <li>Sr²⁺ + CO₃²⁻ → <span class="p-white">SrCO₃↓ (Putih)</span></li>
                <li>Ca²⁺ + CO₃²⁻ → <span class="p-white">CaCO₃↓ (Putih)</span></li>
            </ul>
            <div class="info-box">💡 <strong>NH₄Cl</strong> mencegah pengendapan MgCO₃ yang tidak diinginkan.</div>
        </div>
        """)

# ============================================
# HALAMAN: KUIS
# ============================================

elif page == "📝 Kuis":
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"
    green  = "#56cf86" if dm else "#1a9e56"
    red    = "#ff6b6b" if dm else "#d32f2f"

    st.markdown("""
    <div class="main-header">
        <h1>📝 Kuis Analisis Kation</h1>
        <p>Uji pemahaman Anda — 10 soal acak per golongan</p>
    </div>
    """, unsafe_allow_html=True)

    selected_group = st.selectbox(
        "Pilih Golongan:",
        ["Golongan I", "Golongan III", "Golongan IV"]
    )

    quiz_key = f"quiz_state_{selected_group.replace(' ', '_')}"

    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = {
            'current_question': 0,
            'score': 0,
            'answered': False,
            'selected_option': None,
            'shuffled_questions': get_random_questions(selected_group, 10)
        }

    state = st.session_state[quiz_key]
    quiz_list = state['shuffled_questions']

    progress = state['current_question'] / len(quiz_list)
    st.progress(progress)
    st.markdown(f"<p style='color:{text};font-size:0.9rem;'>Soal {state['current_question']+1} dari {len(quiz_list)} &nbsp;|&nbsp; Skor: <strong>{state['score']}</strong></p>", unsafe_allow_html=True)

    if state['current_question'] < len(quiz_list):
        q = quiz_list[state['current_question']]

        st.markdown(f"""
        <div class="q-box">
            <h3>{q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        for i, option in enumerate(q['options']):
            if not state['answered']:
                if st.button(f"{chr(65+i)}.  {option}", key=f"opt_{selected_group}_{i}_{state['current_question']}", use_container_width=True):
                    state['answered'] = True
                    state['selected_option'] = i
                    if i == q['correct']:
                        state['score'] += 1
                    st.rerun()
            else:
                if i == q['correct']:
                    st.markdown(f'<div class="quiz-option correct">✅ {chr(65+i)}.  {option}</div>', unsafe_allow_html=True)
                elif i == state['selected_option']:
                    st.markdown(f'<div class="quiz-option wrong">❌ {chr(65+i)}.  {option}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="quiz-option">{chr(65+i)}.  {option}</div>', unsafe_allow_html=True)

        if state['answered']:
            st.markdown(f"""
            <div class="reaction-box" style="margin-top:16px;">
                <strong>💡 Penjelasan:</strong><br>{q['explanation']}
            </div>
            """, unsafe_allow_html=True)
            if st.button("Soal Berikutnya →", type="primary", use_container_width=True):
                state['current_question'] += 1
                state['answered'] = False
                state['selected_option'] = None
                st.rerun()
    else:
        score_pct = (state['score'] / len(quiz_list)) * 100
        color = green if score_pct >= 80 else (accent if score_pct >= 60 else red)
        st.markdown(f"""
        <div style="background:{color}15; border:2px solid {color}; border-radius:20px;
            padding:2.5rem; text-align:center; margin:1rem 0;">
            <h1 style="color:{color}; font-size:3rem; margin:0;">
                {state['score']}/{len(quiz_list)}
            </h1>
            <h3 style="color:{text}; margin:0.5rem 0;">Skor Kuis {selected_group}</h3>
            <p style="color:{text}; opacity:0.7;">{score_pct:.0f}% benar</p>
        </div>
        """, unsafe_allow_html=True)

        if score_pct >= 80:
            st.balloons()
            st.markdown('<div class="success-box">🏆 Luar biasa! Anda menguasai materi ini dengan sangat baik!</div>', unsafe_allow_html=True)
        elif score_pct >= 60:
            st.markdown('<div class="info-box">👍 Bagus! Pemahaman Anda sudah cukup baik, tingkatkan lagi!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-box">📚 Perlu belajar lagi. Pelajari bagan dan detail reaksi dengan lebih teliti.</div>', unsafe_allow_html=True)

        if st.button("🔄 Ulangi Kuis", type="primary", use_container_width=True):
            st.session_state[quiz_key] = {
                'current_question': 0,
                'score': 0,
                'answered': False,
                'selected_option': None,
                'shuffled_questions': get_random_questions(selected_group, 10)
            }
            st.rerun()

# ============================================
# HALAMAN: REFERENSI
# ============================================

elif page == "📚 Referensi":
    dm = st.session_state.dark_mode
    accent = "#5c7cfa" if dm else "#3a5bd9"
    text   = "#e8eaf6" if dm else "#1a1a2e"

    st.markdown("""
    <div class="main-header">
        <h1>📚 Referensi & Tabel Ringkasan</h1>
        <p>Warna endapan, larutan, dan rangkuman reaksi kimia</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="cation-card">
        <h3 style="color:{accent};">🎨 Warna Endapan & Larutan</h3>
        <table class="styled-table">
            <tr>
                <th>Senyawa</th><th>Warna</th><th>Keterangan</th><th>Golongan</th>
            </tr>
            <tr><td><span class="mono">AgCl</span></td><td class="p-white">Putih</td><td>Larut dalam NH₄OH</td><td><span class="badge badge-I">I</span></td></tr>
            <tr><td><span class="mono">PbCl₂</span></td><td class="p-white">Putih</td><td>Larut dalam air panas</td><td><span class="badge badge-I">I</span></td></tr>
            <tr><td><span class="mono">Hg₂Cl₂</span></td><td class="p-white">Putih</td><td>Berubah hitam + putih dengan NH₄OH</td><td><span class="badge badge-I">I</span></td></tr>
            <tr><td><span class="mono">PbCrO₄</span></td><td class="p-yellow">Kuning</td><td>Konfirmasi Pb²⁺</td><td><span class="badge badge-I">I</span></td></tr>
            <tr><td><span class="mono">Fe(OH)₃</span></td><td class="p-brown">Coklat/Merah</td><td>Tidak larut dalam basa berlebih</td><td><span class="badge badge-III">III</span></td></tr>
            <tr><td><span class="mono">Al(OH)₃</span></td><td class="p-white">Putih/Gel</td><td>Amfoter — larut dalam NaOH berlebih</td><td><span class="badge badge-III">III</span></td></tr>
            <tr><td><span class="mono">Cr(OH)₃</span></td><td class="p-green">Abu-abu/Hijau</td><td>Dioksidasi → CrO₄²⁻ dengan H₂O₂</td><td><span class="badge badge-III">III</span></td></tr>
            <tr><td><span class="mono">[Fe(SCN)]²⁺</span></td><td class="p-red">Merah Darah</td><td>Konfirmasi Fe³⁺ — sangat sensitif</td><td><span class="badge badge-III">III</span></td></tr>
            <tr><td><span class="mono">PbCrO₄</span></td><td class="p-yellow">Kuning</td><td>Konfirmasi Cr³⁺</td><td><span class="badge badge-III">III</span></td></tr>
            <tr><td><span class="mono">BaCrO₄</span></td><td class="p-yellow">Kuning</td><td>Konfirmasi Ba²⁺</td><td><span class="badge badge-IV">IV</span></td></tr>
            <tr><td><span class="mono">SrSO₄</span></td><td class="p-white">Putih</td><td>Konfirmasi Sr²⁺</td><td><span class="badge badge-IV">IV</span></td></tr>
            <tr><td><span class="mono">CaC₂O₄</span></td><td class="p-white">Putih</td><td>Konfirmasi Ca²⁺ (struvit oksalat)</td><td><span class="badge badge-IV">IV</span></td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="cation-card" style="margin-top:1.5rem;">
        <h3 style="color:{accent};">⚗️ Rangkuman Reaksi Kimia</h3>

        <h4 style="color:{accent}; margin-top:1rem;">Golongan I</h4>
        <div class="reaction-box">Pb²⁺ + 2Cl⁻ → PbCl₂↓  →  H₂O panas  →  larut  →  + K₂CrO₄  →  <span class="p-yellow">PbCrO₄↓ (Kuning)</span></div>
        <div class="reaction-box">Ag⁺ + Cl⁻ → AgCl↓  →  + NH₄OH  →  [Ag(NH₃)₂]⁺  →  + HNO₃  →  <span class="p-white">AgCl↓ (Putih)</span></div>
        <div class="reaction-box">Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓  →  + NH₄OH  →  <span class="p-black">Hg↓ (Hitam)</span> + <span class="p-white">Hg(NH₂)Cl↓ (Putih)</span></div>

        <h4 style="color:{accent}; margin-top:1.2rem;">Golongan III</h4>
        <div class="reaction-box">Fe³⁺ + 3OH⁻ → Fe(OH)₃↓  →  + KSCN  →  <span class="p-red">[Fe(SCN)]²⁺ (Merah Darah)</span></div>
        <div class="reaction-box">Al³⁺ + 3OH⁻ → Al(OH)₃↓  →  + NaOH berlebih  →  [Al(OH)₄]⁻  →  + HCl  →  <span class="p-white">Al(OH)₃↓ (Putih)</span></div>
        <div class="reaction-box">Cr³⁺ + 3OH⁻ → Cr(OH)₃↓  →  + NaOH + H₂O₂  →  CrO₄²⁻  →  + Pb(NO₃)₂  →  <span class="p-yellow">PbCrO₄↓ (Kuning)</span></div>

        <h4 style="color:{accent}; margin-top:1.2rem;">Golongan IV</h4>
        <div class="reaction-box">Ba²⁺ + CO₃²⁻ → BaCO₃↓  →  + CH₃COOH  →  Ba²⁺  →  + K₂CrO₄  →  <span class="p-yellow">BaCrO₄↓ (Kuning)</span></div>
        <div class="reaction-box">Sr²⁺ + CO₃²⁻ → SrCO₃↓  →  + CH₃COOH  →  Sr²⁺  →  + (NH₄)₂SO₄  →  <span class="p-white">SrSO₄↓ (Putih)</span></div>
        <div class="reaction-box">Ca²⁺ + CO₃²⁻ → CaCO₃↓  →  + CH₃COOH  →  Ca²⁺  →  + (NH₄)₂C₂O₄  →  <span class="p-white">CaC₂O₄↓ (Putih)</span></div>
    </div>
    """, unsafe_allow_html=True)
