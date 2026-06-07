"""
================================================================================
QUIZ STORAGE - Bank Soal Analisis Kation
================================================================================
File ini berisi bank soal untuk setiap golongan.
Setiap golongan memiliki 20 soal.
Soal diambil secara acak saat kuis dimulai.
================================================================================
"""

import random

# ============================================
# GOLONGAN I - 20 SOAL
# ============================================

QUIZ_G1 = [
    {
        "question": "Kation manakah yang membentuk endapan putih dengan HCl encer, kemudian larut dalam air panas?",
        "options": ["Ag⁺", "Pb²⁺", "Hg₂²⁺", "Ba²⁺"],
        "correct": 1,
        "explanation": "PbCl₂ membentuk endapan putih dengan HCl encer dan larut dalam air panas, sedangkan AgCl dan Hg₂Cl₂ tidak larut."
    },
    {
        "question": "Apa warna endapan yang terbentuk saat Pb²⁺ direaksikan dengan K₂CrO₄?",
        "options": ["Putih", "Kuning", "Hitam", "Merah"],
        "correct": 1,
        "explanation": "PbCrO₄ membentuk endapan berwarna kuning."
    },
    {
        "question": "Bagaimana perbedaan antara AgCl dan Hg₂Cl₂ saat ditambahkan NH₄OH?",
        "options": ["Keduanya larut", "AgCl larut, Hg₂Cl₂ berubah menjadi hitam + putih", "Keduanya tidak larut", "Hg₂Cl₂ larut, AgCl tidak larut"],
        "correct": 1,
        "explanation": "AgCl larut dalam NH₄OH membentuk kompleks [Ag(NH₃)₂]⁺, sedangkan Hg₂Cl₂ mengalami disproporsionasi menjadi Hg (hitam) dan Hg(NH₂)Cl (putih)."
    },
    {
        "question": "Reagen apa yang digunakan untuk mengkonfirmasi kembali Ag⁺ setelah larut dalam NH₄OH?",
        "options": ["HCl", "HNO₃", "NaOH", "K₂CrO₄"],
        "correct": 1,
        "explanation": "HNO₃ ditambahkan untuk menguraikan kompleks [Ag(NH₃)₂]⁺ sehingga AgCl terendap kembali."
    },
    {
        "question": "Mengapa PbCl₂ larut dalam air panas sedangkan AgCl tidak?",
        "options": ["PbCl₂ bersifat amfoter", "Kelarutan PbCl₂ meningkat dengan suhu", "AgCl bersifat reduktor", "PbCl₂ terhidrolisis"],
        "correct": 1,
        "explanation": "Kelarutan PbCl₂ meningkat secara signifikan dengan kenaikan suhu, sementara kelarutan AgCl hampir tidak berubah."
    },
    {
        "question": "Apa warna endapan Hg₂Cl₂ setelah ditambahkan NH₄OH?",
        "options": ["Putih saja", "Hitam saja", "Hitam dan putih", "Kuning"],
        "correct": 2,
        "explanation": "Hg₂Cl₂ mengalami disproporsionasi membentuk Hg (hitam) dan Hg(NH₂)Cl (putih)."
    },
    {
        "question": "Ion kompleks apa yang terbentuk saat AgCl larut dalam NH₄OH?",
        "options": ["[Ag(NH₃)]⁺", "[Ag(NH₃)₂]⁺", "[Ag(OH)₂]⁻", "[AgCl₂]⁻"],
        "correct": 1,
        "explanation": "AgCl larut dalam NH₄OH membentuk kompleks diamminperak(I) [Ag(NH₃)₂]⁺."
    },
    {
        "question": "Golongan I juga dikenal sebagai golongan kation apa?",
        "options": ["Kation basa kuat", "Kation asam", "Kation logam berat", "Kation logam alkali"],
        "correct": 2,
        "explanation": "Ag⁺, Pb²⁺, dan Hg₂²⁺ termasuk kation logam berat yang terendap oleh HCl encer."
    },
    {
        "question": "Mengapa HCl encer dapat mengendapkan kation Golongan I?",
        "options": ["Karena Cl⁻ merupakan reduktor kuat", "Karena kelarutan kloridanya sangat rendah", "Karena terjadi hidrolisis", "Karena Cl⁻ merupakan oksidator"],
        "correct": 1,
        "explanation": "AgCl, PbCl₂, dan Hg₂Cl₂ memiliki kelarutan yang sangat rendah dalam air (Ksp kecil)."
    },
    {
        "question": "Apa yang terjadi jika endapan Golongan I langsung ditambahkan NH₄OH tanpa pemanasan air terlebih dahulu?",
        "options": ["PbCl₂ ikut larut membentuk kompleks", "Semua endapan larut", "Tidak ada perubahan", "PbCl₂ tetap sebagai endapan"],
        "correct": 0,
        "explanation": "PbCl₂ juga dapat larut sebagian dalam NH₄OH membentuk kompleks, sehingga pemisahan dengan air panas penting."
    },
    {
        "question": "Berapa koordinasi kompleks [Ag(NH₃)₂]⁺?",
        "options": ["1", "2", "3", "4"],
        "correct": 1,
        "explanation": "[Ag(NH₃)₂]⁺ memiliki koordinasi 2 dengan dua ligand NH₃."
    },
    {
        "question": "Apa nama reaksi yang dialami Hg₂Cl₂ dengan NH₄OH?",
        "options": ["Redoks", "Disproporsionasi", "Hidrolisis", "Netralisasi"],
        "correct": 1,
        "explanation": "Hg₂²⁺ mengalami disproporsionasi menjadi Hg⁰ dan Hg²⁺."
    },
    {
        "question": "Kation mana yang TIDAK termasuk Golongan I?",
        "options": ["Ag⁺", "Pb²⁺", "Cu²⁺", "Hg₂²⁺"],
        "correct": 2,
        "explanation": "Cu²⁺ termasuk Golongan II, bukan Golongan I."
    },
    {
        "question": "Apa fungsi pemanasan air dalam analisis Golongan I?",
        "options": ["Mempercepat reaksi", "Melarutkan PbCl₂", "Menguraikan AgCl", "Mengoksidasi Hg₂Cl₂"],
        "correct": 1,
        "explanation": "Pemanasan air digunakan untuk melarutkan PbCl₂ agar terpisah dari AgCl dan Hg₂Cl₂."
    },
    {
        "question": "Senyawa apa yang terbentuk saat Pb²⁺ ditambahkan K₂CrO₄?",
        "options": ["PbCl₂", "PbCrO₄", "PbSO₄", "PbCO₃"],
        "correct": 1,
        "explanation": "Pb²⁺ + CrO₄²⁻ → PbCrO₄↓ (kuning)."
    },
    {
        "question": "Mengapa AgCl dapat larut dalam NH₄OH?",
        "options": ["Karena pembentukan kompleks", "Karena reaksi redoks", "Karena hidrolisis", "Karena penguraian"],
        "correct": 0,
        "explanation": "AgCl larut karena pembentukan kompleks [Ag(NH₃)₂]⁺ yang stabil."
    },
    {
        "question": "Apa warna endapan awal AgCl?",
        "options": ["Kuning", "Putih", "Hitam", "Coklat"],
        "correct": 1,
        "explanation": "AgCl membentuk endapan putih."
    },
    {
        "question": "Reagen apa yang digunakan untuk memisahkan Pb²⁺ dari Ag⁺ dan Hg₂²⁺?",
        "options": ["NH₄OH", "H₂O panas", "K₂CrO₄", "HNO₃"],
        "correct": 1,
        "explanation": "H₂O panas melarutkan PbCl₂ sedangkan AgCl dan Hg₂Cl₂ tidak larut."
    },
    {
        "question": "Apa yang terjadi pada Hg₂Cl₂ saat ditambahkan NH₄OH?",
        "options": ["Larut membentuk kompleks", "Berubah menjadi Hg hitam dan Hg(NH₂)Cl putih", "Tetap putih", "Mengendap lebih banyak"],
        "correct": 1,
        "explanation": "Hg₂Cl₂ mengalami disproporsionasi: Hg₂Cl₂ + 2NH₄OH → Hg↓ + Hg(NH₂)Cl↓ + NH₄Cl + H₂O."
    },
    {
        "question": "Kation Golongan I dapat dipisahkan berdasarkan sifat apa?",
        "options": ["Warna", "Kelarutan dalam air panas dan NH₄OH", "Densitas", "Titik leleh"],
        "correct": 1,
        "explanation": "PbCl₂ larut dalam air panas, AgCl larut dalam NH₄OH, dan Hg₂Cl₂ berubah warna dengan NH₄OH."
    }
]

