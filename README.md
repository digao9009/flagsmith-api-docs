# Flagsmith API — generated API reference (Sourcey)

A static, navigable API reference for the [Flagsmith](https://github.com/Flagsmith/flagsmith)
API, generated with [Sourcey](https://github.com/sourcey/sourcey) 3.6.5 from the
project's own pinned OpenAPI spec.

**Live site:** https://digao9009.github.io/flagsmith-api-docs/

## What is here

- `index.html` / `api-reference.html` — the generated docs site (615 operations, 472 schemas,
  per-operation code samples, client-side search).
- `evidence.json` — recomputable verification evidence for this build (hashes, versions,
  receipt id).
- `report.html` — maintainer-facing notes on gaps surfaced while generating the reference.
- `source/` — everything needed to reproduce the build: the pinned OpenAPI spec, the
  Sourcey config, the captured build log, and the governed validation skill + sealed
  runx receipt (`source/runx-receipt.json`).

## Reproduce

```bash
npm i sourcey
npx sourcey build          # uses sourcey.config.ts → ./flagsmith-openapi.yaml
```

Source spec: `Flagsmith/flagsmith` @ `9fe3c5c44ea47b2db719bdcf64eb149020721779`
(BSD-3-Clause, as stated in the spec's own `info.license`).

## Provenance

- Generated with Sourcey 3.6.5; governed validation run under runx-cli 0.9.1
  (receipt `sha256:d66a1ecc64a29f47a79c3e29ede717e1676a7c915f4685d88505f0d3188ead77`,
  schema `runx.receipt.v1`, outcome `completed`).
- Spec sha256: `ea52d405a9b1250ff83d1664cbb83df0da4706fa2110c836fb4fe101df417e57`.

## Notes

- This is a community-generated reference site for the Flagsmith ecosystem; not affiliated
  with Flagsmith. It can be removed on request.
- Flagsmith and its logo are trademarks of their respective owners. The API spec is used
  under its BSD-3-Clause license.
