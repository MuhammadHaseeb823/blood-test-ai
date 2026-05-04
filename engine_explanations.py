def explain_condition(condition, d):

    explanations = {

        # =========================
        # 1 IRON DEFICIENCY ANEMIA
        # =========================
        "Iron Deficiency Anemia": {
            "explanation": """
CLINICAL SUMMARY:
Iron deficiency anemia is caused by inadequate iron availability leading to reduced hemoglobin synthesis and impaired erythropoiesis.

PATHOPHYSIOLOGY:
Iron depletion reduces heme formation, resulting in microcytic hypochromic red blood cells and reduced oxygen-carrying capacity.

LAB INTERPRETATION:
Hb: {hb}
MCV: {mcv}
Ferritin: {ferritin}

DIFFERENTIAL DIAGNOSIS:
- Chronic blood loss (GI bleeding, menstruation)
- Thalassemia trait
- Anemia of chronic disease
""".format(**d),

            "references": [
                "NICE Guideline NG239: Anaemia Management in Adults (2021)",
                "WHO Haemoglobin Concentrations for the Diagnosis of Anaemia (2011)",
                "American Society of Hematology (ASH) Iron Deficiency Guidelines (2020)",
                "British Society for Haematology: Iron Deficiency Anaemia Guidelines"
            ]
        },

        # =========================
        # 2 VITAMIN B12 / FOLATE DEFICIENCY
        # =========================
        "Vitamin B12/Folate Deficiency Anemia": {
            "explanation": """
CLINICAL SUMMARY:
Megaloblastic anemia due to impaired DNA synthesis caused by vitamin B12 or folate deficiency.

PATHOPHYSIOLOGY:
Defective thymidine synthesis leads to nuclear-cytoplasmic asynchrony and ineffective erythropoiesis.

LAB INTERPRETATION:
Hb: {hb}
MCV: {mcv}
Vitamin B12: {vitamin_b12}
Folate: {folate}

DIFFERENTIAL DIAGNOSIS:
- Liver disease
- Alcohol-induced macrocytosis
- Myelodysplastic syndromes
""".format(**d),

            "references": [
                "British Society for Haematology: Megaloblastic Anaemia Guidelines (2014)",
                "NIH Office of Dietary Supplements: Vitamin B12 Fact Sheet (2023)",
                "NICE Clinical Knowledge Summary: Anaemia - B12 and Folate Deficiency",
                "Mayo Clinic: Vitamin B12 Deficiency Clinical Review"
            ]
        },

        # =========================
        # 3 MICROCYTIC ANEMIA
        # =========================
        "Microcytic Anemia": {
            "explanation": """
CLINICAL SUMMARY:
Microcytic anemia is characterized by reduced red blood cell size due to impaired hemoglobin synthesis.

PATHOPHYSIOLOGY:
Deficient hemoglobin production leads to decreased mean corpuscular volume.

LAB INTERPRETATION:
MCV: {mcv}

DIFFERENTIAL DIAGNOSIS:
- Iron deficiency anemia
- Thalassemia
- Chronic inflammatory anemia
""".format(**d),

            "references": [
                "ASH Red Cell Disorders Guidelines",
                "WHO Hematology Laboratory Manual",
                "BMJ Clinical Review: Microcytic Anemia"
            ]
        },

        # =========================
        # 4 MACROCYTIC ANEMIA
        # =========================
        "Macrocytic Anemia": {
            "explanation": """
CLINICAL SUMMARY:
Macrocytic anemia due to impaired DNA synthesis resulting in enlarged erythrocytes.

PATHOPHYSIOLOGY:
Delayed nuclear maturation with preserved cytoplasmic growth.

LAB INTERPRETATION:
MCV: {mcv}

DIFFERENTIAL DIAGNOSIS:
- Vitamin B12 deficiency
- Folate deficiency
- Liver disease
""".format(**d),

            "references": [
                "NICE Clinical Knowledge Summary: Anaemia",
                "Mayo Clinic Hematology Reference Guide",
                "ASH Macrocytosis Clinical Guidelines"
            ]
        },

        # =========================
        # 5 ANEMIA OF CHRONIC DISEASE
        # =========================
        "Anemia of Chronic Disease": {
            "explanation": """
CLINICAL SUMMARY:
Inflammation-mediated anemia due to impaired iron utilization.

PATHOPHYSIOLOGY:
IL-6 mediated hepcidin increase traps iron in macrophages.

LAB INTERPRETATION:
Ferritin: {ferritin}

DIFFERENTIAL DIAGNOSIS:
- Iron deficiency anemia
- Chronic kidney disease anemia
""".format(**d),

            "references": [
                "UpToDate: Anemia of Chronic Disease (2023)",
                "NICE NG8: Chronic Kidney Disease Anaemia",
                "WHO Iron Metabolism Technical Report"
            ]
        },

        # =========================
        # 6 ACUTE INFECTION
        # =========================
        "Acute Infection": {
            "explanation": """
CLINICAL SUMMARY:
Acute infectious process causing systemic inflammatory response.

PATHOPHYSIOLOGY:
Cytokine release increases leukocyte production and acute phase reactants.

LAB INTERPRETATION:
WBC: {wbc}
CRP: {crp}

DIFFERENTIAL DIAGNOSIS:
- Bacterial infection
- Viral infection
- Sepsis
""".format(**d),

            "references": [
                "CDC Infectious Diseases Manual",
                "WHO Acute Infection Guidelines",
                "Lancet Infectious Diseases Review"
            ]
        },

        # =========================
        # 7 CHRONIC INFECTION
        # =========================
        "Chronic Infection": {
            "explanation": """
CLINICAL SUMMARY:
Long-standing infectious process causing persistent inflammation.

PATHOPHYSIOLOGY:
Continuous immune activation leads to elevated ESR and systemic effects.

LAB INTERPRETATION:
ESR: {esr}

DIFFERENTIAL DIAGNOSIS:
- Tuberculosis
- Chronic viral infections
- Autoimmune disease
""".format(**d),

            "references": [
                "WHO Tuberculosis Treatment Guidelines",
                "CDC ESR Interpretation Manual",
                "BMJ Chronic Infection Review"
            ]
        },

        # =========================
        # 8 ALLERGIC / PARASITIC
        # =========================
        "Allergic Reaction/Parasitic Infection": {
            "explanation": """
CLINICAL SUMMARY:
Immune hypersensitivity or parasitic infection with eosinophilic activation.

PATHOPHYSIOLOGY:
Th2 immune response activation with eosinophil proliferation.

DIFFERENTIAL DIAGNOSIS:
- Allergic disorders
- Helminth infections
""",
            "references": [
                "AAAAI Allergy Practice Parameters",
                "CDC Parasitic Disease Guidelines",
                "WHO Helminth Control Program"
            ]
        },

        # =========================
        # 9 LEUKEMIA
        # =========================
        "Leukemia": {
            "explanation": """
CLINICAL SUMMARY:
Malignant clonal proliferation of hematopoietic stem cells.

PATHOPHYSIOLOGY:
Uncontrolled blast cell expansion in bone marrow leading to marrow failure.

DIFFERENTIAL DIAGNOSIS:
- Severe infection
- Lymphoma
""",
            "references": [
                "NCI Leukemia Treatment Guidelines",
                "WHO Classification of Hematologic Malignancies (2022)",
                "ASH Leukemia Clinical Guide"
            ]
        },

        # =========================
        # 10 MYELOID LEUKEMIA
        # =========================
        "Myeloid Leukemia": {
            "explanation": """
CLINICAL SUMMARY:
Malignancy of myeloid precursor cells.

PATHOPHYSIOLOGY:
Genetic mutations lead to uncontrolled myeloid proliferation.

DIFFERENTIAL DIAGNOSIS:
- Infection
- Other leukemias
""",
            "references": [
                "NCI Acute Myeloid Leukemia Guidelines",
                "WHO Myeloid Neoplasm Classification",
                "ASH Myeloid Leukemia Handbook"
            ]
        },

        # =========================
        # 11 LYMPHOID LEUKEMIA
        # =========================
        "Lymphoid Leukemia": {
            "explanation": """
CLINICAL SUMMARY:
Malignancy of lymphoid precursor cells.

PATHOPHYSIOLOGY:
Accumulation of lymphoblasts in bone marrow.

DIFFERENTIAL DIAGNOSIS:
- Viral infections
- Lymphoma
""",
            "references": [
                "NCI Acute Lymphoblastic Leukemia Guidelines",
                "WHO Lymphoid Neoplasm Classification",
                "ASH Leukemia Reference Guide"
            ]
        },

        # =========================
        # 12 HODGKIN LYMPHOMA
        # =========================
        "Hodgkin Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Reed-Sternberg cell lymphoma with characteristic inflammatory background.

PATHOPHYSIOLOGY:
Abnormal B-cell transformation with cytokine-driven inflammation.

DIFFERENTIAL DIAGNOSIS:
- Non-Hodgkin lymphoma
""",
            "references": [
                "NCI Hodgkin Lymphoma Treatment Guide",
                "WHO Lymphoid Neoplasms Classification",
                "ESMO Clinical Guidelines: Hodgkin Lymphoma"
            ]
        },

        # =========================
        # 13 FOLLICULAR LYMPHOMA
        # =========================
        "Follicular Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Indolent B-cell non-Hodgkin lymphoma.

PATHOPHYSIOLOGY:
t(14;18) mutation causing BCL2 overexpression.

DIFFERENTIAL DIAGNOSIS:
- Reactive lymphadenopathy
""",
            "references": [
                "NCCN Guidelines: Follicular Lymphoma",
                "WHO Hematolymphoid Classification",
                "ESMO Lymphoma Guidelines"
            ]
        },

        # =========================
        # 14 NON-FOLLICULAR LYMPHOMA
        # =========================
        "Non-follicular Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Aggressive B-cell lymphoma subtype.

