#!/usr/bin/env python
"""Governed validation run for the generated Flagsmith API Sourcey docs site.

Verifies the built static site (files, index page, sitemap, search index,
spec hash) and prints a single JSON object ({ "report": {...} }) for the runx
receipt. The Sourcey build itself runs outside this governed run with the
documented command; this run seals the recomputable verification evidence.
"""
import datetime
import hashlib
import json
import os
import re
import sys


def env_input(name, default=None):
    return os.environ.get("RUNX_INPUT_" + name.upper(), default)


site = os.path.abspath(env_input("project") or ".")
out_dir = env_input("output_dir", "dist")
spec = env_input("spec", "flagsmith-openapi.yaml")
dist = os.path.join(site, out_dir)


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


files = []
if os.path.isdir(dist):
    for root, _dirs, names in os.walk(dist):
        for name in names:
            files.append(
                os.path.relpath(os.path.join(root, name), dist).replace("\\", "/")
            )
files.sort()

report = {
    "project": site,
    "output_dir": out_dir,
    "spec_path": os.path.join(site, spec),
    "spec_commit": env_input("spec_commit"),
    "runx_version": env_input("runx_version"),
    "sourcey_version": env_input("sourcey_version"),
    "build_command": env_input("build_command"),
    "python_version": sys.version.split()[0],
    "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "page_count": sum(1 for f in files if f.endswith(".html")),
    "generated_files": files,
}

if os.path.isfile(report["spec_path"]):
    report["spec_sha256"] = sha256_file(report["spec_path"])
    report["spec_bytes"] = os.path.getsize(report["spec_path"])

index_html = os.path.join(dist, "index.html")
report["index_present"] = os.path.isfile(index_html)
if report["index_present"]:
    report["index_sha256"] = sha256_file(index_html)
    report["index_bytes"] = os.path.getsize(index_html)
    with open(index_html, "rb") as fh:
        text = fh.read(400_000).decode("utf-8", "ignore")
    match = re.search(r"<title[^>]*>([^<]*)</title>", text, re.I)
    report["index_title"] = match.group(1).strip() if match else ""
    report["index_headings"] = [
        re.sub(r"<[^>]+>", "", h).strip()
        for h in re.findall(r"<h1[^>]*>(.*?)</h1>", text, re.I | re.S)[:5]
    ]

sitemap = os.path.join(dist, "sitemap.xml")
if os.path.isfile(sitemap):
    report["sitemap_sha256"] = sha256_file(sitemap)
    report["sitemap_head"] = open(sitemap, encoding="utf-8").read()[:800]

search_index = os.path.join(dist, "search-index.json")
if os.path.isfile(search_index):
    try:
        data = json.load(open(search_index, encoding="utf-8"))
        if isinstance(data, list):
            entries = len(data)
        elif isinstance(data, dict):
            entries = len(data.get("documents", data.get("entries", data.get("index", []))))
        else:
            entries = 0
        report["search_index_ok"] = True
        report["search_index_entries"] = entries
    except Exception as exc:  # noqa: BLE001
        report["search_index_ok"] = False
        report["search_index_error"] = str(exc)[:150]

for name in ("llms.txt", "llms-full.txt"):
    path = os.path.join(dist, name)
    if os.path.isfile(path):
        report[name.replace(".", "_") + "_bytes"] = os.path.getsize(path)

build_log = env_input("build_log")
if build_log and os.path.isfile(build_log):
    with open(build_log, encoding="utf-8", errors="ignore") as fh:
        report["build_log_tail"] = fh.read().strip().splitlines()[-8:]

report["verified"] = bool(report.get("index_present") and report.get("page_count", 0) > 0)

print(json.dumps({"report": report}, ensure_ascii=False))
