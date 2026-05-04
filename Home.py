import streamlit as st
import os

# =========================
# 🚀 HEALTH CHECK (FOR UPTIME ROBOT)
# =========================
if os.getenv("RENDER_EXTERNAL_URL") and st.query_params.get("health") == "true":
    st.write("OK")
    st.stop()
# =========================
# 🚀 PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Blood Test AI System",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# =========================
# 💎 PREMIUM UI STYLING
# =========================
st.markdown("""
<style>

/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 40px 20px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1f77b4, #4facfe);
    color: white;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.9;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #4facfe, #00f2fe);
    color: white;
    border-radius: 12px;
    height: 3.2em;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    opacity: 0.9;
}

/* Glass cards */
.card {
    padding: 20px;
    border-radius: 16px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    color: white;
    margin-bottom: 15px;
}

/* Section titles */
.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 10px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
<div class="hero">
    <div class="hero-title">🩸 Blood Test AI Diagnostic System</div>
    <div class="hero-subtitle">
        AI-assisted clinical decision support for hematology screening<br>
        Fast • Transparent • Explainable • Educational
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Start Analysis", use_container_width=True):
        st.switch_page("pages/2_Input.py")

with col2:
    if st.button("📖 About System", use_container_width=True):
        st.switch_page("pages/1_About.py")

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# FEATURES GRID
# =========================
st.markdown('<div class="section-title">🔬 System Capabilities</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    🧠 AI Clinical Reasoning<br><br>
    Advanced rule-based inference engine mimicking diagnostic logic
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    🩸 25+ Conditions<br><br>
    Covers anemia, infections, malignancies and more
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    📊 Severity Analysis<br><br>
    Risk-based classification for clinical interpretation
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
    🔍 Missing Data Handling<br><br>
    Works even with incomplete lab inputs
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
    📄 Structured Reports<br><br>
    Generates interpretable clinical summaries
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
    ⚡ Fast & Interactive<br><br>
    Real-time analysis powered by Streamlit
    </div>
    """, unsafe_allow_html=True)

# =========================
# DISCLAIMER (FIXED POSITION)
# =========================
st.markdown("<br>", unsafe_allow_html=True)

st.warning("""
⚠️ This application is strictly for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
""")

# =========================
# CITATION
# =========================
st.markdown("---")

st.markdown('<div class="section-title">📚 Citation</div>', unsafe_allow_html=True)

st.markdown("""
Tariq, M. H. (2026). *Blood Test AI Diagnostic System (v1.0.0)*. Zenodo.  
https://doi.org/10.5281/zenodo.20028742
""")

st.caption("Built with Streamlit • AI Medical Project")
