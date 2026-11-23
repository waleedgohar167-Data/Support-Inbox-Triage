# Support Inbox Triage — Training Project

Support teams need to organize incoming customer messages so that requests can be categorized and directed to the right people. Support Inbox Triage is a training-only Python starter for a planned workflow that reads messages, classifies them, identifies cases needing human review, and exports an organized CSV. The synthetic messages in `data/inbox.csv` provide consistent examples for development and later testing without using real customer data. Currently, `main.py` only prints a setup message; CSV loading, classification, human-review decisions, and export are not implemented. With Python 3.11+ available, run the starter from the project folder using `python main.py` (or `py main.py` on Windows). Run `python -m unittest discover -s tests -v` for the supplied test, which only checks that `1 + 1 == 2` and does not execute `main.py` or test ticket handling.

## Setup (Day 1)

- Confirm Python 3.11+ and Git are available.
- Open this folder in your code editor.
- Run `python main.py` (on Windows, use `py main.py` if `python` does not work).
- Run `python -m unittest discover -s tests -v`.
- Before each new task after review/merge, switch to the default branch, pull, and create a new feature branch.

## Never use real customer data

The sample records are synthetic. Do not upload company/customer secrets, tokens, or private data to public AI tools.

## Day 1 small task

Using a feature branch, add your own 4–6 sentence explanation of what this training project will do and how to run the existing starter. If you have GitHub access, open a pull request; otherwise, use the offline submission option in `DAY_1_EXECUTION.md`.

## Requirements

To be completed and reviewed on Day 2 in `docs/REQUIREMENTS.md`.

python main.py

python -m unittest discover -s tests -v
