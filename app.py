from flask import Flask, jsonify, request

app = Flask(__name__)


def calculate_bmi(weight_kg, height_cm):
    """Return BMI rounded to 1 decimal. Height is given in cm."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def classify_muac(muac_cm):
    """Classify nutrition status from MUAC (WHO cut-offs, children 6-59 months)."""
    if muac_cm < 11.5:
        return "Severe Acute Malnutrition"
    if muac_cm < 12.5:
        return "Moderate Acute Malnutrition"
    return "Normal"


@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()
    result = calculate_bmi(float(data["weight_kg"]), float(data["height_cm"]))
    return jsonify({"bmi": result})


@app.route("/assess", methods=["POST"])
def assess():
    data = request.get_json()
    muac = float(data["muac_cm"])
    return jsonify({"muac_cm": muac, "status": classify_muac(muac)})


if __name__ == "__main__":
    app.run(debug=True)
