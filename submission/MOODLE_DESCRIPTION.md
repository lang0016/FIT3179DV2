# Moodle description — draft for Ang Lin Shan

Project: **Who farms Australia?**
Domain: **Australian Farmers** · FIT3179 DV2 · Malaysian campus
Author: **Ang Lin Shan**
Expected page address: https://lang0016.github.io/FIT3179DV2/

**Publication pending:** enable GitHub Pages using `PUBLISHING.md` and verify
the public URL before submitting it.
Repository: https://github.com/lang0016/FIT3179DV2

This is a draft description of the implemented visualisation. Review it against
any tutor feedback and the final hand-drawn sketch before submitting it.

## i. Domain, why, and who

The visualisation investigates Australia's agricultural businesses and farming
workforce. It asks where agricultural businesses are concentrated, how farm and
business numbers have changed, what the farmer occupation's age profile looks
like, and how business composition varies between agricultural sectors.

The intended audience is a general Malaysian reader without specialist knowledge
of Australian geography or statistics. State abbreviations are explained, the
financial year is defined, and the page distinguishes a business, an agricultural
worker, a farmer by occupation, and a registered dairy farm. Dairy provides a
well-documented case study rather than being treated as representative of all
farming.

The purpose is presentation: a guided story, not an expert analysis dashboard.
Five sections move from location to change, people, sectors, and perspective.
Findings explain the evidence without claiming unsupported causes. Readers can
compare state totals with state shares, see change over time, understand the age
profile, compare business composition, and inspect exact values when needed.

## ii. What: data and preparation

The project combines two publishers, the Australian Bureau of Statistics (ABS)
and Dairy Australia. The downloadable datasets use different statistical units
and reference periods, which are stated beside each chart.

1. **ABS, Counts of Australian Businesses, including Entries and Exits, July
   2021–June 2025.** Cubes 1–3 provide main-state totals, four-digit industry
   classes, employment-size bins and turnover-size bins. These administrative
   statistics come from the ABS Business Register, using ABR/ATO records and ABS
   profiling. Detailed June 2025 cells were released in December 2025. The August
   2026 release had broader totals, while its detailed cubes were scheduled for
   December; the project therefore uses the latest detailed edition verified
   during research. Only the 34 agriculture classes in groups 011–019 are retained.
   Forestry, fishing, aquaculture and separately classified support services are
   excluded. Disjoint class counts are aggregated into nine groups. National
   class rows and main-state rows are kept separate to prevent double counting.
   State business shares use the same year's all-business state denominator.
   Confidentiality-adjusted cells need not add exactly to published totals; the
   project preserves and explains these differences.
   Source: https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/jul2021-jun2025

2. **ABS, Labour Force, Australia, Detailed, March 2026.** EQ07a supplies age and
   sex cells for the occupation Farmers and Farm Managers. Full-time and part-time
   estimates are added within each of six age groups and two published sex
   categories. The latest actual observation is February 2026. Values are in
   thousands and remain survey estimates, not exact headcounts. Table 06 supplies
   agriculture-only industry employment from 2000 to February 2026. Quarterly
   estimates remain distinct from complete-year averages. Occupation and industry
   totals are never subtracted to estimate an unobserved worker group.
   Source: https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/mar-2026

3. **Dairy Australia, Australian Dairy Industry In Focus 2025.** Table 2, printed
   page 8, supplies registered dairy farms in six states and Australia from
   2011–12 to 2024–25. Its underlying sources are state milk authorities and Dairy
   Australia. The latest season is provisional; NT/ACT are not reported. Numeric
   cells were extracted and all fourteen rows reconciled against the national
   column. Derived calculations include the percentage decline, state shares,
   and each state's contribution to the national change. This series counts
   registered farms, not ABS business units.
   Source: https://www.dairyaustralia.com.au/industry-reports/australian-dairy-industry-in-focus

4. **ABS, ASGS 2021 state boundaries, GDA2020.** Official state polygons are
   simplified with topology preservation and displayed for the eight states and
   territories. Other Territories and remote islands outside the displayed extent
   are omitted; statistical state totals are unchanged. Ordinary maps use an
   Australian Albers equal-area projection. The cartogram starts from equal-area
   projected shapes, changes each reported state's area in proportion to its
   registered dairy-farm count, and relocates silhouettes without overlap for
   legibility. Grey NT/ACT shapes mean not reported, not zero.
   Source: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files

Reproducible scripts, checksums, source-row references and extracted data are
included in the repository. No data values have been invented. Derived
percentages and averages have explicit denominators. The complete research
register records source methods, limitations and rights. ABS material is
attributed under its CC BY 4.0 terms and exceptions. Dairy Australia is credited
for a small factual numeric extract; its report, artwork and photos are not
redistributed or described as openly licensed. Sources were accessed on
15 October 2026 (Malaysia).

## iii. How: idioms, marks, channels and rationale

The What/Why/How framework connects each data type to a reader task and a visual
encoding. The page has twelve charts and nine distinct advanced idioms under
the supplied brief's definition, including three map idioms. The official unit
rubric and tutor determine how those idioms are credited.

