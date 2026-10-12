# Product Backlog

Priority uses MoSCoW (Must / Should / Could). Estimates are story points (Fibonacci).

| ID | User Story | Priority | Points | Sprint |
|----|-----------|----------|--------|--------|
| US1 | As a health worker, I want to enter a child's weight and height and get their BMI, so that I can quickly check body size. | Must | 3 | 1 |
| US2 | As a health worker, I want to enter a child's MUAC (mid-upper arm circumference) and get a nutrition status, so that I can identify malnourished children. | Must | 3 | 1 |
| US3 | As a health worker, I want clear error messages when I enter wrong or missing values, so that I can correct my input. | Should | 2 | 2 |
| US4 | As a system administrator, I want a health check endpoint, so that I can confirm the service is running. | Should | 1 | 2 |
| US5 | As a developer, I want requests and errors to be logged, so that I can monitor and debug the service. | Should | 2 | 2 |
| US6 | As a health worker, I want to see a history of past assessments, so that I can follow a child's progress. | Could | 5 | Future |
| US7 | As a health worker, I want to record whether a child has oedema (swelling in both feet), so that children with severe malnutrition are not missed. | Must | 2 | 2 |
| US8 | As a health worker, I want the service to check that the child is 6–59 months old, so that MUAC cut-offs are only used for the right age group. | Should | 2 | 3 |
| US9 | As a health worker, I want weight-for-height, weight-for-age and height-for-age z-scores (WHZ, WAZ, HAZ), so that I get more information than the MUAC tape alone gives. | Must | 8 | Future |
| US10 | As a health centre or district hospital, I want to see the records of children screened in the community, so that we can follow up referred children. | Could | 8 | Future |

## Acceptance Criteria

**US1 – BMI calculation**
- Given weight (kg) and height (cm), the service returns BMI rounded to 1 decimal.
- Example: 12 kg and 85 cm returns BMI 16.6.

**US2 – MUAC nutrition status** (children 6–59 months, WHO cut-offs)
- MUAC below 11.5 cm returns "Severe Acute Malnutrition".
- MUAC from 11.5 to below 12.5 cm returns "Moderate Acute Malnutrition".
- MUAC 12.5 cm or more returns "Normal".

**US3 – Input validation**
- Missing, non-numeric, zero or negative values return HTTP 400 with an error message.
- Age validation (6–59 months) was moved to its own story, US8, during Sprint 2 planning because the service does not take age yet.

**US4 – Health check**
- GET /health returns HTTP 200 and {"status": "ok"}.

**US5 – Logging**
- Each assessment request is logged with time and result.
- Invalid requests are logged as warnings.

**US7 – Oedema**
- If oedema is true, the status is always "Severe Acute Malnutrition", whatever the MUAC.
- If oedema is not sent, it is treated as false.
- If oedema is not true or false (for example the text "false"), the service returns HTTP 400 with an error message.

**US8 – Age check** (Sprint 3)
- /assess accepts age_months.
- Age below 6 or above 59 months returns HTTP 400 with an error message.

**US6 – Assessment history**
- Past assessments can be listed by child ID. (Not planned for Sprint 1 or 2.)

**US9 / US10** – acceptance criteria to be written in backlog refinement before they are planned.

## Backlog changes
- Sprint 2: added US7 (oedema) after learning that bilateral oedema always means severe malnutrition.
- After Sprint 2: added US8 (age check, split out of US3), US9 (z-scores) and US10 (records for health centres) from the Sprint 2 retrospective.
