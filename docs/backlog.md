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
- Age outside 6–59 months returns HTTP 400.

**US4 – Health check**
- GET /health returns HTTP 200 and {"status": "ok"}.

**US5 – Logging**
- Each assessment request is logged with time and result.
- Invalid requests are logged as warnings.

**US6 – Assessment history**
- Past assessments can be listed by child ID. (Not planned for Sprint 1 or 2.)
