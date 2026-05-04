def evaluate(d):

    results = []

    # =========================
    # CONSTANT THRESHOLDS
    # =========================
    HB_M = 130
    HB_F = 120
    RBC_LOW = 4.5
    MCV_LOW = 80
    MCV_HIGH = 100
    FERRITIN_LOW = 30
    IRON_LOW = 60

    WBC_HIGH = 11
    WBC_LOW = 4

    PLT_LOW = 150
    PLT_HIGH = 450

    LDH_HIGH = 300
    CRP_HIGH = 5
    ESR_HIGH = 20
    CALCIUM_HIGH = 2.5
    BILIRUBIN_HIGH = 1.2

    # =========================
    # 🩸 ANEMIA (8 CONDITIONS)
    # =========================

    hb_cut = HB_M if d["gender"] == "Male" else HB_F

    if d["rbc"] < RBC_LOW and d["hb"] < hb_cut and d["mcv"] < MCV_LOW and d["ferritin"] < FERRITIN_LOW:
        results.append({"condition": "Iron Deficiency Anemia"})

    if d["rbc"] < RBC_LOW and (d["vitamin_b12"] < 200 or d["folate"] < 3):
        results.append({"condition": "Vitamin B12 / Folate Deficiency Anemia"})

    if d["mcv"] < MCV_LOW:
        results.append({"condition": "Microcytic Anemia"})

    if d["mcv"] > MCV_HIGH:
        results.append({"condition": "Macrocytic Anemia"})

    if d["rbc"] < RBC_LOW and d["iron"] < IRON_LOW:
        results.append({"condition": "Nutritional Anemia"})

    if d["rbc"] < RBC_LOW and d["wbc"] < WBC_LOW and d["plt"] < PLT_LOW:
        results.append({"condition": "Aplastic Anemia"})

    if d["total_bilirubin"] > BILIRUBIN_HIGH:
        results.append({"condition": "Hemolytic Anemia"})

    # =========================
    # 🧬 INFECTIONS (3 CONDITIONS)
    # =========================

    if d["wbc"] > WBC_HIGH and d["crp"] > CRP_HIGH:
        results.append({"condition": "Acute Infection"})

    if d["wbc"] > WBC_HIGH and d["esr"] > ESR_HIGH:
        results.append({"condition": "Chronic Infection"})

    if d["monocyte_number"] > 6:
        results.append({"condition": "Allergic / Parasitic Reaction"})

    # =========================
    # 🧫 HEMATOLOGY (3 CONDITIONS)
    # =========================

    if d["plt"] < PLT_LOW:
        results.append({"condition": "Thrombocytopenia"})

    if d["plt"] > PLT_HIGH:
        results.append({"condition": "Thrombocytosis"})

    if d["albumin"] < 3.5:
        results.append({"condition": "Coagulation / Bleeding Disorder Suspected"})

    # =========================
    # 🧠 LEUKEMIA (3 CONDITIONS)
    # =========================

    if d["wbc"] > WBC_HIGH and d["ldh"] > LDH_HIGH:
        results.append({"condition": "Leukemia (suspected)"})

    if d["wbc"] > WBC_HIGH and d["neutrophil_absolute"] >= 7:
        results.append({"condition": "Myeloid Leukemia"})

    if d["wbc"] > WBC_HIGH and d["neutrophil_absolute"] < 7:
        results.append({"condition": "Lymphoid Leukemia"})

    # =========================
    # 🧬 LYMPHOMA (4 CONDITIONS)
    # =========================

    if d["ldh"] > LDH_HIGH and d["esr"] > ESR_HIGH:
        results.append({"condition": "Hodgkin Lymphoma"})

    if d["plt"] < PLT_LOW:
        results.append({"condition": "Follicular Lymphoma"})

    if d["wbc"] > WBC_HIGH and d["crp"] > CRP_HIGH:
        results.append({"condition": "Non-follicular Lymphoma"})

    if d["calcium"] > CALCIUM_HIGH:
        results.append({"condition": "T/NK-cell Lymphoma"})

    # =========================
    # 🧫 PLASMA / OTHER (2 CONDITIONS)
    # =========================

    if d["rbc"] < RBC_LOW and d["calcium"] > CALCIUM_HIGH:
        results.append({"condition": "Multiple Myeloma"})

    if d["wbc"] >= WBC_LOW and d["plt"] >= PLT_LOW:
        results.append({"condition": "Other Blood Disorder"})

    return results