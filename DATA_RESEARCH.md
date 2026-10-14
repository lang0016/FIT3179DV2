# Data research register

Project: Australian Farmers · Ang Lin Shan · Malaysian campus.
Prepared: 15 October 2026 (Malaysia).

## Evidence status

**Research is blocked before dataset verification.** Requests to the official
ABS and ABARES domains failed at the network proxy with `Tunnel connection
failed: 403 Forbidden`. This is evidence of denied access, not missing data,
an invalid dataset, or an authentication requirement.

The environment configuration draft now includes `www.abs.gov.au` and
`www.agriculture.gov.au` in its custom domain allowlist. Existing package-manager
presets were preserved. The save returned `status: saved` and
`requires_publish: true`. A retry after saving still failed. Draft persistence
does not apply the policy to the running machine or publish the environment.
Review and save the changes in environment settings, then publish the
environment; recheck the official requests when the changed policy is active.

No data has been downloaded. No numerical finding, latest-edition claim,
licence, or table availability is verified. Links below are **candidate entry
points**, not citations to successfully accessed releases. Some URLs may redirect
or require correction after network access is available.

## Candidate source register

| ID | Publisher / candidate dataset family | Candidate official entry point | Intended use | Checks still required |
| --- | --- | --- | --- | --- |
| C1 | Australian Bureau of Statistics (ABS), Census of Population and Housing, industry of employment and worker characteristics | https://www.abs.gov.au/census | Agricultural employment, age/sex, sector comparisons, state and regional rates, historical Census comparisons. | Most recent published detailed edition; access method (download/DataPacks/TableBuilder); exact tables and variables; industry codes; reference population; confidentiality; geography; reuse terms. |
| C2 | ABS, Agricultural Commodities, Australia | https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia/latest-release | Historical farm/agricultural-business counts if available and comparable. | Whether discontinued or superseded; latest relevant release; published counts and tables; minimum business/value thresholds; collection changes; breaks in series; licence. Do not extend a discontinued series using incompatible newer collections. |
| C3 | ABS, newer agriculture releases | https://www.abs.gov.au/statistics/industry/agriculture | Locate replacement/current publications and assess whether farm counts are actually included. | Current release names, years and scope. Commodity production data alone does not establish workforce or farm numbers. |
| C4 | ABS, Counts of Australian Businesses, including Entries and Exits | https://www.abs.gov.au/statistics/industry/industry-overview/counts-australian-businesses-including-entries-and-exits/latest-release | Agriculture business counts by state, industry, and employment-size class; consistent historical counts where available. | Latest edition; whether required cross-tabulations are published; active-business definition; industry detail; non-employing definition; size bins; series comparability; reuse terms. These are businesses, not physical farms. |
| C5 | ABARES (Australian Bureau of Agricultural and Resource Economics and Sciences), agricultural workforce research | https://www.agriculture.gov.au/abares/research-topics/agricultural-workforce | Independent farm-survey evidence on family/hired labour and sector differences. | Latest relevant report and download; whether comparable labour-composition tables exist; sectors covered; survey year; units (persons/hours/FTE); survey estimates and uncertainty; methods; reuse licence. |
| C6 | ABARES, farm survey research | https://www.agriculture.gov.au/abares/research-topics/surveys | Alternative directly supported sector workforce or business-size comparison if C5 cannot support chart 9. | Exact report/dataset; downloadable aggregate tables; survey representativeness; whether employment or business-size measures match the story; terms. No individual-farm microdata access is assumed. |
| C7 | ABS, Australian Statistical Geography Standard (ASGS) | https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3 | State and suitable regional boundaries for the three maps and regional comparisons. | Appropriate edition for each Census period; download URLs; code fields; treatment of offshore/external territories; licence; simplified topology. Check for a newer edition before calling this current. |

The intended two independent publishers are **ABS and ABARES**. Using two ABS
publications alone does not meet that planning target. Treat additional articles
as context, not substitutes for a second numerical dataset.

## Research questions to test, not findings

1. Is there a reliable, comparable change in the number of farms/businesses?
2. Where is agricultural work important relative to all local employment?
3. Which sectors employ the most workers, and how has that changed?
4. How does the age/sex profile vary across agriculture and regions?
5. What proportion of businesses have no employees or only a small staff?
6. What independent survey evidence explains differences in how farms use labour?

Do not publish statements such as “fewer farms, more output” or “farmers are
getting older” until the relevant comparisons are computed from verified data.
Business consolidation cannot be inferred merely from declining business counts.

## File-level record to complete after access

For every actual source file, record:

- Exact title, publisher, landing URL, direct download URL, table/sheet identifier.
- Release date, reference period, retrieval date, and evidence of latest edition.
- Licence/terms URL, third-party restrictions, and required attribution.
- Unit of observation, industry codes, population, units, geography and boundary edition.
- Survey coverage, thresholds, suppression, missing codes, and uncertainty notes.
- Original file checksum, filtered columns/rows, aggregation formula, joins, and output file.
- Charts using the extract; computed findings and independent spot checks.

Keep original source files outside the public page's download path. Put small
derived chart inputs in `data/` later, with a source manifest and reproducible
preparation script. Publication rights must be checked before redistributing files.

## Proposed derived schemas

These are target schemas, not downloaded or fabricated data files.

| Extract | Fields |
| --- | --- |
| Workforce by region | `year, region_code, region_name, geography_level, agriculture_workers, all_employed, agriculture_share_pct, status` |
| Sector workforce | `year, state_code, sector_code, sector_name, workers, coverage_note` |
| Workforce age/sex | `year, sector_code, age_band, sex_category, workers, status` |
| Regional older-worker share | `year, region_code, sector_code, workers_55_plus, workers_total, share_55_plus_pct, included, exclusion_reason` |
| Business counts | `reference_date, state_code, industry_code, employment_size_class, businesses, scope_note` |
| Farm-count trend | `year, geographic_code, farm_or_business_count, measure_name, collection_scope, comparable_segment` |
| ABARES labour | `survey_year, farm_sector, labour_category, value, unit, estimate_status, source_table` |
| Geography | Official geographic code plus simplified geometry, reference edition and attribution. |

## Validation before narrative writing

- Check unique keys, numeric types, nonnegative counts, and percentage ranges.
- Reconcile totals against official tables, allowing only documented rounding or
  confidentiality effects. Avoid false precision in small-region percentages.
- Match numerator and denominator population/year/geography for every rate.
- Keep missing/suppressed cells separate from zero and exclude unknown geography
  transparently from maps.
- Check industry concordances before combining Census years; use only harmonised
  categories, and document sectors aggregated or excluded.
- Compare only common business definitions and reference dates in trend charts.
- Verify every boundary join and inspect small territories and detached islands.
- Check the box plot's sample size per sector and disclose regional weighting.
- Verify that the ABARES comparison uses published survey estimates, not invented
  national estimates from a subset of farms.
- Calculate chart findings in the preparation step and trace each displayed value
  to a source table. No causal annotation without a separately verified citation.

## Download and page-size target

Aim for **under 2 MB of total downloadable chart data and geography**, excluding
library code, as a concrete interpretation of the brief's “few megabytes”.
Use compact filtered tables and simplify boundaries while retaining valid shapes.
Shared extracts should be reused by several specs; formatted chart JSON should
remain readable. This target has not yet been measured because no data is downloaded.

## Next action

Activate the saved domain additions in environment settings and publish the
environment. Then retry the source requests, verify current releases and
download tables, and revise [PROJECT_PLAN.md](PROJECT_PLAN.md) using actual
evidence before committing to the sketch or building the page. Add additional
official download hostnames only if redirects reveal they are needed.
