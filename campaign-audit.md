# Campaign Audit

## Current state

- State: `building` until the corrected live deployment is retrieved and matched to the corrected `main` head.
- Target role: Valon — Applied AI Strategist, New Ventures.
- Candidate thesis: **Make AI transformation survive contact with the work.**

## User-directed correction

Observed defects:
- the hero headline exceeded its grid column and visually crossed into the operating artifact;
- the fixed-height Buildline stack and absolutely positioned platform-return block overlapped on narrow screens;
- the full interaction, status, controls, and readouts overloaded the opening viewport;
- the hero CTA pointed to the artifact already beside it;
- the application documents were discoverable primarily as plain footer links;
- every online document route was an iframe wrapper around a PDF rather than a readable web document.

Correction taxonomy:
- hero hierarchy and restraint;
- rendered geometry;
- causal and visual economy;
- CTA and visitor journey;
- screen and print documents.

Approved correction:
- the hero now presents one thesis and one restrained Field-to-Platform principle panel;
- the interactive Buildline moved into a dedicated operating-model section;
- the Buildline uses content-driven grid height and an in-flow platform-return record;
- the default scenario is explicitly labeled illustrative and includes reset-to-baseline behavior;
- a prominent five-card Application Kit appears before the final executive-question section;
- all five document routes are native, responsive online documents with separate PDF download actions;
- resume and cover letter retain reciprocal navigation.

Prior rendered and live proof is invalidated by this material correction.

## Regression coverage

`qa/site-audit.py` now fails when:
- the hero headline's rendered text exceeds its own box;
- the full Buildline returns to the hero;
- the dedicated Buildline section is absent;
- the Application Kit is absent, contains fewer than five cards, or appears after the footer;
- the platform-return record overlaps any Buildline layer;
- any audited viewport has horizontal overflow;
- an online document embeds an iframe, lacks native document content, or lacks a native PDF download.

## Local rendered QA

Validated with Chromium at:
- 1440 × 900;
- 1280 × 800;
- 768 × 1024;
- 390 × 844;
- 320 × 800;
- reduced-motion mode.

Passed locally:
- headline containment and zero horizontal overflow;
- no Buildline layer/platform-return overlap;
- useful illustrative starting state and reset;
- pointer and keyboard scenario operation;
- atomic status, active-layer, posture, evidence, and platform-return updates;
- rapid-selection final-state authority;
- reduced-motion semantic resolution;
- five discoverable document cards;
- five native online document routes with no iframe viewer;
- responsive document reflow at 1280, 390, and 320 pixels;
- reciprocal resume/cover-letter navigation;
- native same-origin PDF download links.

## Documents and PDFs

- Resume PDF: exactly 2 pages.
- Cover letter PDF: exactly 1 page.
- Interview brief PDF: exactly 1 page.
- 90-day plan PDF: exactly 1 page.
- Field-to-Platform Buildline brief PDF: exactly 1 page.

The material correction changes screen document delivery, not the already audited PDF content or pagination.

## Brand fidelity

- Source-sampled cream, near-black, and gold are documented.
- A candidate-original forest accent is restricted to the operating artifact and application-kit panel.
- Typography substitution and independent-candidate treatment are documented.
- **Open gate:** the official wordmark remains unavailable as a locally committed asset because the official public SVG could not be retrieved through the connected environment. Brand fidelity therefore remains blocked rather than marked passed.

## Confidentiality

- Public source scan found zero internal orchestration-name matches.
- No campaign source repository is linked from candidate-facing files.
- PDF filenames and candidate-facing metadata use neutral candidate-owned terminology.
