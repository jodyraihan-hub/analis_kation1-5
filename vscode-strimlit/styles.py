
import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    /* ============================================================ */
    /* ROOT VARIABLES - DAY & NIGHT MODE */
    /* ============================================================ */

    :root {
        /* Day Mode (Default) */
        --bg-primary: #f8fafc;
        --bg-secondary: #ffffff;
        --bg-card: #ffffff;
        --bg-sidebar: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        --bg-hover: #f1f5f9;

        --text-primary: #0f172a;
        --text-secondary: #475569;
        --text-muted: #94a3b8;
        --text-inverse: #ffffff;

        --border-color: #e2e8f0;
        --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
        --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1);
        --shadow-glow: 0 0 20px rgba(99, 102, 241, 0.15);

        /* Warna Kimia - Kontras Tinggi */
        --chem-ag: #FF6B6B;
        --chem-pb: #FFD93D;
        --chem-hg: #6C757D;
        --chem-fe: #8B4513;
        --chem-al: #A0AEC0;
        --chem-cr: #48CAE4;
        --chem-ba: #FFD93D;
        --chem-sr: #E2E8F0;
        --chem-ca: #F8F9FA;

        /* Accent Colors */
        --accent-primary: #6366f1;
        --accent-secondary: #8b5cf6;
        --accent-success: #10b981;
        --accent-warning: #f59e0b;
        --accent-danger: #ef4444;
        --accent-info: #3b82f6;

        /* Gradient */
        --gradient-primary: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
        --gradient-success: linear-gradient(135deg, #10b981 0%, #34d399 100%);
        --gradient-warning: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
        --gradient-danger: linear-gradient(135deg, #ef4444 0%, #f87171 100%);
        --gradient-info: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);

        /* Glass Effect */
        --glass-bg: rgba(255, 255, 255, 0.7);
        --glass-border: rgba(255, 255, 255, 0.3);
        --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }

    /* ============================================================ */
    /* NIGHT MODE */
    /* ============================================================ */

    [data-theme="dark"],
    .stApp[data-theme="dark"] {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-card: #1e293b;
        --bg-sidebar: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        --bg-hover: #334155;

        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #64748b;
        --text-inverse: #0f172a;

        --border-color: #334155;
        --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
        --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.4), 0 2px 4px -2px rgba(0,0,0,0.4);
        --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.5), 0 4px 6px -4px rgba(0,0,0,0.5);
        --shadow-glow: 0 0 30px rgba(99, 102, 241, 0.3);

        /* Warna Kimia - Neon Mode */
        --chem-ag: #FF4757;
        --chem-pb: #FFA502;
        --chem-hg: #A4B0BE;
        --chem-fe: #FF6348;
        --chem-al: #DFE4EA;
        --chem-cr: #00D2D3;
        --chem-ba: #FFA502;
        --chem-sr: #F1F2F6;
        --chem-ca: #FFFFFF;

        --glass-bg: rgba(30, 41, 59, 0.7);
        --glass-border: rgba(255, 255, 255, 0.1);
        --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }

    /* ============================================================ */
    /* GLOBAL STYLES */
    /* ============================================================ */

    .stApp {
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
        transition: all 0.3s ease;
    }

    /* Main Container */
    .main .block-container {
        background: var(--bg-primary) !important;
        padding: 2rem !important;
        max-width: 1200px;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
    }

    h1 {
        background: var(--gradient-primary) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 2.5rem !important;
    }

    p, span, label, .stMarkdown {
        color: var(--text-secondary) !important;
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
    }

    /* ============================================================ */
    /* SIDEBAR - Glassmorphism */
    /* ============================================================ */

    [data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border-color) !important;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: var(--text-inverse) !important;
        font-weight: 500 !important;
        padding: 0.75rem 1rem !important;
        border-radius: 0.75rem !important;
        transition: all 0.2s ease !important;
        margin: 0.25rem 0 !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.1) !important;
        transform: translateX(4px);
    }

    [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
        background: var(--accent-primary) !important;
        border-color: var(--accent-primary) !important;
    }

    /* Sidebar Title */
    [data-testid="stSidebar"] h1 {
        color: var(--text-inverse) !important;
        -webkit-text-fill-color: var(--text-inverse) !important;
        font-size: 1.5rem !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
    }

    [data-testid="stSidebar"] .stCaption {
        color: var(--text-muted) !important;
        text-align: center !important;
    }

    /* ============================================================ */
    /* CARDS - Glassmorphism Effect */
    /* ============================================================ */

    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 1rem !important;
        box-shadow: var(--glass-shadow) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stVerticalBlock"] > div[style*="border"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-lg) !important;
    }

    /* Custom Card Class */
    .chem-card {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 1rem !important;
        padding: 1.5rem !important;
        margin: 0.75rem 0 !important;
        box-shadow: var(--glass-shadow) !important;
        transition: all 0.3s ease !important;
    }

    .chem-card:hover {
        transform: translateY(-4px) !important;
        box-shadow: var(--shadow-glow) !important;
        border-color: var(--accent-primary) !important;
    }

    /* ============================================================ */
    /* BUTTONS - Gradient & Glow */
    /* ============================================================ */

    .stButton > button {
        background: var(--gradient-primary) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.75rem !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
        text-transform: none !important;
        letter-spacing: 0.025em !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5) !important;
        filter: brightness(1.1) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Success Button */
    .stButton > button[kind="primary"] {
        background: var(--gradient-success) !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
    }

    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5) !important;
    }

    /* Danger/Reset Button */
    button[data-testid="baseButton-secondary"] {
        background: var(--gradient-danger) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3) !important;
    }

    /* ============================================================ */
    /* EXPANDER - Modern Style */
    /* ============================================================ */

    .streamlit-expander {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0.75rem !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .streamlit-expanderHeader {
        background: var(--bg-hover) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        padding: 1rem 1.25rem !important;
        border-bottom: 1px solid var(--border-color) !important;
    }

    .streamlit-expanderContent {
        background: var(--bg-card) !important;
        padding: 1.25rem !important;
    }

    /* ============================================================ */
    /* CODE BLOCKS - Syntax Highlighting */
    /* ============================================================ */

    .stCodeBlock {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0.75rem !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .stCodeBlock code {
        color: var(--text-primary) !important;
        font-family: 'Fira Code', 'JetBrains Mono', monospace !important;
        font-size: 0.9rem !important;
        line-height: 1.6 !important;
    }

    /* Chemical formula coloring */
    .stCodeBlock code .chem-ion {
        color: var(--accent-primary) !important;
        font-weight: 600 !important;
    }

    /* ============================================================ */
    /* ALERTS - Colored Cards */
    /* ============================================================ */

    .stAlert {
        border-radius: 0.75rem !important;
        border: none !important;
        padding: 1rem 1.25rem !important;
        box-shadow: var(--shadow-sm) !important;
    }

    .stAlert[data-baseweb="notification"] {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(8px) !important;
    }

    /* Success Alert */
    .stAlert[data-baseweb="notification"][kind="positive"] {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%) !important;
        border-left: 4px solid var(--accent-success) !important;
        color: var(--accent-success) !important;
    }

    /* Warning Alert */
    .stAlert[data-baseweb="notification"][kind="warning"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(251, 191, 36, 0.1) 100%) !important;
        border-left: 4px solid var(--accent-warning) !important;
        color: var(--accent-warning) !important;
    }

    /* Error Alert */
    .stAlert[data-baseweb="notification"][kind="negative"] {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(248, 113, 113, 0.1) 100%) !important;
        border-left: 4px solid var(--accent-danger) !important;
        color: var(--accent-danger) !important;
    }

    /* Info Alert */
    .stAlert[data-baseweb="notification"][kind="info"] {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(96, 165, 250, 0.1) 100%) !important;
        border-left: 4px solid var(--accent-info) !important;
        color: var(--accent-info) !important;
    }

    /* ============================================================ */
    /* PROGRESS BAR - Animated Gradient */
    /* ============================================================ */

    .stProgress > div > div {
        background: var(--gradient-primary) !important;
        border-radius: 999px !important;
        height: 8px !important;
        transition: width 0.5s ease !important;
    }

    .stProgress > div {
        background: var(--bg-hover) !important;
        border-radius: 999px !important;
        height: 8px !important;
    }

    /* ============================================================ */
    /* TABS - Modern Underline */
    /* ============================================================ */

    .stTabs [data-baseweb="tab-list"] {
        background: transparent !important;
        border-bottom: 2px solid var(--border-color) !important;
        gap: 0 !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: var(--text-muted) !important;
        font-weight: 600 !important;
        padding: 1rem 1.5rem !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        transition: all 0.2s ease !important;
        margin: 0 !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--accent-primary) !important;
        background: var(--bg-hover) !important;
    }

    .stTabs [aria-selected="true"] {
        color: var(--accent-primary) !important;
        border-bottom: 2px solid var(--accent-primary) !important;
        background: linear-gradient(180deg, transparent 0%, rgba(99, 102, 241, 0.05) 100%) !important;
    }

    .stTabs [data-baseweb="tab-panel"] {
        background: var(--bg-card) !important;
        border-radius: 0 0 1rem 1rem !important;
        padding: 1.5rem !important;
        border: 1px solid var(--border-color) !important;
        border-top: none !important;
    }

    /* ============================================================ */
    /* SELECTBOX & INPUT - Modern Style */
    /* ============================================================ */

    .stSelectbox > div > div {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0.75rem !important;
        color: var(--text-primary) !important;
    }

    .stSelectbox > div > div:hover {
        border-color: var(--accent-primary) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }

    /* ============================================================ */
    /* TABLE - Modern Style */
    /* ============================================================ */

    .stTable {
        background: var(--bg-card) !important;
        border-radius: 1rem !important;
        overflow: hidden !important;
        box-shadow: var(--shadow-sm) !important;
        border: 1px solid var(--border-color) !important;
    }

    .stTable thead tr {
        background: var(--gradient-primary) !important;
        color: white !important;
    }

    .stTable thead th {
        padding: 1rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        font-size: 0.8rem !important;
        letter-spacing: 0.05em !important;
    }

    .stTable tbody tr {
        border-bottom: 1px solid var(--border-color) !important;
        transition: background 0.2s ease !important;
    }

    .stTable tbody tr:hover {
        background: var(--bg-hover) !important;
    }

    .stTable tbody td {
        padding: 0.875rem 1rem !important;
        color: var(--text-secondary) !important;
    }

    /* ============================================================ */
    /* METRIC CARDS */
    /* ============================================================ */

    [data-testid="stMetric"] {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 1rem !important;
        padding: 1.25rem !important;
        box-shadow: var(--shadow-sm) !important;
    }

    [data-testid="stMetric"] label {
        color: var(--text-muted) !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }

    [data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        background: var(--gradient-primary) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }

    /* ============================================================ */
    /* DIVIDER - Gradient */
    /* ============================================================ */

    hr {
        border: none !important;
        height: 2px !important;
        background: var(--gradient-primary) !important;
        border-radius: 999px !important;
        margin: 2rem 0 !important;
        opacity: 0.3 !important;
    }

    /* ============================================================ */
    /* SCROLLBAR - Custom */
    /* ============================================================ */

    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-primary) !important;
    }

    ::-webkit-scrollbar-thumb {
        background: var(--accent-primary) !important;
        border-radius: 999px !important;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-secondary) !important;
    }

    /* ============================================================ */
    /* ANIMATIONS */
    /* ============================================================ */

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px var(--accent-primary); }
        50% { box-shadow: 0 0 20px var(--accent-primary), 0 0 40px var(--accent-secondary); }
    }

    .animate-fade-in {
        animation: fadeIn 0.5s ease-out forwards;
    }

    .animate-slide-in {
        animation: slideIn 0.5s ease-out forwards;
    }

    /* ============================================================ */
    /* QUIZ OPTIONS - Interactive Cards */
    /* ============================================================ */

    .quiz-option {
        background: var(--bg-card) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 0.75rem !important;
        padding: 1rem 1.25rem !important;
        margin: 0.5rem 0 !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        color: var(--text-primary) !important;
        font-weight: 500 !important;
    }

    .quiz-option:hover {
        border-color: var(--accent-primary) !important;
        background: var(--bg-hover) !important;
        transform: translateX(4px) !important;
    }

    .quiz-option.correct {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%) !important;
        border-color: var(--accent-success) !important;
        color: var(--accent-success) !important;
    }

    .quiz-option.wrong {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(248, 113, 113, 0.1) 100%) !important;
        border-color: var(--accent-danger) !important;
        color: var(--accent-danger) !important;
    }

    /* ============================================================ */
    /* FLOWCHART NODES - Bagan Analisis */
    /* ============================================================ */

    .flow-node {
        background: var(--glass-bg) !important;
        backdrop-filter: blur(8px) !important;
        border: 2px solid var(--border-color) !important;
        border-radius: 1rem !important;
        padding: 1.25rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        position: relative !important;
    }

    .flow-node::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: var(--gradient-primary);
        border-radius: 1rem;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .flow-node:hover::before {
        opacity: 1;
    }

    .flow-node:hover {
        transform: scale(1.02);
        border-color: transparent !important;
    }

    .flow-connector {
        width: 2px;
        height: 30px;
        background: var(--gradient-primary);
        margin: 0 auto;
        position: relative;
    }

    .flow-connector::after {
        content: '▼';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        color: var(--accent-primary);
        font-size: 0.75rem;
    }

    /* ============================================================ */
    /* GROUP COLORS - Specific Styling */
    /* ============================================================ */

    .group-I { --group-color: var(--chem-ag); }
    .group-III { --group-color: var(--chem-fe); }
    .group-IV { --group-color: var(--chem-ba); }

    .group-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.875rem;
        background: var(--group-color);
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    /* ============================================================ */
    /* TOGGLE SWITCH - Day/Night */
    /* ============================================================ */

    .theme-toggle {
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 9999;
        background: var(--glass-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--glass-border);
        border-radius: 999px;
        padding: 0.5rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
    }

    .theme-toggle:hover {
        transform: scale(1.1);
        box-shadow: var(--shadow-glow);
    }

    /* ============================================================ */
    /* RESPONSIVE */
    /* ============================================================ */

    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }

        h1 {
            font-size: 1.75rem !important;
        }

        .chem-card {
            padding: 1rem !important;
        }
    }

    /* ============================================================ */
    /* PARTICLES BACKGROUND (Optional - untuk efek visual tambahan) */
    /* ============================================================ */

    .particles-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        opacity: 0.3;
    }

    </style>
    """, unsafe_allow_html=True)


def subheader_golongan(group_num, ions):
    """Render subheader dengan warna khusus per golongan"""
    colors = {
        "I": "#FF6B6B",
        "III": "#4ECDC4", 
        "IV": "#FFD93D"
    }
    color = colors.get(group_num, "#6366f1")

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}20 0%, {color}10 100%);
        border-left: 4px solid {color};
        border-radius: 0 0.75rem 0.75rem 0;
        padding: 1rem 1.25rem;
        margin: 1.5rem 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    ">
        <span style="
            background: {color};
            color: white;
            padding: 0.35rem 0.75rem;
            border-radius: 0.5rem;
            font-weight: 700;
            font-size: 0.875rem;
        ">Golongan {group_num}</span>
        <span style="
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1.1rem;
        ">{ions}</span>
    </div>
    """, unsafe_allow_html=True)


def render_theme_toggle():
    """Render toggle switch untuk day/night mode"""
    st.markdown("""
    <div class="theme-toggle" onclick="
        const html = document.documentElement;
        const current = html.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    ">
        <span id="theme-icon">🌙</span>
    </div>
    <script>
        (function() {
            const saved = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', saved);
            document.getElementById('theme-icon').textContent = saved === 'dark' ? '☀️' : '🌙';
        })();
    </script>
    """, unsafe_allow_html=True)
