# Maintainer notes: generated API reference for the Flagsmith API

This site is a Sourcey-generated API reference built from the pinned OpenAPI spec
(`Flagsmith/flagsmith` @ `9fe3c5c44ea47b2db719bdcf64eb149020721779`, OpenAPI 3.1.0,
BSD-3-Clause). It renders 615 operations and 472 schemas with per-operation code samples
(cURL, JavaScript, Python), client-side search, a sitemap, and `llms.txt` /
`llms-full.txt` context exports for agent consumption.

## Gaps surfaced while generating the reference

- 612 of 615 operations carry no `summary`, so every operation title falls back to the
  generated identifier (e.g. `api_v1_environments_features_retrieve`).
- 464 of 615 operations carry no `description`, so most entries state parameters and
  responses but not intent, preconditions, or side effects.
- 375 of 472 schemas carry no `description`, so request/response models are structurally
  documented but not explained.
- Tags are consistently present (0 operations without tags), so navigation works; the
  weakness is editorial text, not structure.
- The highest-leverage fix is enriching `summary`/`description` on the ~40 highest-traffic
  operations first (environments, organisations, projects, auth), then regenerating.
- No per-language SDK samples beyond the three generic languages are configured; adding
  more `codeSamples` languages is a one-line config change once prose is improved.

## Why this is useful to the ecosystem

- Static HTML the project (or anyone) can host; no runtime, dashboard, or vendor service
  is needed to render it.
- Per-endpoint deep-linkable anchors and instant search across 1087 indexed entries.
- `llms.txt` exports make the same reference consumable by AI agents.
- Fully reproducible: spec + config + build log + sealed runx receipt are published in
  `source/`, and `evidence.json` carries the recomputable hashes.

## Provenance

- Built with Sourcey 3.6.5 via `npx sourcey build` (see `source/build.log`).
- Governed validation run under runx-cli 0.9.1; sealed receipt
  `sha256:d66a1ecc64a29f47a79c3e29ede717e1676a7c915f4685d88505f0d3188ead77`
  (schema `runx.receipt.v1`, outcome `completed`), published at `source/runx-receipt.json`.
- Spec sha256 `ea52d405a9b1250ff83d1664cbb83df0da4706fa2110c836fb4fe101df417e57`.
- This is a community-generated reference; not affiliated with Flagsmith, removable on
  request.
