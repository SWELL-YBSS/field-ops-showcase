"""
Regenerates the deployable HTML pages from their _source.html equivalents:
    checklist_source.html -> Mine_Ute_Inspection_Checklist.html
    index_source.html     -> index.html

The _source.html files are the editable versions (contain __LOGO_BASE64__
and __FONT_BASE64__ placeholders instead of the actual embedded assets, so
they stay readable/editable). This script embeds the TJC logo and the
Press Start 2P pixel font and writes the final, self-contained HTML files
that get deployed. Add new (source, output) pairs to PAGES as more forms
are added to the app.

Run this after editing any _source.html file:
    python build.py
"""
import base64
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(FOLDER, "Screenshot 2026-06-21 082454.png")
FONT = os.path.join(FOLDER, "press-start-2p.woff2")

PAGES = [
    ("checklist_source.html", "Mine_Ute_Inspection_Checklist.html"),
    ("index_source.html", "index.html"),
]

with open(LOGO, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("ascii")

with open(FONT, "rb") as f:
    font_b64 = base64.b64encode(f.read()).decode("ascii")

for source_name, output_name in PAGES:
    source = os.path.join(FOLDER, source_name)
    output = os.path.join(FOLDER, output_name)

    with open(source, encoding="utf-8") as f:
        html = f.read()

    html = html.replace("__LOGO_BASE64__", logo_b64)
    html = html.replace("__FONT_BASE64__", font_b64)

    with open(output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Written {output} ({len(html)} bytes)")
