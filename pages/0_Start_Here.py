import streamlit as st

st.set_page_config(page_title="Start Here", layout="wide")

st.title("🧭 Start Here — Blood Test AI System")

st.markdown("""
## 👋 Welcome

This system helps interpret blood test results using AI-assisted clinical reasoning.

---

## 🚀 How to Use (Simple Flow)

### 1. Learn About System
Go to **About page** to understand functionality

### 2. Enter Patient Data
Go to **Input page** and fill blood parameters

### 3. View AI Results
System will detect:
- Medical conditions
- Severity level
- Clinical suggestions

### 4. Download Report
Generate a PDF medical report

### 5. Learn Interpretation
Go to **Explanations page**

---

## ⚠️ Important Notice
This system is for **educational and research purposes only**
and must NOT be used for real medical diagnosis.

---

## 🎯 First-Time Users Tip
Start with default values → then slowly modify inputs to understand behavior
""")

if st.button("➡️ Start Analysis"):
    st.switch_page("pages/1_Input.py")
