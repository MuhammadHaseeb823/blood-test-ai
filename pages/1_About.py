import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# =========================
# TITLE
# =========================
st.title("📖 About This Application")

st.markdown("---")

# =========================
# DESCRIPTION
# =========================
st.markdown("""
This is a medical diagnostic support tool that analyzes blood test parameters 
to identify potential hematological conditions and provide structured clinical explanations.
""")

st.markdown("---")

# =========================
# FEATURES
# =========================
st.header("🔬 Features")

st.markdown("""
- Analyzes 25+ blood-related conditions  
- Provides structured clinical reasoning  
- Handles missing values safely  
- Generates severity-based interpretation  
- AI-style explanation formatting  
""")

st.markdown("---")

# =========================
# SUPPORTED CONDITIONS
# =========================
st.header("🧬 Supported Conditions")

conditions = """
• Iron Deficiency Anemia  
• Vitamin B12/Folate Deficiency Anemia  
• Microcytic Anemia  
• Macrocytic Anemia  
• Anemia of Chronic Disease  
• Acute Infection  
• Chronic Infection  
• Leukemia  
• Thrombocytopenia  
• Thrombocytosis  
• Dehydration  
• Hodgkin Lymphoma  
• Follicular Lymphoma  
• Non-follicular Lymphoma  
• Mature T/NK-cell Lymphoma  
• Other Non-Hodgkin Lymphoma  
• Other T/NK-cell Lymphoma  
• B-cell Lymphoma  
• Multiple Myeloma  
• Lymphoid Leukemia  
• Myeloid Leukemia  
• Nutritional Anemia  
• Hemolytic Anemia  
• Aplastic Anemia  
• Coagulation Defects and Other Hemorrhagic Conditions  
• Other Diseases of Blood and Blood-Forming Organs  
"""

st.markdown(conditions)

st.markdown("---")

# =========================
# DISCLAIMER
# =========================
st.error("""
⚠️ Disclaimer: This application is strictly for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
""")