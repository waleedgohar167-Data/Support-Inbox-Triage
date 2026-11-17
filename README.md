# Support Inbox Triage — Training Project

Support Inbox Triage is a training-only Python application designed to help organize incoming customer-support messages by preparing them for categorization, human-review decisions, and structured output. The sample `data/inbox.csv` contains synthetic support messages that provide safe, consistent input for development and later testing, while the project must never use real customer or confidential data. The planned application will eventually read these messages, classify them, determine whether human review is needed, and export an organized CSV result, but those core triage features are not implemented in the current starter. To run the existing starter, confirm Python 3.11+ and Git are available, open the project folder in a terminal, and run `python main.py` (or `py main.py` on Windows if `python` is not recognized). The supplied test suite can be run with `python -m unittest discover -s tests -v`; these starter checks verify the current baseline only and do not prove that ticket classification has been implemented.

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
