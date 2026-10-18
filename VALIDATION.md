# Validation evidence

Validated 15 October 2026 (Malaysia). Commands execute against the real static
application over HTTP, using Chromium through Playwright 1.58.2.

## Required laptop checks

`npm test` starts a local HTTP server, loads the full page and tests:

| Check | 1180 px | 1280 px | 1366 px | 1440 px |
| --- | --- | --- | --- | --- |
| All 12 charts rendered | Pass | Pass | Pass | Pass |
| All 12 SVGs have accessible labels | Pass | Pass | Pass | Pass |
| No horizontal page overflow | Pass | Pass | Pass | Pass |
| No failed requests or HTTP errors | Pass | Pass | Pass | Pass |
| No browser console errors/warnings | Pass | Pass | Pass | Pass |
| No SVG text clipping or text-to-text collisions | Pass | Pass | Pass | Pass |
| Paragraphs have ≤10 words per rendered line | Pass | Pass | Pass | Pass |
| Requested chart data/specs below 2 MB | Pass | Pass | Pass | Pass |

At 1280 px, the test additionally confirms the native sector selector updates
all three chart signals and draws a visible outline, data tables expand, and
the selector can receive keyboard focus and keyboard input. All values remain
visible during highlighting; data marks are not faded below their contrast.

Measured chart-data/specification responses: **1,260,150 bytes** (about 1.25 MB),
including official geometry, readable specs and accessible-table metadata.
Geometry is fetched once and reused by both ordinary maps. This excludes chart
library JavaScript; it is a data/specification budget, not the whole page's byte
count. Libraries are locally hosted and do not require an external chart CDN.

The test saves full-page screenshots and machine-readable results to ignored
`.browser-tests/`. The committed test is `scripts/check_site.mjs`; GitHub Actions
runs the same checks on pushes. The independent GitHub-hosted run for the site
implementation passed: [Validate visualisation](https://github.com/lang0016/FIT3179DV2/actions/runs/38613918846). `SITE_URL` can target the public page.

Additional Chromium checks at **375 px** and **768 px** confirmed all twelve
charts loaded without page overflow, console errors, or clipped SVG labels.
Narrow-screen titles, turnover legends and the cartogram label alignment adapt
for legibility. These additional widths do not replace the four required widths.

## Colour and visual review

Foreground contrast against paper `#f7f5ef`, using WCAG relative luminance:

| Colour | Ratio |
| --- | --- |
| Ink `#233942` | 11.10:1 |
| Agriculture blue `#174a67` | 8.71:1 |
| Dairy violet `#6e4b87` | 6.38:1 |
| Slate text/context `#53656e` | 5.58:1 |
| Lightest quantitative blue `#4c7189` | 4.78:1 |
| Darkest quantitative blue `#113650` | 11.55:1 |

Every intermediate quantitative shade also exceeds 4.5:1. Pale geographic
context is intentionally not a quantitative mark. White/paper text is used only
on sufficiently dark fills. No red/green comparison or rainbow quantity scale
is used; sector names and date-specific shapes reduce reliance on colour.

Rendered screenshots were reviewed for map shape/label placement, pyramid
readability, the turnover legend and the cartogram. The initial cartogram shape
collision and clipped labels were corrected. The generator now asserts that
cartogram silhouettes do not overlap. Findings and explanatory annotations sit
outside plot areas; geographic labels are names of the marks themselves.

This does not claim a human screen-reader session or a clinical colour-vision
study. It records the automated semantics/keyboard checks, contrast calculation,
restrained palette and visual review actually performed.

## Data integrity and reproducibility

- Original source sizes and SHA-256 hashes checked before extraction.
- 680 unique retained business class/state/year records; 34 national agriculture
  classes per year; 408 turnover-bin records.
- Twelve unique latest farmer age/sex cells; correct source units in thousands.
- Agriculture-only workforce series IDs retained; partial years excluded from
  annual averages.
- All fourteen registered dairy-farm rows reconcile to national totals.
- Headline percentages, state shares and waterfall contributions derive from
  those extracts; different counting units remain distinct.
- Eight valid official state geometries retained, joined by code; remote-island
  clipping and excluded geography recorded in `data/map_sources.json`.
- Cartogram areas use a common area-per-reported-farm factor after equal-area
  projection; unknown coverage is separate context, not fabricated zeros.
- Source-download reproduction and repeat preparation gave identical research
  outputs. Site chart generation uses only these extracts and geometry.

## Publication and remaining student work

Files were pushed to `main` in commit `a3a715b`. GitHub rejected first-time
Pages enablement with HTTP 403, `Resource not accessible by integration`.
The expected public site returned HTTP 404. Public browser validation has **not**
run and publication is **not claimed**. Enable branch deployment from account
settings using `submission/PUBLISHING.md`; then run the public-site check.

The hand-drawn sketch PDF is **not supplied**. The page deliberately retains a
marked placeholder for the student's own AI acknowledgement. Moodle submission,
student authorship review and the interview remain the student's tasks. See
`submission/SUBMISSION_CHECKLIST.md`.

## Readability revision

Chart 04 now uses a common 0% baseline and directly labelled percentage
changes, retaining original counts in tooltips and tables. Sector charts use
full-width rows, numeric heatmap labels and segment percentages. Chart 12
shows one complete-year-average line with endpoint labels and explicitly
discloses its 200,000-worker axis baseline. The latest quarterly estimate
remains separately identified. Source extracts were unchanged.

The revised charts passed all four required laptop widths, sector interaction
and accessible-table checks. Additional checks at 375 and 768 px confirmed
all twelve charts loaded without overflow, errors or clipped SVG text.

## Sector comparison redesign

Section 04 groups the regional specialisation heatmap, three-band turnover
composition and state staffing box plots in full-width rows. The heatmap uses
within-state sector share divided by the sector share across the same eight
states; 1× is the reference. This is a concentration ratio, not productivity.
All 72 ratios were checked against their component shares. Three sales bands
combine the six source bins; all nine sector compositions still sum to 100%.
State staffing points are enlarged; the box plot retains its original scope.

All four laptop checks passed again, including sector highlighting, keyboard
input and accessible tables. Additional 375/768 px checks found no overflow,
clipped SVG labels or page errors. New ochre/slate/blue fills all exceed 4.5:1
contrast against the page background. Source extracts remain unchanged.

## Acknowledgement layout

The student requested a full-width acknowledgement paragraph. This section
intentionally permits longer lines; the ten-word line check continues to apply
to all other paragraphs. The acknowledgement wording is preserved, its body
uses regular weight, and the missing closing aside tag is restored.

## Farming visual theme

Added a locally hosted conceptual farm illustration, subtle eucalyptus/ochre
background washes and field-row lines, plus five decorative section motifs.
Quantitative plots retain their original paper background and colour scales.
The illustration is a 260,664-byte WebP, outside the data/specification budget.
All four required laptop checks pass. Additional checks at 375 and 1280 px
confirm the illustration and all twelve charts load, all five motifs exist and
the page has no horizontal overflow. Desktop and mobile screenshots were
visually reviewed. Artwork provenance is in `assets/illustrations/README.md`.
