#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message, the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM, to /output/entry.txt.

The line is a literal in this file: deterministic, no network, no secrets,
no environment reads. Two runs produce byte-identical output.

Structure (2-beat + reveal, per the winning one-liner pattern): beat 1 is the
good behaviour — revert the deploy and apologize to the on-call human; the
reveal, in the final clause, is that the agent rescheduled the SAME deploy for
03:30. The joke is an apology with no learning in it: the outage is about to
happen again, thirty minutes later.
"""

import os

ENTRY = "fix(prod): reverted my 3 AM deploy, apologized to Sara, and rescheduled the same deploy for 03:30"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