PATHOPHYSIOLOGY:
Rapid lymphoid proliferation with tissue invasion.

DIFFERENTIAL DIAGNOSIS:
- Infection
""",
            "references": [
                "WHO Lymphoma Classification (2022)",
                "NCI Non-Hodgkin Lymphoma Guide"
            ]
        },

        # =========================
        # 15 T/NK-CELL LYMPHOMA
        # =========================
        "Mature T/NK-cell Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Aggressive lymphoma arising from T or NK cells.

PATHOPHYSIOLOGY:
Clonal proliferation of cytotoxic lymphocytes.

DIFFERENTIAL DIAGNOSIS:
- Viral infection (EBV/CMV)
""",
            "references": [
                "WHO Hematolymphoid Tumours Classification (2022)",
                "NCCN T-Cell Lymphoma Guidelines",
                "ESMO T-cell Lymphoma Recommendations"
            ]
        },

        # =========================
        # 16 OTHER NON-HODGKIN LYMPHOMA
        # =========================
        "Other Non-Hodgkin Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
A heterogeneous group of lymphoid malignancies not classified as Hodgkin lymphoma.

PATHOPHYSIOLOGY:
Malignant transformation of B or T lymphocytes with abnormal proliferation.

LAB INTERPRETATION:
May show elevated LDH and abnormal lymphocyte counts.

