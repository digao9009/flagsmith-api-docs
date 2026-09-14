import { defineConfig, openapi } from "sourcey";
export default defineConfig({
  name: "Flagsmith API Reference",
  siteUrl: "https://flagsmith-api-docs.readthedocs.io",
  baseUrl: "/",
  codeSamples: ["curl"],
  navigation: { tabs: [{ tab: "API Reference", source: openapi("./sub.yaml") }] },
  theme: { preset: "api-first" },
});
