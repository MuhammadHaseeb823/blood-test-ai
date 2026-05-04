import streamlit as st

st.set_page_config(page_title="Blood Test AI System", layout="wide")

# =========================
# HEADER (CENTERED)
# =========================
st.markdown("""
<div style="text-align: center; padding: 40px 10px;">
    <h1 style="color: #E5E7EB; font-size: 42px; margin-bottom: 10px;">
        🩸 Blood Test AI Diagnostic System
    </h1>
    <h4 style="color: #9CA3AF; font-weight: 400;">
        AI-assisted Clinical Decision Support for Hematology Screening
    </h4>
    <p style="color: #6B7280; font-size: 14px;">
        Fast • Transparent • Explainable • Educational
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# MAIN ACTIONS
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
# KEY FEATURES
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
# DEVELOPER INFO
# =========================
st.subheader("👨‍💻 Developer Information")

st.info("""
**Developer:** Muhammad Haseeb Tariq, Muhammad Muneeb Tariq  
**Project Type:** AI Medical Decision Support System  
**Purpose:** Educational / Academic Project
""")


# =========================
# DISCLAIMER
# =========================
st.error("""
⚠️ Disclaimer: This system is for educational purposes only and does not provide medical diagnosis or treatment.
Always consult a qualified healthcare professional.
""")

# =========================
# FOOTER
# =========================
st.caption("Built with Streamlit • AI-assisted Medical Engineering Project")