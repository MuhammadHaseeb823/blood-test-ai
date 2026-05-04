import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Blood Test AI System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# UI STYLING (DARK MODE SAFE)
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    color: inherit;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
}

/* Buttons */
.stButton > button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
    height: 3.2em;
    width: 100%;
    font-size: 16px;
}

/* Layout spacing */
.block-container {
    padding-top: 2rem;
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

st.markdown("---")

# =========================
# NAVIGATION (FIXED)
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Start Analysis", use_container_width=True):
        st.switch_page("pages/2_Input.py")

with col2:
    if st.button("📖 About System", use_container_width=True):
        st.switch_page("pages/1_About.py")

st.markdown("---")

# =========================
# FEATURES
# =========================
st.subheader("🔬 System Capabilities")

st.markdown("""
- 🧠 AI-style clinical reasoning engine  
- 🩸 25+ hematological condition detection  
- 📊 Severity-based interpretation (Mild / Moderate / Severe)  
- 🔍 Handles missing or incomplete lab data  
- 📄 Structured medical explanations  
""")

st.markdown("---")

# =========================
# DISCLAIMER
# =========================
st.error("""
⚠️ Disclaimer: This application is strictly for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
""")

st.caption("Built with Streamlit • AI Medical Project")