DIFFERENTIAL DIAGNOSIS:
- Reactive lymphadenopathy
- Chronic infections
""".format(**d),

            "references": [
                "WHO Classification of Tumours of Haematopoietic and Lymphoid Tissues (5th Edition, 2022)",
                "NCI PDQ® Adult Non-Hodgkin Lymphoma Treatment",
                "ESMO Clinical Practice Guidelines: Lymphoma"
            ]
        },

        # =========================
        # 17 OTHER T/NK-CELL LYMPHOMA
        # =========================
        "Other T/NK-cell Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Rare aggressive lymphoid malignancies arising from T or NK cells.

PATHOPHYSIOLOGY:
Clonal expansion of abnormal cytotoxic lymphocytes.

LAB INTERPRETATION:
Elevated LDH, cytopenias may be present.

DIFFERENTIAL DIAGNOSIS:
- Viral infections (EBV, CMV)
- Other lymphomas
""".format(**d),

            "references": [
                "WHO Classification of Haematolymphoid Tumours (2022)",
                "NCCN Guidelines: T-Cell Lymphomas",
                "ESMO Guidelines for Peripheral T-Cell Lymphoma"
            ]
        },

        # =========================
        # 18 B-CELL LYMPHOMA
        # =========================
        "B-cell Lymphoma": {
            "explanation": """
CLINICAL SUMMARY:
Malignancy of mature B lymphocytes.

PATHOPHYSIOLOGY:
Genetic mutations leading to uncontrolled B-cell proliferation.

LAB INTERPRETATION:
May show lymphocytosis and elevated LDH.

DIFFERENTIAL DIAGNOSIS:
- Reactive lymphadenopathy
- Chronic infections
""".format(**d),

            "references": [
                "NCCN Clinical Practice Guidelines in Oncology: B-Cell Lymphomas (2024)",
                "WHO Classification of Tumours: Haematolymphoid (2022)",
                "ESMO Guidelines: B-Cell Non-Hodgkin Lymphoma"
            ]
        },

        # =========================
        # 19 MULTIPLE MYELOMA
        # =========================
        "Multiple Myeloma": {
            "explanation": """
CLINICAL SUMMARY:
Plasma cell malignancy characterized by monoclonal protein production.

PATHOPHYSIOLOGY:
Clonal plasma cell proliferation in bone marrow causing bone destruction.

LAB INTERPRETATION:
May show elevated calcium, anemia, renal dysfunction.

DIFFERENTIAL DIAGNOSIS:
- Metastatic bone disease
- Monoclonal gammopathy of undetermined significance (MGUS)
""".format(**d),

            "references": [
                "International Myeloma Working Group (IMWG) Criteria 2014",
                "NCCN Guidelines: Multiple Myeloma (2024)",
                "British Society for Haematology: Myeloma Guidelines"
            ]
        },

        # =========================
        # 20 THROMBOCYTOPENIA
        # =========================
        "Thrombocytopenia": {
            "explanation": """
CLINICAL SUMMARY:
Reduced platelet count leading to bleeding tendency.

PATHOPHYSIOLOGY:
Decreased platelet production or increased destruction.

LAB INTERPRETATION:
Low platelet count (<150 ×10⁹/L).

DIFFERENTIAL DIAGNOSIS:
- Immune thrombocytopenic purpura (ITP)
- Bone marrow suppression
""".format(**d),

            "references": [
                "American Society of Hematology Guidelines for ITP (2019)",
                "NICE Guideline: Blood Disorders (NG46)",
                "UpToDate: Thrombocytopenia Evaluation"
            ]
        },

        # =========================
        # 21 THROMBOCYTOSIS
        # =========================
        "Thrombocytosis": {
            "explanation": """
CLINICAL SUMMARY:
Elevated platelet count due to reactive or clonal causes.

PATHOPHYSIOLOGY:
Increased megakaryocyte proliferation in bone marrow.

LAB INTERPRETATION:
Platelet count >450 ×10⁹/L.

DIFFERENTIAL DIAGNOSIS:
- Iron deficiency
- Myeloproliferative neoplasms
""".format(**d),

            "references": [
                "British Society for Haematology: Thrombocytosis Guidelines",
                "NCCN Myeloproliferative Neoplasms Guidelines",
                "WHO Classification of Myeloid Neoplasms (2022)"
            ]
        },

        # =========================
        # 22 DEHYDRATION
        # =========================
        "Dehydration": {
            "explanation": """
CLINICAL SUMMARY:
Fluid deficit leading to hemoconcentration.

PATHOPHYSIOLOGY:
Reduced plasma volume increases blood concentration markers.

LAB INTERPRETATION:
Increased hematocrit and serum osmolality.

DIFFERENTIAL DIAGNOSIS:
- Diabetes insipidus
- Heat exhaustion
""".format(**d),

            "references": [
                "WHO Guidelines on Fluid and Electrolyte Management",
                "NICE Clinical Knowledge Summary: Dehydration",
                "Merck Manual: Fluid Volume Disorders"
            ]
        },

        # =========================
        # 23 COAGULATION DEFECTS
        # =========================
        "Coagulation Defects and Other Hemorrhagic Conditions": {
            "explanation": """
CLINICAL SUMMARY:
Disorders affecting clotting factor function.

PATHOPHYSIOLOGY:
Deficiency or dysfunction of coagulation cascade proteins.

LAB INTERPRETATION:
Prolonged PT/aPTT depending on defect.

DIFFERENTIAL DIAGNOSIS:
- Hemophilia
- Liver disease
""".format(**d),

            "references": [
                "British Society for Haematology: Coagulation Disorders Guidelines",
                "NHLBI Hemostasis Disorders Manual",
                "UpToDate: Bleeding Disorders Evaluation"
            ]
        },

        # =========================
        # 24 OTHER BLOOD DISORDERS
        # =========================
           "Other Diseases of Blood and Blood-Forming Organs": {
            "explanation": """
CLINICAL SUMMARY:
Miscellaneous hematological disorders not otherwise classified.

PATHOPHYSIOLOGY:
Varies depending on underlying condition affecting blood production or destruction.

LAB INTERPRETATION:
Non-specific hematologic abnormalities.

DIFFERENTIAL DIAGNOSIS:
- Rare hematologic syndromes
- Mixed etiologies
""".format(**d),

            "references": [
                "WHO ICD-11: Diseases of the Blood and Blood-Forming Organs",
                "Merck Manual: Hematologic Disorders Overview",
                "NICE Hematology Reference Guide"
            ]
        }
    }

    return explanations.get(condition, {
        "explanation": "No structured clinical explanation available.",
        "references": []
    })