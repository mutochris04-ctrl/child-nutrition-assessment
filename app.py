import logging

from flask import Flask, jsonify, request

# Show the time and level (INFO / WARNING) in front of every log message
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)


def calculate_bmi(weight_kg, height_cm):
    """Return BMI rounded to 1 decimal. Height is given in cm."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def classify_muac(muac_cm, oedema=False):
    """Classify nutrition status from MUAC (WHO cut-offs, children 6-59 months)."""
    if oedema:
        return "Severe Acute Malnutrition"
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
    try:
        muac = float(data["muac_cm"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "muac_cm is required and must be a number"}), 400
    if muac <= 0:
        return jsonify({"error": "muac_cm must be greater than 0"}), 400
    oedema = data.get("oedema", False)
    if type(oedema) != bool:
        return jsonify({"error": "oedema must be true or false"}), 400
    status = classify_muac(muac, oedema)
    app.logger.info("Assessment: muac_cm=%s oedema=%s -> %s", muac, oedema, status)
    return jsonify({"muac_cm": muac, "status": status})

@app.after_request
def log_request(response):
    if response.status_code >= 400:
        # Wrong input or errors are logged as warnings
        app.logger.warning("%s %s -> %s", request.method, request.path, response.status_code)
    else:
        app.logger.info("%s %s -> %s", request.method, request.path, response.status_code)
    return response


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
