import streamlit as st
from engine import evaluate
from pdf_report import generate_pdf

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Report",
    layout="wide"
)

# =========================
# DARK MODE SAFE CSS FIX
# =========================
st.markdown("""
<style>

/* Global text */
html, body, [class*="css"] {
    color: inherit;
}

/* Headings */
h1, h2, h3, h4, h5 {
    color: inherit !important;
}

/* Fix containers */
.block-container {
    padding-top: 2rem;
}

/* Safe card styling (theme-aware) */
.card {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid rgba(120,120,120,0.3);
    margin-bottom: 10px;
}

/* Improve readability in dark mode */
div {
    color: inherit;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("🏥 Clinical Report")

# =========================
# DATA CHECK
# =========================
data = st.session_state.get("data", None)

if not data:
    st.warning("No data found. Please go back to input page.")
    st.stop()

results = evaluate(data)
st.session_state["results"] = results

# =========================
# SEVERITY FUNCTION
# =========================
def get_severity(condition):
    high_risk = [
        "Leukemia",
        "Multiple Myeloma",
        "Hodgkin Lymphoma",
        "Myeloid Leukemia",
        "Lymphoid Leukemia"
    ]

    moderate_risk = [
        "Anemia",
        "Thrombocytopenia",
        "Thrombocytosis",
        "Chronic Infection"
    ]

    if any(x in condition for x in high_risk):
        return "🔴 HIGH RISK"
    elif any(x in condition for x in moderate_risk):
        return "🟠 MODERATE RISK"
    else:
        return "🟢 LOW RISK"

# =========================
# SUMMARY
# =========================
st.markdown("## 🧠 AI Summary")

summary_points = []

if results:
    summary_points.append(f"{len(results)} abnormal condition(s) detected.")
    summary_points.append("Further diagnostic confirmation recommended.")
else:
    summary_points.append("No significant hematological abnormalities detected.")

for s in summary_points:
    st.write("• " + s)

st.markdown("---")

# =========================
# RESULTS DISPLAY
# =========================
if not results:
    st.success("✅ No abnormal conditions detected.")
else:
    for r in results:
        st.markdown("---")

        st.markdown(f"## 🧬 {r['condition']}")
        st.markdown(f"### {get_severity(r['condition'])}")

        st.markdown("### 🔍 Clinical Suggestions")

        # Suggestion 1 card
        st.markdown(f"""
        <div class="card">
            <b>Suggestion 1:</b><br>
            {r.get('suggestion_1','N/A')}
        </div>
        """, unsafe_allow_html=True)

        # Suggestion 2 card
        st.markdown(f"""
        <div class="card">
            <b>Suggestion 2:</b><br>
            {r.get('suggestion_2','N/A')}
        </div>
        """, unsafe_allow_html=True)

# =========================
# PDF EXPORT
# =========================
st.markdown("---")
st.subheader("📄 Export Report")

pdf_file = generate_pdf(data, results)

st.download_button(
    label="⬇️ Download PDF Report",
    data=pdf_file,
    file_name="clinical_report.pdf",
    mime="application/pdf"
)

# =========================
# NAVIGATION
# =========================
if st.button("🧠 View Clinical Explanation"):
    st.switch_page("pages/5_Explanations.py")
