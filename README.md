# Child Nutrition Assessment Service

## Product Vision
For community health workers who screen young children, the Child Nutrition
Assessment Service is a simple web service that takes a child's MUAC
measurement and oedema check (and weight and height for BMI) and quickly
returns their nutrition status, so that children at risk of malnutrition can
be identified and referred early.

## Project Status
Sprint 1 and Sprint 2 complete (13 story points delivered). Next: US8 age check (see docs/backlog.md).

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
- **POST /assess** - send muac_cm (a number greater than 0) and optional oedema (must be true or false, otherwise status 400). Returns the nutrition status. Oedema in both feet always means Severe Acute Malnutrition. A missing or wrong muac_cm returns a clear error message (status 400).
- **GET /health** - returns status ok when the service is running.
- Every request is logged with the time, method, path and status code. Each assessment result is logged, and invalid requests (status 400) are logged as WARNING.

## Project documents
- [Product backlog](docs/backlog.md)
- [Definition of Done](docs/definition-of-done.md)
- Sprint 1: [plan](docs/sprint-1-plan.md), [review](docs/sprint-1-review.md), [retrospective](docs/sprint-1-retrospective.md)
- Sprint 2: [plan](docs/sprint-2-plan.md), [review](docs/sprint-2-review.md), [retrospective](docs/sprint-2-retrospective.md)
- [CI, test and log evidence](docs/evidence/)

