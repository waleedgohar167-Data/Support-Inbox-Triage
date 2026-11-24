# Day 5 Block B - Negative Input Handling

## Scope

This block adds controlled handling for malformed or unavailable input while preserving valid records.

### Behavior

- Missing `data/inbox.csv`: `main()` prints a clear `ERROR:` message and returns exit code `1`.
- Missing required CSV columns: `read_tickets()` raises `ValueError` identifying the missing column(s).
- Blank `ticket_id`: row is skipped with a warning.
- Empty or whitespace-only `message`: row is skipped with a warning.
- Missing required row values: row is skipped with a warning.
- Headers with no records: returns an empty list.
- UTF-8 BOM headers are accepted with `utf-8-sig`.
- Valid rows are preserved.

The Day 2 assignment proposed skipping blank records with a warning and a useful error for a missing file. Day 5 requires undefined behavior to be reported rather than inventing a new business rule. This implementation stays within that input-handling scope and does not alter category, priority, review, or reply rules.

## Verification

Run:

```powershell
python -m unittest tests.test_day5_negative_inputs -v
python -m unittest discover -s tests -v
```

For the missing-file application behavior:

```powershell
Copy-Item data\inbox.csv data\inbox.csv.backup
Remove-Item data\inbox.csv
python main.py
$LASTEXITCODE
Move-Item data\inbox.csv.backup data\inbox.csv
```

Expected application behavior:

```text
ERROR: Input CSV not found: data/inbox.csv
1
```
