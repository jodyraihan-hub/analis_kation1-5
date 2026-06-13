"""
styles.py — Custom CSS untuk Analisis Kation
Mendukung mode terang (day) dan gelap (night) secara otomatis.
Inject dengan: from styles import inject_css; inject_css()
"""

import streamlit as st

CUSTOM_CSS = """
<style>

/* ============================================================
   ROOT TOKENS — Light Mode Default
   ============================================================ */
:root {
    --bg-primary:        #F0F4FF;
    --bg-card:           #FFFFFF;
    --bg-card-hover:     #EEF2FF;
    --bg-sidebar:        #1E2A78;

    --text-primary:      #0F172A;
    --text-secondary:    #374151;
    --text-muted:        #6B7280;
    --text-on-dark:      #F8FAFC;

    --accent-blue:       #3B5BDB;
    --accent-teal:       #0D9488;
    --accent-amber:      #D97706;
    --accent-rose:       #E11D48;
    --accent-purple:     #7C3AED;
    --accent-emerald:    #059669;

    /* Golongan warna */
    --gol1-bg:           #FFF0F0;
    --gol1-border:       #FF6B6B;
    --gol1-text:         #991B1B;
    --gol1-badge:        #FF6B6B;

    --gol3-bg:           #F0FFFE;
    --gol3-border:       #0D9488;
    --gol3-text:         #0D5752;
    --gol3-badge:        #14B8A6;

    --gol4-bg:           #FFFBEB;
    --gol4-border:       #D97706;
    --gol4-text:         #78350F;
    --gol4-badge:        #F59E0B;

    --shadow-sm:         0 1px 3px rgba(0,0,0,0.10);
    --shadow-md:         0 4px 16px rgba(0,0,0,0.12);
    --shadow-lg:         0 8px 32px rgba(0,0,0,0.14);

    --radius-sm:         8px;
    --radius-md:         14px;
    --radius-lg:         20px;
    --radius-pill:       999px;

    --transition:        all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ============================================================
   ROOT TOKENS — Dark Mode Override
   ============================================================ */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-primary:        #0B0F1A;
        --bg-card:           #141929;
        --bg-card-hover:     #1C2440;
        --bg-sidebar:        #080C18;

        --text-primary:      #E8EEFF;
        --text-secondary:    #A5B4FC;
        --text-muted:        #6B7280;
        --text-on-dark:      #E8EEFF;

        --accent-blue:       #818CF8;
        --accent-teal:       #2DD4BF;
        --accent-amber:      #FCD34D;
        --accent-rose:       #FB7185;
        --accent-purple:     #C084FC;
        --accent-emerald:    #34D399;

        --gol1-bg:           #1F0A0A;
        --gol1-border:       #FF6B6B;
        --gol1-text:         #FCA5A5;
        --gol1-badge:        #EF4444;

        --gol3-bg:           #061714;
        --gol3-border:       #2DD4BF;
        --gol3-text:         #99F6E4;
        --gol3-badge:        #14B8A6;

        --gol4-bg:           #1A1000;
        --gol4-border:       #F59E0B;
        --gol4-text:         #FDE68A;
        --gol4-badge:        #D97706;

        --shadow-sm:         0 1px 3px rgba(0,0,0,0.40);
        --shadow-md:         0 4px 16px rgba(0,0,0,0.50);
        --shadow-lg:         0 8px 32px rgba(0,0,0,0.60);
    }
}

/* ============================================================
   Streamlit Dark Theme Detection via data-theme attribute
   (Streamlit sets this on <html> or body when user switches)
   ============================================================ */
[data-theme="dark"] {
    --bg-primary:        #0B0F1A;
    --bg-card:           #141929;
    --bg-card-hover:     #1C2440;
    --bg-sidebar:        #080C18;
    --text-primary:      #E8EEFF;
    --text-secondary:    #A5B4FC;
    --text-muted:        #6B7280;
    --accent-blue:       #818CF8;
    --accent-teal:       #2DD4BF;
    --accent-amber:      #FCD34D;
    --accent-rose:       #FB7185;
    --accent-purple:     #C084FC;
    --accent-emerald:    #34D399;
    --gol1-bg:           #1F0A0A;
    --gol1-border:       #FF6B6B;
    --gol1-text:         #FCA5A5;
    --gol1-badge:        #EF4444;
    --gol3-bg:           #061714;
    --gol3-border:       #2DD4BF;
    --gol3-text:         #99F6E4;
    --gol3-badge:        #14B8A6;
    --gol4-bg:           #1A1000;
    --gol4-border:       #F59E0B;
    --gol4-text:         #FDE68A;
    --gol4-badge:        #D97706;
    --shadow-sm:         0 1px 3px rgba(0,0,0,0.40);
    --shadow-md:         0 4px 16px rgba(0,0,0,0.50);
    --shadow-lg:         0 8px 32px rgba(0,0,0,0.60);
}

/* ============================================================
   GLOBAL BASE
   ============================================================ */
.stApp {
    background: var(--bg-primary) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* ============================================================
   SIDEBAR
   ============================================================ */
section[data-testid="stSidebar"] {
    background: var(--bg-sidebar) !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] * {
    color: var(--text-on-dark) !important;
}

section[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.06);
    border-radius: var(--radius-sm);
    padding: 0.5rem 0.75rem;
    margin-bottom: 4px;
    display: block;
    transition: var(--transition);
    border: 1px solid transparent;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.15);
}

section[data-testid="stSidebar"] .stDivider {
    border-color: rgba(255,255,255,0.12) !important;
}

/* ============================================================
   PAGE TITLE & HEADINGS
   ============================================================ */
h1 {
    font-size: 2.1rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, var(--accent-blue), var(--accent-teal)) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    letter-spacing: -0.02em !important;
    margin-bottom: 0 !important;
}

h2 {
    font-size: 1.35rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    border-left: 4px solid var(--accent-blue);
    padding-left: 0.65rem;
    margin-top: 1.5rem !important;
}

h3 {
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
}

.stCaption, caption {
    color: var(--text-muted) !important;
    font-size: 0.85rem !important;
}

/* ============================================================
   BUTTONS
   ============================================================ */
.stButton > button {
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.2rem !important;
    transition: var(--transition) !important;
    border: 1.5px solid transparent !important;
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    box-shadow: var(--shadow-sm) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
    border-color: var(--accent-blue) !important;
    color: var(--accent-blue) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)) !important;
    color: white !important;
    border-color: transparent !important;
}

.stButton > button[kind="primary"]:hover {
    opacity: 0.9 !important;
    color: white !important;
}

/* Quiz option buttons */
.stButton > button[data-testid*="opt_"] {
    text-align: left !important;
    border-radius: var(--radius-sm) !important;
}

/* ============================================================
   CONTAINERS / CARDS
   ============================================================ */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius-md) !important;
    border: 1px solid rgba(128,128,255,0.12) !important;
    box-shadow: var(--shadow-sm) !important;
    padding: 1rem !important;
    transition: var(--transition) !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(128,128,255,0.25) !important;
    box-shadow: var(--shadow-md) !important;
}

/* ============================================================
   ALERTS (success / info / warning / error)
   ============================================================ */
div[data-testid="stAlert"] {
    border-radius: var(--radius-sm) !important;
    border-width: 1.5px !important;
    font-weight: 500 !important;
}

/* success → hijau emerald */
div[data-testid="stAlert"][data-baseweb="notification"] .st-emotion-cache-1fttcpj,
div[data-testid="stAlert"][kind="success"],
.stSuccess {
    background: rgba(5, 150, 105, 0.12) !important;
    border-color: var(--accent-emerald) !important;
    color: var(--accent-emerald) !important;
}

/* info → biru */
div[data-testid="stAlert"][kind="info"],
.stInfo {
    background: rgba(59, 91, 219, 0.10) !important;
    border-color: var(--accent-blue) !important;
    color: var(--accent-blue) !important;
}

/* warning → amber */
div[data-testid="stAlert"][kind="warning"],
.stWarning {
    background: rgba(217, 119, 6, 0.10) !important;
    border-color: var(--accent-amber) !important;
    color: var(--accent-amber) !important;
}

/* error → rose */
div[data-testid="stAlert"][kind="error"],
.stError {
    background: rgba(225, 29, 72, 0.10) !important;
    border-color: var(--accent-rose) !important;
    color: var(--accent-rose) !important;
}

/* ============================================================
   TABS
   ============================================================ */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius-pill) !important;
    padding: 4px !important;
    gap: 4px !important;
    border: 1px solid rgba(128,128,255,0.10) !important;
    box-shadow: var(--shadow-sm) !important;
}

.stTabs [data-baseweb="tab"] {
    border-radius: var(--radius-pill) !important;
    color: var(--text-muted) !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    padding: 0.35rem 1rem !important;
    transition: var(--transition) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)) !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(59,91,219,0.35) !important;
}

/* ============================================================
   SELECTBOX / DROPDOWN
   ============================================================ */
.stSelectbox > div > div {
    background: var(--bg-card) !important;
    border-radius: var(--radius-sm) !important;
    border: 1.5px solid rgba(128,128,255,0.20) !important;
    color: var(--text-primary) !important;
    transition: var(--transition) !important;
}

.stSelectbox > div > div:hover {
    border-color: var(--accent-blue) !important;
}

/* ============================================================
   PROGRESS BAR
   ============================================================ */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-teal)) !important;
    border-radius: var(--radius-pill) !important;
}

.stProgress > div > div {
    background: rgba(128,128,255,0.12) !important;
    border-radius: var(--radius-pill) !important;
    height: 10px !important;
}

/* ============================================================
   METRIC WIDGETS
   ============================================================ */
div[data-testid="stMetric"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius-md) !important;
    padding: 1rem 1.25rem !important;
    border: 1px solid rgba(128,128,255,0.12) !important;
    box-shadow: var(--shadow-sm) !important;
}

div[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

div[data-testid="stMetricValue"] {
    color: var(--accent-blue) !important;
    font-weight: 800 !important;
    font-size: 1.6rem !important;
}

/* ============================================================
   CODE BLOCKS (reaksi kimia)
   ============================================================ */
.stCodeBlock, pre, code {
    background: var(--bg-card) !important;
    border: 1px solid rgba(128,128,255,0.15) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--accent-teal) !important;
    font-family: 'JetBrains Mono', 'Fira Code', monospace !important;
    font-size: 0.88rem !important;
}

/* ============================================================
   TABLE
   ============================================================ */
.stTable table, table {
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
    box-shadow: var(--shadow-sm) !important;
    width: 100% !important;
}

.stTable th, thead th {
    background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
    padding: 0.75rem 1rem !important;
    border: none !important;
}

.stTable td, tbody td {
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
    padding: 0.65rem 1rem !important;
    border-bottom: 1px solid rgba(128,128,255,0.08) !important;
    font-size: 0.9rem !important;
}

.stTable tr:hover td, tbody tr:hover td {
    background: var(--bg-card-hover) !important;
}

/* ============================================================
   EXPANDER
   ============================================================ */
details {
    border-radius: var(--radius-sm) !important;
    border: 1px solid rgba(128,128,255,0.15) !important;
    background: var(--bg-card) !important;
    overflow: hidden !important;
    transition: var(--transition) !important;
}

details summary {
    padding: 0.75rem 1rem !important;
    font-weight: 600 !important;
    color: var(--text-primary) !important;
    cursor: pointer !important;
}

details[open] {
    border-color: var(--accent-blue) !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ============================================================
   DIVIDER
   ============================================================ */
hr {
    border: none !important;
    height: 1.5px !important;
    background: linear-gradient(90deg, transparent, var(--accent-blue), var(--accent-teal), transparent) !important;
    margin: 1.5rem 0 !important;
    opacity: 0.35 !important;
}

/* ============================================================
   GOLONGAN BADGE HELPERS (pakai st.markdown custom HTML)
   ============================================================ */
.badge-gol1 {
    display: inline-block;
    background: var(--gol1-badge);
    color: white;
    font-weight: 700;
    font-size: 0.75rem;
    padding: 3px 10px;
    border-radius: var(--radius-pill);
    letter-spacing: 0.04em;
}
.badge-gol3 {
    display: inline-block;
    background: var(--gol3-badge);
    color: white;
    font-weight: 700;
    font-size: 0.75rem;
    padding: 3px 10px;
    border-radius: var(--radius-pill);
    letter-spacing: 0.04em;
}
.badge-gol4 {
    display: inline-block;
    background: var(--gol4-badge);
    color: white;
    font-weight: 700;
    font-size: 0.75rem;
    padding: 3px 10px;
    border-radius: var(--radius-pill);
    letter-spacing: 0.04em;
}

/* Kartu golongan di beranda */
.card-gol1 {
    border-left: 5px solid var(--gol1-border) !important;
    background: var(--gol1-bg) !important;
    padding: 0.8rem 1rem;
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    margin-bottom: 0.5rem;
}
.card-gol3 {
    border-left: 5px solid var(--gol3-border) !important;
    background: var(--gol3-bg) !important;
    padding: 0.8rem 1rem;
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    margin-bottom: 0.5rem;
}
.card-gol4 {
    border-left: 5px solid var(--gol4-border) !important;
    background: var(--gol4-bg) !important;
    padding: 0.8rem 1rem;
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    margin-bottom: 0.5rem;
}
.card-gol1 *, .card-gol3 *, .card-gol4 * {
    color: var(--text-primary) !important;
}

/* ============================================================
   QUIZ SPECIFIC
   ============================================================ */
.quiz-question-box {
    background: var(--bg-card);
    border: 2px solid var(--accent-blue);
    border-radius: var(--radius-md);
    padding: 1.25rem 1.5rem;
    box-shadow: var(--shadow-md);
    margin-bottom: 1rem;
}

/* ============================================================
   SCROLLBAR
   ============================================================ */
::-webkit-scrollbar { width: 7px; height: 7px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(100,120,255,0.25);
    border-radius: var(--radius-pill);
}
::-webkit-scrollbar-thumb:hover { background: rgba(100,120,255,0.45); }

/* ============================================================
   ANIMATION — subtle entrance
   ============================================================ */
@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

.main .block-container > * {
    animation: fadeSlideIn 0.35s ease both;
}

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media (max-width: 768px) {
    h1 { font-size: 1.5rem !important; }
    h2 { font-size: 1.1rem !important; }
    .main .block-container { padding: 1rem 0.75rem !important; }
}

</style>
"""

def inject_css():
    """Inject custom CSS ke seluruh aplikasi Streamlit."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ============================================================
# HELPER: Kartu subheader berwarna per golongan
# ============================================================

def subheader_golongan(golongan: str, label: str):
    """Render subheader berwarna sesuai golongan (I/III/IV)."""
    css_class = {"I": "card-gol1", "III": "card-gol3", "IV": "card-gol4"}.get(golongan, "card-gol1")
    badge_class = {"I": "badge-gol1", "III": "badge-gol3", "IV": "badge-gol4"}.get(golongan, "badge-gol1")
    icons = {"I": "⬛", "III": "🟦", "IV": "🟨"}
    icon = icons.get(golongan, "⚗️")
    st.markdown(
        f'<div class="{css_class}">'
        f'<span class="{badge_class}">GOL. {golongan}</span> '
        f'<strong style="font-size:1.05rem;margin-left:8px;">{icon} {label}</strong>'
        f'</div>',
        unsafe_allow_html=True
    )
