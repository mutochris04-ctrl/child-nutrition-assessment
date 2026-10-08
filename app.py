from flask import Flask, jsonify, request

app = Flask(__name__)


def calculate_bmi(weight_kg, height_cm):
    """Return BMI rounded to 1 decimal. Height is given in cm."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()
    result = calculate_bmi(float(data["weight_kg"]), float(data["height_cm"]))
    return jsonify({"bmi": result})


if __name__ == "__main__":
    app.run(debug=True)
