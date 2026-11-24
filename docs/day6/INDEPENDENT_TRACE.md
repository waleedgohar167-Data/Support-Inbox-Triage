# Day 6 — Ticket Trace

## Selected ticket
Ticket ID: T002
Source file: data/inbox.csv
Message: I was charged twice for last month

## 1. Read the input
File: main.py
Function: read_tickets()

The function reads the CSV and checks the required columns.
T002 has a nonblank ID and message, so it is retained.
Its original ID and message are preserved.

## 2. Coordinate processing
File: main.py
Function: triage_tickets()

The function copies each ticket, adds its category and priority,
then passes it to process_ticket().

## 3. Assign the category
File: category.py
Function: categorize()

The function checks a lowercase version of the message.
The word "charged" matches a billing keyword.
Expected category: billing.

## 4. Assign the priority
File: priority.py
Function: assign_priority()

The phrase "charged twice" matches a high-priority pattern.
Expected priority: high.

## 5. Decide whether human review is needed
File: review.py
Functions: process_ticket() and needs_human_review()

Human review is required when priority is high OR category is other.
T002 has high priority, so its review flag is True.
This flag identifies a ticket for review; it does not prove that a
person has reviewed it or that a review task was assigned elsewhere.

## 6. Select the reply draft
File: review.py
Function: process_ticket()

The billing category selects this fixed draft:

"Thank you for contacting us about your billing concern. Our support
team will review the details and follow up with you."

The application generates draft text. It does not send the reply,
issue a refund or change the customer's account.

## 7. Export the result
File: exporter.py
Function: export_triaged_tickets()

The function writes the processed ticket to output/triaged.csv.
It writes the six defined columns and overwrites the output on reruns.
The boolean review flag is written as True in the CSV.

## Expected output
- ticket_id: T002
- message: I was charged twice for last month
- category: billing
- priority: high
- needs_human_review: True
- reply_draft: the billing draft quoted above

## Execution verification

I ran the application and inspected ticket T002 in output/triaged.csv.
The output showed category billing, priority high, human review True,
and the billing reply draft. These values matched the expected result.

