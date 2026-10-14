# Who farms Australia—and how is farming changing?

Research-backed plan for **Ang Lin Shan**, FIT3179, Malaysian campus.
Updated **15 October 2026 (Malaysia)** · `lang0016/FIT3179DV2`.

**Stage: data research and planning, before the hand-drawn sketch and website.**
Official data has now been downloaded and checked. This replaces the earlier
blocked, provisional plan. Source details and remaining implementation checks
are in [DATA_RESEARCH.md](DATA_RESEARCH.md). Reproducible extracts are in
[data/research](data/research), not invented example data.

## Story

Australia's farming story depends on what we count: businesses, working farmers,
all agricultural workers, or registered farms in a particular sector. This page
will first locate agricultural businesses, then show how farming is changing,
introduce the age profile of farmers, compare different types of agricultural
business, and finish with the changing shape of the workforce. Dairy provides a
well-documented example of falling registered farm numbers; it must not stand
in for every sector. Malaysian readers need no knowledge of Australian geography
or statistics. Explain state names, financial years, and the different counting
units at the first use.

A useful Malaysian connection, if included: Malaysia was among the five largest
export markets by value for Australian dairy in 2024–25, according to Dairy
Australia's *In Focus 2025*, printed page 4. This is context, not a claim about
Malaysia's dependence on Australian food or a reason to change the assigned topic.

## Findings that can anchor the story

| Finding | Verified basis and limit |
| --- | --- |
| Registered dairy farms fell from **6,770 in 2011–12 to 3,772 in 2024–25**, a **44.3% decrease**. | Dairy Australia, Table 2, printed p.8; latest season is provisional. Dairy-specific, not all Australian farms. |
| Victoria accounted for **65.6%** of registered dairy farms in 2024–25. | 2,476 / 3,772, same table. A count of registered dairy farms, not milk output or land area. |
| About **59% of Farmers and Farm Managers were aged 55 or older** in February 2026. | ABS Labour Force EQ07a, sum of 55–64 and 65+ age cells / all age/sex cells for that occupation. Survey estimate, not an exact Census count. |
| The same occupation had an estimated **150,300 workers** in February 2026; around **29.6% were female**. | EQ07a, full-time + part-time, in thousands. “Farmer” is an occupation; this excludes many farm labourers and other agricultural jobs. |
| Agriculture as an industry employed an estimated **245,900 people** in February 2026. | ABS Table 06, agriculture subdivision only, total persons. Different definition from the occupation above; do not subtract the two to estimate farm labourers. |
| Sheep, beef cattle and grain accounted for about **70.4%** of agriculture-business class totals in June 2025. | Derived from 34 disjoint CABEE agriculture classes: 101,788 / 144,681. Confidentiality-adjusted counts; a business is not a physical farm. |
| Tasmania's agriculture businesses were about **9.1% of all its actively trading businesses**, compared with about **4.9% in NSW**. | Sum of agriculture class cells by main state / official state business total, June 2025. Rates measure business composition, not employment dependence. |

Use these as supported statements, with source and period immediately beside
them. They do not establish causes such as mechanisation, migration, drought,
or policy. Additional causal annotations require separate verified evidence.

## What / why / how

| Framework | Application |
| --- | --- |
| What | Geographic states; agricultural business classes and sector groups; dates; business and farm counts; workforce survey estimates; ordered age, employment-size, and turnover classes. |
| Why | Locate farming businesses; distinguish concentration from local importance; follow change; compare sectors; understand who works as a farmer. |
| How | Five scrolling sections; 12 complementary Vega/Vega-Lite charts; consistent sector colours, direct findings, small data inputs, and restrained interaction. |

## Revised chart sequence

Source abbreviations: **B2** = ABS CABEE June 2025 data cube 2; **B3** = cube 3;
**B1** = cube 1; **DA2** = Dairy Australia Table 2; **LFA** = ABS EQ07a;
**LFI** = ABS Table 06. Full URLs are in the research register.

