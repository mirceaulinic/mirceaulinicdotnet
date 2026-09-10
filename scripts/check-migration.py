#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
posts = list((root / "content/posts").glob("*.md"))

print(f"Posts: {len(posts)}")
for p in sorted(posts):
    text = p.read_text(encoding="utf-8")
    if "{%" in text or "{{" in text:
        print(f"Possible template syntax: {p}")
    if "http://mirceaulinic.net/" in text:
        print(f"Old HTTP link: {p}")

print("Migration checks complete.")
