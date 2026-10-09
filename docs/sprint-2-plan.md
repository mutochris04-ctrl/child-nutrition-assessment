# Sprint 2 Plan

## Sprint Goal
Make the nutrition service safer and more reliable: detect oedema, give clear error messages, and make the service easy to monitor.

## Selected User Stories

| ID | Story | Priority | Points |
|----|-------|----------|--------|
| US7 | Record bilateral oedema so severe malnutrition is not missed | Must | 2 |
| US3 | Clear error messages for wrong or missing values | Should | 2 |
| US4 | Health check endpoint to confirm the service is running | Should | 1 |
| US5 | Log requests and errors to monitor and debug the service | Should | 2 |

**Total: 7 points**

## Tasks
- Add oedema to the MUAC assessment (US7) with tests
- Add input validation and clear error messages (US3) with tests
- Add a /health endpoint (US4) with a test
- Add logging for requests and errors (US5)
- Update the README with run and test instructions
- Keep CI green after every commit

## Definition of Done
Each story meets its acceptance criteria, has passing tests, passes CI, and is committed in small steps.