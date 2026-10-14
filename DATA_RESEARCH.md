# Australian Farmers: verified data research

Prepared for **Ang Lin Shan**, Malaysian campus · **15 October 2026 (Malaysia)**.

## Result and access status

Official ABS access now works. The environment configuration read reports
unrestricted networking; the earlier domain-allowlist blocker is resolved.
ABARES and Jobs and Skills Australia still return HTTP 503 with an upstream
connection reset. This is not evidence that their datasets are missing or that
credentials are needed. No additional credential or network setting is requested.

The research now uses two publishers: **ABS** and **Dairy Australia**, with
independent statistical collections. Dairy Australia's registered-farm series
credits state milk authorities and Dairy Australia. Do not count a second ABS
publication or an NFF page quoting ABS as an independent publisher.

The original 12-chart plan was revised to fit data actually inspected. It no
longer assumes that free Census tables provide agriculture-only sector/age
cross-tabulations. See [PROJECT_PLAN.md](PROJECT_PLAN.md).

## Verified source register

All sources below were retrieved on 15 October 2026 (Malaysia). The exact raw
file URLs, sizes, and SHA-256 hashes are in [data/source_manifest.json](data/source_manifest.json).
Hashes identify the downloaded bytes; they are not official signatures.

### S1. ABS Counts of Australian Businesses, including Entries and Exits (CABEE)

- **Latest general release:** [July 2022–June 2026](https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/jul2022-jun2026), released 18 August 2026.
- **Latest detailed class/state breakdown verified:** [July 2021–June 2025](https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/jul2021-jun2025), detailed cubes added 16 December 2025.
- The latest release explicitly schedules detailed cubes 2–11 for December.
  June 2025 therefore remains the latest verified detailed edition for this plan;
  do not replace agriculture-only figures with 2026 Agriculture, Forestry and
  Fishing division totals just to use a newer date.
- Downloaded **8165DC01.xlsx**, Table 4 (all-business state denominators),
  **8165DC02.xlsx**, Tables 1–2 (industry class × main state × employment size,
  June 2025 and June 2024), and **8165DC03.xlsx**, Tables 1–2 (turnover size).
  Downloaded 2026 cube 1 for release/scope comparison; it is not used to extend
  the detailed agriculture class series.
- Authors/publisher: Australian Bureau of Statistics. Underlying collection:
  ABS Business Register, using ABR/ATO administrative records and ABS profiling.
- [2025 methodology](https://www.abs.gov.au/methodologies/counts-australian-businesses-including-entries-and-exits-methodology/jul2021-jun2025).
- Scope: actively trading market-sector business units, not all ABNs, farms, land
  holdings, or individual workers. A business has one main industry and main
  state; multiple operating sites are not individually counted here.
- Detailed cells are perturbed for confidentiality. Component sums can differ
  from published totals, including across states and size bins. The script
  preserves original class cells and their totals; it never inserts balancing
  values or forces them to agree.
- Preparation: retain the **34 four-digit classes from 0111 through 0199** actually
  present in the workbook; group by the first three digits (011–019). Exclude
  aquaculture, forestry, fishing, and support services. Preserve unknown/other
  main-state rows separately. Aggregate published national class rows separately
  from state rows to avoid double counting.
- Rights: ABS CC BY 4.0, subject to the website's exclusions. Attribute derived
  calculations as **“Based on Australian Bureau of Statistics data”**, with title,
  reference period, access date and source link.
- Charts: 1, 2, 4, 7, 8, 9, 11.

### S2. ABS Labour Force, Australia, Detailed: EQ07a

- [March 2026 publication](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/mar-2026), page dated 23 April 2026. Workbook contents record 26 March 2026 for EQ07a.
- Exact table: **EQ07a — Employed persons by Age, Occupation sub-major group of
  main job (ANZSCO) and Sex, August 1986 onwards**, sheet **Data 1**.
- Latest actual observation in the downloaded data: **February 2026**. This was
  checked from the records, not inferred from the publication month or pivot
  table's saved column order.
- Select **Farmers and Farm Managers**, six age groups, Males/Females, full-time
  and part-time. Source units are **thousands of employed persons**. The derived
  total is the sum of full-time and part-time estimates, not an exact headcount.
- Data creation: ABS Labour Force Survey, weighted employment estimates. The
  occupation concerns a person's main job, not every role on a farm. It is
  distinct from employment in the agriculture industry.
- Preparation: preserve full precision, dates, source row numbers, sex/age labels,
  and units. Retain history from 2000 in a compact CSV; use the latest 12 cells
  for the pyramid. Calculate the 55+ share from the 55–64 and 65+ groups.
- The publication has ceased under this title. [Current Labour Force publication](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release)
  was August 2026 when checked; it includes newer headline labour statistics,
  which are not substitutes for this occupation/age cross-tabulation. February
  2026 is the latest detailed occupation period verified here; recheck detailed
  replacement tables when building, and never label these figures October 2026.
- Rights: ABS CC BY 4.0 and derivative attribution as above.
- Chart: 6.

### S3. ABS Labour Force, Australia, Detailed: Table 06

- Same [March 2026 publication](https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/mar-2026).
- Exact file **6291006.xlsx**, sheet **Data1**: **Employed persons by Industry
  sub-division of main job (ANZSIC) and Sex**. Latest observation February 2026.
- Retain only the **Agriculture** subdivision's nine series (total/full-time/
  part-time × persons/males/females). Exclude the broader division that includes
  forestry/fishing and the other subdivision series. Series IDs are retained.
