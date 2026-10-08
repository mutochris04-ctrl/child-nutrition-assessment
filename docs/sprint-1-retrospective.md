# Sprint 1 Retrospective

## What went well
- Both planned stories (US1 and US2) were delivered, so the sprint goal was met.
- Seeing the CI pipeline run green after every commit was motivating. It felt great that things were running well.
- Writing tests directly from the acceptance criteria (e.g. 12 kg / 85 cm = BMI 16.6, WHO MUAC cut-offs) made it clear when a story was really done.
- Small, frequent commits with clear messages made the progress easy to follow.
- I enjoyed the work and learned a lot about GitHub, Flask and automated testing.

## What did not go so well
- Finding the right buttons in GitHub required a lot of focus, so I worked slowly.
- Once I pasted an old version of app.py by mistake and had to redo the step.
- The README still does not explain how to run the service, so one Definition of Done item was only partly met.
- The service has no input validation: if a value is missing or not a number, it crashes with a server error (HTTP 500) instead of a helpful message.

## Improvements for Sprint 2
| # | Improvement | How I will apply it |
|---|-------------|---------------------|
| 1 | Handle bad input properly | Deliver US3: return HTTP 400 with a clear error message for missing, non-numeric or negative values. |
| 2 | Keep the README up to date | Add "how to run" and "how to test" instructions in Sprint 2, and update the README as part of each story. |
| 3 | Check my changes before committing | Use the Preview tab / read the code once before clicking Commit, to avoid pasting the wrong version. |
