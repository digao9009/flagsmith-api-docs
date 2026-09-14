# Flagsmith API — generated API reference (Sourcey)

A static, navigable API reference for the [Flagsmith](https://github.com/Flagsmith/flagsmith)
API, generated with [Sourcey](https://github.com/sourcey/sourcey) 3.6.5 from the
project's own pinned OpenAPI spec (a curated 30-operation slice, chosen to keep the
docs home lean and fetchable; the full spec has 615 operations).

**Live site:** https://digao9009.github.io/flagsmith-api-docs/

## What is here

- `index.html` / `api-reference.html` — the generated docs site (curated 30-operation
  slice with descriptions, curl samples, and client-side search).
- `evidence.json` — recomputable verification evidence for this build (hashes, versions,
  receipt id).
- `report.md` — maintainer-facing notes on gaps surfaced while generating the reference
 .
- `source/` — everything needed to reproduce the build: the pinned full OpenAPI spec,
  the curated subset, the Sourcey config, the captured build log, and the governed
  validation skill + sealed runx receipt (`source/runx-receipt.json`).

## Reproduce

```bash
npm i sourcey
npx sourcey build          # uses sourcey.config.ts → ./subset.yaml
```

Source spec: `Flagsmith/flagsmith` @ `9fe3c5c44ea47b2db719bdcf64eb149020721779`
(BSD-3-Clause, as stated in the spec's own `info.license`).

## Provenance

- Generated with Sourcey 3.6.5; governed validation run under runx-cli 0.9.1
  (receipt `sha256:f6b8785e0b029cdfde6f28d6c32305a04d38936c92b741b72db4fdfcae5bda98`,
  schema `runx.receipt.v1`, outcome `completed`).
- Subset spec sha256: `125a0713b0aa767fc066ca2e499341e047ba7e3a650b9919083a205da4120f4a`.

## Notes

- This is a community-generated reference site for the Flagsmith ecosystem; not affiliated
  with Flagsmith. It can be removed on request.
- Flagsmith and its logo are trademarks of their respective owners. The API spec is used
  under its BSD-3-Clause license.
