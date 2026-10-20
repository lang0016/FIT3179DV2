# Review against the official DV2 rubric

Reviewed 20 October 2026 against the uploaded **Data Visualisation 2
Specifications, Semester 2 2026, version 1.1** (six pages), and the lecturer's
additional general suggestions. The PDF is assessment reference material;
this review is not a predicted mark or a claim that the lecturer has approved
the chosen idioms.

## What the official rubric actually asks for

- Pages 1–3: a public, single scrolling GitHub page; Vega/Vega-Lite diagrams;
  readable JSON specifications; three different map idioms; small downloads;
  accurate real-world data from two sources; meaningful interaction; a story
  for the relevant campus audience.
- Page 3: at least ten charts. Page 5's HD descriptor is stricter: **more than
  ten charts and at least eight advanced idioms**, all used effectively and
  meaningfully. Similar charts or small multiples count as one chart, not one
  per panel. Basic idioms include stacked bars, dot plots, lines, scatterplots
  and bubble charts; elaborate styling does not make them advanced.
- Pages 2–3: the Malaysian-campus audience is a general Malaysian reader.
  Australian geography, currencies and statistical terms need explanation.
- Pages 4–6: public accessibility is essential; fewer than three map idioms
  caps the idioms component at 4% instead of 8%. The sketch, written rationale
  and interview are assessed separately from the website.

| Assessed component | Weight | Current evidence and remaining work |
| --- | --- | --- |
| Sketch | 2% | Five sections and a sketch guide exist. The actual hand-drawn A4 sketch PDF is not in the repository. A digital sketch earns zero under the rubric. Draw/scan the student's own sketch, make it match the final design, and upload it. |
| Idioms and complexity | 8% | Twelve rendered charts, three proposed map idioms and nine candidate advanced idioms. Nested hierarchy, shared baselines, size scaling and geography explanations have been strengthened. Effective use and classification remain the marker's decision. |
| Layout, colour, figure-ground | 3% | Column structure, aligned paired chart rows, restrained decoration, contrast checks, and no page overflow at the required laptop widths. |
| Typography | 2% | Locally hosted Lora headings; consistent Arial body and quantitative labels; dark paragraph text; controlled line lengths and hierarchy. The student specifically requested a full-width AI acknowledgement, which is the deliberate long-line exception. |
| Storytelling, annotations, grammar/style | 5% | Five-section narrative, scoped units and periods, selective findings, geographic key, natural-language tooltip titles and visible source links. Useful annotations remain; repetitive values are available through tooltips/tables. |
| Domain, who, what, why, how description | 2% | `submission/MOODLE_DESCRIPTION.md` describes the Malaysian audience, source preparation, tasks and encoding choices. Review it in the student's own voice and use the actual Moodle template. |
| Interview | 3% | `submission/INTERVIEW_NOTES.md` supports preparation. Only the student can demonstrate understanding in the interview. |

## Chart inventory in reading order

| Number | Idiom | Task and review |
| --- | --- | --- |
| 01 | Choropleth map | Compare agriculture's share of state businesses. Rate, rather than raw count, is appropriate for polygon colour. |
| 02 | Proportional-symbol map | Compare counts. Continuous circle area remains proportional to counts; circles are smaller to reduce crowding. State labels remain, but numeric labels now emphasise only the two states in the finding. |
| 03 | Line chart | Show the long dairy-farm trend; endpoints are annotated, not every year. Basic idiom. |
| 04 | Indexed dumbbell | Compare two dates through a shared 2024 baseline. The original counts and percentage calculation remain accessible. Treat its advanced classification as a tutor decision, not an automatic entitlement. |
| 05 | Waterfall | Account for each state's contribution to a national dairy-farm decline; does not claim causes. |
| 06 | Population pyramid | Compare age distributions by source sex category. Symmetric signed scale, separate colours, clear zero rule. |
| 07 | Heatmap | Reveal relative sector concentration, with a defined 1× reference. Labels highlight the finding or selected sector rather than all 72 cells. |
| 08 | 100% stacked bars | Compare three annual-sales bands on a shared 0–100% scale. Rows rank the 2-million-or-more share. Smaller high-sales segments are directly labelled, outside the bar when necessary. This remains a basic stacked-bar idiom. |
| 09 | Box plot with observations | Compare state variation in non-employing shares. All sectors share a 0–100% axis; the middle half/median and scope restrictions are explained. |
| 10 | Non-contiguous cartogram | A complete Australia reference supplies context; six reported state shapes use a common count-to-area factor. Missing territory counts are explicitly unreported. |
| 11 | Hierarchical treemap | Employment status is the first split; employing businesses are then divided by staff count. Contrasting blue/gold status groups, a strong parent outline and four external leader-line labels name even tiny groups and their exact counts. |
| 12 | Annual-average workforce line | Show long-term industry employment on a zero baseline, with explicit worker units. The latest quarter is reported separately. Basic idiom. |

