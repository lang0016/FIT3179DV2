# Research data and provenance

These are **real, filtered source extracts** for research and chart planning.
The website uses generated readable chart specifications and simplified state
boundaries. See [the research register](../DATA_RESEARCH.md) for
source URLs, rights, reference periods, methods, and limitations.

| File in `research/` | Meaning / unit |
| --- | --- |
| `business_classes_employment.csv` | Original retained ABS CABEE class cells, main state/national class total, June 2024/2025, business counts and five employment-size bins. Source table and row retained. |
| `business_groups_employment.csv` | Disjoint agriculture classes aggregated to nine groups. National class totals remain separate from state class sums. |
| `all_businesses_by_state.csv` | Official June 2025 state business totals from CABEE cube 1 Table 4; denominator for business-share map. |
| `business_turnover.csv` | National agriculture class × six turnover bins, June 2024/2025. Counts, not turnover dollars. Published class total retained separately. |
| `farmers_age_sex_latest.csv` | Farmers and Farm Managers, February 2026, six age bands × two source sex categories. Values in **thousands of estimated workers**. |
| `farmers_age_sex_history.csv` | Same occupation from 2000 to February 2026. Not a Census series. |
| `agriculture_employment.csv` | Agriculture subdivision only, quarterly original survey estimates from 2000 to February 2026; nine total/full-/part-time and sex series, IDs retained. Values in **thousands**. |
| `dairy_registered_farms.csv` | Dairy Australia Table 2, 14 financial years × six states and Australia; latest year provisional. Registered farms, not CABEE businesses. |
| `findings.json` | Computed values behind the rounded findings in the plan. |

`source_manifest.json` records exact original filenames, URLs, hashes and sizes.
To reproduce, install the pinned packages in `scripts/requirements-research.txt`
and run `scripts/prepare_research_data.py --source-dir /path/outside/checkout`
with `--download` if the originals are not already present. Do not check original
PDFs/workbooks into the repository. Source file access uses normal HTTPS and
checksum matching; changed downloads stop the script for review.

Agriculture classes are the 34 workbook classes whose four-digit codes fall in
0111–0199. Group codes 011–019 preserve leading zeroes. This excludes separately
classified forestry, fishing, aquaculture and support services. Do not sum the
published national class rows together with the state rows.

CABEE detailed cells are perturbed: size bins and states may not add exactly to
published totals. Keep these discrepancies; do not invent corrections. Rates
and box plots are derived, approximate comparisons. For a 100% composition,
define the denominator as the displayed bin sum and disclose the difference
from any published total. Unknown/other geography is retained separately.

ABS-derived material: **Based on Australian Bureau of Statistics data**.
ABS data is CC BY 4.0 subject to the source exclusions. Dairy Australia data:
small factual table extract from *Australian Dairy Industry In Focus 2025*,
Table 2, printed p.8, credited to state milk authorities and Dairy Australia.
No open-data licence was identified for that report; the original PDF, text,
photos and charts are not redistributed here. No blanket software licence
should be interpreted as relicensing source material.

`states.geojson` contains simplified official ABS state geometry; `map_sources.json`
records its source, checksum, clipping extent and exclusions. It is prepared by
`scripts/prepare_maps.py`. Chart JSON and accessible table metadata are generated
by `scripts/build_charts.py`; no browser-side calculation invents source records.
