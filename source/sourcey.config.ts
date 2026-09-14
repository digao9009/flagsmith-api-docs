import { defineConfig, openapi } from "sourcey";
export default defineConfig({
  name: "Flagsmith API Reference",
  siteUrl: "https://digao9009.github.io",
  baseUrl: "/flagsmith-api-docs",
  codeSamples: ["curl"],
  navigation: { tabs: [{ tab: "API Reference", source: openapi("./sub.yaml") }] },
  theme: { preset: "api-first" },
});
