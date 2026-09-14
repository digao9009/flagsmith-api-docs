---
name: flagsmith-sourcey-docs
description: Governed validation run for the generated Flagsmith API Sourcey docs site (pinned OpenAPI spec), sealing a runx receipt with recomputable verification evidence.
---

Seal a governed validation run over a generated Sourcey documentation site for the pinned Flagsmith OpenAPI spec.

What this skill does:

1. Verifies the generated static site produced by the documented Sourcey build (`npx sourcey build` in the project, Sourcey 3.6.5).
2. Checks: index page present, page list and count, sha256 of index.html / sitemap / spec, search-index.json parses, llms.txt/llms-full.txt present, title and headings.
3. Emits a bounded JSON verification report (all recomputable values included) for the sealed runx receipt.

The Sourcey build itself runs outside this governed run with the exact documented command; this run seals the recomputable verification evidence for a reviewer.

Inputs:

- `project` (required): project directory containing `sourcey.config.ts`, `node_modules/sourcey`, and the OpenAPI spec.
- `output_dir`: build output directory relative to the project (default `dist`).
- `spec`: OpenAPI spec path relative to the project (default `flagsmith-openapi.yaml`).
- `spec_commit`: pinned upstream commit the spec was taken from.
- `runx_version`, `sourcey_version`, `build_command`, `build_log`: recorded evidence values from the host build.