There are nine candidate advanced idioms: choropleth, proportional-symbol map,
indexed dumbbell, waterfall, pyramid, heatmap, box plot, cartogram and treemap.
The geographical proportional-symbol map should not be confused with a generic
bubble chart; nevertheless, confirm map/advanced classifications with the tutor.
The two ordinary time-series charts are basic. Even if those two are counted
as one similar-chart series, the inventory has eleven charts; the marker still
decides how the chart-count rule applies.

## Applying the general lecturer suggestions

| Suggestion | Decision for this project |
| --- | --- |
| Typography and whitespace | Added a licensed topic-appropriate editorial serif for headings; kept body/axes consistent. Retained restrained banner treatment and aligned chart rows. |
| Do not annotate every point | Heatmap already labels only the selected finding/sector. Circle-map numeric labels are now selective. Sales bars retain segment labels where they fit and four focal high-sales shares; narrow segments use outside labels. Endpoints and accounting contributions retain useful labels. |
| Crowded proportional circles; consider classes | Reduced the circle-area range while preserving continuous proportions. There are eight state points, not hundreds of regional points. Binning would lose exact count relationships and would require a different legend/description; it is unnecessary here. |
| Treemap hierarchy | Changed a flat set of size bins into an explicit employment-status → employing staff-size hierarchy, without inventing data categories or changing totals. |
| Consistent y-axes | Worker-count time series now start at zero; percentage distributions share 0–100%. The pyramid uses symmetric negative/positive positions. Counts, percentages, ratios and workforce estimates are different units, so forcing every chart to the same numeric range would be wrong. |
| No overlap | Existing browser checks cover clipping, text collisions and page overflow at four laptop widths. Small-screen screenshots are reviewed separately; these checks do not establish perfect placement at every possible width. |
| Double-encoding scatterplot | Not applicable: there is no scatterplot. Adding one merely to satisfy a general suggestion would weaken the story. |
| Avoid abbreviations and underscores | Tooltip field titles are human-readable. Currency is expanded in the sales legend; the title spells out New South Wales. Geographic state codes are retained where space is limited and explicitly defined in the adjacent state key and full-name tooltips. Source table identifiers remain in provenance, not presented as analytic concepts. |
| Improve a stacked bar | Use a common 0–100% scale, meaningful row ranking and readable segment labels. The caption explains the currency and why sales are not profit. Smaller high-sales segments retain labels without forcing text into insufficient space. |
| Regional place annotations | Both ordinary maps retain place labels and an eight-state/territory name key. Chart 10 includes a complete geographic reference with state labels at laptop widths. |

## Source freshness and integrity

Source extracts are unchanged. The latest ABS business page was rechecked on
20 October: the general release is July 2022–June 2026, but it currently links
only cube 1. The detailed agriculture class/state/size cubes used here remain
from the June 2025 edition; the research register explains the December detailed
release schedule. Replacing them with the newer combined Agriculture, Forestry
and Fishing division would change scope and would be misleading. The ABS Labour
Force detailed latest-release page still identifies March 2026. Dairy figures
retain their explicitly identified 2024–25 provisional period.

The primary publishers are ABS and Dairy Australia. Official geography is a
separate ABS source, not a fabricated data layer. AI-generated landscape artwork
is decorative, not evidence; its generation is now also disclosed visibly on the
page. Lora's SIL Open Font License is bundled and linked.

## Items the website cannot complete

1. Upload a working URL to the student's **hand-drawn** sketch PDF and make it
   match the final page. The current intended sketch URL is not a valid deliverable
   until the PDF actually exists and is publicly accessible.
2. Review the final deployed page in a private browser. The live page returned
   HTTP 200 on 20 October; this does not mean an unpushed change is deployed.
3. Review the personal AI acknowledgement for truthfulness, including the actual
   verification and design decisions the student performed.
4. Adapt the description to Moodle's provided template and submit the required
   page URL, sketch URL and rationale. The PDF lists **25 October 2026, 11:55 PM**;
   confirm the campus deadline/timezone shown in Moodle.
5. Prepare to explain scope, normalisation, hierarchy, map area distortion and
   interaction choices in the interview. No automated audit guarantees a grade.
