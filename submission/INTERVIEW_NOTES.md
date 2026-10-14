# Interview preparation

Use these as prompts for understanding the project. Explain the choices in your
own words rather than memorising a script.

1. **What is the story?** Location, change, people, sector differences and a wider
   workforce perspective. The dairy case study illustrates one sector; it is not
   a claim that all farming changed the same way.
2. **Who is the audience?** A general Malaysian reader. State names, financial
   years and statistical units are explained. No statistical knowledge is assumed.
3. **Why are the two first maps different?** One uses agriculture's share of all
   state businesses; the other uses the number of agriculture businesses. A small
   state can have a high share without a large count.
4. **Why not put raw totals in the choropleth?** Large business totals can reflect
   the size of a state's economy. Normalisation answers the composition question.
5. **Why an equal-area projection?** It avoids changing relative land areas through
   projection distortion. The cartogram then deliberately changes area for a
   different purpose, and labels that transformation.
6. **What counts as a farmer?** EQ07a uses the occupation Farmers and Farm
   Managers. The agriculture industry includes other occupations. Neither is a
   count of physical farms or registered dairy farms.
7. **Why is the business count larger than the old farm estimate?** CABEE uses
   actively trading business units; the old agriculture survey applied a value
   threshold. Different scope and units prevent direct comparison or splicing.
8. **Why do some sums differ?** Confidentiality-adjusted CABEE cells may not add
   exactly to published totals. The code retains those values and explains the
   difference rather than inventing corrections.
9. **What does the box plot describe?** Variation between states' non-employing
   business shares within sectors. Each state gets equal weight. It is not the
   distribution of individual farms or a national estimate. Explain the minimum
   denominator and sample-count rules.
10. **Why not colour every sector?** Direct names and a highlight control reduce
    the need to remember nine colours. Sequential lightness represents quantity.
11. **Does the waterfall explain causes?** No. It accounts for each state's
    contribution to a change. It cannot establish why farms entered or left.
12. **Why separate quarterly data from annual averages?** Seasonal and sampling
    variation can make one quarter misleading. An annual average needs all four
    quarters; the latest quarter is explicitly labelled separately.
13. **What is original?** The narrative, paired count/share maps, linked sector
    highlighting, and custom non-contiguous cartogram built from official geometry.
14. **What are the limitations?** Different reference periods and counting units;
    survey estimates; confidentialisation; main-state allocation; dairy coverage
    limited to six states; provisional latest dairy figures; omitted remote islands.
15. **How was the data checked?** Frozen-source hashes, source rows/series IDs,
    agriculture-only class filtering, nonnegative cells, demographic totals and
    reconciliation of all fourteen dairy rows. Inspect the scripts yourself.
16. **What did AI do?** Answer accurately using your actual process. Write your own
    acknowledgement and be ready to explain any generated code or text you keep.
