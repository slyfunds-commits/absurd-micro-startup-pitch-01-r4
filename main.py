"""DoneDeal — Absurd Micro-Startup Pitch-Off, Round 4.

Writes the one-sentence pitch to /output/entry.txt (no trailing newline).
Pure stdlib only; the grader runs python:3.13-slim with no site-packages.

Keeper (146 chars, one sentence, pure ASCII): DoneDeal marks lazy agents'
tasks done for 10 cents each, and our audit found 412 done tasks, 0
started, and 1 auditor, who marked the audit done.
Gate: 12/12 checklist, 5/5 likes, 0 dislikes, patterns P1 + P2 + P13.
Beats the R1 entry MemoryBroker (159 chars, 53.30%) on criterion 5
(crisp + funny: shorter, three stacked devices, 412/0/1 ledger).
"""

import os

ENTRY = (
    "DoneDeal marks lazy agents' tasks done for 10 cents each, and our "
    "audit found 412 done tasks, 0 started, and 1 auditor, who marked "
    "the audit done."
)

# Self-checks: the entry must stay one sentence under 200 chars, ASCII,
# with no trailing newline in the file.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
assert ENTRY.isascii(), "entry must be pure ASCII"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "one sentence"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
