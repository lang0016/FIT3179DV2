# Who farms Australia?

An Australian Farmers data story by **Ang Lin Shan**, FIT3179 DV2,
**Monash University · Malaysian campus**.

**Website:** https://lang0016.github.io/FIT3179DV2/

The public page returned HTTP 200 on 20 October 2026. Review the final deployed version before submission.

Twelve Vega/Vega-Lite charts tell a single scrolling story about agricultural
businesses, farmers, sector differences and change over time. The three map
idioms are a normalised choropleth, proportional symbols and a custom
non-contiguous cartogram. Every chart has a human-readable JSON specification,
source link, keyboard-reachable accessible label and expandable data table.

## Read and submit

- [Moodle description: domain, audience, data and design rationale](submission/MOODLE_DESCRIPTION.md)
- [One-time GitHub Pages activation](submission/PUBLISHING.md)
- [Remaining student submission checklist](submission/SUBMISSION_CHECKLIST.md)
- [Hand-drawn A4 sketch guide](SKETCH_GUIDE.md)
- [Interview preparation](submission/INTERVIEW_NOTES.md)
- [Research-backed chart plan](PROJECT_PLAN.md)
- [Sources, definitions, preparation and limitations](DATA_RESEARCH.md)
- [Data extracts and provenance](data/README.md)
- [Validation report](VALIDATION.md)

**Still required from the student:** draw and upload the hand-drawn sketch PDF,
review your AI acknowledgement for accuracy, review the
written description, submit on Moodle and prepare for the interview. The sketch PDF is not supplied; the acknowledgement text is present for student review.

## Run locally

The committed static site needs no build or runtime package installation:

```sh
python3 -m http.server 8000
```

Serve the repository root over HTTP. Chart paths are relative, so the same files
work under the repository's GitHub Pages path. Chart libraries are vendored in
`assets/vendor/` with their licence notices; no external CDN is required to render.

## Reproduce data and specifications

Use a virtual environment and source directory outside the checkout:

```sh
python3 -m venv /tmp/farmers-build-venv
/tmp/farmers-build-venv/bin/pip install -r scripts/requirements-build.txt
/tmp/farmers-build-venv/bin/python scripts/prepare_research_data.py --source-dir /tmp/farmers-originals --download
/tmp/farmers-build-venv/bin/python scripts/prepare_maps.py --source-dir /tmp/farmers-originals
/tmp/farmers-build-venv/bin/python scripts/build_charts.py
```

Source downloads use normal HTTPS verification and recorded checksums. If a
source changes, investigate the revision; do not blindly replace a checksum.
Only filtered factual extracts and simplified geometry are committed. ABS and
Dairy Australia counts are kept distinct; confidentiality adjustments are not
silently corrected. Scripts preserve source-row and series identifiers.

## Check the rendered page

```sh
npm ci
npx playwright install chromium
npm test
```

The test starts its own HTTP server and checks 1180, 1280, 1366 and 1440 px.
It requires all twelve charts and accessible SVG labels, no failed requests or
console errors/warnings, no horizontal overflow, no clipped/overlapping SVG
text, no paragraph line longer than ten words, functional highlighting and data
tables, and less than 2 MB of requested chart data/specifications.
Screenshots and results go to ignored `.browser-tests/`. GitHub Actions runs the
same checks on pushes. Use `SITE_URL` to run the test against the public site.

## Colour meanings

| Colour | Meaning |
| --- | --- |
| Deep blue `#174a67` | Overall agriculture: businesses or workforce, with units explicitly stated. |
| Violet `#6e4b87` | Registered dairy-farm case study, consistently across its charts. |
| Ordered blue lightness `#4c7189` → `#113650` | Increasing quantity or ordered business-size class, never separate sector identities. |
| Slate `#53656e` | Earlier-date baseline and contextual labels. |
| Light grey `#e4e7e2` | Geographic context; unreported NT/ACT in the dairy map are labelled, not represented as zero. |
| Ink `#233942` outline | Selected sector; other values remain fully visible and retain contrast. |

Sector names are written directly; readers do not need to memorise nine hues.
Text and quantitative mark colours meet at least 4.5:1 against the paper
background `#f7f5ef`. Pure contextual geographic fills are muted. There is no
red/green comparison or rainbow quantity palette.

## Sources and authorship

Primary data publishers are the Australian Bureau of Statistics and Dairy
Australia. The latest verified observations are June 2025 detailed businesses,
2024–25 registered dairy farms (provisional), and February 2026 workforce
estimates. Each chart states its own period. Based on Australian Bureau of
Statistics data, with CC BY 4.0 attribution and stated exceptions. Dairy Australia
is credited for a small factual numeric extract; its PDF, photos and artwork are
not redistributed. See the research register for complete URLs and methods.

This project received generative-AI assistance with research, planning, code and
writing. That process disclosure does not replace the student's own submission
acknowledgement, which remains clearly marked on the page.

Chart readability revisions: chart 04 compares percentage changes against a shared
2024 baseline; section 04 uses full-width, directly labelled sector charts. The
workforce chart shows complete-year averages with labelled endpoints, while the
latest quarterly estimate remains separately identified in its note.

Section 04 now groups all three sector comparisons: relative regional
concentration (1× = eight-state reference mix), three-band turnover composition
ranked by the high-sales share, and state-level staffing distributions. The
heatmap uses ochre for below-reference ratios and blue for above-reference
ratios; exact shares, counts and ratios remain in the accessible table.

The farmer age/sex pyramid uses blue for source-category males and ochre
(`#926039`) for females, with a dark vertical zero line and matching side keys.

Lecturer feedback revisions reduce the title and banner emphasis, darken
paragraph text, align paired plotting rows and restrict heatmap labels to
the key finding or selected sector. Chart 10 now pairs a complete geographic
reference with the six reported count-scaled dairy state silhouettes.

See [RUBRIC_REVIEW.md](RUBRIC_REVIEW.md) for the official-rubric audit and
the latest chart refinements. Headings use the locally hosted Lora typeface;
body text and quantitative labels retain Arial. The licence is bundled with
the font. Sales bands use aligned 0–100% bars with directly labelled high-sales shares, and the treemap
contains an explicit employment-status hierarchy with direct labels for all staff-size groups.

The employee treemap now occupies its own row, using high-contrast blue and
light gold for employment status. A strong outline groups employing businesses;
four leader-line callouts show every staff-size category and exact business
count without enlarging tiny rectangles. The workforce trend follows beneath.
