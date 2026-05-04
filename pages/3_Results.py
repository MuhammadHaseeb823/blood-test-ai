import streamlit as st
from engine import evaluate
from pdf_report import generate_pdf

st.set_page_config(page_title="Report", layout="wide")

st.title("🏥 Report")

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
summary_points = []

if results:
    summary_points.append(f"{len(results)} abnormal condition(s) detected.")
    summary_points.append("Further diagnostic confirmation recommended.")
else:
    summary_points.append("No significant hematological abnormalities detected.")

st.markdown("## 🧠 Summary")
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

        st.markdown(
            f"""
            <div style="
                padding:15px;
                border-radius:10px;
                background-color:#f5f7ff;
                border:1px solid #d0d7ff;
                margin-bottom:10px;
            ">
                <b>Suggestion 1:</b><br>
                {r.get('suggestion_1','N/A')}
            </div>

            <div style="
                padding:15px;
                border-radius:10px;
                background-color:#fff7f5;
                border:1px solid #ffd0d0;
            ">
                <b>Suggestion 2:</b><br>
                {r.get('suggestion_2','N/A')}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# PDF DOWNLOAD
# =========================
from pdf_report import generate_pdf

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