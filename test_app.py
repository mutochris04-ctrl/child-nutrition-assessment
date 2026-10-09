from app import app, calculate_bmi, classify_muac


# ---------- US1: BMI ----------

def test_calculate_bmi():
    # 12 kg and 85 cm should give BMI 16.6 (from US1 acceptance criteria)
    assert calculate_bmi(12, 85) == 16.6


def test_bmi_endpoint():
    client = app.test_client()
    response = client.post("/bmi", json={"weight_kg": 12, "height_cm": 85})
    assert response.status_code == 200
    assert response.get_json() == {"bmi": 16.6}


# ---------- US2: MUAC nutrition status ----------

def test_muac_severe():
    assert classify_muac(11.0) == "Severe Acute Malnutrition"


def test_muac_moderate():
    assert classify_muac(12.0) == "Moderate Acute Malnutrition"


def test_muac_normal():
    assert classify_muac(13.0) == "Normal"


def test_muac_boundaries():
    # Exactly 11.5 is moderate, exactly 12.5 is normal (WHO cut-offs)
    assert classify_muac(11.5) == "Moderate Acute Malnutrition"
    assert classify_muac(12.5) == "Normal"


def test_assess_endpoint():
    client = app.test_client()
    response = client.post("/assess", json={"muac_cm": 11.0})
    assert response.status_code == 200
    assert response.get_json()["status"] == "Severe Acute Malnutrition"


def test_muac_oedema():
    assert classify_muac(13.0, oedema=True) == "Severe Acute Malnutrition"

def test_assess_missing_muac():
    client = app.test_client()
    response = client.post('/assess', json={})
    assert response.status_code == 400


def test_assess_invalid_muac():
    client = app.test_client()
    response = client.post('/assess', json={'muac_cm': 'abc'})
    assert response.status_code == 400

