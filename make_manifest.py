#!/usr/bin/env python3
# make_manifest.py — scans your data folder for COGs and writes data/manifest.json
#
# Use this only if AUTOLOAD.mode = "manifest" in the viewer.
# (If you use AUTOLOAD.mode = "github" you DON'T need a manifest at all —
#  the app discovers the .tif files in the repo folder by itself.)
#
# Run it from your repository root (the folder that contains "data"):
#     python make_manifest.py
# Re-run it whenever you add or remove year mosaics, then commit/push.

import json, os, re

DATA_DIR = "data"                 # folder holding your *.tif COGs
EXTS = (".tif", ".tiff")

def year_of(name):
    m = re.search(r"(?:19|20)\d{2}", name)
    return int(m.group(0)) if m else None

if not os.path.isdir(DATA_DIR):
    raise SystemExit(f'Folder "{DATA_DIR}" not found. Run this from your repo root.')

files = sorted(f for f in os.listdir(DATA_DIR) if f.lower().endswith(EXTS))
layers = [{"url": f"{DATA_DIR}/{f}", "year": year_of(f)} for f in files]

out_path = os.path.join(DATA_DIR, "manifest.json")
with open(out_path, "w", encoding="utf-8") as fh:
    json.dump({"layers": layers}, fh, indent=2)

print(f"Wrote {out_path} with {len(layers)} layer(s):")
for l in layers:
    print(f"  {l['year']}  {l['url']}")
