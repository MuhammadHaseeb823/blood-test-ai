def get_severity(condition):

    high = [
        "Leukemia",
        "Myeloid Leukemia",
        "Lymphoid Leukemia",
        "Multiple Myeloma",
        "Hodgkin Lymphoma"
    ]

    moderate = [
        "Thrombocytopenia",
        "Thrombocytosis",
        "Chronic Infection",
        "Anemia of Chronic Disease"
    ]

    if condition in high:
        return "HIGH", "red"
    elif condition in moderate:
        return "MODERATE", "orange"
    else:
        return "LOW", "green"


def generate_summary(results):
    if not results:
        return "No significant abnormalities detected."

    high = sum(1 for r in results if get_severity(r["condition"])[0] == "HIGH")
    moderate = sum(1 for r in results if get_severity(r["condition"])[0] == "MODERATE")

    return (
        f"{len(results)} abnormal findings detected. "
        f"{high} high-risk and {moderate} moderate-risk conditions identified. "
        "Clinical correlation and further diagnostic confirmation recommended."
    )


def group_conditions(results):
    grouped = {
        "🔴 High Risk": [],
        "🟠 Moderate Risk": [],
        "🟢 Low Risk": []
    }

    for r in results:
        severity, _ = get_severity(r["condition"])

        if severity == "HIGH":
            grouped["🔴 High Risk"].append(r)
        elif severity == "MODERATE":
            grouped["🟠 Moderate Risk"].append(r)
        else:
            grouped["🟢 Low Risk"].append(r)

    return grouped