| # / section | Question and idiom | Exact data / operations | Marks, channels and intended finding |
| --- | --- | --- | --- |
| 1 / Where | Where is agriculture a larger part of the business landscape? **Choropleth map** — advanced. | B2 agriculture classes 0111–0199, June 2025, sum by main state / B1 Table 4 all businesses in that state. Join state codes to ABS boundaries. | Polygon lightness = percent; Australia Albers equal-area projection. Tasmania has a higher business share than NSW despite fewer businesses. Label this as business share, never workforce share. |
| 2 / Where | Which states have the most agricultural businesses? **Proportional-symbol map** — advanced. | B2, same state class sums, June 2025. Include all eight states/territories; report unknown/other main-state cells separately. | Circle area = count, constant hue, labelled reference positions; same Albers projection. NSW has the largest count in the extract. Pair with chart 1 to explain why a large total and a high share are different. Circles are state totals, not farm locations. |
| 3 / Change | How have registered dairy-farm numbers changed? **Line chart** — basic. | DA2, all 14 financial years from 2011–12 to 2024–25, Australia total. | Time x; registered farms y; direct endpoint labels. Finding: 44.3% fewer registered dairy farms, with the latest year explicitly provisional. Do not label this “all farms”. |
| 4 / Change | How did agriculture-business counts change across states? **Dumbbell chart** — advanced. | B2 Table 1 start/end totals, or Table 2 end vs Table 1 end, June 2024 and June 2025, same agriculture class scope. | Two date-labelled endpoints and joining lines, state rows, common count scale. Show which states account for the largest absolute changes; final wording must use the extracted state deltas, with confidentiality caveats for small changes. |
| 5 / Change | Which states contributed to the recent dairy-farm decline? **Waterfall chart** — advanced. | DA2, national count in 2021–22 plus each state's change to 2024–25, ending at the national 2024–25 count. The six state changes sum exactly to the national change. | Floating bars at cumulative positions; constant change hue plus explicit minus labels; start/end total bars. Victoria contributes the largest absolute decline. Attribute contribution only, not causation. |
| 6 / People | What is the age and sex profile of farmers? **Population pyramid** — advanced. | LFA latest actual data month, February 2026; “Farmers and Farm Managers”, six age bands × Males/Females; full-time + part-time. | Mirrored horizontal bars, shared age bands, positive count labels in thousands. Finding: roughly 59% are 55+. This concerns the occupation, not everyone employed by agriculture. Retain the source's sex labels and explain the scope. |
| 7 / People and business | Does the share of businesses without employees vary between states? **Box plot with state observations** — advanced. | B2 June 2025: each observation = state × sector non-employing cells / sector total. Keep denominators ≥100 businesses, then sectors with at least five eligible states. This yields eight sectors; deer is excluded. | Sector x; percentage y; boxes for median/middle half plus visible state points and sample counts. Dairy's eligible states range approximately 48–78%, versus about 51–61% for nurseries/floriculture. Equal state weighting describes variation between states, not a national worker or business distribution. |
| 8 / Sectors | Which sectors make up each state's agriculture businesses? **Heatmap** — advanced. | B2 June 2025; sum disjoint classes to nine agriculture groups, then divide by that state's sum across the same groups. | State rows, sector columns, sequential lightness = within-state business share. Exact calculated cells determine the annotations. Directly names sectors; do not imply a sector employing many people necessarily has many businesses. |
| 9 / Sectors | How does annual turnover differ between agricultural sectors? **100% stacked bars** — basic. | B3 June 2025; national class cells aggregated to sector × six published turnover classes. Percent of the displayed turnover-bin sum; retain published totals separately because perturbation can prevent exact additivity. | Common 0–100% x scale, sector rows, ordered size-class segments and direct labels. Compare low/high-turnover composition. Turnover means money from sales before expenses; it is not profit, hectares, or staff. Use actual bin shares to choose the final finding. |
| 10 / Businesses | Where are registered dairy farms concentrated? **Non-contiguous cartogram** — advanced, third map idiom. | DA2 2024–25 six reported states; ABS state geometry. | State silhouette area = registered dairy farms, with count labels. Begin with Albers equal-area projected shapes, then shrink around state reference points using square-root area scaling. Explain deliberate distortion. Victoria accounts for 65.6%. NT/ACT are not reported in DA2: retain contextual outlines marked “not reported”, not invented zeroes. |
| 11 / Businesses | How many agricultural businesses have employees? **Treemap** — advanced. | B2 national agriculture class cells by five employment-size bins, June 2025. | Rectangle area = count; direct size-class labels/counts; one focus hue. About three-quarters of the derived agriculture-business class total is non-employing. Explain that owners/family may still work in a non-employing business. If component sums differ from the published-total sum, disclose that difference rather than silently forcing equality. |
| 12 / Conclusion | How has agriculture's workforce changed over time? **Time-series line chart** — basic. | LFI agriculture-only employed persons, original quarterly estimates, 2000 to February 2026. Use annual averages only for years with all four quarters; do not compare an incomplete year with a full-year average. | Time x; estimated workers in thousands y; mark latest observation and explain seasonal/sampling variation. The latest verified point is about 245,900. No causal story or comparison of unlike seasonal quarters. Keep the chart distinct from the dairy-farm-count line in chart 3. |

