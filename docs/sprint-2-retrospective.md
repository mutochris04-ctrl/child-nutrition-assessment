# Sprint 2 Retrospective

## Did I apply the Sprint 1 improvements?

| Sprint 1 improvement | What I did in Sprint 2 | Result |
|----------------------|------------------------|--------|
| Handle bad input properly | Delivered US3: missing or wrong muac_cm returns HTTP 400 with a clear message | Done |
| Keep the README up to date | Added run, test and endpoint instructions; updated it with each change | Done |
| Check my changes before committing | Moved from Notepad to VS Code so I can see my changes before committing | Done |

## What went well
- The whole process was fun.
- All 4 planned stories were finished, each with tests.
- Small commits and green CI gave clear proof of progress.
- Moving from Notepad to VS Code made my work easier to track and prove.

## What was difficult
- Learning VS Code, the Terminal and Git for the first time.
- Signing in to GitHub from VS Code and pushing my work.

## What I will do better
- Ask myself WHY before adding a feature to the project.
- Example: the MUAC tape already shows the nutrition status with colours, so an online service adds more value by calculating weight-for-age, weight-for-height and height-for-age (z-scores).
- For MUAC, the online value is recording children so leaders, health centres and district hospitals can follow them.

## Ideas for the next sprint
- Add WHZ, WAZ and HAZ z-score assessment.
- Store child records that health centres and district hospitals can view.

## Improvements for Sprint 3

| # | Improvement | How I will apply it |
|---|-------------|---------------------|
| 1 | Test edge cases, not only normal values | Write tests for values at, just below and just above each cut-off (11.5 and 12.5), and for wrong types (like "false" as text). This would have caught the oedema bug earlier. |
| 2 | Check every acceptance criterion before saying "Done" | Go through the criteria one by one in the review. The age check in US3 was missed, so it is now its own story (US8). |
| 3 | Ask "why" before adding a feature | Plan US9 (z-scores) because it gives value the MUAC tape cannot give. |
