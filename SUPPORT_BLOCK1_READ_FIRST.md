# Block 1 checkpoint update

This update contains two completed draft logs and the assisted verification transcript. It does not replace the application, tests, README, sample data or assignment guides.

## Apply in order

1. Extract the ORIGINAL `Day_1_Candidate_Ready_To_Send.zip` into a separate project folder and open the inner `Day_1_AI_Engineering_Candidate_Package` folder in VS Code. It is the folder containing `main.py`.
2. Preserve the original starter in Git before applying this update, following the supplied guide:

```powershell
git init -b main
git add .
git commit -m "chore: initialize day 1 starter"
git switch -c docs/day1-onboarding
```

If this project is already initialized, inspect its status and preserve existing work instead of repeating initialization. Use your own configured Git identity if Git requests it. No remote repository is needed for these local steps.

3. Extract `Support_Inbox_Triage_Day1_Block1_Update.zip` into that same inner project folder. It replaces only `docs/WORKLOG.md` and `docs/AI_USAGE_LOG.md`, and adds the transcript and this instruction file. If you already added entries to either log, merge the supplied entries rather than overwriting your work.
4. Read the notes and compare the implementation in `main.py`, `tests/test_smoke.py`, the CSV files and the README. Revise the explanation to reflect your own understanding. Record the personal checks you actually performed in `docs/AI_USAGE_LOG.md` and update the Block 1 worklog status when your review is complete.

## Local verification for the next checkpoint

```powershell
python --version
git --version
python main.py
python -m unittest discover -s tests -v
```

Use `py` instead of `python` on Windows if the Python command is unavailable. No pip installation or paid API is needed.

Expected app output: `Project setup OK — core ticket triage is not built yet.`

Expected test result: one passing arithmetic smoke test. Record the output you actually observe. A pass does not demonstrate CSV processing or classification.

The included transcript is Linux verification evidence and must remain labeled that way. Add your own local output separately. The root instruction file does not need to be committed. GitHub access, if absent, has an offline submission route in the original guide.
