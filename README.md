# Australian Farmers — FIT3179 Data Visualisation 2

**Ang Lin Shan · Malaysian campus**

GitHub: [lang0016/FIT3179DV2](https://github.com/lang0016/FIT3179DV2)

Current stage: **verified data research and chart planning**. A website has not
been built or deployed. The next milestone is the student's hand-drawn A4 sketch
and tutor feedback.

- [Story, findings and 12-chart plan](PROJECT_PLAN.md)
- [Verified sources, preparation and limitations](DATA_RESEARCH.md)
- [Hand-drawn sketch outline](SKETCH_GUIDE.md)
- [Data extracts and provenance](data/README.md)
- [Reproducible preparation script](scripts/prepare_research_data.py)

The planned page investigates agricultural businesses, farmers' workforce
characteristics, sector differences, and change over time. Sources are the
Australian Bureau of Statistics and Dairy Australia. Findings keep agriculture
businesses, Farmers and Farm Managers, agricultural workers, and registered
dairy farms distinct.

The plan has 12 charts, nine advanced idioms under the supplied brief, and three
map idioms. The colour-meaning table is in `PROJECT_PLAN.md`; use it consistently
when implementing charts. The final page will use Vega/Vega-Lite and cite each
source. No marks or rubric interpretation are guaranteed.

Reproduce the extracts using a virtual environment outside the repository:

```sh
python3 -m venv /tmp/farmers-research-venv
/tmp/farmers-research-venv/bin/pip install -r scripts/requirements-research.txt
/tmp/farmers-research-venv/bin/python scripts/prepare_research_data.py --source-dir /tmp/farmers-originals --download
```

Original source files remain outside the checkout; only small factual extracts,
provenance, and the preparation script are stored here. Read source-specific
rights and definitions in the research register before reusing them.

The student must draw and upload the sketch PDF, write their own AI
acknowledgement, submit the required Moodle materials, and prepare for the
interview. This research and planning was assisted by generative AI; this note
is a project-process disclosure, not the student's submission acknowledgement.