# ============================================
# GOLONGAN III - 20 SOAL
# ============================================

QUIZ_G3 = [
    {
        "question": "Reagen pengendap untuk Golongan III adalah?",
        "options": ["HCl encer", "H₂S dalam suasana asam", "NH₄OH + NH₄Cl", "(NH₄)₂CO₃"],
        "correct": 2,
        "explanation": "Golongan III menggunakan NH₄OH berlebih + NH₄Cl untuk mengendapkan Fe(OH)₃, Al(OH)₃, dan Cr(OH)₃."
    },
    {
        "question": "Apa fungsi NH₄Cl dalam pengendapan Golongan III?",
        "options": ["Sebagai katalis", "Menekan ionisasi NH₄OH sehingga OH⁻ tidak cukup untuk Mg(OH)₂", "Memberikan warna", "Menghasilkan panas"],
        "correct": 1,
        "explanation": "NH₄Cl menekan ionisasi NH₄OH (efek ion senama) sehingga konsentrasi OH⁻ cukup untuk mengendapkan Fe(OH)₃, Al(OH)₃, Cr(OH)₃ tetapi tidak cukup untuk Mg(OH)₂."
    },
    {
        "question": "Kation manakah yang membentuk endapan coklat/merah dengan NH₄OH?",
        "options": ["Al³⁺", "Fe³⁺", "Cr³⁺", "Mg²⁺"],
        "correct": 1,
        "explanation": "Fe(OH)₃ membentuk endapan berwarna coklat/merah, sedangkan Al(OH)₃ putih/gel dan Cr(OH)₃ abu-abu/hijau."
    },
    {
        "question": "Apa yang terjadi pada Al(OH)₃ saat ditambahkan NaOH berlebih?",
        "options": ["Tetap sebagai endapan", "Larut membentuk [Al(OH)₄]⁻", "Berubah warna menjadi merah", "Mengendap lebih banyak"],
        "correct": 1,
        "explanation": "Al(OH)₃ bersifat amfoter dan larut dalam NaOH berlebih membentuk ion aluminate [Al(OH)₄]⁻."
    },
    {
        "question": "Reagen apa yang digunakan untuk mengkonfirmasi Fe³⁺?",
        "options": ["K₂CrO₄", "KSCN", "NH₄OH", "HCl"],
        "correct": 1,
        "explanation": "Fe³⁺ membentuk kompleks merah darah [Fe(SCN)]²⁺ dengan KSCN."
    },
    {
        "question": "Bagaimana cara memisahkan Al³⁺ dan Cr³⁺ dari Fe³⁺?",
        "options": ["Tambahkan HCl", "Tambahkan NaOH berlebih + H₂O₂", "Tambahkan KSCN", "Tambahkan NH₄Cl"],
        "correct": 1,
        "explanation": "NaOH berlebih + H₂O₂ membuat Al(OH)₃ larut menjadi [Al(OH)₄]⁻ dan Cr(OH)₃ teroksidasi menjadi CrO₄²⁻, sedangkan Fe(OH)₃ tidak larut."
    },
    {
        "question": "Apa warna endapan Cr(OH)₃?",
        "options": ["Putih", "Coklat", "Abu-abu/hijau", "Kuning"],
        "correct": 2,
        "explanation": "Cr(OH)₃ membentuk endapan berwarna abu-abu kehijauan."
    },
    {
        "question": "Mengapa Mg²⁺ tidak ikut terendap dalam Golongan III?",
        "options": ["Karena Mg²⁺ sudah terendap sebelumnya", "Karena Ksp Mg(OH)₂ lebih besar dan [OH⁻] ditekan oleh NH₄Cl", "Karena Mg²⁺ membentuk kompleks", "Karena Mg²⁺ tidak bereaksi dengan NH₄OH"],
        "correct": 1,
        "explanation": "Ksp Mg(OH)₂ relatif besar. Dengan adanya NH₄Cl, [OH⁻] diturunkan hingga di bawah ambang pengendapan Mg(OH)₂."
    },
    {
        "question": "Apa yang terjadi pada Cr(OH)₃ saat ditambahkan NaOH berlebih dan H₂O₂?",
        "options": ["Tetap sebagai endapan", "Larut menjadi CrO₄²⁻", "Berubah menjadi Cr₂O₃", "Mengendap lebih banyak"],
        "correct": 1,
        "explanation": "H₂O₂ mengoksidasi Cr(III) menjadi Cr(VI) yang larut sebagai kromat (CrO₄²⁻)."
    },
    {
        "question": "Bagaimana mengkonfirmasi kembali Al³⁺ setelah larut dalam NaOH berlebih?",
        "options": ["Tambahkan KSCN", "Tambahkan HCl perlahan", "Tambahkan NH₄OH", "Tambahkan H₂O₂"],
        "correct": 1,
        "explanation": "Penambahan HCl perlahan menurunkan pH sehingga Al(OH)₃ terendap kembali."
    },
    {
        "question": "Apa nama kompleks berwarna merah darah yang terbentuk dari Fe³⁺ dan KSCN?",
        "options": ["[Fe(SCN)]²⁺", "[Fe(SCN)₂]⁺", "[Fe(SCN)₃]", "[Fe(SCN)₄]⁻"],
        "correct": 0,
        "explanation": "[Fe(SCN)]²⁺ adalah kompleks berwarna merah darah yang sangat sensitif."
    },
    {
        "question": "Mengapa NH₄Cl disebut penyangga dalam pengendapan Golongan III?",
        "options": ["Karena menstabilkan pH", "Karena menekan [OH⁻] melalui efek ion senama", "Karena memberikan ion NH₄⁺", "Karena mencegah oksidasi"],
        "correct": 1,
        "explanation": "NH₄Cl menekan ionisasi NH₄OH sehingga [OH⁻] terkontrol."
    },
    {
        "question": "Kation mana yang termasuk Golongan III?",
        "options": ["Cu²⁺, Cd²⁺", "Fe³⁺, Al³⁺, Cr³⁺", "Ba²⁺, Sr²⁺, Ca²⁺", "Ag⁺, Pb²⁺"],
        "correct": 1,
        "explanation": "Golongan III terdiri dari Fe³⁺, Al³⁺, dan Cr³⁺."
    },
    {
        "question": "Apa yang dimaksud sifat amfoter Al(OH)₃?",
        "options": ["Larut dalam asam dan basa", "Hanya larut dalam asam", "Hanya larut dalam basa", "Tidak larut dalam keduanya"],
        "correct": 0,
        "explanation": "Al(OH)₃ bersifat amfoter, artinya dapat larut dalam asam kuat maupun basa kuat berlebih."
    },
    {
        "question": "Reagen apa yang digunakan untuk mengkonfirmasi Cr³⁺?",
        "options": ["KSCN", "Pb(NO₃)₂", "HCl", "NH₄OH"],
        "correct": 1,
        "explanation": "CrO₄²⁻ yang terbentuk direaksikan dengan Pb(NO₃)₂ membentuk PbCrO₄ kuning."
    },
    {
        "question": "Apa peran H₂O₂ dalam analisis Golongan III?",
        "options": ["Sebagai reduktor", "Sebagai oksidator untuk Cr(III) menjadi Cr(VI)", "Sebagai katalis", "Sebagai penyangga"],
        "correct": 1,
        "explanation": "H₂O₂ mengoksidasi Cr³⁺ menjadi CrO₄²⁻ (Cr VI) yang larut dalam air."
    },
    {
        "question": "Mengapa Fe(OH)₃ tidak larut dalam NaOH berlebih?",
        "options": ["Karena bersifat basa", "Karena bersifat asam", "Karena teroksidasi", "Karena tereduksi"],
        "correct": 0,
        "explanation": "Fe(OH)₃ bersifat basa (bukan amfoter) sehingga tidak larut dalam basa berlebih."
    },
    {
        "question": "Apa warna larutan setelah Fe³⁺ ditambahkan KSCN?",
        "options": ["Kuning", "Merah darah", "Hijau", "Biru"],
        "correct": 1,
        "explanation": "[Fe(SCN)]²⁺ berwarna merah darah yang sangat khas."
    },
    {
        "question": "Kation mana yang akan mengganggu analisis Golongan III jika tidak ditambahkan NH₄Cl?",
        "options": ["Na⁺", "K⁺", "Mg²⁺", "Ca²⁺"],
        "correct": 2,
        "explanation": "Tanpa NH₄Cl, Mg²⁺ akan ikut terendap sebagai Mg(OH)₂ karena [OH⁻] terlalu tinggi."
    },
    {
        "question": "Apa nama ion aluminate?",
        "options": ["[Al(OH)₃]⁻", "[Al(OH)₄]⁻", "[AlO₂]⁻", "[Al(H₂O)₆]³⁺"],
        "correct": 1,
        "explanation": "Al(OH)₃ larut dalam NaOH berlebih membentuk ion aluminate [Al(OH)₄]⁻."
    }
]

