import { defineConfig, openapi } from "sourcey";

export default defineConfig({
  name: "Flagsmith API Reference",
  siteUrl: "https://digao9009.github.io",
  baseUrl: "/flagsmith-api-docs",
  navigation: {
    tabs: [{ tab: "API Reference", source: openapi("./flagsmith-openapi.yaml") }],
  },
  theme: { preset: "api-first" },
});
