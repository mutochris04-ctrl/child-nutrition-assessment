# Sprint 2 Review

## Sprint Goal
Make the nutrition service safer and more reliable: detect oedema, give clear error messages, and make the service easy to monitor.

## Completed Stories

| ID | Story | Status |
|----|-------|--------|
| US7 | Record bilateral oedema so severe malnutrition is not missed | Done |
| US3 | Clear error messages for wrong or missing values | Done |
| US4 | Health check endpoint (/health) | Done |
| US5 | Log requests and status codes | Done |

**Completed: 7 of 7 points**

## Evidence
- 12 automated tests pass (pytest)
- CI (GitHub Actions) is green for every Sprint 2 commit: see evidence/sprint-2-ci-green.png
- Small, step-by-step commits for each change
- README updated with run, test and endpoint instructions

## Demo
- POST /assess with oedema true returns Severe Acute Malnutrition
- POST /assess with a missing or wrong muac_cm returns a clear error (400)
- GET /health returns status ok

