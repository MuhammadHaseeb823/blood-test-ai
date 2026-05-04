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
# DARK MODE SAFE UI FIX
# =========================
st.markdown("""
<style>

/* Global text color fix (dark + light mode safe) */
html, body, [class*="css"] {
    color: inherit;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: inherit !important;
}

/* Paragraphs */
p {
    color: inherit !important;
}

/* Buttons */
.stButton > button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

/* Remove white blocks in dark mode */
.block-container {
    padding-top: 2rem;
}

/* Center title */
.title-center {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle-center {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE (CENTERED)
# =========================
st.markdown('<div class="title-center">🩸 Blood Test AI Diagnostic System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle-center">
AI-assisted clinical decision support for hematology screening<br>
Fast • Transparent • Explainable • Educational
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# NAVIGATION BUTTONS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.button("🔍 Start Analysis", use_container_width=True)

with col2:
    st.button("📖 About System", use_container_width=True)

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
- 💎 Clean hospital-style UI  
""")

st.markdown("---")

# =========================
# DEVELOPER INFO
# =========================
st.subheader("👨‍💻 Developer Information")

st.info("""
**Developers:** Muhammad Haseeb Tariq, Muhammad Muneeb Tariq  
**Project Type:** AI Medical Decision Support System  
**Purpose:** Educational / Academic Research
""")

st.markdown("---")

# =========================
# DISCLAIMER (IMPORTANT)
# =========================
st.error("""
⚠️ Disclaimer: This application is strictly for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare professional.
""")

# =========================
# FOOTER
# =========================
st.caption("Built with Streamlit • AI-assisted Medical Engineering Project")
