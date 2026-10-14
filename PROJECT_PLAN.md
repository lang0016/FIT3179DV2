# Australian Farmers: research and presentation plan

Prepared for **Ang Lin Shan**, FIT3179, Malaysian campus. 15 October 2026 (Malaysia).
Repository: `lang0016/FIT3179DV2`.

**Status: provisional plan, not a completed data investigation.** The official
ABS and ABARES sites returned proxy `403 Forbidden` responses during research.
No datasets, statistics, licences, release dates, or findings have been verified.
Read [DATA_RESEARCH.md](DATA_RESEARCH.md) for the source shortlist and access blocker.
The uploaded brief is the planning specification; its rubric has not been
independently checked against an official unit specification.

## Story and audience

**Working title: Who farms Australia—and how is farming changing?**

This page will help Malaysian readers understand the people and businesses
behind Australian agriculture. It will begin by locating agricultural work,
then compare change over time, introduce workforce characteristics, contrast
agricultural sectors, and explain business size. The reader should leave knowing
which changes are national and which depend on the region or type of farming.
The data must determine the final conclusions: fewer farms, ageing workers,
larger businesses, and labour shortages are questions to investigate, not
established findings.

The audience needs no Australian geography or statistical background. Explain
state names on the first map. Define agriculture, a farm business, a worker,
employment size, and a financial year before using those terms. Do not assume a
Malaysian audience requires Malaysian data; Australia remains the assigned topic.

## What / why / how

| Framework | Application |
| --- | --- |
| What | Geographic regions; agricultural industry categories; time; worker counts and percentages; age and sex categories; business counts and size classes. |
| Why | Locate farming; compare regions and sectors; follow change; understand workforce and business composition. |
| How | One scrolling presentation, five sections, direct explanations, Vega/Vega-Lite charts, limited controls, consistent colour, and source notes. |

Two geographic levels are proposed: states/territories for national orientation
and business comparisons, and suitable Census regions for employment rates.
Choose the regional level only after checking data access, confidentiality,
boundary consistency, and readable map size. Prefer SA3 if SA2 is too detailed.

## Proposed chart sequence

Every row is **conditional on obtaining appropriate verified data**. Questions
below are not chart findings. Before building, replace each question with a
supported finding and record its calculation. Do not add a chart solely to
reach the rubric's count.

| # / section | Reader question and proposed idiom | Data and preparation | Marks, channels, and rationale |
| --- | --- | --- | --- |
| 1 / Where | Where does agricultural work make up a larger share of local employment? **Choropleth map** (advanced). | Census agriculture employment / all employed people in the same region, year, and population; percent. Join official boundaries by geographic code. | Geographic polygons; lightness for rate; Albers equal-area projection for Australia. Rates allow fairer comparison than raw counts. Tooltip includes numerator and denominator. |
| 2 / Where | Which states have the most agricultural workers? **Proportional-symbol map** (advanced). | Census agricultural workers by state, same year as chart 1. Exclude forestry/fishing if detailed industry codes allow. | Circles at labelled state reference points; area proportional to count; constant colour. Same Albers projection as chart 1. Distinguish concentration from local dependence. Points represent state totals, not farm locations. |
| 3 / Change | How have farm numbers changed within a consistent statistical series? **Line chart** (basic). | ABS agricultural business/farm series with a consistent scope; use only compatible years. If no comparable farm series exists, substitute a clearly labelled agriculture-business series, not an invented splice. | Year on x, number on y, line and endpoint labels. Preserve gaps and explain scope breaks. Use actual counts; any optional index must define its base year. |
| 4 / Change | Which states gained or lost agricultural businesses between comparable years? **Dumbbell chart** (advanced). | Same-scope agriculture business counts, two comparable dates, by state. | Two endpoints and a joining line on one common count axis; temporal direction labels. Shows start, end, and size of change together. Distinct from chart 3's national trajectory. |
| 5 / Change | Which farm sectors moved up or down the employment ranking? **Bump chart** (advanced). | At least three comparable Census years, four or more consistently defined agriculture sectors. Use rankings of counts, not incompatible Labour Force/Census estimates. | Time on x, rank on y, sector-coloured paths and direct labels. Explain that rank hides magnitude; pair with chart 12. If rankings barely change, choose a better idiom and reassess the advanced-idiom target. |
| 6 / People | How does the farming workforce's age profile differ between women and men? **Population pyramid** (advanced). | Census workers by age band and recorded sex, same agriculture definition. Use counts, not unmatched percentages; preserve the source's category names. | Horizontal bars, shared age bands, mirrored counts, labelled sides. Explain mirroring, and show positive axis labels. Categories reflect the source and do not describe all gender identities. |
| 7 / People | Do some agricultural sectors have more older workers across regions? **Box plot** (advanced). | Regional share of workers aged 55+ within each sector, one Census year. Retain only regions meeting a justified denominator threshold; report exclusions. | Sector on x, regional percentages on y, median and middle-half boxes. Explain in plain language; each observation is a region, not an individual or farm. Equal weighting describes the typical region, not the national worker. Use only if sufficient meaningful observations exist. |
| 8 / Sectors | Which agricultural sectors make up each state's workforce? **Heatmap** (advanced). | State × sector employment / total agricultural employment within each state; percent. | Rows for states, columns for sectors, sequential lightness for share. Row totals should be approximately 100% only if categories are exhaustive. State clearly that this is composition, not absolute jobs. |
| 9 / Sectors | How do farm sectors organise family and hired labour? **Stacked bar chart** (basic). | ABARES farm survey published labour composition, if available with common units, periods, and compatible sector coverage. Keep persons, annual averages, hours, and full-time equivalents separate. | Aligned bars; segments for verified labour categories. Use 100% bars only if categories form a complete whole in the same unit. If unavailable, replace with another directly supported ABARES workforce comparison; do not manufacture a breakdown. |
| 10 / Businesses | How are agricultural businesses distributed geographically? **Non-contiguous cartogram** (advanced, third map idiom). | ABS agriculture business counts by state/territory and official state boundaries for the same reference geography. | State silhouettes with areas proportional to business counts, labels and counts. Start from an Albers equal-area layout; shrink shapes without overlap. Explicitly explain intentional distortion and that area represents businesses. Include Tasmania and small territories. This is a different encoding from charts 1 and 2, not a recoloured map. |
| 11 / Businesses | How many agricultural businesses fall into each employment-size class? **Treemap** (advanced). | ABS agriculture business counts by published employment-size classes, one date; retain the non-employing class. | Rectangle area for number of businesses, direct size-class labels and counts; single focus hue. This measures employment size, not hectares, revenue, productivity, or number of farms. A non-employing business does not necessarily mean nobody works there. |
| 12 / Conclusion | Which sectors account for the largest workforce changes? **Diverging change bars** (basic). | Absolute change in Census employment by harmonised sector between two compatible years; include percentage change in text/tooltip with the base count. | Shared zero baseline, horizontal bars, sector labels. Connect rank changes in chart 5 to the number of workers affected. If all changes have the same sign, use ordinary bars. |

