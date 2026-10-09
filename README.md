# Child Nutrition Assessment Service

## Product Vision
For community health workers who screen young children, the Child Nutrition
Assessment Service is a simple web service that takes a child's age, weight
and height and quickly returns their nutrition status, so that children at
risk of malnutrition can be identified and referred early.

## Project Status
Sprint 0 – Planning (in progress)

## How to run

1. Install the requirements:

        pip install -r requirements.txt

2. Start the service:

        python app.py

   The service runs at http://127.0.0.1:5000

## How to test

        python -m pytest

Tests also run automatically on GitHub Actions (CI) after every push.

## Endpoints

- **POST /bmi** - send weight_kg and height_cm, get the BMI.
- **POST /assess** - send muac_cm (a number greater than 0) and optional oedema (true/false). Returns the nutrition status. Oedema in both feet always means Severe Acute Malnutrition. A missing or wrong muac_cm returns a clear error message (status 400).
- **GET /health** - returns status ok when the service is running.
- Every request is logged with its method, path and status code.