# ============================================
# GOLONGAN IV - 20 SOAL
# ============================================

QUIZ_G4 = [
    {
        "question": "Reagen pengendap untuk Golongan IV adalah?",
        "options": ["HCl encer", "H₂S", "NH₄OH + NH₄Cl", "(NH₄)₂CO₃ + NH₄OH + NH₄Cl"],
        "correct": 3,
        "explanation": "Golongan IV menggunakan (NH₄)₂CO₃ dalam suasana basa (NH₄OH) dengan adanya NH₄Cl."
    },
    {
        "question": "Kation manakah yang termasuk Golongan IV?",
        "options": ["Cu²⁺, Cd²⁺", "Fe³⁺, Al³⁺", "Ba²⁺, Sr²⁺, Ca²⁺", "Ag⁺, Pb²⁺"],
        "correct": 2,
        "explanation": "Ba²⁺, Sr²⁺, dan Ca²⁺ adalah kation basa alkali tanah yang termasuk Golongan IV."
    },
    {
        "question": "Apa fungsi NH₄Cl dalam pengendapan Golongan IV?",
        "options": ["Sebagai katalis", "Mencegah pengendapan MgCO₃", "Memberikan warna", "Menghasilkan panas"],
        "correct": 1,
        "explanation": "NH₄Cl mencegah pengendapan MgCO₃ dengan menekan ionisasi (NH₄)₂CO₃."
    },
    {
        "question": "Kation manakah yang membentuk endapan kuning dengan K₂CrO₄ dalam Golongan IV?",
        "options": ["Sr²⁺", "Ca²⁺", "Ba²⁺", "Mg²⁺"],
        "correct": 2,
        "explanation": "BaCrO₄ membentuk endapan kuning, sedangkan Sr²⁺ dan Ca²⁺ tidak bereaksi dengan K₂CrO₄ dalam kondisi ini."
    },
    {
        "question": "Apa warna endapan CaC₂O₄ yang terbentuk dari reaksi Ca²⁺ dengan (NH₄)₂C₂O₄?",
        "options": ["Kuning", "Putih", "Hitam", "Merah"],
        "correct": 1,
        "explanation": "CaC₂O₄ (kalsium oksalat) membentuk endapan putih."
    },
    {
        "question": "Bagaimana memisahkan Ba²⁺ dari Sr²⁺ dan Ca²⁺?",
        "options": ["Tambahkan K₂CrO₄", "Tambahkan (NH₄)₂SO₄", "Tambahkan NaOH", "Tambahkan HCl"],
        "correct": 0,
        "explanation": "Ba²⁺ membentuk endapan kuning BaCrO₄, sedangkan Sr²⁺ dan Ca²⁺ tetap larut."
    },
    {
        "question": "Bagaimana memisahkan Sr²⁺ dari Ca²⁺?",
        "options": ["Tambahkan K₂CrO₄", "Tambahkan (NH₄)₂SO₄", "Tambahkan NaOH", "Tambahkan HCl"],
        "correct": 1,
        "explanation": "Sr²⁺ membentuk endapan putih SrSO₄, sedangkan Ca²⁺ tetap larut."
    },
    {
        "question": "Apa warna endapan karbonat Golongan IV (BaCO₃, SrCO₃, CaCO₃)?",
        "options": ["Kuning", "Putih", "Hitam", "Coklat"],
        "correct": 1,
        "explanation": "Semua karbonat Golongan IV membentuk endapan putih."
    },
    {
        "question": "Mengapa endapan karbonat Golongan IV dilarutkan dengan asam asetat terlebih dahulu?",
        "options": ["Untuk menghilangkan warna", "Untuk mengubah menjadi asetat agar dapat dipisahkan", "Untuk mengoksidasi", "Untuk mengurangi volume"],
        "correct": 1,
        "explanation": "Asam asetat melarutkan karbonat menjadi asetat yang lebih mudah dipisahkan dengan reagen selanjutnya."
    },
    {
        "question": "Kation manakah yang terakhir dikonfirmasi dalam analisis Golongan IV?",
        "options": ["Ba²⁺", "Ca²⁺", "Sr²⁺", "Mg²⁺"],
        "correct": 1,
        "explanation": "Ca²⁺ dikonfirmasi terakhir dengan membentuk endapan putih CaC₂O₄ menggunakan (NH₄)₂C₂O₄."
    },
    {
        "question": "Apa nama lain dari kation Golongan IV?",
        "options": ["Kation logam berat", "Kation basa alkali tanah", "Kation logam transisi", "Kation halogen"],
        "correct": 1,
        "explanation": "Ba²⁺, Sr²⁺, Ca²⁺ termasuk kation basa alkali tanah (alkaline earth metals)."
    },
    {
        "question": "Mengapa BaCrO₄ berwarna kuning?",
        "options": ["Karena kromat", "Karena barium", "Karena oksidasi", "Karena reduksi"],
        "correct": 0,
        "explanation": "Ion kromat (CrO₄²⁻) memberikan warna kuning pada senyawanya."
    },
    {
        "question": "Apa yang terjadi jika (NH₄)₂CO₃ ditambahkan tanpa NH₄OH?",
        "options": ["Mg²⁺ ikut terendap", "Tidak ada perubahan", "Endapan tidak terbentuk", "Reaksi lebih cepat"],
        "correct": 0,
        "explanation": "Tanpa NH₄OH, kondisi tidak cukup basa dan Mg²⁺ dapat ikut terendap sebagai MgCO₃."
    },
    {
        "question": "Reagen apa yang digunakan untuk mengkonfirmasi Sr²⁺?",
        "options": ["K₂CrO₄", "(NH₄)₂SO₄", "(NH₄)₂C₂O₄", "NaOH"],
        "correct": 1,
        "explanation": "Sr²⁺ membentuk endapan putih SrSO₄ dengan (NH₄)₂SO₄."
    },
    {
        "question": "Apa warna endapan SrSO₄?",
        "options": ["Kuning", "Putih", "Hitam", "Merah"],
        "correct": 1,
        "explanation": "SrSO₄ membentuk endapan putih."
    },
    {
        "question": "Mengapa Ca²⁺ tidak terendap dengan (NH₄)₂SO₄?",
        "options": ["Karena CaSO₄ larut", "Karena Ca²⁺ tidak bereaksi", "Karena terbentuk kompleks", "Karena teroksidasi"],
        "correct": 0,
        "explanation": "CaSO₄ memiliki kelarutan yang lebih tinggi dibandingkan SrSO₄ sehingga Ca²⁺ tetap larut."
    },
    {
        "question": "Apa nama senyawa CaC₂O₄?",
        "options": ["Kalsium sulfat", "Kalsium oksalat", "Kalsium karbonat", "Kalsium fosfat"],
        "correct": 1,
        "explanation": "CaC₂O₄ adalah kalsium oksalat."
    },
    {
        "question": "Kation Golongan IV berasal dari golongan berapa dalam sistem periodik?",
        "options": ["Golongan 1", "Golongan 2", "Golongan 13", "Golongan 14"],
        "correct": 1,
        "explanation": "Ba, Sr, Ca termasuk Golongan 2 (alkali tanah) dalam sistem periodik."
    },
    {
        "question": "Apa yang terjadi pada BaCO₃ saat ditambahkan asam asetat?",
        "options": ["Tetap sebagai endapan", "Larut membentuk Ba(CH₃COO)₂", "Berubah warna", "Mengendap lebih banyak"],
        "correct": 1,
        "explanation": "BaCO₃ + 2CH₃COOH → Ba(CH₃COO)₂ + H₂O + CO₂↑"
    },
    {
        "question": "Mengapa analisis Golongan IV memerlukan suasana basa (NH₄OH)?",
        "options": ["Agar reaksi lebih cepat", "Agar karbonat terendap sempurna", "Agar Mg²⁺ tidak terendap", "Agar warna lebih jelas"],
        "correct": 1,
        "explanation": "Suasana basa memastikan ion CO₃²⁻ cukup untuk mengendapkan Ba²⁺, Sr²⁺, Ca²⁺ sebagai karbonat."
    }
]

