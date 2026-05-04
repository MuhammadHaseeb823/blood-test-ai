import streamlit as st

st.warning(
    "⚠️ Disclaimer: This application is strictly for educational purposes only "
    "and should not be used as a substitute for professional medical advice, "
    "diagnosis, or treatment."
)

import streamlit as st
import sqlite3
import json
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Blood Test Input", layout="wide")

st.title("🧪 Blood Test Input System")
st.markdown("Enter all patient parameters below")
st.markdown("---")

# =========================
# DATABASE SETUP
# =========================
conn = sqlite3.connect("patients.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    data TEXT
)
""")
conn.commit()

# =========================
# PATIENT INFO
# =========================
st.subheader("🧍 Patient Information")
gender = st.selectbox("Gender", ["Male", "Female"])

st.markdown("---")

# =========================
# INPUT COLUMNS
# =========================
col1, col2, col3 = st.columns(3)

# =========================
# COLUMN 1 - RBC / IRON / VITAMINS
# =========================
with col1:
    st.subheader("🩸 Red Cell Parameters")

    rbc = st.number_input("RBC (×10¹²/L)")
    hb = st.number_input("Hemoglobin (Hb) (g/dL)")
    mcv = st.number_input("MCV (fL)")
    hct = st.number_input("Hematocrit (%)")

    st.subheader("🧪 Iron Studies")
    iron = st.number_input("Serum Iron (µg/dL)")
    ferritin = st.number_input("Ferritin (µg/L)")
    tibc = st.number_input("TIBC (µg/dL)")

    st.subheader("🧬 Vitamins")
    vitamin_b12 = st.number_input("Vitamin B12 (pg/mL)")
    folate = st.number_input("Folate (ng/mL)")

# =========================
# COLUMN 2 - WBC / IMMUNE / INFLAMMATION
# =========================
with col2:
    st.subheader("🧬 White Cell Parameters")

    wbc = st.number_input("WBC (×10⁹/L)")
    lymphocyte_count = st.number_input("Lymphocyte Count (%)")
    neutrophils = st.number_input("Neutrophils (%)")
    monocyte_number = st.number_input("Monocyte Number (%)")

    st.subheader("📊 Absolute Counts")
    neutrophil_absolute = st.number_input("Neutrophil Absolute Number (×10⁹/L)")
    monocyte_absolute = st.number_input("Monocyte Absolute Number (×10⁹/L)")

    st.subheader("🔥 Inflammatory Markers")

    crp = st.number_input("CRP (mg/L)")
    esr = st.number_input("ESR (mm/hr)")
    ldh = st.number_input("LDH (U/L)")
    reticulocyte_count = st.number_input("Reticulocyte Count (%)")

# =========================
# COLUMN 3 - PLATELETS / METABOLIC
# =========================
with col3:
    st.subheader("🧫 Platelets")

    plt = st.number_input("Platelets (×10⁹/L)")

    st.subheader("🧬 Liver Function")

    total_bilirubin = st.number_input("Total Bilirubin (µmol/L)")
    albumin = st.number_input("Albumin (g/L)")

    st.subheader("🧂 Renal Function")

    urea = st.number_input("Urea (mmol/L)")
    creatinine = st.number_input("Creatinine (µmol/L)")

    st.subheader("⚡ Electrolytes")

    calcium = st.number_input("Calcium (mmol/L)")
    osmolality = st.number_input("Serum Osmolality (mOsm/kg)")

st.markdown("---")

# =========================
# SUBMIT BUTTON
# =========================
if st.button("🔍 Run Analysis"):

    data = {
        "timestamp": str(datetime.now()),
        "gender": gender,

        # RBC
        "rbc": rbc,
        "hb": hb,
        "mcv": mcv,
        "hct": hct,

        # Iron
        "iron": iron,
        "ferritin": ferritin,
        "tibc": tibc,

        # Vitamins
        "vitamin_b12": vitamin_b12,
        "folate": folate,

        # WBC
        "wbc": wbc,
        "lymphocyte_count": lymphocyte_count,
        "neutrophils": neutrophils,
        "monocyte_number": monocyte_number,

        "neutrophil_absolute": neutrophil_absolute,
        "monocyte_absolute": monocyte_absolute,

        # Inflammation
        "crp": crp,
        "esr": esr,
        "ldh": ldh,
        "reticulocyte_count": reticulocyte_count,

        # Platelets
        "plt": plt,

        # Liver
        "total_bilirubin": total_bilirubin,
        "albumin": albumin,

        # Renal
        "urea": urea,
        "creatinine": creatinine,

        # Electrolytes
        "calcium": calcium,
        "osmolality": osmolality
    }

    # Store session
    st.session_state["data"] = data

    # Save to DB
    c.execute(
        "INSERT INTO patients (timestamp, data) VALUES (?, ?)",
        (data["timestamp"], json.dumps(data))
    )
    conn.commit()

    # Optional download
    st.download_button(
        "⬇️ Download JSON",
        json.dumps(data, indent=2),
        file_name="patient_data.json",
        mime="application/json"
    )

    # Move to results page
    st.switch_page("pages/3_Results.py")