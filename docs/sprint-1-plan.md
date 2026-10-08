# Sprint 1 Plan

## Sprint Goal
Deliver a working first version of the service that can calculate BMI and
classify nutrition status from MUAC, with automated tests running in a CI pipeline.

## Selected Stories
| ID | Story | Points |
|----|-------|--------|
| US1 | BMI calculation from weight and height | 3 |
| US2 | Nutrition status from MUAC | 3 |
| **Total** | | **6** |

## Tasks
- Set up the project structure (Flask app, requirements.txt, .gitignore)
- Write the BMI calculation function and the /bmi endpoint (US1)
- Write the MUAC classification function and the /assess endpoint (US2)
- Write unit tests with pytest for US1 and US2
- Set up a GitHub Actions CI pipeline that runs the tests on every push
- Update the README with how to run the service

## Out of Scope for Sprint 1
- Input validation (US3), health endpoint (US4) and logging (US5) are planned for Sprint 2.