# ============================================
# FUNGSI UNTUK MENGAMBIL SOAL ACAK
# ============================================

def get_random_questions(group_name, num_questions=10):
    """
    Mengambil soal secara acak dari bank soal.
    
    Parameters:
        group_name (str): Nama golongan ("Golongan I", "Golongan III", "Golongan IV")
        num_questions (int): Jumlah soal yang diambil (default: 10)
    
    Returns:
        list: Daftar soal yang diacak
    """
    group_map = {
        "Golongan I": QUIZ_G1,
        "Golongan III": QUIZ_G3,
        "Golongan IV": QUIZ_G4
    }
    
    if group_name not in group_map:
        return []
    
    questions = group_map[group_name]
    
    # Jika jumlah soal yang diminta lebih banyak dari yang tersedia, ambil semua
    if num_questions >= len(questions):
        return random.sample(questions, len(questions))
    
    # Ambil soal secara acak
    return random.sample(questions, num_questions)

# ============================================
# FUNGSI UNTUK MELIHAT SEMUA SOAL (DEBUG)
# ============================================

def get_all_questions(group_name):
    """Mengembalikan semua soal dari suatu golongan (untuk debug)."""
    group_map = {
        "Golongan I": QUIZ_G1,
        "Golongan III": QUIZ_G3,
        "Golongan IV": QUIZ_G4
    }
    return group_map.get(group_name, [])

def get_total_questions():
    """Mengembalikan jumlah total soal di bank."""
    return {
        "Golongan I": len(QUIZ_G1),
        "Golongan III": len(QUIZ_G3),
        "Golongan IV": len(QUIZ_G4),
        "TOTAL": len(QUIZ_G1) + len(QUIZ_G3) + len(QUIZ_G4) 
    }
