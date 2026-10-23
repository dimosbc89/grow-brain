#!/usr/bin/env python3
"""Markdown -> καθαρό A4 PDF (ελληνικά OK) μέσω headless Chromium.
Χρήση: python3 to_pdf.py input.md output.pdf
"""
import sys, subprocess, tempfile, os, glob, shutil, markdown

src, dst = sys.argv[1], sys.argv[2]
body = markdown.markdown(open(src, encoding="utf-8").read(), extensions=["tables", "sane_lists"])
css = """
@page { size: A4; margin: 16mm 16mm 14mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1d1d1b; }
h1 { font-size: 20pt; margin: 0 0 4px; color: #1F3A2E; letter-spacing: -0.3px; }
h2 { font-size: 12.5pt; margin: 16px 0 6px; color: #1F3A2E; border-bottom: 1.5px solid #9BE15D; padding-bottom: 3px; }
h3 { font-size: 11pt; margin: 12px 0 4px; }
p { margin: 4px 0 8px; }
ul, ol { margin: 4px 0 8px 18px; padding: 0; } li { margin: 2px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9.5pt; }
th { background: #1F3A2E; color: #fff; text-align: left; padding: 5px 6px; }
td { border-bottom: 1px solid #ddd; padding: 4px 6px; vertical-align: top; }
blockquote { margin: 6px 0; padding: 6px 10px; background: #F3F8EE; border-left: 3px solid #9BE15D; }
strong { color: #111; } em { color: #555; }
.footer { margin-top: 14px; font-size: 8.5pt; color: #777; }
"""
html = f"<!doctype html><html lang='el'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
tmp = tempfile.mkdtemp()
hp = os.path.join(tmp, "doc.html"); open(hp, "w", encoding="utf-8").write(html)

candidates = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome") + ["/opt/pw-browsers/chromium"] + [shutil.which(x) or "" for x in ("chromium", "chromium-browser", "google-chrome")]
chrome = next((c for c in candidates if c and os.path.exists(c)), None)
if chrome:
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.abspath(dst)}", "file://" + hp], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
else:  # fallback: LibreOffice
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, hp], check=True, timeout=180)
    shutil.move(os.path.join(tmp, "doc.pdf"), dst)
print("ok", dst)
