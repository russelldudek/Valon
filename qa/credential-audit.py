#!/usr/bin/env python3
"""Fail when role-irrelevant credentials leak into the Valon campaign."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = "Food Safety Management Certification"
TEXT_FILES = [
    p for p in ROOT.rglob("*")
    if p.is_file() and p.suffix.lower() in {".html", ".css", ".js", ".json", ".md", ".txt"}
]

matches = []
for path in TEXT_FILES:
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
