import streamlit as st

st.warning(
    "⚠️ Disclaimer: This application is strictly for educational purposes only "
    "and should not be used as a substitute for professional medical advice, "
    "diagnosis, or treatment."
)

def add(results, condition, s1, s2):
    results.append({
        "condition": condition,
        "suggestion_1": s1,
        "suggestion_2": s2
    })

def valid(x):
    return x is not None and x != 0


def evaluate(d):

    results = []

    hb_cut = 130 if d["gender"] == "Male" else 120

    # =========================
    # 1 IRON DEFICIENCY ANEMIA
    # =========================
    if d["rbc"] < 4.5 and d["hb"] < hb_cut and d["mcv"] < 80 and d["ferritin"] < 30:
        results.append({
            "condition": "Iron Deficiency Anemia",
            "suggestion_1": "Blood morphology to confirm Iron Deficiency",
            "suggestion_2": "Consider Bone Marrow Biopsy if no improvement with iron supplementation"
        })

    # =========================
    # 2 B12 / FOLATE DEFICIENCY
    # =========================
    if d["rbc"] < 4.5 and (d["vitamin_b12"] < 200 or d["folate"] < 3):
        results.append({
            "condition": "Vitamin B12/Folate Deficiency Anemia",
            "suggestion_1": "Consider Serum Methylmalonic Acid (MMA) test for B12 deficiency",
            "suggestion_2": "Blood morphology for further confirmation for B12 deficiency"
        })

    # =========================
    # 3 MICROCYTIC ANEMIA
    # =========================
    if d["rbc"] < 4.5 and d["mcv"] < 80:
        results.append({
            "condition": "Microcytic Anemia",
            "suggestion_1": "Serum Iron levels, TIBC, Serum Ferritin, Blood morphology for further confirmation",
            "suggestion_2": "After confirmation Bone Marrow Biopsy for microcytic anemia"
        })

    # =========================
    # 4 MACROCYTIC ANEMIA
    # =========================
    if d["rbc"] < 4.5 and d["mcv"] > 100:
        results.append({
            "condition": "Macrocytic Anemia",
            "suggestion_1": "B12, Homocysteine, Blood smear, MMA, Serum Folate for confirmation",
            "suggestion_2": "Consider Serum Methylmalonic Acid (MMA) test and blood morphology confirmation"
        })

    # =========================
    # 5 ANEMIA OF CHRONIC DISEASE
    # =========================
    if d["rbc"] < 4.5 and 80 <= d["mcv"] <= 100 and d["iron"] >= 30:
        results.append({
            "condition": "Anemia of Chronic Disease",
            "suggestion_1": "Reticulocyte count and blood morphology for confirmation",
            "suggestion_2": "Consider Erythropoietin level and Bone Marrow Biopsy if indicated"
        })

    # =========================
    # 6 ACUTE INFECTION
    # =========================
    if d["wbc"] > 11 and d["crp"] > 5:
        results.append({
            "condition": "Acute Infection",
            "suggestion_1": "Consider Blood Cultures and specific pathogen testing",
            "suggestion_2": "Further infectious disease workup depending on clinical suspicion"
        })

    # =========================
    # 7 CHRONIC INFECTION
    # =========================
    if d["wbc"] > 11 and d["esr"] > 20:
        results.append({
            "condition": "Chronic Infection",
            "suggestion_1": "Consider PCR Testing for specific pathogens",
            "suggestion_2": "Serology testing for chronic infection confirmation"
        })

    # =========================
    # 8 ALLERGIC / PARASITIC
    # =========================
    if d["monocyte_number"] > 6:
        results.append({
            "condition": "Allergic Reaction/Parasitic Infection",
            "suggestion_1": "Consider Skin Prick Test for allergies",
            "suggestion_2": "Wide range of immunology allergy testing for confirmation"
        })

    # =========================
    # 9 LEUKEMIA
    # =========================
    if d["wbc"] > 11 and d["ldh"] > 300:
        results.append({
            "condition": "Leukemia",
            "suggestion_1": "Blood morphology, Immunophenotyping, Cytogenetic and Molecular testing",
            "suggestion_2": "Bone Marrow Biopsy and flow cytometry for confirmation"
        })

    # =========================
    # 10 THROMBOCYTOPENIA
    # =========================
    if d["plt"] < 150:
        results.append({
            "condition": "Thrombocytopenia",
            "suggestion_1": "Coagulation screen and blood morphology",
            "suggestion_2": "Bone Marrow Biopsy if etiology is unclear"
        })

    # =========================
    # 11 THROMBOCYTOSIS
    # =========================
    if d["plt"] > 450:
        results.append({
            "condition": "Thrombocytosis",
            "suggestion_1": "Coagulation screen and inflammatory markers",
            "suggestion_2": "Bone Marrow Biopsy if secondary causes suspected"
        })

    # =========================
    # 12 DEHYDRATION
    # =========================
    if d["urea"] > 20 and d["creatinine"] > 110:
        results.append({
            "condition": "Dehydration",
            "suggestion_1": "Serum electrolytes and osmolality",
            "suggestion_2": "Urinalysis to assess hydration status"
        })

    # =========================
    # 13 HODGKIN LYMPHOMA
    # =========================
    if d["wbc"] > 11 and d["ldh"] > 300 and d["esr"] > 20:
        results.append({
            "condition": "Hodgkin Lymphoma",
            "suggestion_1": "Blood morphology to confirm suspicion",
            "suggestion_2": "Lymph node biopsy for definitive diagnosis"
        })

    # =========================
    # 14 FOLLICULAR LYMPHOMA
    # =========================
    if d["ldh"] <= 300 and d["esr"] > 20:
        results.append({
            "condition": "Follicular Lymphoma",
            "suggestion_1": "Blood morphology and immunophenotyping",
            "suggestion_2": "Lymph node biopsy for confirmation"
        })

    # =========================
    # 15 NON-FOLLICULAR LYMPHOMA
    # =========================
    if d["wbc"] > 11 and d["ldh"] > 300:
        results.append({
            "condition": "Non-follicular Lymphoma",
            "suggestion_1": "Blood morphology and immunophenotyping",
            "suggestion_2": "Lymph node biopsy and flow cytometry"
        })

    # =========================
    # 16 T/NK CELL LYMPHOMA
    # =========================
    if d["calcium"] > 2.5:
        results.append({
            "condition": "T/NK-cell Lymphoma",
            "suggestion_1": "Blood morphology and flow cytometry",
            "suggestion_2": "Lymph node biopsy for confirmation"
        })

    # =========================
    # 17 OTHER NON-HODGKIN
    # =========================
    if d["crp"] > 5:
        results.append({
            "condition": "Other Non-Hodgkin Lymphoma",
            "suggestion_1": "Blood morphology and immunophenotyping",
            "suggestion_2": "Lymph node biopsy for confirmation"
        })

    # =========================
    # 18 MULTIPLE MYELOMA
    # =========================
    if d["calcium"] > 2.5 and d["rbc"] < 4.5:
        results.append({
            "condition": "Multiple Myeloma",
            "suggestion_1": "Serum protein electrophoresis",
            "suggestion_2": "Bone marrow biopsy for confirmation"
        })

    # =========================
    # 19 OTHER BLOOD DISEASE
    # =========================
    if d["wbc"] >= 4 and d["plt"] >= 150:
        results.append({
            "condition": "Other Diseases of Blood and Blood-forming Organs",
            "suggestion_1": "Additional hematological testing based on clinical suspicion",
            "suggestion_2": "Further diagnostic workup as required"
        })

    return results