**Count: 12 charts, nine distinct advanced idioms, three map idioms.** Advanced:
choropleth, proportional symbols, dumbbell, waterfall, population pyramid, box
plot, heatmap, cartogram, treemap. This follows the uploaded brief's definition;
credit is the tutor's decision. Confirm that the cartogram meets the unit's
third-map interpretation before drawing the final sketch.

The important changes from the first plan are deliberate: replace unverified
sector workforce ranks with a dairy-change waterfall; use actual farmer
occupation data for age/sex; replace unavailable ABARES labour categories with
verified business-turnover classes; and keep geography about businesses rather
than relabelling forestry/fishing workers as farmers.

## Definitions and comparability

- **CABEE business:** an actively trading business unit, assigned to one main
  industry and main state. Counts are not property/farm locations, and complex
  businesses can operate in several states while being assigned to one.
- **Agriculture:** ANZSIC subdivision 01. The selected classes exclude aquaculture,
  forestry, fishing, and the separately classified support-services subdivision.
- **Farmers and Farm Managers:** the occupation used in EQ07a. It is neither all
  agriculture workers nor a complete list of everyone who works on a farm.
- **Registered dairy farm:** the unit used by state milk authorities and Dairy
  Australia. Do not substitute the CABEE dairy-business count.
- **Older farm-count survey:** ABS's 2021–22 agricultural-business estimate used
  an estimated agricultural-operations value threshold of AUD 40,000. It cannot
  be spliced to CABEE or current commodity model outputs as one continuous series.
- Different charts legitimately use 2025 business/farm data and February 2026
  workforce data. Show the period and unit on every chart; don't title the whole
  page “2026 farm census”.
- CABEE cells are adjusted for confidentiality. Small differences can come from
  those adjustments; not every small change is a real change in activity.
- Labour Force values are survey estimates, in thousands. Display sensible rounded
  figures and use “estimated/about”; retain unrounded source values in data.

## Colour meanings, before implementation

| Meaning | Proposed colour / rule |
| --- | --- |
| Agriculture overall | Deep blue `#174A67`; sequential blue lightness for quantities. Final map bins must pass contrast testing. |
| Geographic context | Light neutral grey; no-data uses hatching and a label. |
| Earlier / later time | Charcoal / deep blue, always date-labelled. |
| Dairy | Violet `#6E4B87` everywhere a sector identity is encoded. |
| Nursery/floriculture | `#795548` |
| Mushrooms/vegetables | `#496B83` |
| Fruit/tree nuts | `#9A651D` |
| Sheep/beef/grain | `#174A67` (agriculture focus; avoid using this alongside an ambiguous aggregate category). |
| Other crops | `#666A35` |
| Poultry | `#8B4975` |
| Deer | `#4C6271` |
| Other livestock | `#694B3E` |
| Employment/turnover size | Ordered single-hue lightness, explicitly labelled; do not reuse sector hues to mean size. |

These are proposed semantic assignments, not a claim that a palette already
passes all visual tests. Colour alone must never identify a sector. Nine sectors
are difficult to distinguish by hue: use direct names, legends and sector
highlighting rather than requiring a reader to memorise a nine-colour key.

## Layout, interaction, and future validation

Use five scrolling sections and two equal laptop columns. Full-width charts
span both columns. Serif titles; sans-serif body and axes; comfortable labels,
short paragraphs, and consistent whitespace/source-note spacing. The brief's
maximum ten words per rendered paragraph line must be checked in the browser.

A sector highlight can connect charts 7–9 without hiding the data. Use tooltips
for exact values; chart headings/findings must stand alone without hover. Provide
keyboard-reachable chart containers, native controls, and accessible labels.

The extract CSVs plus findings JSON total about **292 KB** before map geometry.
Full source workbooks and the PDF stay outside the repository. Boundary download,
simplification and geometry join checks belong to implementation; choose the
2021 state geography deliberately for stable state comparisons, rather than
calling it the latest geography. Keep total delivered chart data/geometry below
2 MB and verify the actual requests later.

Before publication: build only after the student has drawn the agreed A4 sketch;
render every Vega/Vega-Lite specification over HTTP; test widths 1180, 1280, 1366,
and 1440; check overflow, requests/console, labels/annotations, contrast,
accessibility, line lengths, data totals and source citations. These browser
checks have **not** run because the website has not been built.

Next student milestone: follow [SKETCH_GUIDE.md](SKETCH_GUIDE.md), obtain tutor
feedback on the map idioms and box plot, and supply any revisions. The AI
acknowledgement remains the student's own writing; no sketch PDF has been generated.