The proposed plan has **12 charts and 9 distinct advanced idioms** under the
uploaded brief's definition: choropleth, proportional-symbol map, dumbbell,
bump, population pyramid, box plot, heatmap, cartogram, and treemap. A small
multiple is counted once. The 3 map idioms are choropleth, proportional symbols,
and non-contiguous cartogram. These counts are design targets, not a claim of
completed charts or guaranteed rubric credit. Verify the cartogram's suitability
with the tutor, especially if their interpretation of map idioms differs.

## Data comparability rules

- Agricultural businesses, operating farms, agricultural workers, and people
  whose occupation is farmer are different populations. Labels must name the
  actual measure. A person employed by a dairy farm is not necessarily a farmer
  by occupation; one business can operate more than one property.
- Start with industry-defined **agriculture**, and exclude forestry and fishing
  when detailed codes permit. A broad industry series that includes them must
  keep that label and cannot silently substitute for agriculture-only data.
- Prefer a recent release for each measure, not a single year forced onto all
  sources. Census workforce detail may be older than current business or survey
  data; display reference periods beside each chart.
- Check farm-survey scope, turnover/value thresholds, classification changes,
  weighting, geography, and collection changes before drawing trend lines.
- Never join business-size classes to farms as if they count the same units.
- Never join an ABARES survey mean to Census regional data as though records
  describe the same people. Compare aggregate evidence with explicit scope notes.
- Treat confidentiality perturbation, suppressed values, missing categories,
  and small denominators explicitly. Missing is not zero.
- Do not attribute changes to climate, migration, policy, or mechanisation
  without verified supporting evidence. The charts alone do not establish causes.

## Presentation and interaction

Use a two-column grid on laptops. Full-width maps or major charts span both
columns; charts within one row use equal widths. Stack on narrow screens.
Keep all five sections visible by scrolling; no tabs swapping major sections.
Use serif headings, sans-serif body/axes, comfortable label sizes, generous
spacing, and short paragraphs. Test the brief's ten-words-per-rendered-line
requirement in a browser rather than claiming a CSS width guarantees it.

Use tooltips for exact values. A highlighted sector can connect the bump chart,
heatmap, and change bars while keeping the entire dataset visible. A year control
is optional only where a verified comparable series supports it; the initial
view must communicate the story without interaction. Native controls must work
with the keyboard. Give each chart a heading, finding, source, and accessible label.

### Provisional colour meanings

Do not finalise sector colours until source categories are known.

| Role | Meaning | Design rule |
| --- | --- | --- |
| Deep blue | Agriculture overall / focus | Used for aggregate marks; lighter blue represents lower quantities in sequential scales. |
| Neutral grey | Geographic context | Muted boundaries and contextual marks. |
| Grey hatching + label | Missing or suppressed | Must be distinguishable from a true low value. |
| Dark blue / charcoal | Later / earlier date | Endpoint comparisons use explicit date labels; no red-green pairing. |
| Distinct reserved category hues | Verified agricultural sectors | Assign once after harmonisation and reuse in every sector chart. |

Audit text and mark contrast before implementation. Quantitative map/heatmap
palettes must balance the brief's contrast rule with distinguishable lightness;
use borders, labels, or discrete bins if necessary. Do not imply a proposed
palette has already passed a contrast or colour-vision check.

## Decision gates before building

1. Activate official-source network access and verify/download the shortlisted
   releases, data dictionaries, methodology, and reuse terms.
2. Record exact files, table identifiers, reference years, coverage, licence,
   attribution, and retrieval date. Demonstrate two publishers in the actual
   chart data: ABS and ABARES, not just two ABS tables.
3. Check numeric consistency, missingness, cross-year classification alignment,
   and boundary joins. Produce a small clean extract and reproducible preparation
   notes before writing narrative claims.
4. Confirm all 12 charts have useful distinct messages and that the 3 maps add
   information. Replace unsupported charts, then recount advanced idioms.
5. Share the data-backed plan for the student's hand-drawn A4 sketch and tutor
   feedback. Preserve the agreed structure when building the final page.

The current work stops at research/planning. It does not create a website,
publish to GitHub Pages, generate a digital sketch, or write the student's AI
acknowledgement. The student will draw/upload the sketch and write that
acknowledgement themselves.
