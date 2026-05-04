import streamlit as st
from engine_explanations import explain_condition

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Clinical AI Dashboard", layout="wide")

# =========================
# DISCLAIMER
# =========================
st.warning(
    "⚠️ Disclaimer: This application is strictly for educational purposes only "
    "and should not be used as a substitute for professional medical advice, "
    "diagnosis, or treatment."
)

st.title("🧠 Clinical AI Explanation Dashboard")

# =========================
# CHECK SESSION DATA
# =========================
if "results" not in st.session_state or "data" not in st.session_state:
    st.error("No analysis found. Please run the test first.")
    st.stop()

results = st.session_state["results"]
data = st.session_state["data"]

# =========================
# FILTER ABNORMAL CONDITIONS ONLY
# =========================
abnormal_conditions = results  # already abnormal in your pipeline

if not abnormal_conditions:
    st.success("✅ No abnormal conditions detected")
    st.stop()

# =========================
# SIDEBAR - CLICKABLE CONDITIONS
# =========================
st.sidebar.title("🧪 Abnormal Conditions")

selected_condition = st.sidebar.radio(
    "Select Condition",
    [r["condition"] for r in abnormal_conditions]
)

# find selected object
selected_data = next(
    (r for r in abnormal_conditions if r["condition"] == selected_condition),
    None
)

# =========================
# LAYOUT: DOCTOR VIEW + AI VIEW
# =========================
col1, col2 = st.columns([1, 2])

# =========================
# LEFT PANEL (DOCTOR VIEW)
# =========================
with col1:
    st.subheader("🩺 Doctor View")

    st.markdown("### Patient Data")

    st.json(data)

    st.markdown("---")

    st.markdown("### Condition Summary")

    st.write("**Condition:**", selected_data["condition"])
    st.write("**Suggestion 1:**", selected_data.get("suggestion_1", "N/A"))
    st.write("**Suggestion 2:**", selected_data.get("suggestion_2", "N/A"))

    st.markdown("---")

    st.markdown("### Severity (basic)")

    # simple severity logic (you can upgrade later)
    severity = "Moderate"

    if "Leukemia" in selected_condition or "Myeloma" in selected_condition:
        severity = "High"
    elif "Anemia" in selected_condition:
        severity = "Mild to Moderate"

    st.success(f"Severity: {severity}")

# =========================
# RIGHT PANEL (AI EXPLANATION)
# =========================
with col2:
    st.subheader("🧠 AI Clinical Explanation")

    explanation_data = explain_condition(selected_condition, data)

    st.markdown("### 📌 Clinical Interpretation")

    st.info(explanation_data["explanation"])

    st.markdown("### 📚 References")

    for ref in explanation_data["references"]:
        st.markdown(f"- {ref}")

    st.markdown("---")

    st.markdown("### 🧾 Condition Name")
    st.markdown(f"**{selected_condition}**")