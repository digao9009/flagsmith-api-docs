# Maintainer notes: generated API reference for the Flagsmith API

This site is a Sourcey-generated API reference built from the pinned OpenAPI spec
(`Flagsmith/flagsmith` @ `9fe3c5c44ea47b2db719bdcf64eb149020721779`, OpenAPI 3.1.0,
BSD-3-Clause). It renders a curated 30-operation slice of the spec with descriptions,
parameters, responses, curl samples, client-side search, a sitemap, and `llms.txt` /
`llms-full.txt` context exports. The full spec contains 615 operations and 472 schemas;
the slice keeps the docs home small enough to load for plain-fetch crawlers and readers.

## Gaps surfaced while generating the reference

- 612 of 615 operations carry no `summary`, so operation titles often fall back to
  generated identifiers; the curated slice favors the operations that do carry prose.
- 464 of 615 operations carry no `description`, so most entries state parameters and
  responses but not intent, preconditions, or side effects.
- 375 of 472 schemas carry no `description`, so request/response models are structurally
  documented but not explained.
- Tags are consistently present (0 operations without tags), so navigation works; the
  weakness is editorial text, not structure.
- The highest-leverage fix is enriching `summary`/`description` on the ~40 highest-traffic
  operations first (environments, organisations, projects, auth), then regenerating.
- When a spec is this large, a single generated page can exceed crawler byte budgets;
  curating a documented slice (or splitting by tag) keeps the docs home durable.

## Why this is useful to the ecosystem

- Static HTML the project (or anyone) can host; no runtime, dashboard, or vendor service
  is needed to render it.
- Per-endpoint deep-linkable anchors and instant search across the indexed entries.
- `llms.txt` exports make the same reference consumable by AI agents.
- Fully reproducible: spec + subset + config + build log + sealed runx receipt are
  published in `source/`, and `evidence.json` carries the recomputable hashes.

## Provenance

- Built with Sourcey 3.6.5 via `npx sourcey build` (see `source/build.log`).
- Governed validation run under runx-cli 0.9.1; sealed receipt
  `sha256:3239ab7fba8e77fe6f24b1d5cfca31e36409614a1bce9f0cda149326dcec2120`
  (schema `runx.receipt.v1`, outcome `completed`), published at `source/runx-receipt.json`.
- Docs home: https://flagsmith-api-docs.readthedocs.io/ (806,877 bytes; sha256
  `21c0e53ff4f3a1eee1468d0fd7b2577b98a07849abfbef15df7c2d678f6fba66`).
- Subset spec sha256 `125a0713b0aa767fc066ca2e499341e047ba7e3a650b9919083a205da4120f4a`.
- This is a community-generated reference; not affiliated with Flagsmith, removable on
  request.
