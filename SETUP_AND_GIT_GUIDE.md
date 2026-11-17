# Setup and Git guide — Day 1

The project uses **Python standard library only**. No `pip install`, credit card, paid API, or cloud subscription is required.

## Step A — Open the project
1. Extract the candidate ZIP into a folder you can edit.
2. Open the extracted folder in VS Code or another code editor.
3. Open a terminal in the folder that contains `main.py`.
4. Verify your location: `pwd` (macOS/Linux) or `cd` (Windows Command Prompt); list files with `ls` (macOS/Linux) or `dir` (Windows).

## Step B — Check tools and run
```
python --version
git --version
python main.py
python -m unittest discover -s tests -v
```
If `python` is not recognized on Windows, try `py`; on macOS/Linux try `python3`. The starter app should print a setup message, and the smoke test should pass. These tests do **not** prove future ticket classification features.

If Python or Git is missing, download only from the official websites:
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads
- VS Code (optional if another approved editor works): https://code.visualstudio.com/

**Timebox environment fixes:** 15 minutes per blocking problem, then report what failed and continue with independent reading/README notes while access is resolved.

## Step C — Version control on a newly extracted folder
Run from the project folder. The candidate ZIP does not include Git history.
```
git init -b main
git add .
git commit -m "chore: initialize day 1 starter"
git switch -c docs/day1-onboarding
```
If Git asks for your name/email, configure **your own** identity, then retry the commit:
```
git config user.name "Your Name"
git config user.email "your-email@example.com"
```
Use your actual name/email; the example is not a real address.

After editing `README.md`, `docs/WORKLOG.md`, `docs/AI_USAGE_LOG.md`:
```
git diff
git status
python main.py
python -m unittest discover -s tests -v
git add README.md docs/WORKLOG.md docs/AI_USAGE_LOG.md
git commit -m "docs: complete day 1 onboarding"
git log -1 --oneline
```

## Step D — Submission with or without GitHub
**If you have authorized access to a private company repository:** follow your company's repository instructions; push your branch and create a pull request. Do not accidentally create a public repository with company materials.

**If you do not have GitHub access:** do not wait or create an unauthorized public repository. Save the local Git commit, zip the changed project folder, and submit the ZIP + your commit hash + an explanation in your final report. The supervisor can review it and help set up a private repository later.

## Troubleshooting
- `python` is unknown: try `py` or `python3`, then official Python installation if needed.
- `git` is unknown: install Git and reopen the terminal.
- `Author identity unknown`: set your own local Git name/email as above.
- `not a git repository`: make sure your terminal is in the folder containing `main.py` and run initialization if needed.
- Tests fail: copy exact error into WORKLOG. Do not report PASS unless you saw PASS.
- GitHub access denied: use the offline submission route; report the blocker.
