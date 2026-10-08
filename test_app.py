from app import app, calculate_bmi


def test_calculate_bmi():
    # 12 kg and 85 cm should give BMI 16.6 (from US1 acceptance criteria)
    assert calculate_bmi(12, 85) == 16.6


def test_bmi_endpoint():
    client = app.test_client()
    response = client.post("/bmi", json={"weight_kg": 12, "height_cm": 85})
    assert response.status_code == 200
    assert response.get_json() == {"bmi": 16.6}
