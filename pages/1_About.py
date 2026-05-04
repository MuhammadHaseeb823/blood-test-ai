import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("📖 About This Application")

tab1, tab2, tab3 = st.tabs(["📌 Overview", "🧭 How to Use", "⚠️ Disclaimer"])

with tab1:
    st.markdown("""
This is a medical diagnostic support tool that analyzes blood test parameters to identify potential hematological conditions and provide structured clinical explanations.

---

## 🔬 Features
- 25+ hematological conditions detection  
- AI-style clinical reasoning  
- Severity classification  
- Handles missing values  
- PDF report generation  
""")

with tab2:
    st.markdown("""
## 🧭 How to Use

1. Go to **Input page**
2. Enter blood test values
3. Click analyze (automatic processing)
4. View **Results page**
5. Download PDF report
6. Read **Explanations page** for interpretation

---

## 🎯 Designed For
- Medical students  
- Educational labs  
- Research demonstrations  
""")

with tab3:
    st.markdown("""
⚠️ **Disclaimer**

This tool is for educational purposes only and must not be used for real medical diagnosis.
""")
