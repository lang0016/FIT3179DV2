# Locally hosted chart libraries

- Vega 5.33.0 — npm package `vega`, `build/vega.min.js`
- Vega-Lite 5.23.0 — npm package `vega-lite`, `build/vega-lite.min.js`
- Vega-Embed 6.29.0 — npm package `vega-embed`, `build/vega-embed.min.js`

The corresponding BSD licence notices are included beside the files. These
are unmodified distribution files installed through npm with normal registry
integrity verification. Local hosting avoids a runtime chart-CDN dependency.
The `$schema` links in chart JSON identify schemas; they are not fetched to render.