| # | Idiom and reader task | Marks and channels | Data types and reason |
| --- | --- | --- | --- |
| 1 | Choropleth: compare agriculture's share of state businesses. | State polygons; geographic position; sequential lightness for percentage. | Geographic state, quantitative rate. Normalisation separates local composition from raw business volume; equal-area projection avoids misleading area distortion. |
| 2 | Proportional-symbol map: locate large business totals. | Circles; geographic reference positions; circle area for count; direct labels and leaders. | Geographic state, quantitative count. Comparing this with chart 1 reveals how a large total can coexist with a smaller share. Circles are state totals, not precise farm locations. |
| 3 | Line chart: follow registered dairy-farm numbers over time. | Connected points and a line; horizontal year; vertical count; endpoint labels. | Ordered time and quantitative count. The connected sequence shows the direction and extent of change without splicing incompatible farm-count definitions. |
| 4 | Dumbbell: compare two dates within each state. | Two differently shaped/date-labelled points and a connecting rule; common horizontal count scale; categorical state rows. | Nominal state, ordered dates, quantitative counts. Start and end positions reveal both business scale and absolute movement. |
| 5 | Waterfall: account for the national dairy-farm change. | Floating bars; cumulative vertical positions; explicit signed labels; start/end totals. | Nominal state contributions, quantitative changes and totals. The six changes reconcile exactly to the national decline, showing contribution rather than asserting causation. |
| 6 | Population pyramid: compare age profiles by recorded sex. | Mirrored bars; shared ordered age bands; common worker-count scale; labelled sides. | Ordinal age, nominal source sex categories, quantitative survey estimates. Mirroring lets readers compare both group size and age concentration without statistical expertise. |
| 7 | Box plot with observations: compare variation between states. | Boxes for the middle half; median lines; range rules; overlaid state points; common percentage axis. | Nominal sector/state, quantitative non-employing business share. The plot distinguishes within-sector state variation from a national average. Every state observation remains visible. Denominators must be at least 100 and each sector needs at least five eligible states. |
| 8 | Heatmap: compare state-sector business composition. | Rectangular cells; state columns and sector rows; sequential lightness for within-state percentage. | Two nominal categories and a quantitative proportion. Aligned cells make business composition comparable across states while conserving space. |
| 9 | 100% stacked bars: compare turnover-size composition. | Aligned segmented bars; common percentage scale; ordered size-bin lightness; direct sector labels. | Nominal sector, ordinal turnover class, quantitative proportion. Normalising the displayed bin sums separates composition from the very unequal number of businesses in each sector. Turnover is explained as sales before expenses. |
| 10 | Non-contiguous cartogram: reveal dairy-farm concentration. | Equal-area source state silhouettes, resized and relocated; area for registered farms; direct count labels. | Geographic state and quantitative count. Deliberately replacing land area with farm counts makes Victoria's dominance visible; the distortion is explicitly explained. Unknown coverage has separate grey context shapes. |
| 11 | Treemap: see employment-size composition. | Nested partition rectangles; area for number of businesses; direct labels and exact values. | Ordinal employment-size category and quantitative count. The dominant non-employing category is immediately visible; smaller categories remain available through tooltips and the table. |
| 12 | Time-series lines: distinguish long-run workforce change from quarterly variation. | Thin quarterly line, thick complete-year-average line; temporal position and common quantitative worker scale; latest-quarter point. | Time and quantitative survey estimates. Separate treatment prevents an incomplete year or a seasonal quarter being mistaken for an annual average. |

### Design and special features

The page uses a consistent two-column editorial layout, serif headings and
sans-serif explanatory text. Section numbers, headings and source notes guide a
single scrolling reading path. Charts remain visible; there are no tabs that
swap major sections. Colour is restrained: blue for overall agriculture, violet
for the dairy case study, and ordered blue lightness for quantities. Direct
labels, shape differences and text carry meaning without relying on colour alone.

One native sector selector highlights related observations in charts 7–9 without
hiding other sectors. Tooltips show details; the main finding remains visible
without hover. Every chart has a keyboard-reachable container, an accessible SVG
label, source/specification links and a native expandable data table. An ordinary
reader can therefore follow the story; a reviewer can inspect the underlying
numbers and human-readable JSON specification.

The custom cartogram is an original transformation of official boundaries,
not a copied design. It preserves a common area-per-farm factor for all reported
states and explicitly separates unreported NT/ACT context. No outside causal
claims are used to explain data changes. Vega/Vega-Lite libraries are stored
locally so chart loading does not require an external CDN.

### Student review before submission

Draw and upload the required hand-drawn A4 sketch, review the description in your
own voice, add your own generative-AI acknowledgement to the page, and check that
the sketch reflects the final implementation. Do not claim a hand-drawn sketch
exists until you have supplied it. See `SUBMISSION_CHECKLIST.md` and
`INTERVIEW_NOTES.md`.
