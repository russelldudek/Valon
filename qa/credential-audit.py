#!/usr/bin/env python3
"""Fail when a role-irrelevant credential appears in recruiter-facing Valon materials."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = "Food Safety Management " + "Certification"
TEXT_FILES = [
    ROOT / "resume.html",
    ROOT / "index.html",
    ROOT / "cover-letter.html",
    ROOT / "interview-brief.html",
    ROOT / "entry-plan.html",
    ROOT / "field-build-brief.html",
]

matches = []
for path in TEXT_FILES:
    if not path.exists():
        matches.append(f"missing:{path.relative_to(ROOT)}")
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    if EXCLUDED.casefold() in text.casefold():
        matches.append(str(path.relative_to(ROOT)))

resume_pdf = ROOT / "docs" / "Russell-Dudek-Valon-Resume.pdf"
if resume_pdf.exists():
    result = subprocess.run(
        ["pdftotext", str(resume_pdf), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    if EXCLUDED.casefold() in result.stdout.casefold():
        matches.append(str(resume_pdf.relative_to(ROOT)))
else:
    matches.append(f"missing:{resume_pdf.relative_to(ROOT)}")

if matches:
    print("Excluded credential found in: " + ", ".join(matches), file=sys.stderr)
    raise SystemExit(1)

print("Credential relevance audit passed: excluded credential matches = 0")