- Original quarterly survey estimates, in thousands, from 1984 onwards. The
  research extract starts in 2000. Seasonal variation and sampling variation
  make isolated quarter-to-quarter movements unsuitable for strong trend claims.
- Calculate a full-year average only from all four quarters; February 2026 alone
  is not the 2026 annual average. Do not splice this survey to Census counts.
- Rights: ABS CC BY 4.0 and derivative attribution.
- Chart: 12.

### S4. Dairy Australia, Australian Dairy Industry In Focus 2025

- [Official current-report landing page](https://www.dairyaustralia.com.au/industry-reports/australian-dairy-industry-in-focus).
  The current-report download is labelled **2025**; the archive includes 2024 and
  earlier reports. No newer In Focus edition was listed when checked.
- [Exact PDF](https://assets.dairyaustralia.com.au/api/public/content/In-Focus-2025?v=42fe4d04), 2,025,718 bytes; report mainly describes the **2024–25 season**.
  The landing page did not expose a precise publication date; do not invent one.
- Primary table: **Table 2, Number of registered dairy farms**, printed page **8**,
  PDF page **10**, 2011–12 through 2024–25. Publisher: Dairy Australia. Table source:
  **State milk authorities and Dairy Australia**. Latest season marked **(p)**,
  meaning provisional.
- Preparation: extract the numeric table, retain NSW/Vic/Qld/SA/WA/Tas and the
  national total, retain provisional status. All 14 rows' state totals were
  checked against the national column. Exact formulas support percent decline,
  Victoria's share, and state contributions to change.
- NT/ACT have no rows in the table. Missing coverage must not become invented
  zeroes on a map.
- Units are registered dairy farms, **not CABEE dairy-cattle businesses**. For
  example, CABEE's 2025 dairy-business class total is 8,044, while this table has
  3,772 registered dairy farms. These are not interchangeable and their difference
  is not a count of closures, inactive farms, or errors.
- Context only: printed page 4 identifies Malaysia among the top five dairy export
  destinations by value; printed page 5 explains that the reported dairy workforce
  also includes processing companies. Do not call its 30,400 industry workforce
  figure an on-farm-only count.
- Rights/terms checked: [Dairy Australia disclaimer](https://www.dairyaustralia.com.au/disclaimer)
  and the report. Copyright Dairy Australia; **no open-data licence was identified**.
  The research uses a small factual numeric table extract with attribution; do
  not redistribute the PDF, copy its charts/photos/text, or describe it as CC BY.
  Confirm any additional reuse terms before reproducing substantial report material.
- Charts: 3, 5, 10.

### S5. ABS geographic boundaries

- [ASGS Edition 3 digital boundaries](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files).
- State/territory shapefile GDA2020 is listed as a **20.56 MB ZIP**. Use the **2021
  state geography** deliberately; the page explicitly says this is not the latest
  ASGS edition. Do not call it the current edition.
- Rights: ABS CC BY 4.0 subject to source exceptions and derivative attribution.
- Status: official geometry downloaded, checksum recorded, simplified and joined
  to all eight state/territory codes. See `data/map_sources.json` and
  `scripts/prepare_maps.py`. The implemented preparation preserves state codes and topology and records exclusions.
- Charts: 1, 2, 10; Albers equal-area for ordinary maps, then explicit area
  transformation for the cartogram.

### S6. ABS older agricultural-business survey (context only)

- [Agricultural Commodities, Australia, 2021–22](https://www.abs.gov.au/statistics/industry/agriculture/agricultural-commodities-australia/2021-22)
  is the **final issue**, originally released 17 January 2023, with historical
  additions and later page updates.
- Downloaded **AGCDCNAT_STATE202122.xlsx**, Table 1. Its all-agriculture row has
  an estimated **87,786.57 businesses**, reported as about 87,800 on the page.
- [Methodology](https://www.abs.gov.au/methodologies/agricultural-commodities-australia-methodology/2021-22)
  requires agricultural activity and an estimated value of agricultural operations
  of at least **AUD 40,000**. It used the Rural Environment and Agricultural
  Commodity Survey; the response rate was 68% from a sample of 24,871 businesses.
- This is not the same scope as CABEE. No trend splicing is allowed.
- Newer commodity-specific releases exist; the [agriculture index](https://www.abs.gov.au/statistics/industry/agriculture)
  lists livestock, horticulture and broadacre releases for 2024–25. Their crop or
  animal totals are not a current all-farm-count series.
- Rights: ABS CC BY 4.0. No core chart depends on the discontinued survey.

## Sources investigated but not selected

- **Census 2021:** DataPacks downloaded and metadata inspected, including G54,
  T34, and working-population profiles. G54 combines **Agriculture, Forestry and
  Fishing**, not agriculture alone. This contradicts the first plan's assumed
  fine-grained sector availability. Census extracts are not used in the revised
  core plan; do not relabel those broad tables as farming-only data.
- **ABARES:** HTTP 503 on workforce and main pages, upstream connection reset.
  Replaced by accessible ABS workforce tables and Dairy Australia farm data;
  the current plan does not depend on waiting for that site.
- **Jobs and Skills Australia:** same HTTP 503 when tested; no dataset claimed.
- **NFF Farm Facts:** accessible at its [new location](https://nff.org.au/initiatives/resources/farm-facts/),
  but mostly quotes ABS/ABARES and mixes reference periods. Useful source-finding
  context; it does not supply an independent numerical series for our charts.
- Earlier candidate URLs for CABEE under `/industry/industry-overview/` were
  incorrect. The verified location is `/economy/business-indicators/` above.

## Prepared files and reproduction

- [Source manifest](data/source_manifest.json): eight originals, exact download
  URLs, byte counts, retrieval date, SHA-256 hashes.
- [Preparation script](scripts/prepare_research_data.py): frozen-source validation,
  class filtering/grouping, workforce extraction, Dairy Australia table extraction,
  source-row references, and computed findings.
- [Dependencies](scripts/requirements-research.txt): pinned spreadsheet/PDF parsers.
- [Derived extract guide](data/README.md): field meanings and scope.
- [Calculated findings](data/research/findings.json): precise values underlying
  rounded narrative claims.

From the repository root, create a virtual environment outside the checkout,
install `scripts/requirements-research.txt`, then run:

```sh
python scripts/prepare_research_data.py --source-dir /path/to/originals --download
```

`--download` retrieves missing original files with normal HTTPS verification.
An integrity mismatch stops processing; investigate a revised source, rather
than blindly replacing a checksum. Without that flag the script reads existing
original files. It does not commit originals or publish anything.

## Validation completed and remaining

Completed: exact input hashes and sizes; agriculture class scope; 34 national
class records per year; nonnegative retained business/worker cells; all eight
state denominators; latest actual workforce month; 12 unique farmer age/sex
cells; all 14 dairy state sums; selected source-row/series-ID spot checks; numerical
headline calculations. The box plot has 5–8 eligible states for each retained
sector; deer has none at the threshold and is excluded.

The prepared CSVs and findings JSON total approximately **292 KB**. The original
files remain outside the checkout. This is an extract-size measurement, not a
claim about a finished website's network download size.

The website and map preparation are now implemented. Executed browser checks,
contrast measurements and download size are recorded in [VALIDATION.md](VALIDATION.md).
The student still supplies the hand-drawn sketch, personal AI acknowledgement,
Moodle submission and interview. No sketch PDF is claimed.
