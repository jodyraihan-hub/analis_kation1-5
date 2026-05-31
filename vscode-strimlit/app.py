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
    page_title="Analisis Kation Golongan I, III, IV, V",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS CUSTOM
# ============================================
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .reaction-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .cation-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 2px solid #e0e0e0;
    }
    .quiz-option {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .quiz-option:hover {
        background-color: #e3f2fd;
        transform: translateX(5px);
    }
    .correct {
        background-color: #c8e6c9 !important;
        border: 2px solid #4caf50;
    }
    .wrong {
        background-color: #ffcdd2 !important;
        border: 2px solid #f44336;
    }
    .precipitate-white { color: #9e9e9e; font-weight: bold; }
    .precipitate-yellow { color: #ffc107; font-weight: bold; }
    .precipitate-black { color: #212121; font-weight: bold; }
    .precipitate-brown { color: #8D6E63; font-weight: bold; }
    .solution-red { color: #f44336; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ============================================
# DATA KATION (SUDAH DIKOREKSI)
# ============================================

cation_data = {
    "Golongan I (Ag⁺, Pb²⁺, Hg₂²⁺)": {
        "color": "#FF6B6B",
        "reagen": "HCl encer",
        "precipitate": "AgCl (putih), PbCl₂ (putih), Hg₂Cl₂ (putih)",
        "steps": [
            {
                "action": "Tambahkan HCl encer ke sampel",
                "result": "Terbentuk endapan putih: AgCl, PbCl₂, Hg₂Cl₂",
                "filtrate": "Filtrat menuju Golongan II (dilewati dalam analisis ini)",
                "residue": "AgCl, PbCl₂, Hg₂Cl₂"
            },
            {
                "action": "Tambahkan H₂O panas pada endapan",
                "result": "PbCl₂ larut (kelarutan meningkat dengan suhu), AgCl dan Hg₂Cl₂ tidak larut",
                "filtrate": "Pb²⁺",
                "residue": "AgCl, Hg₂Cl₂"
            },
            {
                "action": "Pada filtrat Pb²⁺: Tambahkan K₂CrO₄",
                "result": "Endapan kuning PbCrO₄",
                "confirm": "Pb²⁺ terkonfirmasi"
            },
            {
                "action": "Pada residu AgCl, Hg₂Cl₂: Tambahkan NH₄OH",
                "result": "AgCl larut membentuk [Ag(NH₃)₂]⁺, Hg₂Cl₂ berubah menjadi Hg (hitam) + Hg(NH₂)Cl (putih)",
                "filtrate": "[Ag(NH₃)₂]⁺",
                "residue": "Hg (hitam) + Hg(NH₂)Cl (putih)"
            },
            {
                "action": "Pada filtrat [Ag(NH₃)₂]⁺: Tambahkan HNO₃",
                "result": "Endapan putih AgCl kembali terbentuk",
                "confirm": "Ag⁺ terkonfirmasi"
            }
        ]
    },
    "Golongan III (Fe³⁺, Al³⁺, Cr³⁺)": {
        "color": "#4ECDC4",
        "reagen": "NH₄OH berlebih + NH₄Cl",
        "precipitate": "Fe(OH)₃ (coklat/merah), Al(OH)₃ (putih/gel), Cr(OH)₃ (abu-abu/hijau)",
        "steps": [
            {
                "action": "Tambahkan NH₄OH + NH₄Cl pada filtrat dari Golongan II",
                "result": "Fe(OH)₃ (coklat), Al(OH)₃ (putih/gel), Cr(OH)₃ (abu-abu/hijau) terendap. NH₄Cl menekan [OH⁻] agar Mg²⁺ tidak ikut terendap sebagai Mg(OH)₂",
                "filtrate": "Filtrat menuju Golongan IV (Mg²⁺, K⁺, Na⁺, NH₄⁺)",
                "residue": "Fe(OH)₃, Al(OH)₃, Cr(OH)₃"
            },
            {
                "action": "Pada endapan: Tambahkan NaOH berlebih + H₂O₂",
                "result": "Al(OH)₃ larut → [Al(OH)₄]⁻, Cr(OH)₃ → CrO₄²⁻ (larut), Fe(OH)₃ tidak larut",
                "filtrate": "[Al(OH)₄]⁻, CrO₄²⁻",
                "residue": "Fe(OH)₃"
            },
            {
                "action": "Pada residu Fe(OH)₃: Tambahkan HCl + KSCN",
                "result": "Larutan merah darah [Fe(SCN)]²⁺",
                "confirm": "Fe³⁺ terkonfirmasi"
            },
            {
                "action": "Pada filtrat [Al(OH)₄]⁻: Tambahkan HCl (asam) perlahan",
                "result": "Endapan putih/gel Al(OH)₃ kembali",
                "confirm": "Al³⁺ terkonfirmasi"
            },
            {
                "action": "Pada filtrat CrO₄²⁻: Tambahkan Pb(NO₃)₂",
                "result": "Endapan kuning PbCrO₄",
                "confirm": "Cr³⁺ terkonfirmasi"
            }
        ]
    },
    "Golongan IV (Ba²⁺, Sr²⁺, Ca²⁺)": {
        "color": "#FFD93D",
        "reagen": "(NH₄)₂CO₃ + NH₄OH + NH₄Cl",
        "precipitate": "BaCO₃ (putih), SrCO₃ (putih), CaCO₃ (putih)",
        "steps": [
            {
                "action": "Tambahkan (NH₄)₂CO₃ + NH₄OH + NH₄Cl pada filtrat dari Golongan III",
                "result": "BaCO₃, SrCO₃, CaCO₃ terendap putih. NH₄Cl mencegah pengendapan MgCO₃",
                "filtrate": "Filtrat menuju Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺)",
                "residue": "BaCO₃, SrCO₃, CaCO₃"
            },
            {
                "action": "Pada endapan: Tambahkan asam asetat (CH₃COOH)",
                "result": "Semua karbonat larut membentuk asetat",
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
                "confirm": "Ca²⁺ terkonfirmasi"
            }
        ]
    },
    "Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺)": {
        "color": "#6BCB77",
        "reagen": "Tidak ada reagen pengendap spesifik (kation larut/residu)",
        "precipitate": "Tidak terdapat endapan",
        "steps": [
            {
                "action": "Uji Mg²⁺: Tambahkan NH₄OH + (NH₄)₂HPO₄",
                "result": "Endapan putih kristalin MgNH₄PO₄·6H₂O (magnesium amonium fosfat/struvit)",
                "confirm": "Mg²⁺ terkonfirmasi"
            },
            {
                "action": "Uji K⁺: Tambahkan asam tartrat (H₂C₄H₄O₆)",
                "result": "Endapan putih KHC₄H₄O₆",
                "confirm": "K⁺ terkonfirmasi"
            },
            {
                "action": "Uji Na⁺: Tambahkan asam asetat uranil Zn(UO₂)₃(CH₃COO)₈",
                "result": "Kristal kuning NaZn(UO₂)₃(CH₃COO)₉·6H₂O",
                "confirm": "Na⁺ terkonfirmasi"
            },
            {
                "action": "Uji NH₄⁺: Tambahkan NaOH dan panaskan",
                "result": "Gas NH₃ yang berbau tajam (merahkan lakmus merah basah)",
                "confirm": "NH₄⁺ terkonfirmasi"
            }
        ]
    }
}

# ============================================
# BAGAN INTERAKTIF (SUDAH DIKOREKSI)
# ============================================

def create_flowchart_nodes():
    nodes = []
    edges = []

    # Level 0 - Sample
    nodes.append(Node(id="sample", label="Sampel\n(Ag⁺, Pb²⁺, Hg₂²⁺,\nFe³⁺, Al³⁺, Cr³⁺,\nBa²⁺, Sr²⁺, Ca²⁺,\nMg²⁺, K⁺, Na⁺, NH₄⁺)", 
                     color="#9C27B0", size=35, shape="box"))

    # ============ GOLONGAN I ============
    nodes.append(Node(id="hcl", label="+ HCl encer", color="#FF9800", size=25))
    nodes.append(Node(id="group1", label="Endapan Putih\nAgCl, PbCl₂, Hg₂Cl₂\nGOLONGAN I", 
                     color="#FF6B6B", size=30, shape="box"))
    nodes.append(Node(id="filtrat1", label="Filtrat G-II\n(Cu²⁺, Cd²⁺, Bi³⁺,\nHg²⁺, Sn²⁺, Sb³⁺, As³⁺)\nDILEWATI →", 
                     color="#BDBDBD", size=25, shape="box"))

    edges.append(Edge(source="sample", target="hcl", color="#666"))
    edges.append(Edge(source="hcl", target="group1", color="#666"))
    edges.append(Edge(source="hcl", target="filtrat1", color="#999", dashes=True))

    # Group I branches
    nodes.append(Node(id="hot_water", label="+ H₂O panas", color="#FF9800", size=25))
    nodes.append(Node(id="pb", label="Pb²⁺\n(larut)", color="#FFD93D", size=25, shape="box"))
    nodes.append(Node(id="ag_hg", label="AgCl, Hg₂Cl₂\n(tidak larut)", 
                     color="#FF6B6B", size=25, shape="box"))

    edges.append(Edge(source="group1", target="hot_water", color="#666"))
    edges.append(Edge(source="hot_water", target="pb", color="#666"))
    edges.append(Edge(source="hot_water", target="ag_hg", color="#666"))

    # Pb confirmation
    nodes.append(Node(id="k2cro4", label="+ K₂CrO₄", color="#FF9800", size=25))
    nodes.append(Node(id="pbcro4", label="PbCrO₄\n(Kuning)", color="#FFD93D", size=25, shape="box"))
    edges.append(Edge(source="pb", target="k2cro4", color="#666"))
    edges.append(Edge(source="k2cro4", target="pbcro4", color="#666"))

    # Ag/Hg branch
    nodes.append(Node(id="nh4oh_g1", label="+ NH₄OH", color="#FF9800", size=25))
    nodes.append(Node(id="ag_complex", label="[Ag(NH₃)₂]⁺\n(larut)", color="#C8E6C9", size=25, shape="box"))
    nodes.append(Node(id="hg_mix", label="Hg + Hg(NH₂)Cl\n(Hitam + Putih)", 
                     color="#757575", size=25, shape="box"))

    edges.append(Edge(source="ag_hg", target="nh4oh_g1", color="#666"))
    edges.append(Edge(source="nh4oh_g1", target="ag_complex", color="#666"))
    edges.append(Edge(source="nh4oh_g1", target="hg_mix", color="#666"))

    # Ag confirmation
    nodes.append(Node(id="hno3", label="+ HNO₃", color="#FF9800", size=25))
    nodes.append(Node(id="agcl_back", label="AgCl\n(Putih)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="ag_complex", target="hno3", color="#666"))
    edges.append(Edge(source="hno3", target="agcl_back", color="#666"))

    # ============ SKIP GOLONGAN II ============
    nodes.append(Node(id="skip_g2_note", label="Golongan II\ndilewati\ndalam analisis ini", 
                     color="#EEEEEE", size=20, shape="ellipse"))

    edges.append(Edge(source="filtrat1", target="skip_g2_note", color="#BDBDBD", dashes=True))

    # ============ GOLONGAN III ============
    nodes.append(Node(id="nh4oh_g3", label="+ NH₄OH + NH₄Cl\n(penyangga)", color="#FF9800", size=25))
    nodes.append(Node(id="group3", label="Endapan\nFe(OH)₃ (Coklat)\nAl(OH)₃ (Putih)\nCr(OH)₃ (Abu²)\nGOLONGAN III", 
                     color="#4ECDC4", size=30, shape="box"))
    nodes.append(Node(id="filtrat3", label="Filtrat G-IV\n(Ba²⁺, Sr²⁺, Ca²⁺,\nMg²⁺, K⁺, Na⁺, NH₄⁺)", 
                     color="#E0E0E0", size=25, shape="box"))

    edges.append(Edge(source="skip_g2_note", target="nh4oh_g3", color="#BDBDBD", dashes=True))
    edges.append(Edge(source="nh4oh_g3", target="group3", color="#666"))
    edges.append(Edge(source="nh4oh_g3", target="filtrat3", color="#666", dashes=True))

    # Group III branches
    nodes.append(Node(id="naoh_h2o2", label="+ NaOH berlebih\n+ H₂O₂", color="#FF9800", size=25))
    nodes.append(Node(id="fe_oh", label="Fe(OH)₃\n(tidak larut)", color="#8D6E63", size=25, shape="box"))
    nodes.append(Node(id="al_cr_sol", label="[Al(OH)₄]⁻\nCrO₄²⁻\n(larut)", color="#C8E6C9", size=25, shape="box"))

    edges.append(Edge(source="group3", target="naoh_h2o2", color="#666"))
    edges.append(Edge(source="naoh_h2o2", target="fe_oh", color="#666"))
    edges.append(Edge(source="naoh_h2o2", target="al_cr_sol", color="#666"))

    # Fe confirmation
    nodes.append(Node(id="kscn", label="+ KSCN", color="#FF9800", size=25))
    nodes.append(Node(id="fe_red", label="[Fe(SCN)]²⁺\n(Merah Darah)", color="#F44336", size=25, shape="box"))
    edges.append(Edge(source="fe_oh", target="kscn", color="#666"))
    edges.append(Edge(source="kscn", target="fe_red", color="#666"))

    # Al confirmation
    nodes.append(Node(id="hcl_slow", label="+ HCl perlahan", color="#FF9800", size=25))
    nodes.append(Node(id="al_oh_back", label="Al(OH)₃\n(Putih/Gel)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="al_cr_sol", target="hcl_slow", color="#666"))
    edges.append(Edge(source="hcl_slow", target="al_oh_back", color="#666"))

    # Cr confirmation
    nodes.append(Node(id="pb_no3", label="+ Pb(NO₃)₂", color="#FF9800", size=25))
    nodes.append(Node(id="cr_yellow", label="PbCrO₄\n(Kuning)", color="#FFD93D", size=25, shape="box"))
    edges.append(Edge(source="al_cr_sol", target="pb_no3", color="#666", dashes=True))
    edges.append(Edge(source="pb_no3", target="cr_yellow", color="#666", dashes=True))

    # ============ GOLONGAN IV ============
    nodes.append(Node(id="nh4co3", label="+ (NH₄)₂CO₃\n+ NH₄OH + NH₄Cl", color="#FF9800", size=25))
    nodes.append(Node(id="group4", label="Endapan Putih\nBaCO₃, SrCO₃, CaCO₃\nGOLONGAN IV", 
                     color="#FFD93D", size=30, shape="box"))
    nodes.append(Node(id="filtrat4", label="Filtrat G-V\n(Mg²⁺, K⁺, Na⁺, NH₄⁺)", 
                     color="#E0E0E0", size=25, shape="box"))

    edges.append(Edge(source="filtrat3", target="nh4co3", color="#666"))
    edges.append(Edge(source="nh4co3", target="group4", color="#666"))
    edges.append(Edge(source="nh4co3", target="filtrat4", color="#666", dashes=True))

    # Group IV branches
    nodes.append(Node(id="acetic", label="+ CH₃COOH", color="#FF9800", size=25))
    nodes.append(Node(id="acetates", label="Ba²⁺, Sr²⁺, Ca²⁺\n(sebagai asetat)", color="#FFF9C4", size=25, shape="box"))
    edges.append(Edge(source="group4", target="acetic", color="#666"))
    edges.append(Edge(source="acetic", target="acetates", color="#666"))

    # Ba separation
    nodes.append(Node(id="k2cro4_g4", label="+ K₂CrO₄", color="#FF9800", size=25))
    nodes.append(Node(id="ba_cro4", label="BaCrO₄\n(Kuning)", color="#FFD93D", size=25, shape="box"))
    nodes.append(Node(id="sr_ca", label="Sr²⁺, Ca²⁺\n(larut)", color="#4ECDC4", size=25, shape="box"))

    edges.append(Edge(source="acetates", target="k2cro4_g4", color="#666"))
    edges.append(Edge(source="k2cro4_g4", target="ba_cro4", color="#666"))
    edges.append(Edge(source="k2cro4_g4", target="sr_ca", color="#666"))

    # Sr separation
    nodes.append(Node(id="ammonium_sulfate", label="+ (NH₄)₂SO₄", color="#FF9800", size=25))
    nodes.append(Node(id="sr_so4", label="SrSO₄\n(Putih)", color="#E0E0E0", size=25, shape="box"))
    nodes.append(Node(id="ca_only", label="Ca²⁺\n(larut)", color="#4ECDC4", size=25, shape="box"))

    edges.append(Edge(source="sr_ca", target="ammonium_sulfate", color="#666"))
    edges.append(Edge(source="ammonium_sulfate", target="sr_so4", color="#666"))
    edges.append(Edge(source="ammonium_sulfate", target="ca_only", color="#666"))

    # Ca confirmation
    nodes.append(Node(id="oxalate", label="+ (NH₄)₂C₂O₄", color="#FF9800", size=25))
    nodes.append(Node(id="ca_ox", label="CaC₂O₄\n(Putih)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="ca_only", target="oxalate", color="#666"))
    edges.append(Edge(source="oxalate", target="ca_ox", color="#666"))

    # ============ GOLONGAN V ============
    nodes.append(Node(id="group5", label="GOLONGAN V\nMg²⁺, K⁺, Na⁺, NH₄⁺\n(Kation Residu)", 
                     color="#6BCB77", size=30, shape="box"))

    edges.append(Edge(source="filtrat4", target="group5", color="#666"))

    # Group V tests
    nodes.append(Node(id="mg_test", label="Mg²⁺: + NH₄OH\n+ (NH₄)₂HPO₄", color="#FF9800", size=25))
    nodes.append(Node(id="mg_precip", label="MgNH₄PO₄·6H₂O\n(Putih)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="group5", target="mg_test", color="#666"))
    edges.append(Edge(source="mg_test", target="mg_precip", color="#666"))

    nodes.append(Node(id="k_test", label="K⁺: + H₂C₄H₄O₆\n(asam tartrat)", color="#FF9800", size=25))
    nodes.append(Node(id="k_precip", label="KHC₄H₄O₆\n(Putih)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="group5", target="k_test", color="#666", dashes=True))
    edges.append(Edge(source="k_test", target="k_precip", color="#666", dashes=True))

    nodes.append(Node(id="na_test", label="Na⁺: + Zn(UO₂)₃\n(CH₃COO)₈", color="#FF9800", size=25))
    nodes.append(Node(id="na_precip", label="Kristal Kuning\nNaZn(UO₂)₃(CH₃COO)₉", color="#FFD93D", size=25, shape="box"))
    edges.append(Edge(source="group5", target="na_test", color="#666", dashes=True))
    edges.append(Edge(source="na_test", target="na_precip", color="#666", dashes=True))

    nodes.append(Node(id="nh4_test", label="NH₄⁺: + NaOH\n+ panas", color="#FF9800", size=25))
    nodes.append(Node(id="nh4_gas", label="Gas NH₃\n(Berbau tajam)", color="#E0E0E0", size=25, shape="box"))
    edges.append(Edge(source="group5", target="nh4_test", color="#666", dashes=True))
    edges.append(Edge(source="nh4_test", target="nh4_gas", color="#666", dashes=True))

    return nodes, edges

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("🧪 Navigasi")
page = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Beranda", "📊 Bagan Interaktif", "🔬 Detail Reaksi", "📝 Kuis", "📚 Referensi"]
)

# ============================================
# HALAMAN BERANDA
# ============================================

if page == "🏠 Beranda":
    st.markdown('<h1 class="main-header">🧪 Analisis Kation Golongan I, III, IV, V</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div style="font-size: 1.2rem; line-height: 1.8;">
        <p>Selamat datang di aplikasi <strong>Analisis Kation</strong>!</p>
        <p>Aplikasi ini dirancang untuk membantu memahami skema analisis kation secara sistematis.</p>
        
        <div style="background-color: #fff3cd; padding: 15px; border-radius: 10px; border-left: 5px solid #ffc107; margin: 15px 0;">
            <strong>⚠️ Catatan Penting:</strong> Aplikasi ini mencakup <strong>Golongan I, III, IV, dan V</strong> saja. 
            Golongan II (Cu²⁺, Cd²⁺, Bi³⁺, Hg²⁺, Sn²⁺, Sb³⁺, As³⁺) dilewati dalam analisis ini.
        </div>

        <h3 style="color: #1f77b4;">📋 Fitur Utama:</h3>
        <ul>
            <li><strong>Bagan Interaktif</strong> - Visualisasi lengkap alur analisis</li>
            <li><strong>Detail Reaksi</strong> - Penjelasan step-by-step setiap reaksi</li>
            <li><strong>Kuis Interaktif</strong> - Uji pemahaman (soal acak dari bank soal)</li>
            <li><strong>Referensi</strong> - Tabel ringkasan reaksi dan warna endapan</li>
        </ul>

        <h3 style="color: #1f77b4;">🔬 Kation yang Dianalisis:</h3>
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f2f6;">
                <th style="padding: 10px; border: 1px solid #ddd;">Golongan</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Kation</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Reagen Pengendap</th>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>I</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Ag⁺, Pb²⁺, Hg₂²⁺</td>
                <td style="padding: 10px; border: 1px solid #ddd;">HCl encer</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>III</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Fe³⁺, Al³⁺, Cr³⁺</td>
                <td style="padding: 10px; border: 1px solid #ddd;">NH₄OH + NH₄Cl</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>IV</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Ba²⁺, Sr²⁺, Ca²⁺</td>
                <td style="padding: 10px; border: 1px solid #ddd;">(NH₄)₂CO₃ + NH₄OH + NH₄Cl</td>
            </tr>
            <tr style="background-color: #f9f9f9;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>V</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">Mg²⁺, K⁺, Na⁺, NH₄⁺</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Tidak terendap</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 20px; border-radius: 15px; margin-top: 20px;">
            <h3 style="color: #1565c0;">💡 Tips Penggunaan</h3>
            <ol>
                <li>Pelajari <strong>Bagan Interaktif</strong> untuk memahami alur analisis</li>
                <li>Baca <strong>Detail Reaksi</strong> untuk memahami setiap langkah</li>
                <li>Uji pemahaman dengan <strong>Kuis</strong> per golongan</li>
                <li>Gunakan <strong>Referensi</strong> untuk mengingat kembali</li>
            </ol>
            <p style="margin-top: 20px; font-style: italic; color: #555;">
                "Kimia analitik adalah seni memisahkan dan mengidentifikasi"
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# HALAMAN BAGAN INTERAKTIF
# ============================================

elif page == "📊 Bagan Interaktif":
    st.markdown('<h1 class="main-header">📊 Bagan Analisis Kation</h1>', unsafe_allow_html=True)

    st.info("🖱️ **Cara menggunakan:** Klik dan drag untuk navigasi, scroll untuk zoom. Hover pada node untuk melihat detail. Garis putus-putus = alur yang dilewati/dilewati.")

    nodes, edges = create_flowchart_nodes()

    config = Config(
        width=1400,
        height=900,
        directed=True,
        physics=True,
        hierarchical=True,
        nodeHighlightBehavior=True,
        highlightColor="#F57C00",
        collapsible=True,
        node={'labelProperty': 'label'},
        link={'labelProperty': 'label', 'renderLabel': False},
        hierarchicalLayout={
            'direction': 'UD',
            'sortMethod': 'directed',
            'levelSeparation': 180,
            'nodeSpacing': 220
        }
    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)

    if return_value:
        st.success(f"Anda memilih: **{return_value}**")

        node_details = {
            "sample": "Sampel awal mengandung kation: Ag⁺, Pb²⁺, Hg₂²⁺, Fe³⁺, Al³⁺, Cr³⁺, Ba²⁺, Sr²⁺, Ca²⁺, Mg²⁺, K⁺, Na⁺, NH₄⁺",
            "group1": "Endapan putih terbentuk: AgCl, PbCl₂, Hg₂Cl₂. Ini adalah Golongan I.",
            "filtrat1": "Filtrat mengandung kation Golongan II-V. Dalam aplikasi ini, Golongan II dilewati.",
            "pb": "PbCl₂ larut dalam air panas karena kelarutannya meningkat dengan suhu.",
            "ag_hg": "AgCl dan Hg₂Cl₂ tidak larut dalam air panas.",
            "pbcro4": "PbCrO₄ adalah endapan kuning yang mengkonfirmasi keberadaan Pb²⁺.",
            "ag_complex": "[Ag(NH₃)₂]⁺ adalah kompleks diamminperak(I) yang larut.",
            "hg_mix": "Hg₂Cl₂ mengalami disproporsionasi: Hg₂²⁺ → Hg⁰ + Hg²⁺",
            "agcl_back": "AgCl terendap kembali saat ditambahkan asam kuat (HNO₃).",
            "skip_g2_note": "Golongan II (Cu²⁺, Cd²⁺, Bi³⁺, Hg²⁺, Sn²⁺, Sb³⁺, As³⁺) dilewati dalam analisis ini.",
            "group3": "Endapan terbentuk: Fe(OH)₃ (coklat), Al(OH)₃ (putih/gel), Cr(OH)₃ (abu-abu/hijau). Ini adalah Golongan III.",
            "filtrat3": "Filtrat mengandung kation Golongan IV dan V.",
            "fe_oh": "Fe(OH)₃ tidak larut dalam basa berlebih (bersifat basa).",
            "al_cr_sol": "Al(OH)₃ larut menjadi [Al(OH)₄]⁻. Cr(OH)₃ dioksidasi menjadi CrO₄²⁻.",
            "al_oh_back": "Al(OH)₃ terendap kembali saat ditambahkan asam perlahan.",
            "fe_red": "[Fe(SCN)]²⁺ adalah kompleks berwarna merah darah yang sangat sensitif.",
            "cr_yellow": "PbCrO₄ berwarna kuning mengkonfirmasi Cr³⁺.",
            "group4": "Endapan putih terbentuk: BaCO₃, SrCO₃, CaCO₃. Ini adalah Golongan IV.",
            "filtrat4": "Filtrat mengandung kation Golongan V.",
            "acetates": "Semua karbonat dilarutkan dengan asam asetat menjadi asetat.",
            "ba_cro4": "BaCrO₄ berwarna kuning mengkonfirmasi Ba²⁺.",
            "sr_so4": "SrSO₄ berwarna putih mengkonfirmasi Sr²⁺.",
            "ca_ox": "CaC₂O₄ berwarna putih mengkonfirmasi Ca²⁺.",
            "group5": "Kation residu yang tidak terendap: Mg²⁺, K⁺, Na⁺, NH₄⁺. Ini adalah Golongan V.",
            "mg_precip": "MgNH₄PO₄·6H₂O (struvit) berwarna putih kristalin.",
            "k_precip": "KHC₄H₄O₆ berwarna putih mengkonfirmasi K⁺.",
            "na_precip": "Kristal kuning NaZn(UO₂)₃(CH₃COO)₉ mengkonfirmasi Na⁺.",
            "nh4_gas": "Gas NH₃ berbau tajam mengkonfirmasi NH₄⁺."
        }

        if return_value in node_details:
            st.markdown(f'<div class="reaction-box">{node_details[return_value]}</div>', 
                       unsafe_allow_html=True)

# ============================================
# HALAMAN DETAIL REAKSI
# ============================================

elif page == "🔬 Detail Reaksi":
    st.markdown('<h1 class="main-header">🔬 Detail Reaksi Analisis</h1>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Golongan I (Ag⁺, Pb²⁺, Hg₂²⁺)", 
        "Golongan III (Fe³⁺, Al³⁺, Cr³⁺)",
        "Golongan IV (Ba²⁺, Sr²⁺, Ca²⁺)",
        "Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺)"
    ])

    with tab1:
        st.markdown('<h2 class="sub-header">Analisis Golongan I</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="cation-card">
            <h3>🧪 Reagen Pengendap: HCl encer</h3>
            <p><strong>Reaksi:</strong></p>
            <ul>
                <li>Ag⁺ + Cl⁻ → <span class="precipitate-white">AgCl↓ (Putih)</span></li>
                <li>Pb²⁺ + 2Cl⁻ → <span class="precipitate-white">PbCl₂↓ (Putih)</span></li>
                <li>Hg₂²⁺ + 2Cl⁻ → <span class="precipitate-white">Hg₂Cl₂↓ (Putih)</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        for i, step in enumerate(cation_data["Golongan I (Ag⁺, Pb²⁺, Hg₂²⁺)"]["steps"], 1):
            with st.expander(f"Langkah {i}: {step['action']}"):
                st.markdown(f"""
                <div class="reaction-box">
                    <p><strong>Aksi:</strong> {step['action']}</p>
                    <p><strong>Hasil:</strong> {step['result']}</p>
                    {f'<p><strong>Filtrat:</strong> {step["filtrate"]}</p>' if 'filtrate' in step else ''}
                    {f'<p><strong>Residu:</strong> {step["residue"]}</p>' if 'residue' in step else ''}
                    {f'<p><strong>Konfirmasi:</strong> <span style="color: green;">{step["confirm"]}</span></p>' if 'confirm' in step else ''}
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<h2 class="sub-header">Analisis Golongan III</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="cation-card">
            <h3>🧪 Reagen Pengendap: NH₄OH berlebih + NH₄Cl</h3>
            <p><strong>Reaksi:</strong></p>
            <ul>
                <li>Fe³⁺ + 3OH⁻ → <span class="precipitate-brown">Fe(OH)₃↓ (Coklat/Merah)</span></li>
                <li>Al³⁺ + 3OH⁻ → <span class="precipitate-white">Al(OH)₃↓ (Putih/Gel)</span></li>
                <li>Cr³⁺ + 3OH⁻ → <span style="color: #6B8E23; font-weight: bold;">Cr(OH)₃↓ (Abu-abu/Hijau)</span></li>
            </ul>
            <p><em>⚠️ <strong>NH₄Cl berfungsi sebagai penyangga</strong> untuk menekan [OH⁻] agar Mg²⁺ tidak ikut terendap sebagai Mg(OH)₂</em></p>
        </div>
        """, unsafe_allow_html=True)

        for i, step in enumerate(cation_data["Golongan III (Fe³⁺, Al³⁺, Cr³⁺)"]["steps"], 1):
            with st.expander(f"Langkah {i}: {step['action']}"):
                st.markdown(f"""
                <div class="reaction-box">
                    <p><strong>Aksi:</strong> {step['action']}</p>
                    <p><strong>Hasil:</strong> {step['result']}</p>
                    {f'<p><strong>Filtrat:</strong> {step["filtrate"]}</p>' if 'filtrate' in step else ''}
                    {f'<p><strong>Residu:</strong> {step["residue"]}</p>' if 'residue' in step else ''}
                    {f'<p><strong>Konfirmasi:</strong> <span style="color: green;">{step["confirm"]}</span></p>' if 'confirm' in step else ''}
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<h2 class="sub-header">Analisis Golongan IV</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="cation-card">
            <h3>🧪 Reagen Pengendap: (NH₄)₂CO₃ + NH₄OH + NH₄Cl</h3>
            <p><strong>Reaksi:</strong></p>
            <ul>
                <li>Ba²⁺ + CO₃²⁻ → <span class="precipitate-white">BaCO₃↓ (Putih)</span></li>
                <li>Sr²⁺ + CO₃²⁻ → <span class="precipitate-white">SrCO₃↓ (Putih)</span></li>
                <li>Ca²⁺ + CO₃²⁻ → <span class="precipitate-white">CaCO₃↓ (Putih)</span></li>
            </ul>
            <p><em>NH₄Cl mencegah pengendapan MgCO₃ yang juga dapat terbentuk dalam kondisi basa</em></p>
        </div>
        """, unsafe_allow_html=True)

        for i, step in enumerate(cation_data["Golongan IV (Ba²⁺, Sr²⁺, Ca²⁺)"]["steps"], 1):
            with st.expander(f"Langkah {i}: {step['action']}"):
                st.markdown(f"""
                <div class="reaction-box">
                    <p><strong>Aksi:</strong> {step['action']}</p>
                    <p><strong>Hasil:</strong> {step['result']}</p>
                    {f'<p><strong>Filtrat:</strong> {step["filtrate"]}</p>' if 'filtrate' in step else ''}
                    {f'<p><strong>Residu:</strong> {step["residue"]}</p>' if 'residue' in step else ''}
                    {f'<p><strong>Konfirmasi:</strong> <span style="color: green;">{step["confirm"]}</span></p>' if 'confirm' in step else ''}
                </div>
                """, unsafe_allow_html=True)

    with tab4:
        st.markdown('<h2 class="sub-header">Analisis Golongan V</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="cation-card">
            <h3>🧪 Tidak ada reagen pengendap spesifik</h3>
            <p>Kation Golongan V adalah <strong>kation residu</strong> yang tersisa setelah pengendapan Golongan I-IV.</p>
            <p><strong>Reaksi Konfirmasi:</strong></p>
            <ul>
                <li>Mg²⁺ + NH₄⁺ + PO₄³⁻ → <span class="precipitate-white">MgNH₄PO₄·6H₂O↓ (Putih)</span></li>
                <li>K⁺ + HC₄H₄O₆⁻ → <span class="precipitate-white">KHC₄H₄O₆↓ (Putih)</span></li>
                <li>Na⁺ + Zn(UO₂)₃(CH₃COO)₈ → <span class="precipitate-yellow">NaZn(UO₂)₃(CH₃COO)₉·6H₂O (Kuning)</span></li>
                <li>NH₄⁺ + OH⁻ → <span class="solution-red">NH₃↑ + H₂O</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        for i, step in enumerate(cation_data["Golongan V (Mg²⁺, K⁺, Na⁺, NH₄⁺)"]["steps"], 1):
            with st.expander(f"Langkah {i}: {step['action']}"):
                st.markdown(f"""
                <div class="reaction-box">
                    <p><strong>Aksi:</strong> {step['action']}</p>
                    <p><strong>Hasil:</strong> {step['result']}</p>
                    {f'<p><strong>Konfirmasi:</strong> <span style="color: green;">{step["confirm"]}</span></p>' if 'confirm' in step else ''}
                </div>
                """, unsafe_allow_html=True)

# ============================================
# HALAMAN KUIS (MENGGUNAKAN STORAGE SOAL)
# ============================================

elif page == "📝 Kuis":
    st.markdown('<h1 class="main-header">📝 Kuis Analisis Kation</h1>', unsafe_allow_html=True)

    # Pilih golongan
    selected_group = st.selectbox(
        "Pilih Golongan:",
        ["Golongan I", "Golongan III", "Golongan IV", "Golongan V"]
    )

    # Ambil soal acak dari storage (10 soal)
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

    # Progress bar
    progress = (state['current_question']) / len(quiz_list)
    st.progress(progress)
    st.write(f"Soal {state['current_question'] + 1} dari {len(quiz_list)} | Skor: {state['score']}")

    if state['current_question'] < len(quiz_list):
        q = quiz_list[state['current_question']]

        st.markdown(f"""
        <div class="cation-card">
            <h3>{q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        # Tampilkan opsi
        for i, option in enumerate(q['options']):
            col1, col2 = st.columns([1, 10])
            with col1:
                st.write(f"{chr(65+i)}.")
            with col2:
                if not state['answered']:
                    if st.button(option, key=f"opt_{selected_group}_{i}_{state['current_question']}", use_container_width=True):
                        state['answered'] = True
                        state['selected_option'] = i
                        if i == q['correct']:
                            state['score'] += 1
                        st.rerun()
                else:
                    if i == q['correct']:
                        st.markdown(f'<div class="quiz-option correct">✅ {option}</div>', 
                                   unsafe_allow_html=True)
                    elif i == state['selected_option'] and i != q['correct']:
                        st.markdown(f'<div class="quiz-option wrong">❌ {option}</div>', 
                                   unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="quiz-option">{option}</div>', 
                                   unsafe_allow_html=True)

        if state['answered']:
            st.markdown(f"""
            <div class="reaction-box" style="margin-top: 20px;">
                <h4>💡 Penjelasan:</h4>
                <p>{q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Soal Berikutnya →", type="primary", use_container_width=True):
                state['current_question'] += 1
                state['answered'] = False
                state['selected_option'] = None
                st.rerun()
    else:
        # Hasil akhir
        score_percent = (state['score'] / len(quiz_list)) * 100

        st.markdown(f"""
        <div class="cation-card" style="text-align: center;">
            <h1>🎉 Kuis {selected_group} Selesai!</h1>
            <h2>Skor Anda: {state['score']}/{len(quiz_list)} ({score_percent:.0f}%)</h2>
        </div>
        """, unsafe_allow_html=True)

        if score_percent >= 80:
            st.balloons()
            st.success("🏆 Luar biasa! Anda menguasai materi ini dengan sangat baik!")
        elif score_percent >= 60:
            st.info("👍 Bagus! Pemahaman Anda sudah cukup baik, tingkatkan lagi!")
        else:
            st.warning("📚 Perlu belajar lagi. Pelajari bagan dan detail reaksi dengan lebih teliti.")

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
# HALAMAN REFERENSI
# ============================================

elif page == "📚 Referensi":
    st.markdown('<h1 class="main-header">📚 Tabel Referensi</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="cation-card">
        <h3>🎨 Warna Endapan dan Larutan</h3>
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #1f77b4; color: white;">
                <th style="padding: 12px; border: 1px solid #ddd;">Senyawa</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Warna</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Keterangan</th>
            </tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">AgCl</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Larut dalam NH₄OH</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">PbCl₂</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Larut dalam air panas</td></tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">Hg₂Cl₂</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Berubah hitam dengan NH₄OH</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">PbCrO₄</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-yellow">Kuning</span></td><td style="padding: 10px; border: 1px solid #ddd;">Konfirmasi Pb²⁺</td></tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">Fe(OH)₃</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-brown">Coklat/Merah</span></td><td style="padding: 10px; border: 1px solid #ddd;">Tidak larut dalam basa berlebih</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">Al(OH)₃</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih/Gel</span></td><td style="padding: 10px; border: 1px solid #ddd;">Amfoter, larut dalam NaOH berlebih</td></tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">Cr(OH)₃</td><td style="padding: 10px; border: 1px solid #ddd;"><span style="color: #6B8E23; font-weight: bold;">Abu-abu/Hijau</span></td><td style="padding: 10px; border: 1px solid #ddd;">Dioksidasi jadi CrO₄²⁻ dengan H₂O₂</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">BaCrO₄</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-yellow">Kuning</span></td><td style="padding: 10px; border: 1px solid #ddd;">Konfirmasi Ba²⁺</td></tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">SrSO₄</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Konfirmasi Sr²⁺</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">CaC₂O₄</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Konfirmasi Ca²⁺</td></tr>
            <tr><td style="padding: 10px; border: 1px solid #ddd;">[Fe(SCN)]²⁺</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="solution-red">Merah Darah</span></td><td style="padding: 10px; border: 1px solid #ddd;">Konfirmasi Fe³⁺</td></tr>
            <tr style="background-color: #f9f9f9;"><td style="padding: 10px; border: 1px solid #ddd;">MgNH₄PO₄·6H₂O</td><td style="padding: 10px; border: 1px solid #ddd;"><span class="precipitate-white">Putih</span></td><td style="padding: 10px; border: 1px solid #ddd;">Struvit, konfirmasi Mg²⁺</td></tr>
        </table>
    </div>

    <div class="cation-card" style="margin-top: 20px;">
        <h3>⚗️ Rangkuman Reaksi Kimia</h3>
        <h4>Golongan I:</h4>
        <ul>
            <li>Pb²⁺ + 2Cl⁻ → PbCl₂↓ (Putih) → <strong>H₂O panas</strong> → larut → + K₂CrO₄ → PbCrO₄↓ (Kuning)</li>
            <li>Ag⁺ + Cl⁻ → AgCl↓ (Putih) → <strong>NH₄OH</strong> → [Ag(NH₃)₂]⁺ → <strong>HNO₃</strong> → AgCl↓ (Putih)</li>
            <li>Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂↓ (Putih) → <strong>NH₄OH</strong> → Hg↓ (Hitam) + Hg(NH₂)Cl↓ (Putih)</li>
        </ul>
        <h4>Golongan III:</h4>
        <ul>
            <li>Fe³⁺ + 3OH⁻ → Fe(OH)₃↓ (Coklat) → <strong>KSCN</strong> → [Fe(SCN)]²⁺ (Merah Darah)</li>
            <li>Al³⁺ + 3OH⁻ → Al(OH)₃↓ (Putih/Gel) → <strong>NaOH berlebih</strong> → [Al(OH)₄]⁻ → <strong>HCl</strong> → Al(OH)₃↓</li>
            <li>Cr³⁺ + 3OH⁻ → Cr(OH)₃↓ (Abu²) → <strong>NaOH + H₂O₂</strong> → CrO₄²⁻ → <strong>Pb(NO₃)₂</strong> → PbCrO₄↓ (Kuning)</li>
        </ul>
        <h4>Golongan IV:</h4>
        <ul>
            <li>Ba²⁺ + CO₃²⁻ → BaCO₃↓ (Putih) → <strong>CH₃COOH</strong> → Ba²⁺ → <strong>K₂CrO₄</strong> → BaCrO₄↓ (Kuning)</li>
            <li>Sr²⁺ + CO₃²⁻ → SrCO₃↓ (Putih) → <strong>CH₃COOH</strong> → Sr²⁺ → <strong>(NH₄)₂SO₄</strong> → SrSO₄↓ (Putih)</li>
            <li>Ca²⁺ + CO₃²⁻ → CaCO₃↓ (Putih) → <strong>CH₃COOH</strong> → Ca²⁺ → <strong>(NH₄)₂C₂O₄</strong> → CaC₂O₄↓ (Putih)</li>
        </ul>
        <h4>Golongan V:</h4>
        <ul>
            <li>Mg²⁺ + NH₄⁺ + PO₄³⁻ → MgNH₄PO₄·6H₂O↓ (Putih)</li>
            <li>K⁺ + HC₄H₄O₆⁻ → KHC₄H₄O₆↓ (Putih)</li>
            <li>Na⁺ + Zn(UO₂)₃(CH₃COO)₈ → NaZn(UO₂)₃(CH₃COO)₉·6H₂O (Kuning)</li>
            <li>NH₄⁺ + OH⁻ → NH₃↑ + H₂O (gas berbau tajam)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================

st.sidebar.markdown("---")
st.sidebar.info("""
**Aplikasi Analisis Kation** 
Dibuat untuk pembelajaran kimia analitik

Versi 2.0 | 2026
""")