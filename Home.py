import streamlit as st

# =========================
# 🚀 PAGE CONFIG (OPTIMIZED)
# =========================
st.set_page_config(
    page_title="Blood Test AI System",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# =========================
# 🚀 PERFORMANCE OPTIMIZATION
# =========================
@st.cache_resource
def get_engine():
    from engine import evaluate
    return evaluate

@st.cache_resource
def get_pdf():
    from pdf_report import generate_pdf
    return generate_pdf

evaluate = get_engine()
generate_pdf = get_pdf()

# =========================
# 🎨 ADVANCED UI STYLING
# =========================
st.markdown("""
<style>

/* Global text */
html, body, [class*="css"] {
    color: inherit;
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.85;
    margin-bottom: 25px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #1f77b4, #4facfe);
    color: white;
    border-radius: 12px;
    height: 3.2em;
    font-size: 16px;
    border: none;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 14px;
    background-color: rgba(240, 242, 246, 0.6);
    margin-bottom: 15px;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    .card {
        background-color: rgba(30, 30, 30, 0.6);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🩸 Blood Test AI Diagnostic System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
AI-assisted clinical decision support for hematology screening<br>
Fast • Transparent • Explainable • Educational
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
# DEMO INFO
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🧪 Quick Demo Mode")
st.info("Demo mode is currently disabled to ensure accurate input flow consistency.")
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FEATURES (CARD STYLE)
# =========================
st.subheader("🔬 System Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    🧠 AI-style clinical reasoning engine<br><br>
    🩸 25+ hematological condition detection<br><br>
    📊 Severity-based interpretation
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    🔍 Handles missing/incomplete data<br><br>
    📄 Structured medical explanations<br><br>
    ⚡ Fast interactive analysis
    </div>
    """, unsafe_allow_html=True)

# =========================
# DISCLAIMER
# =========================
st.markdown("<br>", unsafe_allow_html=True)

st.error("""
⚠️ Disclaimer: This application is strictly for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
""")

# =========================
# 📚 CITATION
# =========================
st.markdown("---")

st.subheader("📚 Citation")

st.markdown("""
**Please cite this work as:**

Tariq, M. H. (2026). *Blood Test AI Diagnostic System (v1.0.0)*. Zenodo.  
https://doi.org/10.5281/zenodo.20028742
""")

st.caption("Built with Streamlit • AI Medical Project")
