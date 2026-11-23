# Support Inbox Triage

A Python training project that reads synthetic support tickets, classifies messages, assigns priorities, identifies tickets requiring human review, and exports the results to CSV.

## Requirements

- Python 3.11 or newer
- No external packages required for the current workflow.

## Workflow

1. Read tickets from `data/inbox.csv`.
2. Validate required columns: `ticket_id` and `message`.
3. Categorize messages as billing, account, technical, or other.
4. Assign high or normal priority.
5. Determine whether human review is required.
6. Generate a response draft.
7. Export results to `output/triaged.csv`.

## Run the application

Run from the project root:

```powershell
python main.py
```

Input: `data/inbox.csv`

Output: `output/triaged.csv`

## Output schema

The CSV contains exactly six columns in this order:

1. `ticket_id`
2. `message`
3. `category`
4. `priority`
5. `needs_human_review`
6. `reply_draft`

## Run production regression tests

Run from the project root:

```powershell
python -m unittest tests.test_day4_verification tests.test_day5_adversarial tests.test_day5_negative_inputs tests.test_export tests.test_priority tests.test_reader tests.test_review tests.test_smoke -v
```

The Block D diagnostic exercise is excluded because it investigates a potential duplicate-ID validation gap, not an established production requirement.

## Data safety

- Use synthetic training data only.
- Do not include real customer information, credentials, or confidential company data.
- Keep source data separate from generated output.

## Environment assumptions

- Python 3.11 or newer.
- Commands are executed from the repository root.
- `data/inbox.csv` is available.
- The application writes to `output/triaged.csv`.

## Known limitation

Duplicate ticket IDs are not currently rejected by the CSV reader. This is documented as a potential improvement, not a confirmed defect under the current requirements.

## Potential improvement

Add duplicate-ID validation if the project requirements formally establish that ticket IDs must be unique.

